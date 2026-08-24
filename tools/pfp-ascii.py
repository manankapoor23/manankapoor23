#!/usr/bin/env python3
"""Regenerate assets/pfp.svg -- the ASCII avatar that streams in at the top of README.md.

ponytail: macOS `sips` does the decode/crop/resize, so there is no Pillow or
ImageMagick dependency -- we only hand-parse the uncompressed BMP it writes.
"""
import os, struct, subprocess, sys

USER    = "manankapoor23"
CROP    = (150, 120, 140, 85)   # height, width, top, left -- retune if the avatar changes
COLS    = 96
RAMP    = " .:-=+*#%@"          # sparse -> dense == dark -> bright, so it reads right on a dark panel
WINDOW  = (0.03, 0.62)          # tone percentiles: the avatar is backlit, so let the sky blow out
STAGGER = 0.035                 # seconds between lines; ROWS*STAGGER = total runtime
BG      = "#0d1117"
FS, ADV, LH = 14, 8.4, 16.8     # font-size, monospace advance (0.6em), line height


def pixels():
    """Fetch the live avatar, crop to the face, and return it as rows of (r, g, b)."""
    h, w, top, left = CROP
    rows_n = round(COLS * (h / w) / 2)          # chars are ~2x taller than wide
    run = lambda c: subprocess.run(c, shell=True, check=True, capture_output=True)
    run(f'curl -sfL -o /tmp/pfp.jpg "https://github.com/{USER}.png"')
    run(f"sips -c {h} {w} --cropOffset {top} {left} /tmp/pfp.jpg --out /tmp/pfp-crop.jpg")
    run(f"sips -s format bmp -z {rows_n} {COLS} /tmp/pfp-crop.jpg --out /tmp/pfp.bmp")

    d = open("/tmp/pfp.bmp", "rb").read()
    assert d[:2] == b"BM", "sips did not write a BMP"
    off = struct.unpack_from("<I", d, 10)[0]
    bw, bh = struct.unpack_from("<ii", d, 18)
    bpp = struct.unpack_from("<H", d, 28)[0]
    assert bpp in (24, 32), f"unsupported bpp {bpp}"
    px, stride = bpp // 8, ((bpp * bw + 31) // 32) * 4
    rows = [[(d[off + y*stride + x*px + 2], d[off + y*stride + x*px + 1], d[off + y*stride + x*px])
             for x in range(bw)] for y in range(abs(bh))]
    if bh > 0:                                   # positive height means bottom-up rows
        rows.reverse()
    return rows


def svg(rows):
    lum = [[(r*299 + g*587 + b*114) // 1000 for r, g, b in row] for row in rows]
    vals = sorted(v for row in lum for v in row)
    lo = vals[int(len(vals) * WINDOW[0])]
    hi = vals[min(int(len(vals) * WINDOW[1]), len(vals) - 1)]
    span = max(hi - lo, 1)
    lift = lambda v: min(255, max(0, (v - lo) * 255 // span))
    clamp = lambda i: min(max(i, 0), len(RAMP) - 1)

    w, h = round(COLS * ADV), round(len(rows) * LH + 6)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
           f'viewBox="0 0 {w} {h}" role="img" aria-label="ASCII portrait of Manan Kapoor">',
           f'<rect width="100%" height="100%" rx="6" fill="{BG}"/>',
           # GitHub strips <script> from README SVGs but keeps CSS, so the reveal is pure keyframes.
           f'<style>text{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,'
           f'"Liberation Mono",monospace;font-size:{FS}px;white-space:pre}}'
           f'.l{{opacity:0;animation:print .01s steps(1,end) forwards}}'
           f'@keyframes print{{to{{opacity:1}}}}</style>']

    for y, row in enumerate(rows):
        spans, run, cur = [], "", None
        for x, (r, g, b) in enumerate(row):
            ch = RAMP[clamp((lum[y][x] - lo) * len(RAMP) // (span + 1))]
            # colour gets the same window as the ramp, else shadowed skin stays near-black
            col = f"#{lift(r)>>4:x}{lift(g)>>4:x}{lift(b)>>4:x}"
            if col != cur:
                if run:
                    spans.append(f'<tspan fill="{cur}">{run}</tspan>')
                run, cur = ch, col
            else:
                run += ch
        spans.append(f'<tspan fill="{cur}">{run}</tspan>')
        out.append(f'<text class="l" x="0" y="{round(13 + y*LH, 1)}" xml:space="preserve" '
                   f'style="animation-delay:{round(y*STAGGER, 3)}s">{"".join(spans)}</text>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "pfp.svg")
    rows = pixels()
    open(dest, "w").write(svg(rows) + "\n")
    print(f"wrote {os.path.normpath(dest)}  {COLS}x{len(rows)} chars, "
          f"{os.path.getsize(dest)//1024} KB, {round(len(rows)*STAGGER, 1)}s runtime", file=sys.stderr)
