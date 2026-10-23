"""Drives the release app on the emulator and saves raw screenshots for the store.

    python store/tools/take_screenshots.py [--device phone|tablet7|tablet10] <lang> [<lang> ...]

Per language: wipes the emulator's app data, fills a fictional profile, opens the demo form,
auto-fills it, signs it, converts it to Word and captures every step.
The emulator only; never the physical phone.
"""
import json
import re
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, str(Path(__file__).resolve().parent))
import adbdrv as d  # noqa: E402
import sigdraw  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / 'store' / 'graphics' / 'raw'
FILES = {'en': 'registration-form', 'it': 'modulo-iscrizione', 'fr': 'formulaire-inscription',
         'de': 'anmeldeformular', 'es': 'formulario-inscripcion'}
BIRTH = {'de': '14.05.1988'}
DEVICES = {  # name -> (width, height, density) ; None keeps the emulator's own screen
    'phone': None,
    'tablet7': (1200, 1920, 320),
    'tablet10': (1600, 2560, 280),
}
# Material's tooltips, which is how the app bar buttons are announced in each language.
BACK = '^(Back|Indietro|Retour|Zurück|Atrás)$'
MENU = 'men[uúü]'  # "Show menu", "Mostra il menu", "Afficher le menu", "Menü anzeigen", "Mostrar menú"
SIGN_FIELD = (246, 234, 225)  # fill of the empty signature field

SUB = 'phone'
W = H = 0


def arb(lang):
    return json.loads((ROOT / 'lib' / 'l10n' / f'app_{lang}.arb').read_text(encoding='utf-8'))


def rx(text):
    """Regex for the first line of a localized string."""
    return '^' + re.escape(text.split(chr(10))[0][:24])


def editor_label(text):
    """Toolbar buttons carry a badge on its own line: "12" + newline + "Fill & sign"."""
    first = text.split(chr(10))[0]
    return '(^|' + chr(10) + ')' + re.escape(first) + '$'


def demo_mode():
    """Clean status bar (fixed clock, full battery, no notifications) for the captures."""
    d.shell('settings', 'put', 'global', 'sysui_demo_allowed', '1')
    for c in (
        ['enter'],
        ['clock', '-e', 'hhmm', '0941'],
        ['battery', '-e', 'level', '100', '-e', 'plugged', 'false'],
        ['network', '-e', 'wifi', 'show', '-e', 'level', '4', '-e', 'fully', 'true'],
        ['network', '-e', 'mobile', 'hide'],
        ['notifications', '-e', 'visible', 'false'],
    ):
        d.shell('am', 'broadcast', '-a', 'com.android.systemui.demo', '-e', 'command', c[0], *c[1:])


def set_screen(device):
    global SUB, W, H
    SUB = device
    spec = DEVICES[device]
    if spec:
        d.shell('wm', 'size', f'{spec[0]}x{spec[1]}')
        d.shell('wm', 'density', str(spec[2]))
    else:
        d.shell('wm', 'size', 'reset')
        d.shell('wm', 'density', 'reset')
    time.sleep(2.0)
    W, H = d.size()
    print('screen', W, H)


def shot(lang, name):
    out = RAW / SUB / lang / f'{name}.png'
    d.screenshot(out)
    print('  shot', out.name)


def back_button():
    d.tap_text(BACK, wait=1.4)


