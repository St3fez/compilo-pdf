"""Builds the GitHub Pages site into docs/ : landing + privacy policy in 5 languages.

Run:  python store/tools/build_site.py
"""
import html
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

REPO = 'St3fez/compilo-pdf'
BASE = 'https://st3fez.github.io/compilo-pdf'
ISSUES = f'https://github.com/{REPO}/issues'
UPDATED = {'en': '23 October 2026', 'it': '23 ottobre 2026', 'fr': '23 octobre 2026',
           'de': '23. Oktober 2026', 'es': '23 de octubre de 2026'}
NAMES = {'en': 'English', 'it': 'Italiano', 'fr': 'Français', 'de': 'Deutsch', 'es': 'Español'}

T = {
    'en': dict(
        tagline='Fill, sign and convert your PDFs',
        sub='Everything stays on your phone. No account, no internet permission, no ads.',
        soon='Coming soon on Google Play',
        features=[
            ('Fill forms faster', 'Finds the blanks in any PDF and fills the recurring ones from your details, in the document\'s own font and size.'),
            ('Sign with your finger', 'Draw your signature once, save it, place it anywhere on the page.'),
            ('PDF to Word, offline', 'Editable Word documents with text, columns, tables and images in place.'),
            ('Private by design', 'No internet permission, no tracking, no advertising. Cloud backup is off.'),
        ],
        privacy='Privacy policy', home='Home', back='Back to the app page',
        title='Privacy Policy – Compilo PDF',
        h1='Privacy Policy',
        updated='Last updated',
        sections=[
            ('In short', ['Compilo PDF does not collect, transmit, sell or share any personal data. The app works entirely on your phone and has no permission to use the internet.']),
            ('What the app keeps on your phone', [
                'To work, the app stores the following in its private storage on your device, where other apps cannot read it:',
                '<ul><li>the PDF documents you open or import, with the changes you make;</li><li>the details you enter under “My details” (for example name, address, tax or ID number, phone, email);</li><li>the signatures you choose to save;</li><li>the values the app learns after you type them repeatedly in the same field;</li><li>technical files such as temporary copies used to print, share or convert a document.</li></ul>',
                'None of this is sent to the developer or to anyone else. You can remove a document from the app at any time, forget learned values in “My details”, and delete everything by clearing the app\'s storage or uninstalling it.']),
            ('Permissions and network', ['The app does not request the internet permission, so it cannot send data over the network. It does not request access to your photos, contacts, location, camera, microphone or storage: files reach the app only when you pick them with Android\'s file picker or share them with the app.']),
            ('When you share or open a file with another app', ['If you choose Share, Open with, Save or Print, the file is handed to the app, printer or service you select. From that moment the policy of that app or service applies; Compilo PDF has no control over it and receives nothing back.']),
            ('No third parties', ['Compilo PDF contains no advertising, analytics, crash-reporting or tracking software, and no component that collects data about you or your device.']),
            ('Backups', ['Cloud backup of the app\'s data is switched off, so your documents and details are not uploaded to your Google account. Android may still copy them directly to a new phone if you use its phone-to-phone transfer.']),
            ('Children', ['The app is not directed at children and, since it collects no data, it knows nothing about its users\' age.']),
            ('Your rights', ['Because the developer holds no data about you, there is nothing to access, correct or erase on the developer\'s side. You are in full control of the data stored in the app. If you have questions about your rights under the GDPR or other laws, contact us using the link below.']),
            ('Changes to this policy', ['If the app\'s data practices ever change, this page will be updated and the date above changed before the new version is released.']),
            ('Contact', [f'Compilo PDF is developed by an independent developer. Questions about privacy can be sent through <a href="{ISSUES}">{ISSUES}</a>.']),
        ]),
    'it': dict(
        tagline='Compila, firma e converti i tuoi PDF',
        sub='Tutto resta sul tuo telefono. Nessun account, nessun permesso internet, nessuna pubblicità.',
        soon='Prossimamente su Google Play',
        features=[
            ('Compila i moduli più in fretta', 'Trova gli spazi da compilare in qualsiasi PDF e riempie quelli ricorrenti con i tuoi dati, con il carattere e la dimensione del documento.'),
            ('Firma con il dito', 'Disegna la firma una volta, salvala, mettila dove vuoi sulla pagina.'),
            ('PDF in Word, offline', 'Documenti Word modificabili con testo, colonne, tabelle e immagini al loro posto.'),
            ('Privato per scelta', 'Nessun permesso internet, nessun tracciamento, nessuna pubblicità. Il backup nel cloud è disattivato.'),
        ],
        privacy='Informativa sulla privacy', home='Home', back='Torna alla pagina dell\'app',
        title='Informativa sulla privacy – Compilo PDF',
        h1='Informativa sulla privacy',
        updated='Ultimo aggiornamento',
        sections=[
            ('In breve', ['Compilo PDF non raccoglie, non trasmette, non vende e non condivide dati personali. L\'app funziona interamente sul tuo telefono e non ha il permesso di usare internet.']),
            ('Cosa conserva l\'app sul tuo telefono', [
                'Per funzionare, l\'app salva nel proprio spazio privato sul dispositivo, dove le altre app non possono leggerlo:',
                '<ul><li>i documenti PDF che apri o importi, con le modifiche che fai;</li><li>i dati che inserisci in «I miei dati» (ad esempio nome, indirizzo, codice fiscale o documento, telefono, email);</li><li>le firme che scegli di salvare;</li><li>i valori che l\'app impara dopo che li scrivi più volte nello stesso campo;</li><li>file tecnici, come le copie temporanee usate per stampare, condividere o convertire un documento.</li></ul>',
                'Niente di tutto questo viene inviato allo sviluppatore o a terzi. Puoi rimuovere un documento dall\'app in qualsiasi momento, far dimenticare i valori appresi in «I miei dati» e cancellare tutto svuotando la memoria dell\'app o disinstallandola.']),
            ('Permessi e rete', ['L\'app non richiede il permesso internet, quindi non può inviare dati in rete. Non richiede l\'accesso a foto, contatti, posizione, fotocamera, microfono o archivio: i file arrivano all\'app solo quando li scegli con il selettore di file di Android o li condividi con l\'app.']),
            ('Quando condividi o apri un file con un\'altra app', ['Se scegli Condividi, Apri con, Salva o Stampa, il file viene consegnato all\'app, alla stampante o al servizio che selezioni. Da quel momento vale l\'informativa di quell\'app o servizio; Compilo PDF non ne ha il controllo e non riceve nulla in cambio.']),
            ('Nessuna terza parte', ['Compilo PDF non contiene pubblicità, strumenti di analisi, di segnalazione errori o di tracciamento, né componenti che raccolgano dati su di te o sul tuo dispositivo.']),
            ('Backup', ['Il backup nel cloud dei dati dell\'app è disattivato: i tuoi documenti e i tuoi dati non vengono caricati sul tuo account Google. Android può comunque copiarli direttamente su un nuovo telefono se usi il trasferimento da telefono a telefono.']),
            ('Minori', ['L\'app non è rivolta ai minori e, poiché non raccoglie dati, non sa nulla dell\'età di chi la usa.']),
            ('I tuoi diritti', ['Poiché lo sviluppatore non detiene alcun dato su di te, non c\'è nulla da accedere, rettificare o cancellare presso di lui. Hai il pieno controllo dei dati salvati nell\'app. Per domande sui tuoi diritti ai sensi del GDPR o di altre leggi, scrivici tramite il link qui sotto.']),
            ('Modifiche a questa informativa', ['Se le pratiche sui dati dell\'app dovessero cambiare, questa pagina verrà aggiornata e la data qui sopra modificata prima del rilascio della nuova versione.']),
            ('Contatti', [f'Compilo PDF è sviluppata da uno sviluppatore indipendente. Le domande sulla privacy possono essere inviate tramite <a href="{ISSUES}">{ISSUES}</a>.']),
        ]),
    'fr': dict(
        tagline='Remplissez, signez et convertissez vos PDF',
        sub='Tout reste sur votre téléphone. Pas de compte, pas d\'autorisation internet, pas de publicité.',
        soon='Bientôt sur Google Play',
        features=[
            ('Remplissez plus vite', 'Repère les zones à remplir dans n\'importe quel PDF et remplit les champs récurrents avec vos informations, dans la police et la taille du document.'),
            ('Signez du doigt', 'Dessinez votre signature une fois, enregistrez-la, placez-la où vous voulez sur la page.'),
            ('PDF vers Word, hors ligne', 'Documents Word modifiables, avec texte, colonnes, tableaux et images à leur place.'),
            ('Privé par conception', 'Aucune autorisation internet, aucun suivi, aucune publicité. La sauvegarde cloud est désactivée.'),
        ],
        privacy='Politique de confidentialité', home='Accueil', back='Retour à la page de l\'application',
        title='Politique de confidentialité – Compilo PDF',
        h1='Politique de confidentialité',
        updated='Dernière mise à jour',
        sections=[
            ('En bref', ['Compilo PDF ne collecte, ne transmet, ne vend et ne partage aucune donnée personnelle. L\'application fonctionne entièrement sur votre téléphone et n\'a pas l\'autorisation d\'utiliser internet.']),
            ('Ce que l\'application conserve sur votre téléphone', [
                'Pour fonctionner, l\'application enregistre dans son espace privé sur votre appareil, où les autres applications ne peuvent pas le lire :',
                '<ul><li>les documents PDF que vous ouvrez ou importez, avec vos modifications ;</li><li>les informations saisies dans « Mes informations » (par exemple nom, adresse, numéro fiscal ou d\'identité, téléphone, e-mail) ;</li><li>les signatures que vous choisissez d\'enregistrer ;</li><li>les valeurs que l\'application apprend après que vous les avez saisies plusieurs fois dans le même champ ;</li><li>des fichiers techniques, comme les copies temporaires servant à imprimer, partager ou convertir un document.</li></ul>',
                'Rien de tout cela n\'est envoyé au développeur ni à quiconque. Vous pouvez retirer un document de l\'application à tout moment, faire oublier les valeurs apprises dans « Mes informations » et tout supprimer en effaçant les données de l\'application ou en la désinstallant.']),
            ('Autorisations et réseau', ['L\'application ne demande pas l\'autorisation internet : elle ne peut donc envoyer aucune donnée sur le réseau. Elle ne demande l\'accès ni à vos photos, contacts, position, appareil photo, micro ou stockage : les fichiers n\'arrivent dans l\'application que lorsque vous les choisissez avec le sélecteur de fichiers d\'Android ou que vous les partagez avec elle.']),
            ('Lorsque vous partagez ou ouvrez un fichier avec une autre application', ['Si vous choisissez Partager, Ouvrir avec, Enregistrer ou Imprimer, le fichier est remis à l\'application, à l\'imprimante ou au service que vous sélectionnez. À partir de là, la politique de cette application ou de ce service s\'applique ; Compilo PDF n\'en a pas le contrôle et ne reçoit rien en retour.']),
            ('Aucun tiers', ['Compilo PDF ne contient ni publicité, ni outil d\'analyse, de rapport de plantage ou de suivi, ni composant qui collecte des données sur vous ou votre appareil.']),
            ('Sauvegardes', ['La sauvegarde cloud des données de l\'application est désactivée : vos documents et vos informations ne sont pas envoyés vers votre compte Google. Android peut toutefois les copier directement vers un nouveau téléphone si vous utilisez son transfert de téléphone à téléphone.']),
            ('Enfants', ['L\'application ne s\'adresse pas aux enfants et, ne collectant aucune donnée, ne sait rien de l\'âge de ses utilisateurs.']),
            ('Vos droits', ['Le développeur ne détenant aucune donnée vous concernant, il n\'y a rien à consulter, rectifier ou effacer de son côté. Vous contrôlez entièrement les données enregistrées dans l\'application. Pour toute question sur vos droits au titre du RGPD ou d\'autres lois, contactez-nous via le lien ci-dessous.']),
            ('Modifications de cette politique', ['Si les pratiques de l\'application en matière de données devaient changer, cette page serait mise à jour et la date ci-dessus modifiée avant la publication de la nouvelle version.']),
            ('Contact', [f'Compilo PDF est développée par un développeur indépendant. Les questions sur la confidentialité peuvent être envoyées via <a href="{ISSUES}">{ISSUES}</a>.']),
        ]),
    'de': dict(
        tagline='PDFs ausfüllen, unterschreiben und umwandeln',
        sub='Alles bleibt auf Ihrem Telefon. Kein Konto, keine Internetberechtigung, keine Werbung.',
        soon='Demnächst bei Google Play',
        features=[
            ('Formulare schneller ausfüllen', 'Findet die auszufüllenden Stellen in jedem PDF und füllt die wiederkehrenden mit Ihren Daten aus – in Schrift und Größe des Dokuments.'),
            ('Mit dem Finger unterschreiben', 'Unterschrift einmal zeichnen, speichern und an beliebiger Stelle der Seite platzieren.'),
            ('PDF in Word, offline', 'Bearbeitbare Word-Dokumente mit Text, Spalten, Tabellen und Bildern an ihrem Platz.'),
            ('Privat aus Prinzip', 'Keine Internetberechtigung, kein Tracking, keine Werbung. Die Cloud-Sicherung ist aus.'),
        ],
        privacy='Datenschutzerklärung', home='Startseite', back='Zurück zur App-Seite',
        title='Datenschutzerklärung – Compilo PDF',
        h1='Datenschutzerklärung',
        updated='Zuletzt aktualisiert',
        sections=[
            ('Kurz gesagt', ['Compilo PDF erhebt, überträgt, verkauft oder teilt keine personenbezogenen Daten. Die App arbeitet vollständig auf Ihrem Telefon und hat keine Berechtigung, das Internet zu nutzen.']),
            ('Was die App auf Ihrem Telefon speichert', [
                'Damit die App funktioniert, speichert sie in ihrem privaten Speicherbereich auf Ihrem Gerät, den andere Apps nicht lesen können:',
                '<ul><li>die PDF-Dokumente, die Sie öffnen oder importieren, samt Ihren Änderungen;</li><li>die Angaben, die Sie unter „Meine Daten“ eintragen (zum Beispiel Name, Adresse, Steuer- oder Ausweisnummer, Telefon, E-Mail);</li><li>die Unterschriften, die Sie speichern;</li><li>Werte, die die App lernt, nachdem Sie sie mehrfach in dasselbe Feld eingegeben haben;</li><li>technische Dateien, etwa temporäre Kopien zum Drucken, Teilen oder Umwandeln eines Dokuments.</li></ul>',
                'Nichts davon wird an den Entwickler oder an Dritte gesendet. Sie können ein Dokument jederzeit aus der App entfernen, gelernte Werte unter „Meine Daten“ vergessen lassen und alles löschen, indem Sie den App-Speicher leeren oder die App deinstallieren.']),
            ('Berechtigungen und Netzwerk', ['Die App fordert die Internetberechtigung nicht an und kann daher keine Daten über das Netzwerk senden. Sie fordert keinen Zugriff auf Fotos, Kontakte, Standort, Kamera, Mikrofon oder Speicher an: Dateien gelangen nur in die App, wenn Sie sie mit der Android-Dateiauswahl auswählen oder mit der App teilen.']),
            ('Wenn Sie eine Datei mit einer anderen App teilen oder öffnen', ['Wenn Sie Teilen, Öffnen mit, Speichern oder Drucken wählen, wird die Datei an die von Ihnen gewählte App, den Drucker oder den Dienst übergeben. Ab dann gilt die Datenschutzerklärung dieser App oder dieses Dienstes; Compilo PDF hat darauf keinen Einfluss und erhält nichts zurück.']),
            ('Keine Dritten', ['Compilo PDF enthält weder Werbung noch Analyse-, Absturzberichts- oder Tracking-Software noch Komponenten, die Daten über Sie oder Ihr Gerät erfassen.']),
            ('Sicherungen', ['Die Cloud-Sicherung der App-Daten ist deaktiviert, Ihre Dokumente und Angaben werden also nicht in Ihr Google-Konto hochgeladen. Android kann sie bei der direkten Telefon-zu-Telefon-Übertragung dennoch auf ein neues Telefon kopieren.']),
            ('Kinder', ['Die App richtet sich nicht an Kinder und weiß, da sie keine Daten erhebt, nichts über das Alter ihrer Nutzer.']),
            ('Ihre Rechte', ['Da der Entwickler keine Daten über Sie besitzt, gibt es auf seiner Seite nichts, was Sie einsehen, berichtigen oder löschen lassen könnten. Sie haben die volle Kontrolle über die in der App gespeicherten Daten. Bei Fragen zu Ihren Rechten nach der DSGVO oder anderen Gesetzen wenden Sie sich über den Link unten an uns.']),
            ('Änderungen dieser Erklärung', ['Sollte sich der Umgang der App mit Daten ändern, wird diese Seite aktualisiert und das Datum oben geändert, bevor die neue Version erscheint.']),
            ('Kontakt', [f'Compilo PDF wird von einem unabhängigen Entwickler betrieben. Fragen zum Datenschutz können über <a href="{ISSUES}">{ISSUES}</a> gestellt werden.']),
        ]),
    'es': dict(
        tagline='Rellena, firma y convierte tus PDF',
        sub='Todo se queda en tu teléfono. Sin cuenta, sin permiso de internet, sin anuncios.',
        soon='Próximamente en Google Play',
        features=[
            ('Rellena formularios más rápido', 'Encuentra los espacios por completar en cualquier PDF y rellena los recurrentes con tus datos, con la fuente y el tamaño del documento.'),
            ('Firma con el dedo', 'Dibuja tu firma una vez, guárdala y colócala donde quieras en la página.'),
            ('PDF a Word, sin conexión', 'Documentos Word editables con texto, columnas, tablas e imágenes en su sitio.'),
            ('Privado por diseño', 'Sin permiso de internet, sin seguimiento, sin publicidad. La copia en la nube está desactivada.'),
        ],
        privacy='Política de privacidad', home='Inicio', back='Volver a la página de la aplicación',
        title='Política de privacidad – Compilo PDF',
        h1='Política de privacidad',
        updated='Última actualización',
        sections=[
            ('En resumen', ['Compilo PDF no recopila, transmite, vende ni comparte datos personales. La aplicación funciona por completo en tu teléfono y no tiene permiso para usar internet.']),
            ('Qué guarda la aplicación en tu teléfono', [
                'Para funcionar, la aplicación guarda en su espacio privado de tu dispositivo, donde otras aplicaciones no pueden leerlo:',
                '<ul><li>los documentos PDF que abres o importas, con los cambios que haces;</li><li>los datos que introduces en «Mis datos» (por ejemplo nombre, dirección, NIF o número de identificación, teléfono, correo);</li><li>las firmas que decides guardar;</li><li>los valores que la aplicación aprende después de que los escribas varias veces en el mismo campo;</li><li>archivos técnicos, como las copias temporales usadas para imprimir, compartir o convertir un documento.</li></ul>',
                'Nada de esto se envía al desarrollador ni a nadie más. Puedes quitar un documento de la aplicación en cualquier momento, hacer que olvide los valores aprendidos en «Mis datos» y borrarlo todo vaciando el almacenamiento de la aplicación o desinstalándola.']),
            ('Permisos y red', ['La aplicación no solicita el permiso de internet, por lo que no puede enviar datos por la red. No solicita acceso a tus fotos, contactos, ubicación, cámara, micrófono ni almacenamiento: los archivos llegan a la aplicación solo cuando los eliges con el selector de archivos de Android o los compartes con ella.']),
            ('Cuando compartes o abres un archivo con otra aplicación', ['Si eliges Compartir, Abrir con, Guardar o Imprimir, el archivo se entrega a la aplicación, impresora o servicio que selecciones. Desde ese momento se aplica la política de esa aplicación o servicio; Compilo PDF no la controla y no recibe nada a cambio.']),
            ('Sin terceros', ['Compilo PDF no contiene publicidad, herramientas de análisis, de informe de errores ni de seguimiento, ni ningún componente que recopile datos sobre ti o tu dispositivo.']),
            ('Copias de seguridad', ['La copia de seguridad en la nube de los datos de la aplicación está desactivada: tus documentos y datos no se suben a tu cuenta de Google. Android aún puede copiarlos directamente a un teléfono nuevo si usas su transferencia de teléfono a teléfono.']),
            ('Menores', ['La aplicación no está dirigida a menores y, como no recopila datos, no sabe nada de la edad de quienes la usan.']),
            ('Tus derechos', ['Como el desarrollador no conserva ningún dato sobre ti, no hay nada que consultar, rectificar o suprimir por su parte. Tienes pleno control de los datos guardados en la aplicación. Si tienes preguntas sobre tus derechos según el RGPD u otras leyes, escríbenos mediante el enlace de abajo.']),
            ('Cambios en esta política', ['Si las prácticas de la aplicación con los datos cambiaran, esta página se actualizaría y se modificaría la fecha de arriba antes de publicar la nueva versión.']),
            ('Contacto', [f'Compilo PDF está desarrollada por un desarrollador independiente. Las preguntas sobre privacidad pueden enviarse a través de <a href="{ISSUES}">{ISSUES}</a>.']),
        ]),
}

