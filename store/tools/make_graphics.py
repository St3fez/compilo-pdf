"""Composes the Play Store graphics from the raw emulator captures.

    python store/tools/make_graphics.py            # all languages, phone + feature graphic
    python store/tools/make_graphics.py tablet10

Output: store/graphics/screenshots/<device>/<play-locale>/NN-name.png (tablet10: portrait 1600 x 2560) and
        store/graphics/feature/feature-graphic-<play-locale>.png (1024 x 500)
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from render import render  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
RAW = ROOT / 'store' / 'graphics' / 'raw'
OUT = ROOT / 'store' / 'graphics'
LOCALE = {'en': 'en-US', 'it': 'it-IT', 'fr': 'fr-FR', 'de': 'de-DE', 'es': 'es-ES'}

# (store order) raw capture -> caption
SCENES = [
    ('01-home', 'home'),
    ('06-profile', 'profile'),
    ('02-autofill', 'autofill'),
    ('03-sign', 'sign'),
    ('04-signed', 'signed'),
    ('05-word', 'word'),
]
CAPTIONS = {
    'en': dict(home='Fill, sign and convert your PDFs', profile='Your details, entered once',
               autofill='Recurring fields fill themselves', sign='Sign with your finger',
               signed='Signed and ready to send', word='PDF to Word, offline'),
    'it': dict(home='Compila, firma e converti i tuoi PDF', profile='I tuoi dati, una volta sola',
               autofill='I campi ricorrenti si compilano da soli', sign='Firma con il dito',
               signed='Firmato e pronto da inviare', word='Da PDF a Word, offline'),
    'fr': dict(home='Remplissez, signez et convertissez vos PDF', profile='Vos informations, saisies une seule fois',
               autofill='Les champs récurrents se remplissent seuls', sign='Signez du doigt',
               signed='Signé et prêt à envoyer', word='Du PDF au Word, hors ligne'),
    'de': dict(home='PDFs ausfüllen, unterschreiben und umwandeln', profile='Ihre Daten, nur einmal eingeben',
               autofill='Wiederkehrende Felder füllen sich selbst', sign='Mit dem Finger unterschreiben',
               signed='Unterschrieben und versandfertig', word='PDF in Word, offline'),
    'es': dict(home='Rellena, firma y convierte tus PDF', profile='Tus datos, una sola vez',
               autofill='Los campos repetidos se rellenan solos', sign='Firma con el dedo',
               signed='Firmado y listo para enviar', word='De PDF a Word, sin conexión'),
}
TAGLINE = {'en': 'Fill, sign and convert your PDFs', 'it': 'Compila, firma e converti i tuoi PDF',
           'fr': 'Remplissez, signez et convertissez vos PDF', 'de': 'PDFs ausfüllen, unterschreiben und umwandeln',
           'es': 'Rellena, firma y convierte tus PDF'}
PILLS = {'en': ['Offline', 'Private', 'No account'], 'it': ['Offline', 'Privato', 'Senza account'],
         'fr': ['Hors ligne', 'Privé', 'Sans compte'], 'de': ['Offline', 'Privat', 'Ohne Konto'],
         'es': ['Sin conexión', 'Privado', 'Sin cuenta']}

FONT = "'Segoe UI','Helvetica Neue',Arial,sans-serif"
BG = 'linear-gradient(160deg,#1c4f86 0%,#12335f 45%,#0a1d3b 100%)'


def uri(p):
    return Path(p).resolve().as_uri()


def shot_html(w, h, caption, img, *, font, top, phone_w, phone_top, landscape=False):
    left = (w - phone_w) // 2
    return f'''<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;width:{w}px;height:{h}px;overflow:hidden;background:#0a1d3b}}
.s{{position:relative;width:{w}px;height:{h}px;background:{BG};font-family:{FONT};overflow:hidden}}
.c1{{position:absolute;width:{int(w*0.9)}px;height:{int(w*0.9)}px;border-radius:50%;right:-{int(w*0.35)}px;top:-{int(w*0.3)}px;background:rgba(255,255,255,.07)}}
.c2{{position:absolute;width:{int(w*0.6)}px;height:{int(w*0.6)}px;border-radius:50%;left:-{int(w*0.25)}px;bottom:{int(h*0.12)}px;background:rgba(37,99,235,.18)}}
h1{{position:absolute;left:{int(w*0.07)}px;right:{int(w*0.07)}px;top:{top}px;margin:0;color:#fff;font-size:{font}px;line-height:1.08;
font-weight:800;letter-spacing:-.02em;text-wrap:balance}}
.p{{position:absolute;left:{left}px;top:{phone_top}px;width:{phone_w}px;border:{max(8, w // 100)}px solid #070f1f;border-bottom:none;
border-radius:{int(min(phone_w, 1000)*0.075)}px {int(min(phone_w, 1000)*0.075)}px 0 0;overflow:hidden;box-shadow:0 30px 90px rgba(0,0,0,.5);background:#fff}}
.p img{{display:block;width:100%}}
</style><div class="s"><div class="c1"></div><div class="c2"></div><h1>{caption}</h1>
<div class="p"><img src="{uri(img)}"></div></div>'''


def feature_html(lang):
    a = RAW / 'phone' / lang / '02-autofill.png'
    b = RAW / 'phone' / lang / '04-signed.png'
    pills = ''.join(f'<span>{p}</span>' for p in PILLS[lang])
    return f'''<!doctype html><meta charset="utf-8"><style>
html,body{{margin:0;padding:0;width:1024px;height:500px;overflow:hidden;background:#0a1d3b}}
.f{{position:relative;width:1024px;height:500px;background:linear-gradient(135deg,#1c4f86 0%,#12335f 50%,#0a1d3b 100%);font-family:{FONT};overflow:hidden}}
.c1{{position:absolute;width:620px;height:620px;border-radius:50%;right:-120px;top:-250px;background:rgba(255,255,255,.07)}}
.c2{{position:absolute;width:380px;height:380px;border-radius:50%;left:-120px;bottom:-190px;background:rgba(37,99,235,.22)}}
.ic{{position:absolute;left:64px;top:92px;width:112px;height:112px;border-radius:26px;box-shadow:0 14px 34px rgba(0,0,0,.4)}}
h1{{position:absolute;left:64px;top:214px;margin:0;color:#fff;font-size:66px;font-weight:800;letter-spacing:-.02em;line-height:1}}
p{{position:absolute;left:64px;top:296px;width:470px;margin:0;color:#d4e3f7;font-size:29px;line-height:1.22;font-weight:500}}
.pills{{position:absolute;left:64px;top:410px;display:flex;gap:10px}}
.pills span{{padding:8px 18px;border-radius:999px;background:rgba(255,255,255,.14);color:#fff;font-size:20px;font-weight:600}}
.ph{{position:absolute;width:250px;border:7px solid #070f1f;border-bottom:none;border-radius:34px 34px 0 0;overflow:hidden;background:#fff;box-shadow:0 20px 50px rgba(0,0,0,.5)}}
.ph img{{display:block;width:100%}}
.a{{left:590px;top:70px;transform:rotate(-5deg)}}
.b{{left:780px;top:118px;transform:rotate(4deg)}}
</style><div class="f"><div class="c1"></div><div class="c2"></div>
<img class="ic" src="{uri(OUT / 'icon-512.png')}">
<h1>Compilo PDF</h1><p>{TAGLINE[lang]}</p><div class="pills">{pills}</div>
<div class="ph a"><img src="{uri(a)}"></div><div class="ph b"><img src="{uri(b)}"></div></div>'''


def build(devices):
    specs = {
        'phone': dict(w=1080, h=1920, font=78, top=92, phone_w=900, phone_top=420),
        'tablet10': dict(w=1600, h=2560, font=96, top=110, phone_w=1240, phone_top=520),
    }
    with tempfile.TemporaryDirectory() as tmp:
        for dev in devices:
            if dev == 'feature':
                for lang, loc in LOCALE.items():
                    page = Path(tmp) / f'feature-{lang}.html'
                    page.write_text(feature_html(lang), encoding='utf-8')
                    out = OUT / 'feature' / f'feature-graphic-{loc}.png'
                    render(page, out, 1024, 500)
                    print(out.name)
                continue
            sp = specs[dev]
            for lang, loc in LOCALE.items():
                n = 0
                for raw_name, key in SCENES:
                    src = RAW / dev / lang / f'{raw_name}.png'
                    if not src.exists():
                        continue
                    n += 1
                    page = Path(tmp) / f'{dev}-{lang}-{raw_name}.html'
                    page.write_text(shot_html(sp['w'], sp['h'], CAPTIONS[lang][key], src, font=sp['font'],
                                              top=sp['top'], phone_w=sp['phone_w'], phone_top=sp['phone_top'],
                                              landscape=sp.get('landscape', False)),
                                    encoding='utf-8')
                    out = OUT / 'screenshots' / dev / loc / f'{n:02d}-{key}.png'
                    render(page, out, sp['w'], sp['h'])
                print(dev, loc, n, 'shots')


if __name__ == '__main__':
    build(sys.argv[1:] or ['phone', 'feature'])
