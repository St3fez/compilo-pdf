"""Contact sheet of the raw captures of one language: python contact_sheet.py <dir> <out.png>."""
import sys
from pathlib import Path

from PIL import Image

src, out = Path(sys.argv[1]), Path(sys.argv[2])
files = sorted(src.glob('*.png'))
tw = 300
thumbs = []
for f in files:
    im = Image.open(f).convert('RGB')
    th = int(im.height * tw / im.width)
    thumbs.append(im.resize((tw, th)))
sheet = Image.new('RGB', (len(thumbs) * (tw + 10) + 10, max(t.height for t in thumbs) + 20), 'white')
for i, t in enumerate(thumbs):
    sheet.paste(t, (10 + i * (tw + 10), 10))
sheet.save(out)
print(len(files), sheet.size)
