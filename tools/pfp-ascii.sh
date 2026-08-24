#!/bin/sh
# Regenerate assets/pfp.svg -- the ASCII avatar that streams in line by line
# at the top of README.md.
# ponytail: macOS `sips` does the decode+resize, so no Pillow/ImageMagick needed.
# Tune the crop if the avatar changes: SIZE is <height> <width>, OFFSET is <top> <left>.
set -e
USER=manankapoor23
CROP_SIZE="170 150"
CROP_OFFSET="140 70"
COLS=66
ROWS=37
STAGGER=0.06   # seconds between lines; ROWS*STAGGER = total runtime

cd "$(dirname "$0")"
curl -sL -o /tmp/pfp.jpg "https://github.com/$USER.png"   # GitHub serves whatever was uploaded
# shellcheck disable=SC2086
sips -c $CROP_SIZE --cropOffset $CROP_OFFSET /tmp/pfp.jpg --out /tmp/pfp-crop.jpg >/dev/null
sips -s format bmp -z "$ROWS" "$COLS" /tmp/pfp-crop.jpg --out /tmp/pfp.bmp >/dev/null

python3 - /tmp/pfp.bmp "$STAGGER" > ../assets/pfp.svg <<'PY'
import struct, sys
d = open(sys.argv[1], 'rb').read()
assert d[:2] == b'BM'
off = struct.unpack_from('<I', d, 10)[0]
w, h = struct.unpack_from('<ii', d, 18)
bpp = struct.unpack_from('<H', d, 28)[0]
assert bpp in (24, 32), f'unsupported bpp {bpp}'
px, stride = bpp // 8, ((bpp * w + 31) // 32) * 4
rows = [[(d[off+y*stride+x*px+2]*299 + d[off+y*stride+x*px+1]*587
          + d[off+y*stride+x*px]*114) // 1000 for x in range(w)]
        for y in range(abs(h))]
if h > 0:                      # positive height means bottom-up rows
    rows.reverse()
lo = min(min(r) for r in rows)
hi = max(max(r) for r in rows)
span = max(hi - lo, 1)
RAMP = "@%#*+=-:. "            # dark -> light
art = [''.join(RAMP[min((v - lo) * len(RAMP) // (span + 1), len(RAMP) - 1)] for v in r).rstrip()
       for r in rows]

# GitHub strips <script> from README SVGs but keeps CSS animation, so the
# line-by-line reveal is pure @keyframes on a staggered animation-delay.
FS, ADV, LH = 14, 8.4, 16.8    # font-size, monospace advance (0.6em), line height
stagger = float(sys.argv[2])
W, H = round(max(len(l) for l in art) * ADV), round(len(art) * LH + 6)
esc = lambda t: t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

print(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
      f'viewBox="0 0 {W} {H}" role="img" aria-label="ASCII portrait">')
print(f"""<style>
text{{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
font-size:{FS}px;fill:#1f2328;white-space:pre}}
@media (prefers-color-scheme:dark){{text{{fill:#c9d1d9}}}}
.l{{opacity:0;animation:print .01s steps(1,end) forwards}}
@keyframes print{{to{{opacity:1}}}}
</style>""")
for i, line in enumerate(art):
    print(f'<text class="l" x="0" y="{round(13 + i * LH, 1)}" xml:space="preserve" '
          f'style="animation-delay:{round(i * stagger, 2)}s">{esc(line)}</text>')
print('</svg>')
PY
