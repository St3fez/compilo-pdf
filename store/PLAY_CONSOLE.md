# Compilo PDF – checklist Play Console

Tutto quello che serve per pubblicare, nell'ordine in cui lo chiede la Console. I nomi delle voci
possono cambiare leggermente: contano le risposte.

| Dato | Valore |
| --- | --- |
| Nome app | Compilo PDF |
| ID pacchetto | `com.pdfcraft.pdfcraft_mobile` (non si può più cambiare dopo la prima pubblicazione) |
| Versione | 1.0.0 (versionCode 1) |
| Lingue | italiano, inglese, francese, tedesco, spagnolo |
| Lingua predefinita consigliata | Inglese (Stati Uniti), `en-US` |
| Categoria | Produttività (Strumenti/Produttività) |
| Prezzo | Gratuita, senza pubblicità né acquisti in-app |
| Sito web | https://st3fez.github.io/compilo-pdf/ |
| **Privacy policy** | **https://st3fez.github.io/compilo-pdf/privacy.html** (EN) · `/it/privacy.html` · `/fr/…` · `/de/…` · `/es/…` |
| Email di contatto (pubblica) | quella che scegli tu: la Console la chiede e la mostra nello store |

## 0. File pronti

```
store/release/compilo-pdf-1.0.0-1.aab        ← da caricare su Play (firmato con la chiave di upload)
store/release/compilo-pdf-1.0.0-1.apk        ← per provarlo a mano su un telefono (stessa firma)
store/listings/<lingua>/title|short|full|whatsnew.txt   ← testi della scheda, già nei limiti Play
store/graphics/icon-512.png                  ← icona 512×512
store/graphics/feature/feature-graphic-<lingua>.png      ← grafica in evidenza 1024×500
store/graphics/screenshots/phone/<lingua>/   ← 6 screenshot telefono 1080×1920
store/graphics/screenshots/tablet7/en-US/    ← tablet 7" 1200×1920
store/graphics/screenshots/tablet10/en-US/   ← tablet 10" 1600×2560
```

Lingue della scheda: `en-US`, `it-IT`, `fr-FR`, `de-DE`, `es-ES`.

**Chiave di upload** (fuori dal progetto, non finisce mai su GitHub):
`C:\Users\Pc\Documents\CompiloPDF-keys\upload-keystore.jks`, alias `upload`, password in
`android/key.properties`. **Fai una copia di backup in un posto sicuro.**
Impronta SHA-256: `79:FF:5C:73:75:CC:37:F5:79:2E:CC:A7:BE:89:BA:66:41:6B:F8:C6:B8:A2:F1:B2:A8:C4:21:C1:3C:FD:2E:98`
Con Play App Signing, se la perdi si può chiedere il reset a Google; senza backup è una seccatura.

## 1. Crea l'app