CSS = """:root{--bg:#f4f6fb;--card:#fff;--text:#0f172a;--muted:#475569;--accent:#2563eb;--navy:#0c2547;--line:#e2e8f0}
@media (prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2c;--text:#e6ebf5;--muted:#9fb0c8;--accent:#6ea0ff;--line:#22304a}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}
.wrap{max-width:760px;margin:0 auto;padding:20px 16px 56px}
header.top{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap;padding:8px 0 20px}
.brand{display:flex;align-items:center;gap:12px;text-decoration:none;color:var(--text);font-weight:700;font-size:18px}
.brand img{width:44px;height:44px;border-radius:12px;display:block}
nav.langs{display:flex;gap:6px;flex-wrap:wrap}
nav.langs a{padding:4px 10px;border-radius:999px;text-decoration:none;font-size:14px;color:var(--muted);border:1px solid var(--line)}
nav.langs a[aria-current=true]{background:var(--accent);border-color:var(--accent);color:#fff}
.hero{background:linear-gradient(135deg,#17406f,#0c2547);color:#fff;border-radius:24px;padding:36px 24px;margin:8px 0 24px}
.hero h1{margin:0 0 8px;font-size:clamp(26px,6vw,38px);line-height:1.15}
.hero p{margin:0;opacity:.92;font-size:18px}
.soon{display:inline-block;margin-top:20px;padding:10px 18px;border-radius:999px;background:rgba(255,255,255,.14);font-weight:600}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}
.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:18px 20px}
.card h2{margin:0 0 6px;font-size:18px}.card p{margin:0;color:var(--muted)}
h1.doc{font-size:clamp(26px,6vw,34px);line-height:1.2;margin:8px 0 4px}
.meta{color:var(--muted);margin:0 0 24px}
article h2{font-size:20px;margin:28px 0 6px}
article p,article li{color:var(--text)}
article ul{padding-left:22px}
footer{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);color:var(--muted);font-size:14px;display:flex;gap:16px;flex-wrap:wrap}
"""

ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108" role="img" aria-label="Compilo PDF">
  <defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#17406F"/><stop offset="1" stop-color="#0C2547"/></linearGradient></defs>
  <rect width="108" height="108" fill="url(#bg)"/>
  <g transform="translate(54 54) scale(1.3) translate(-54 -54)">
  <g transform="translate(1.2 1.8)" fill="#050E22" opacity=".3"><path d="M40 26h18l14 14v38a4 4 0 0 1-4 4H40a4 4 0 0 1-4-4V30a4 4 0 0 1 4-4Z"/></g>
  <path fill="#FFFFFF" d="M40 26h18l14 14v38a4 4 0 0 1-4 4H40a4 4 0 0 1-4-4V30a4 4 0 0 1 4-4Z"/>
  <path fill="#CBD5E1" d="M58 26v10a4 4 0 0 0 4 4h10Z"/>
  <rect x="41" y="44" width="18" height="3.4" rx="1.7" fill="#CBD5E1"/>
  <rect x="41" y="51" width="26" height="3.4" rx="1.7" fill="#CBD5E1"/>
  <path d="M41.5 69.5c2-7 4.2-10 5.6-7.2s-1 6.6 2 5.8 3-5.6 6-4.6 1.6 3.6 4.4 3.6" fill="none" stroke="#2563EB" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  <rect x="41" y="72.5" width="26" height="1.8" rx=".9" fill="#94A3B8"/>
  <g transform="translate(61 71) rotate(36)">
    <path d="M0 0L-3.2 -7.5H3.2Z" fill="#1E293B"/>
    <path d="M-1.9 -30h3.8a1.3 1.3 0 0 1 1.3 1.3V-8.8a1.3 1.3 0 0 1-1.3 1.3h-3.8a1.3 1.3 0 0 1-1.3-1.3V-28.7a1.3 1.3 0 0 1 1.3-1.3Z" fill="#F59E0B"/>
    <path d="M-1.9 -30h3.8a1.3 1.3 0 0 1 1.3 1.3V-25h-6.4V-28.7a1.3 1.3 0 0 1 1.3-1.3Z" fill="#D97706"/>
  </g></g>
