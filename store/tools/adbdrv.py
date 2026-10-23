"""Tiny adb/uiautomator driver used to take the store screenshots on the emulator.

Never targets a physical phone: every call goes to the emulator serial.
"""
import re
import subprocess
import time
import xml.etree.ElementTree as ET
from pathlib import Path

ADB = r'C:\Users\Pc\AppData\Local\Android\Sdk\platform-tools\adb.exe'
SERIAL = 'emulator-5554'
PKG = 'com.pdfcraft.pdfcraft_mobile'


def adb(*args, check=True, binary=False):
    r = subprocess.run([ADB, '-s', SERIAL, *args], capture_output=True, timeout=120)
    if check and r.returncode != 0:
        raise RuntimeError(f'adb {args} failed: {r.stderr.decode(errors="replace")[:300]}')
    return r.stdout if binary else r.stdout.decode('utf-8', errors='replace')


def shell(*args, **kw):
    return adb('shell', *args, **kw)


def screenshot(path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_bytes(adb('exec-out', 'screencap', '-p', binary=True))


def dump():
    for attempt in range(4):
        shell('uiautomator', 'dump', '/sdcard/ui.xml', check=False)
        xml = adb('exec-out', 'cat', '/sdcard/ui.xml', check=False)
        if '<' in xml:
            return ET.fromstring(xml[xml.index('<'):])
        time.sleep(1.5)  # the screen was changing; try again
    raise RuntimeError('uiautomator returned no hierarchy')


def _center(bounds):
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', bounds))
    return (x1 + x2) // 2, (y1 + y2) // 2


def nodes(root=None):
    root = root if root is not None else dump()
    for n in root.iter('node'):
        label = n.get('content-desc') or n.get('text') or ''
        yield label, n.get('bounds'), n


def find(pattern, root=None, nth=0):
    """Center of the nth node whose label matches the regex, or None."""
    hits = [b for label, b, _ in nodes(root) if label and re.search(pattern, label, re.I | re.S)]
    return _center(hits[nth]) if len(hits) > nth and hits[nth] else None


def tap(x, y):
    shell('input', 'tap', str(x), str(y))


def tap_text(pattern, wait=1.0, nth=0, required=True):
    for _ in range(6):
        c = find(pattern, nth=nth)
        if c:
            tap(*c)
            time.sleep(wait)
            return True
        time.sleep(0.8)
    if required:
        labels = [l for l, _, _ in nodes() if l][:40]
        raise RuntimeError(f'no node matches {pattern!r}; visible: {labels}')
    return False


def labels():
    return [l for l, _, _ in nodes() if l]


def swipe(x1, y1, x2, y2, ms=300):
    shell('input', 'swipe', str(x1), str(y1), str(x2), str(y2), str(ms))


def text(s):
    shell('input', 'text', s.replace(' ', '%s'))


def set_app_locale(lang):
    shell('cmd', 'locale', 'set-app-locales', PKG, '--locales', lang)
    time.sleep(1.5)


def force_stop():
    shell('am', 'force-stop', PKG)


def launch():
    shell('am', 'start', '-n', f'{PKG}/.MainActivity')
    time.sleep(2.5)


def back():
    shell('input', 'keyevent', 'KEYCODE_BACK')
    time.sleep(0.8)


def size():
    """Current screen size in pixels, rotation included (read from a real capture)."""
    import io

    from PIL import Image
    return Image.open(io.BytesIO(adb('exec-out', 'screencap', '-p', binary=True))).size
