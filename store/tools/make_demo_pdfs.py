"""Fictional registration forms (one per language) used for the store screenshots.

Writes store/demo/<name>.pdf (see FILES). Hand-written PDF, Helvetica, A4, labels followed by a
ruled line, a row of comb cells for the ID, a declaration and a signature line.
"""
import sys
from pathlib import Path

from PIL import ImageFont

sys.stdout.reconfigure(encoding='utf-8')

W, H = 595, 842
FILES = {'en': 'registration-form', 'it': 'modulo-iscrizione', 'fr': 'formulaire-inscription',
         'de': 'anmeldeformular', 'es': 'formulario-inscripcion'}
ARIAL = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', 100)  # same metrics as Helvetica
ARIAL_B = ImageFont.truetype(r'C:\Windows\Fonts\arialbd.ttf', 100)

T = {
    'en': dict(
        title='Course registration form', org='Example Cultural Association · Season 2026/27',
        s1='Personal details', s2='Contact', s3='Declaration',
        surname='Surname', name='First name', born='Date of birth', place='Place of birth',
        tax='Tax code / ID number', addr='Address', zip='Postal code', city='City',
        phone='Phone', email='Email', placedate='Place and date', sign='Signature',
        decl=['I, the undersigned, declare that the information given above is true and',
              'authorise Example Cultural Association to use it for the sole purpose of',
              'managing my registration.']),
    'it': dict(
        title='Modulo di iscrizione al corso', org='Associazione Culturale Esempio · Stagione 2026/27',
        s1='Dati personali', s2='Contatti', s3='Dichiarazione',
        surname='Cognome', name='Nome', born='Data di nascita', place='Luogo di nascita',
        tax='Codice fiscale', addr='Indirizzo', zip='CAP', city='Comune',
        phone='Telefono', email='Email', placedate='Luogo e data', sign='Firma',
        decl=['Il/La sottoscritto/a dichiara che i dati sopra riportati sono veritieri e',
              'autorizza l\'Associazione Culturale Esempio a utilizzarli al solo fine di',
              'gestire la propria iscrizione.']),
    'fr': dict(
        title='Formulaire d\'inscription au cours', org='Association culturelle Exemple · Saison 2026/27',
        s1='Données personnelles', s2='Contact', s3='Déclaration',
        surname='Nom', name='Prénom', born='Date de naissance', place='Lieu de naissance',
        tax='Numéro d\'identification fiscale', addr='Adresse', zip='Code postal', city='Ville',
        phone='Téléphone', email='E-mail', placedate='Lieu et date', sign='Signature',
        decl=['Je soussigné(e) déclare que les informations ci-dessus sont exactes et',
              'autorise l\'Association culturelle Exemple à les utiliser dans le seul but de',
              'gérer mon inscription.']),
    'de': dict(
        title='Anmeldeformular für den Kurs', org='Kulturverein Beispiel · Saison 2026/27',
        s1='Persönliche Daten', s2='Kontakt', s3='Erklärung',
        surname='Nachname', name='Vorname', born='Geburtsdatum', place='Geburtsort',
        tax='Steuer-ID', addr='Straße und Hausnummer', zip='PLZ', city='Wohnort',
        phone='Telefon', email='E-Mail', placedate='Ort, Datum', sign='Unterschrift',
        decl=['Ich erkläre, dass die obigen Angaben wahr sind, und ermächtige den',
              'Kulturverein Beispiel, sie ausschließlich zur Verwaltung meiner Anmeldung',
              'zu verwenden.']),
    'es': dict(
        title='Formulario de inscripción al curso', org='Asociación Cultural Ejemplo · Temporada 2026/27',
        s1='Datos personales', s2='Contacto', s3='Declaración',
        surname='Apellidos', name='Nombre', born='Fecha de nacimiento', place='Lugar de nacimiento',
        tax='DNI/NIE', addr='Domicilio', zip='Código postal', city='Localidad',
        phone='Teléfono', email='Correo electrónico', placedate='Lugar y fecha', sign='Firma',
        decl=['El abajo firmante declara que los datos anteriores son ciertos y autoriza',
              'a la Asociación Cultural Ejemplo a utilizarlos únicamente para gestionar su',
              'inscripción.']),
}