*Tutte le app → Crea app*: nome **Compilo PDF**, lingua predefinita **English (United States)**,
tipo **App**, **Gratuita**. Accetta le dichiarazioni (norme per gli sviluppatori e leggi sull'esportazione USA).

## 2. Contenuti dell'app (Dashboard → "Configura la tua app")

| Voce | Risposta |
| --- | --- |
| Norme sulla privacy | URL sopra |
| Accesso all'app | Tutte le funzioni sono disponibili senza account né credenziali |
| Annunci | **No**, l'app non contiene annunci |
| Classificazione dei contenuti | Questionario IARC, categoria **Utility, produttività, comunicazione o altro**. Tutte le risposte **No** (violenza, sesso, linguaggio, droghe, gioco d'azzardo, contenuti generati dagli utenti condivisi, condivisione posizione, acquisti digitali, accesso libero a internet). Esito atteso: PEGI 3 / USK 0 / Everyone |
| Pubblico di destinazione | **18 anni e oltre** (non è un'app per bambini: evita i requisiti "Famiglie") |
| App di notizie | No |
| App di tracciamento contatti COVID-19 | No |
| ID pubblicità | **No**, l'app non usa l'ID pubblicità (nel manifest non c'è il permesso) |
| App governative | No |
| Funzioni finanziarie | Nessuna |
| App per la salute | No |

### Sicurezza dei dati (Data safety)

- *L'app raccoglie o condivide tipi di dati utente obbligatori?* → **No.**
- Il resto del modulo si chiude da solo. Motivo da avere a mente se la Console chiede chiarimenti:
  documenti, dati personali inseriti in "I miei dati", firme e valori appresi restano nella memoria
  privata dell'app sul telefono; il manifest di release **non dichiara il permesso INTERNET**;
  nessun SDK di analisi, pubblicità o segnalazione errori; backup cloud disattivato.
- Cosa succede se l'utente sceglie *Condividi / Apri con / Stampa*: il file va all'app o al servizio
  scelto dall'utente. Non è condivisione da parte dell'app (azione avviata dall'utente).

### Autorizzazioni

Nessuna autorizzazione sensibile (niente foto, contatti, posizione, microfono, fotocamera, archivio
completo). I file arrivano dal selettore di Android o dalla condivisione da un'altra app.

## 3. Scheda dello store

*Presenza sullo store → Scheda principale dello store*. Per ogni lingua (aggiungi le altre con
"Gestisci traduzioni"): copia i file di `store/listings/<lingua>/`:

- **Nome** ← `title.txt` (11 caratteri, limite 30)
- **Breve descrizione** ← `short.txt` (limite 80)
- **Descrizione completa** ← `full.txt` (limite 4000)
- **Icona** ← `store/graphics/icon-512.png`
- **Grafica in evidenza** ← `store/graphics/feature/feature-graphic-<lingua>.png`
- **Screenshot telefono** (min 2, max 8) ← `store/graphics/screenshots/phone/<lingua>/`
- **Screenshot tablet 7" e 10"** ← cartelle `tablet7` e `tablet10` (le stesse per tutte le lingue)
- Categoria: **Produttività** · Email, sito web e privacy policy come in tabella.

Se per una lingua non carichi immagini proprie, la Console mostra quelle della lingua predefinita.

## 4. Primo test: test interno (subito, senza revisione lunga)

1. *Test e release → Test interno → Crea nuova release*.
2. Alla prima release la Console propone **Play App Signing**: accetta. Google custodisce la chiave
   di firma; tu carichi sempre con la chiave di upload.
3. Carica `compilo-pdf-1.0.0-1.aab`. Note di rilascio ← `whatsnew.txt` della lingua.
4. *Tester → Crea elenco email*: aggiungi i tuoi indirizzi Gmail (fino a 100).
5. *Salva → Verifica release → Avvia lancio sul test interno*.
6. In *Tester* copia il **link di partecipazione**: aprilo dal telefono con quell'account e installa
   dal Play Store. Gli aggiornamenti arrivano come per un'app normale.

Verifiche utili: *Release → Report di pre-lancio* (dispositivi reali di Google). Eventuali avvisi sulle
API "edge-to-edge deprecate" vengono dal framework Flutter, non dal codice dell'app.

## 5. Test chiuso (obbligatorio per gli account personali nuovi)

Se il tuo account sviluppatore è **personale** e creato dopo novembre 2023, prima di chiedere la
produzione serve un test chiuso con **almeno 12 tester che restano iscritti per 14 giorni di fila**.
(Gli account **organizzazione** non hanno questo obbligo. Verifica la regola attuale nella Console:
*Dashboard → "Prova la tua app"*.)

1. *Test e release → Test chiuso → Crea traccia* (nome libero, es. "Beta").
2. Crea una release con lo stesso AAB, aggiungi i tester (elenco email o un Google Group).
3. Invia loro il link di partecipazione. Devono **accettare l'invito e installare l'app**, e tenerla
   installata per i 14 giorni. Meglio reclutarne 15–20.
4. Dopo i 14 giorni: *Dashboard → Richiedi l'accesso alla produzione* e rispondi al questionario
   (come hai testato, feedback ricevuto, cosa hai migliorato).

Testo da mandare ai tester (adattalo):

> **IT** – Ciao! Sto provando Compilo PDF, un'app per compilare, firmare e convertire in Word i PDF
> direttamente dal telefono, senza internet. Mi aiuti? 1) apri questo link col tuo account Google:
> *[link]* 2) tocca "Diventa tester" 3) installa dal Play Store. Tienila installata per due settimane
> e, se puoi, aprila ogni tanto. Grazie!
>
> **EN** – Hi! I'm testing Compilo PDF, an app to fill, sign and convert PDFs to Word on your phone,
> offline. Could you help? 1) open this link with your Google account: *[link]* 2) tap "Become a
> tester" 3) install it from Google Play. Please keep it installed for two weeks and open it now
> and then. Thank you!

## 6. Produzione

*Produzione → Crea nuova release* (stesso AAB, o uno nuovo con versionCode più alto), paesi
(es. tutta l'Europa o tutti), note di rilascio, invia per revisione. La prima revisione può durare
qualche giorno.

Per ogni nuovo AAB: aumenta `version:` in `pubspec.yaml` (es. `1.0.1+2`; il numero dopo il `+` è il
versionCode e deve crescere) e ricostruisci con `flutter build appbundle --release`.

## 7. Requisiti tecnici già verificati

| Requisito | Stato |
| --- | --- |
| Target API | **36** (Android 16), compile 36, minSdk 24 |
| Pagine di memoria da **16 KB** | Librerie native a 64 bit allineate a ≥ 16 KB (`libflutter.so`, `libapp.so`, `libdartjni.so`, `libpdfium.so`: p_align 0x4000/0x10000); archivio allineato a 16 KB (`zipalign -c -P 16`); NDK 28; librerie non compresse. **Provato su emulatore Android 16 con kernel a 16 KB** (`getconf PAGE_SIZE` = 16384): l'app non è in modalità di compatibilità (`pageSizeCompat=0`) |
| **Edge-to-edge** | Interfaccia sotto status bar e barra gesti (`SystemUiMode.edgeToEdge`), insets gestiti nelle schermate e nei bottom sheet, `windowLayoutInDisplayCutoutMode=shortEdges` |
| Back predittivo | `enableOnBackInvokedCallback=true` e transizione Material predittiva |
| Lingua per app (Android 13+) | `localeConfig` con it, en, fr, de, es; risorse filtrate alle stesse lingue |
| 64 bit | arm64-v8a e x86_64 (più armeabi-v7a) |
| Firma | AAB/APK firmati con la chiave di upload; R8 e shrink risorse attivi; simboli nativi inclusi |
| Permessi | Nessuno richiesto (niente INTERNET nel manifest di release) |
| Backup | Disattivato verso il cloud; consentito solo il trasferimento diretto tra telefoni |
| Schermi grandi | Nessun blocco di orientamento, attività ridimensionabile |
| Dimensione | AAB ~50 MB (limite base 200 MB); l'APK scaricato da Play è per singola architettura |

## 8. Dopo la pubblicazione

- Controlla *Qualità → Android vitals* e il report di pre-lancio dopo ogni release.
- Il sito e la privacy policy si aggiornano dal repository GitHub (`docs/`): modifica
  `store/tools/build_site.py`, rilancialo e fai push; Pages si aggiorna da solo.
- Se un giorno aggiungi permessi, SDK di terze parti o funzioni online, **aggiorna prima la privacy
  policy e il modulo Sicurezza dei dati**.