</svg>
"""


def page(lang, kind):
    t = T[lang]
    prefix = '' if lang == 'en' else f'{lang}/'
    root = '' if lang == 'en' else '../'
    fname = 'index.html' if kind == 'index' else 'privacy.html'
    title = 'Compilo PDF – ' + t['tagline'] if kind == 'index' else t['title']
    desc = t['sub'] if kind == 'index' else t['sections'][0][1][0]
    langs = ''.join(
        f'<a href="{BASE}/{"" if l == "en" else l + "/"}{fname}" hreflang="{l}" lang="{l}"'
        f'{" aria-current=true" if l == lang else ""}>{NAMES[l]}</a>' for l in T)
    alt = ''.join(
        f'<link rel="alternate" hreflang="{l}" href="{BASE}/{"" if l == "en" else l + "/"}{fname}">' for l in T)
    if kind == 'index':
        feats = ''.join(f'<div class="card"><h2>{html.escape(h)}</h2><p>{html.escape(p)}</p></div>' for h, p in t['features'])
        body = (f'<section class="hero"><h1>Compilo PDF</h1><p>{html.escape(t["tagline"])}</p>'
                f'<p style="font-size:16px;margin-top:10px">{html.escape(t["sub"])}</p>'
                f'<span class="soon">{html.escape(t["soon"])}</span></section>'
                f'<div class="grid">{feats}</div>')
    else:
        secs = ''.join(
            f'<h2>{html.escape(h)}</h2>' + ''.join(p if p.startswith('<') else f'<p>{p if "<a " in p else html.escape(p)}</p>' for p in ps)
            for h, ps in t['sections'])
        body = (f'<article><h1 class="doc">{html.escape(t["h1"])}</h1>'
                f'<p class="meta">Compilo PDF · {html.escape(t["updated"])}: {UPDATED[lang]}</p>{secs}</article>')
    foot = (f'<footer><a href="{root}index.html">{html.escape(t["home"] if kind == "privacy" else "Compilo PDF")}</a>'
            f'<a href="{root}privacy.html" >{html.escape(t["privacy"])}</a>'
            f'<a href="{ISSUES}">GitHub</a></footer>')
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}/{prefix}{fname}">
{alt}
<link rel="icon" href="{root}assets/icon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{root}assets/style.css">
</head>
<body><div class="wrap">
<header class="top"><a class="brand" href="{root}index.html"><img src="{root}assets/icon-192.png" alt="" width="44" height="44">Compilo PDF</a><nav class="langs" aria-label="Language">{langs}</nav></header>
{body}
{foot}
</div></body></html>
'''


def main():
    docs = Path(__file__).resolve().parent.parent.parent / 'docs'
    (docs / 'assets').mkdir(parents=True, exist_ok=True)
    (docs / 'assets' / 'style.css').write_text(CSS, encoding='utf-8')
    (docs / 'assets' / 'icon.svg').write_text(ICON_SVG, encoding='utf-8')
    (docs / '.nojekyll').write_text('', encoding='utf-8')
    for lang in T:
        d = docs if lang == 'en' else docs / lang
        d.mkdir(parents=True, exist_ok=True)
        for kind in ('index', 'privacy'):
            (d / ('index.html' if kind == 'index' else 'privacy.html')).write_text(page(lang, kind), encoding='utf-8')
    print('site written to', docs)


main()
