"""Writes store/listings/<play-locale>/{title,short,full,whatsnew}.txt and checks Play's limits.

Run:  python store/tools/make_listings.py
Limits: title 30, short description 80, full description 4000, release notes 500.
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

TITLE = 'Compilo PDF'

L = {
    'en-US': dict(
        short='Fill, sign and convert PDFs to Word. Offline, private, no account.',
        whatsnew='First release: fill and sign PDFs, convert them to Word, print and share. Everything stays on your phone.',
        full='''Compilo PDF fills in, signs and converts your PDF documents right on your phone. No account, no internet connection, no ads: your documents never leave your device.

FILL FORMS FASTER
• Finds the blanks in any PDF: underlines, dotted lines, boxes, one-letter-per-cell fields, table cells and standard form fields.
• Enter your details once (name, address, tax code or ID number, phone, email…) and Compilo PDF fills the recurring fields of every form for you, in the same font and size as the document.
• It learns as you go: type the same value in the same field three times and it will fill it in by itself from then on.
• Add free text, today's date, ticks, crosses, dots, images or text from the clipboard anywhere on the page.

SIGN WITH YOUR FINGER
• Draw your signature on the screen, choose the thickness and save it to reuse in one tap.
• Place it exactly where it belongs, move it, resize it, redo it.

PDF TO WORD, OFFLINE
• Converts a PDF into an editable Word document keeping text, columns, tables and images in place.
• Values you have filled in end up inside their line, not floating on top of it.
• Open the result in Word, Google Docs or any other app, or save and share it.

EVERYTHING YOU NEED FOR THE FINAL DOCUMENT
• Print to any printer or save as PDF.
• Rotate, insert or delete pages.
• "Make final" turns fields and signatures into part of the page before you send it.
• Undo and redo, automatic saving, password-protected PDFs supported.
• Open a PDF from another app, or share it with Compilo PDF from your email, chat or file manager.

PRIVATE BY DESIGN
• No internet permission, no tracking, no advertising, no account.
• Your details, signatures and documents are stored only in the app's private space on your phone.
• Cloud backup of the app's data is switched off.

Available in Italian, English, French, German and Spanish. Works on phones and tablets, in light and dark mode.''',
    ),
    'it-IT': dict(
        short='Compila, firma e converti PDF in Word. Offline, privato, senza account.',
        whatsnew='Prima versione: compila e firma i PDF, convertili in Word, stampa e condividi. Tutto resta sul tuo telefono.',
        full='''Compilo PDF compila, firma e converte i tuoi documenti PDF direttamente sul telefono. Nessun account, nessuna connessione a internet, nessuna pubblicità: i tuoi documenti non lasciano mai il dispositivo.

COMPILA I MODULI PIÙ IN FRETTA
• Trova gli spazi da compilare in qualsiasi PDF: righe, puntini, riquadri, caselle una lettera per cella, celle di tabella e campi modulo standard.
• Inserisci i tuoi dati una volta sola (nome, indirizzo, codice fiscale, telefono, email…) e Compilo PDF compila al posto tuo i campi ricorrenti di ogni modulo, con lo stesso carattere e la stessa dimensione del documento.
• Impara mentre lo usi: se scrivi tre volte lo stesso valore nello stesso campo, da quel momento lo compila da solo.
• Aggiungi testo libero, la data di oggi, spunte, croci, pallini, immagini o testo dagli appunti dove vuoi sulla pagina.

FIRMA CON IL DITO
• Disegna la firma sullo schermo, scegli lo spessore e salvala per riutilizzarla con un tocco.
• Posizionala esattamente dove serve, spostala, ridimensionala, rifalla.

PDF IN WORD, OFFLINE
• Trasforma un PDF in un documento Word modificabile mantenendo testo, colonne, tabelle e immagini al loro posto.
• I valori che hai compilato finiscono dentro la loro riga, non sovrapposti.
• Apri il risultato con Word, Google Documenti o qualsiasi altra app, oppure salvalo e condividilo.

TUTTO PER IL DOCUMENTO FINALE
• Stampa su qualsiasi stampante o salva come PDF.
• Ruota, inserisci o elimina pagine.
• «Rendi definitivo» trasforma campi e firme in parte della pagina prima dell'invio.
• Annulla e ripristina, salvataggio automatico, PDF protetti da password supportati.
• Apri un PDF da un'altra app, o condividilo con Compilo PDF da email, chat o gestione file.

PRIVATO PER SCELTA
• Nessun permesso internet, nessun tracciamento, nessuna pubblicità, nessun account.
• I tuoi dati, le firme e i documenti restano solo nello spazio privato dell'app sul telefono.
• Il backup nel cloud dei dati dell'app è disattivato.

Disponibile in italiano, inglese, francese, tedesco e spagnolo. Funziona su telefoni e tablet, con tema chiaro e scuro.''',
    ),
    'fr-FR': dict(
        short='Remplissez, signez et convertissez vos PDF en Word. Hors ligne, privé.',
        whatsnew='Première version : remplissez et signez vos PDF, convertissez-les en Word, imprimez et partagez. Tout reste sur votre téléphone.',
        full='''Compilo PDF remplit, signe et convertit vos documents PDF directement sur votre téléphone. Pas de compte, pas de connexion internet, pas de publicité : vos documents ne quittent jamais votre appareil.

REMPLISSEZ LES FORMULAIRES PLUS VITE
• Repère les zones à remplir dans n'importe quel PDF : lignes, pointillés, cadres, cases à une lettre par case, cellules de tableau et champs de formulaire standard.
• Saisissez vos informations une seule fois (nom, adresse, numéro d'identification fiscale, téléphone, e-mail…) et Compilo PDF remplit à votre place les champs récurrents de chaque formulaire, avec la même police et la même taille que le document.
• Il apprend au fur et à mesure : saisissez trois fois la même valeur dans le même champ et il la remplira tout seul ensuite.
• Ajoutez du texte libre, la date du jour, des coches, des croix, des points, des images ou du texte du presse-papiers où vous voulez sur la page.

SIGNEZ DU DOIGT
• Dessinez votre signature à l'écran, choisissez l'épaisseur et enregistrez-la pour la réutiliser en un geste.
• Placez-la exactement où il faut, déplacez-la, redimensionnez-la, recommencez-la.

PDF VERS WORD, HORS LIGNE
• Transforme un PDF en document Word modifiable en conservant le texte, les colonnes, les tableaux et les images à leur place.
• Les valeurs que vous avez saisies se retrouvent dans leur ligne, pas par-dessus.
• Ouvrez le résultat dans Word, Google Docs ou n'importe quelle autre application, ou enregistrez-le et partagez-le.

TOUT POUR LE DOCUMENT FINAL
• Imprimez sur n'importe quelle imprimante ou enregistrez en PDF.
• Pivotez, insérez ou supprimez des pages.
• « Rendre définitif » intègre champs et signatures à la page avant l'envoi.
• Annuler et rétablir, enregistrement automatique, PDF protégés par mot de passe pris en charge.
• Ouvrez un PDF depuis une autre application, ou partagez-le avec Compilo PDF depuis votre messagerie, votre chat ou votre gestionnaire de fichiers.

PRIVÉ PAR CONCEPTION
• Aucune autorisation internet, aucun suivi, aucune publicité, aucun compte.
• Vos informations, signatures et documents restent uniquement dans l'espace privé de l'application sur votre téléphone.
• La sauvegarde cloud des données de l'application est désactivée.

Disponible en italien, anglais, français, allemand et espagnol. Fonctionne sur téléphones et tablettes, en mode clair et sombre.''',
    ),
    'de-DE': dict(
        short='PDFs ausfüllen, unterschreiben und in Word umwandeln. Offline, privat.',
        whatsnew='Erste Version: PDFs ausfüllen und unterschreiben, in Word umwandeln, drucken und teilen. Alles bleibt auf Ihrem Telefon.',
        full='''Compilo PDF füllt Ihre PDF-Dokumente aus, unterschreibt sie und wandelt sie um – direkt auf Ihrem Telefon. Kein Konto, keine Internetverbindung, keine Werbung: Ihre Dokumente verlassen nie Ihr Gerät.

FORMULARE SCHNELLER AUSFÜLLEN
• Findet die auszufüllenden Stellen in jedem PDF: Linien, Punktreihen, Kästchen, Felder mit einem Buchstaben pro Kästchen, Tabellenzellen und Standard-Formularfelder.
• Geben Sie Ihre Daten einmal ein (Name, Adresse, Steuer- oder Ausweisnummer, Telefon, E-Mail …) und Compilo PDF füllt die wiederkehrenden Felder jedes Formulars für Sie aus – in derselben Schrift und Größe wie das Dokument.
• Lernt beim Benutzen: Geben Sie denselben Wert dreimal in dasselbe Feld ein, füllt es ihn danach selbst aus.
• Fügen Sie freien Text, das heutige Datum, Häkchen, Kreuze, Punkte, Bilder oder Text aus der Zwischenablage an beliebiger Stelle der Seite ein.

MIT DEM FINGER UNTERSCHREIBEN
• Zeichnen Sie Ihre Unterschrift auf dem Bildschirm, wählen Sie die Strichstärke und speichern Sie sie für die Wiederverwendung mit einem Tipp.
• Platzieren Sie sie genau dort, wo sie hingehört, verschieben Sie sie, ändern Sie die Größe, zeichnen Sie sie neu.

PDF IN WORD, OFFLINE
• Wandelt ein PDF in ein bearbeitbares Word-Dokument um und behält Text, Spalten, Tabellen und Bilder an ihrem Platz.
• Ausgefüllte Werte stehen in ihrer Zeile und schweben nicht darüber.
• Öffnen Sie das Ergebnis in Word, Google Docs oder einer anderen App – oder speichern und teilen Sie es.

ALLES FÜR DAS FERTIGE DOKUMENT
• Auf jedem Drucker drucken oder als PDF speichern.
• Seiten drehen, einfügen oder löschen.
• „Endgültig machen“ macht Felder und Unterschriften vor dem Versand zum Teil der Seite.
• Rückgängig und Wiederholen, automatisches Speichern, passwortgeschützte PDFs werden unterstützt.
• Öffnen Sie ein PDF aus einer anderen App oder teilen Sie es aus E-Mail, Chat oder Dateimanager mit Compilo PDF.

PRIVAT AUS PRINZIP
• Keine Internetberechtigung, kein Tracking, keine Werbung, kein Konto.
• Ihre Daten, Unterschriften und Dokumente liegen nur im privaten Bereich der App auf Ihrem Telefon.
• Die Cloud-Sicherung der App-Daten ist deaktiviert.

Verfügbar in Italienisch, Englisch, Französisch, Deutsch und Spanisch. Für Smartphones und Tablets, im hellen und dunklen Design.''',
    ),
    'es-ES': dict(
        short='Rellena, firma y convierte PDF a Word. Sin conexión, privado, sin cuenta.',
        whatsnew='Primera versión: rellena y firma PDF, conviértelos a Word, imprime y comparte. Todo se queda en tu teléfono.',
        full='''Compilo PDF rellena, firma y convierte tus documentos PDF directamente en el teléfono. Sin cuenta, sin conexión a internet, sin anuncios: tus documentos nunca salen de tu dispositivo.

RELLENA FORMULARIOS MÁS RÁPIDO
• Encuentra los espacios por completar en cualquier PDF: líneas, puntos suspensivos, recuadros, casillas de una letra por celda, celdas de tabla y campos de formulario estándar.
• Introduce tus datos una sola vez (nombre, dirección, NIF o número de identificación, teléfono, correo…) y Compilo PDF rellena por ti los campos recurrentes de cada formulario, con la misma fuente y el mismo tamaño que el documento.
• Aprende sobre la marcha: si escribes tres veces el mismo valor en el mismo campo, desde entonces lo rellena él solo.
• Añade texto libre, la fecha de hoy, marcas, cruces, puntos, imágenes o texto del portapapeles donde quieras en la página.

FIRMA CON EL DEDO
• Dibuja tu firma en la pantalla, elige el grosor y guárdala para reutilizarla con un toque.
• Colócala justo donde corresponde, muévela, cambia su tamaño, vuelve a hacerla.

PDF A WORD, SIN CONEXIÓN
• Convierte un PDF en un documento Word editable manteniendo texto, columnas, tablas e imágenes en su sitio.
• Los valores que has rellenado quedan dentro de su línea, no encima.
• Abre el resultado en Word, Google Docs o cualquier otra aplicación, o guárdalo y compártelo.

TODO PARA EL DOCUMENTO FINAL
• Imprime en cualquier impresora o guarda como PDF.
• Gira, inserta o elimina páginas.
• «Hacer definitivo» convierte campos y firmas en parte de la página antes de enviarla.
• Deshacer y rehacer, guardado automático, compatible con PDF protegidos con contraseña.
• Abre un PDF desde otra aplicación, o compártelo con Compilo PDF desde el correo, el chat o el gestor de archivos.

PRIVADO POR DISEÑO
• Sin permiso de internet, sin seguimiento, sin publicidad, sin cuenta.
• Tus datos, firmas y documentos se guardan solo en el espacio privado de la aplicación en tu teléfono.
• La copia de seguridad en la nube de los datos de la aplicación está desactivada.

Disponible en italiano, inglés, francés, alemán y español. Funciona en teléfonos y tablets, con tema claro y oscuro.''',
    ),
}

LIMITS = dict(title=30, short=80, full=4000, whatsnew=500)
root = Path(__file__).resolve().parent.parent / 'listings'
ok = True
for loc, d in L.items():
    d = dict(d, title=TITLE)
    out = root / loc
    out.mkdir(parents=True, exist_ok=True)
    for k, v in d.items():
        if len(v) > LIMITS[k]:
            ok = False
            print(f'TOO LONG {loc}/{k}: {len(v)} > {LIMITS[k]}')
        (out / f'{k}.txt').write_text(v.strip() + '\n', encoding='utf-8')
    print(loc, {k: len(v) for k, v in d.items()})
sys.exit(0 if ok else 1)