def esc(s):
    return s.replace('\\', '\\\\').replace('(', '\\(').replace(')', '\\)')


def width(text, size, bold=False):
    return (ARIAL_B if bold else ARIAL).getlength(text) * size / 100


def build(lang):
    t = T[lang]
    c = []

    def text(x, y, s, size=10, bold=False, gray=0.0):
        font = 'F2' if bold else 'F1'
        c.append(f'BT {gray} g /{font} {size} Tf {x:.1f} {y:.1f} Td ({esc(s)}) Tj ET')

    def line(x1, y, x2, w=0.6, gray=0.35):
        c.append(f'{gray} G {w} w {x1:.1f} {y:.1f} m {x2:.1f} {y:.1f} l S')

    def field(x, y, label, x_end):
        text(x, y, label, 10, gray=0.2)
        line(x + width(label, 10) + 8, y - 2, x_end)

    # header
    c.append('0.09 0.25 0.44 rg 0 782 595 60 re f')
    c.append('1 g BT /F2 19 Tf 50 806 Td (' + esc(t['title']) + ') Tj ET')
    c.append('0.8 0.86 0.95 g BT /F1 9 Tf 50 790 Td (' + esc(t['org']) + ') Tj ET')

    y = 735
    text(50, y, t['s1'], 12, bold=True, gray=0.09)
    line(50, y - 6, 545, 1.2, 0.09)
    y -= 38
    field(50, y, t['surname'], 280)
    field(310, y, t['name'], 545)
    y -= 36
    field(50, y, t['born'], 280)
    field(310, y, t['place'], 545)
    y -= 38
    text(50, y, t['tax'], 10, gray=0.2)
    x0 = 50 + width(t['tax'], 10) + 12
    n = 12
    cell = min(18, (545 - x0) / n)
    for i in range(n):
        c.append(f'0.35 G 0.6 w {x0 + i * cell:.1f} {y - 6:.1f} {cell:.1f} 20 re S')
    y -= 50
    text(50, y, t['s2'], 12, bold=True, gray=0.09)
    line(50, y - 6, 545, 1.2, 0.09)
    y -= 38
    field(50, y, t['addr'], 545)
    y -= 36
    field(50, y, t['zip'], 200)
    field(230, y, t['city'], 545)
    y -= 36
    field(50, y, t['phone'], 280)
    field(310, y, t['email'], 545)
    y -= 58
    text(50, y, t['s3'], 12, bold=True, gray=0.09)
    line(50, y - 6, 545, 1.2, 0.09)
    y -= 28
    for row in t['decl']:
        text(50, y, row, 10, gray=0.15)
        y -= 15
    y -= 40
    field(50, y, t['placedate'], 290)
    field(320, y, t['sign'], 545)
    content = '\n'.join(c).encode('cp1252')

    objs = [
        b'<< /Type /Catalog /Pages 2 0 R >>',
        b'<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
        b'<< /Type /Page /Parent 2 0 R /MediaBox [0 0 595 842] /Contents 6 0 R '
        b'/Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>',
        b'<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>',
        b'<< /Length ' + str(len(content)).encode() + b' >>\nstream\n' + content + b'\nendstream',
    ]
    out = bytearray(b'%PDF-1.7\n')
    offsets = []
    for i, o in enumerate(objs):
        offsets.append(len(out))
        out += f'{i + 1} 0 obj\n'.encode() + o + b'\nendobj\n'
    xref = len(out)
    out += f'xref\n0 {len(objs) + 1}\n0000000000 65535 f \n'.encode()
    for o in offsets:
        out += f'{o:010d} 00000 n \n'.encode()
    out += f'trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n'.encode()
    return bytes(out)


root = Path(__file__).resolve().parent.parent / 'demo'
root.mkdir(parents=True, exist_ok=True)
for lang in T:
    p = root / f'{FILES[lang]}.pdf'
    p.write_bytes(build(lang))
    print(p.name, p.stat().st_size)