def sign_field_center():
    """Where the empty signature field is on screen, found by its fill colour."""
    tmp = RAW / '_probe.png'
    d.screenshot(tmp)
    a = np.asarray(Image.open(tmp).convert('RGB')).astype(int)
    m = (np.abs(a - np.array(SIGN_FIELD)).max(axis=2) <= 3)
    ys, xs = np.nonzero(m)
    tmp.unlink()
    if len(xs) < 1500:
        raise RuntimeError('signature field not found')
    return int((xs.min() + xs.max()) // 2), int((ys.min() + ys.max()) // 2)


def fill_profile(lang, L):
    values = ['Martin', 'Anna', 'AB1234567', BIRTH.get(lang, '14/05/1988'), 'Torino', 'TO',
              'Via Roma 12', '10121', 'Torino', 'TO', '+39 000 000 0000', 'anna.martin@example.com']
    dp = 160 / int(d.shell('wm', 'density').split(':')[-1].split()[0])

    def edits():
        out = []
        for n in d.dump().iter('node'):
            if n.get('class', '').endswith('EditText'):
                x1, y1, x2, y2 = map(int, re.findall(r'\d+', n.get('bounds')))
                out.append((n.get('text') or '', x1, y1, x2, y2))
        return out

    d.tap_text(rx(L['profileTitle']) + '$', wait=1.8)
    done, guard = 0, 0
    cx = W // 2
    while done < len(values) and guard < 60:
        guard += 1
        e = edits()
        filled = [i for i, t in enumerate(e) if t[0] != '']
        nxt = (max(filled) + 1) if filled else 0
        if nxt >= len(e):
            d.swipe(cx, int(H * 0.52), cx, int(H * 0.33), 400)
            time.sleep(0.8)
            continue
        t = e[nxt]
        if (t[4] - t[2]) * dp < 50 or t[2] < H * 0.18 or t[4] > H * 0.62:
            d.swipe(cx, int(H * 0.52), cx, int(H * 0.38), 400)
            time.sleep(0.8)
            continue
        d.tap((t[1] + t[3]) // 2, (t[2] + t[4]) // 2)
        time.sleep(0.7)
        d.text(values[done])
        time.sleep(0.4)
        done += 1
    d.tap_text('^' + re.escape(L['save']) + '$', wait=1.8)


def open_from_picker(L, filename):
    d.tap_text(rx(L['homePick']), wait=2.5)
    for _ in range(4):
        d.tap_text('Show roots', wait=2.2)
        d.tap_text('^Downloads$', wait=2.5)
        if d.find('Files in Downloads'):
            break
    pat = '^' + re.escape(filename) + r'\.pdf$'
    # The list order changes and the last row can sit under the gesture bar: search instead.
    d.tap_text('^Search$', wait=1.2)
    d.text(filename)
    time.sleep(2.0)
    d.tap_text(pat, wait=3.0)


def run(lang):
    L = arb(lang)
    fname = FILES[lang]
    print('==', SUB, lang)
    d.force_stop()
    d.shell('pm', 'clear', d.PKG)
    d.set_app_locale(lang)
    d.launch()
    time.sleep(1.0)
    fill_profile(lang, L)
    # My details, filled
    d.tap_text(rx(L['profileTitle']) + '$', wait=2.0)
    shot(lang, '06-profile')
    d.back()
    # open the form, auto-fill it
    open_from_picker(L, fname)
    # Tapping the "to fill" chip opens the first field and zooms the page onto it; the zoom
    # stays when the sheet is dismissed, which makes a much more readable capture.
    d.tap_text(r'^\d+ [^/]', wait=1.8)
    for _ in range(3):
        if not d.find(rx(L['confirm'])):
            break
        d.back()
    d.tap_text(editor_label(L['homeFillSign']), wait=1.5)
    d.tap_text(rx(L['formAutoTitle']), wait=2.4)
    shot(lang, '02-autofill')
    # reopen at fit-to-page zoom and sign
    back_button()
    d.tap_text('^' + re.escape(fname), wait=2.6)
    shot(lang, '01b-form')
    x, y = sign_field_center()
    d.tap(x, y)
    time.sleep(1.8)
    d.tap_text('^' + re.escape(L['padRemember']) + '$', wait=0.5, required=False)
    sigdraw.signature(W, H)
    time.sleep(0.8)
    shot(lang, '03-sign')
    d.tap_text('^' + re.escape(L['padUse']) + '$', wait=2.0)
    d.tap_text('^' + re.escape(L['applyPdf']) + '$', wait=2.5)
    shot(lang, '04-signed')
    # PDF -> Word from the menu
    d.tap_text(MENU, wait=1.2)
    d.tap_text(rx(L['menuToWord']), wait=1.0)
    for _ in range(40):
        if d.find(rx(L['wordReady'])):
            break
        time.sleep(1.0)
    time.sleep(0.8)
    shot(lang, '05-word')
    d.back()
    back_button()
    time.sleep(1.0)
    shot(lang, '01-home')


if __name__ == '__main__':
    args = sys.argv[1:]
    device = 'phone'
    if args and args[0] == '--device':
        device, args = args[1], args[2:]
    demo_mode()
    set_screen(device)
    try:
        for lang in args:
            run(lang)
    finally:
        if device != 'phone':
            set_screen('phone')
