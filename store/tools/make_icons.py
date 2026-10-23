"""Store icon (512x512 PNG, opaque, full bleed: Play applies its own mask) and the site icon."""
import sys
import tempfile
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import render  # noqa: E402

root = Path(__file__).resolve().parent.parent.parent
svg = (root / 'docs' / 'assets' / 'icon.svg').as_uri()

for size, out in ((512, root / 'store' / 'graphics' / 'icon-512.png'),
                  (192, root / 'docs' / 'assets' / 'icon-192.png')):
    with tempfile.TemporaryDirectory() as d:
        page = Path(d) / 'icon.html'
        page.write_text(
            f'<!doctype html><meta charset="utf-8"><style>html,body{{margin:0;background:#17406f;'
            f'overflow:hidden}}img{{display:block;width:{size}px;height:{size}px}}</style>'
            f'<img src="{svg}">', encoding='utf-8')
        render(page, out, size, size)
    im = Image.open(out)
    print(out.name, im.size, im.mode)
