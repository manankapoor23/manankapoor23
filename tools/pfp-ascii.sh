#!/bin/sh
# Regenerate the ASCII avatar at the top of README.md.
# ponytail: macOS `sips` does the decode+resize, so no Pillow/ImageMagick needed.
# Tune the crop if the avatar changes: SIZE is <height> <width>, OFFSET is <top> <left>.
set -e
USER=manankapoor23
CROP_SIZE="170 150"
CROP_OFFSET="140 70"
COLS=66
ROWS=37

cd "$(dirname "$0")"
curl -sL -o /tmp/pfp.jpg "https://github.com/$USER.png"   # GitHub serves whatever was uploaded
# shellcheck disable=SC2086
sips -c $CROP_SIZE --cropOffset $CROP_OFFSET /tmp/pfp.jpg --out /tmp/pfp-crop.jpg >/dev/null
sips -s format bmp -z "$ROWS" "$COLS" /tmp/pfp-crop.jpg --out /tmp/pfp.bmp >/dev/null

python3 - /tmp/pfp.bmp <<'PY'
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
for r in rows:
    print(''.join(RAMP[min((v - lo) * len(RAMP) // (span + 1), len(RAMP) - 1)] for v in r).rstrip())
PY
