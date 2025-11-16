# 📺 VIDEO-TUTORIAL TESTUALE - DEPLOY IN 10 MINUTI

## 🎬 SCENA 1: PREPARAZIONE (2 minuti)

```
👤 TU:
├─ Hai la cartella "webapp_secure" sul desktop
├─ Hai creato account Heroku
└─ Hai installato Heroku CLI

📁 FILE NELLA CARTELLA:
├─ app.py (il server con login)
├─ Procfile (config Heroku)
├─ requirements.txt (librerie Python)
├─ runtime.txt (versione Python)
└─ DEPLOY_GUIDE.md (questa guida)
```

**✅ CHECKPOINT**: Apri la cartella e verifica che ci siano tutti i file

---

## 🎬 SCENA 2: APRI IL TERMINALE (30 secondi)

**Windows:**
```
1. Premi: Windows + R
2. Digita: cmd
3. Premi: Invio
```

**Mac:**
```
1. Premi: Cmd + Spazio
2. Digita: terminal
3. Premi: Invio
```

**Schermo del terminale:**
```
C:\Users\TuoNome> _
```

---

## 🎬 SCENA 3: VAI NELLA CARTELLA (1 minuto)

**Digita nel terminale:**

```bash
cd Desktop/webapp_secure
```

(Se la cartella è altrove, usa il percorso corretto)

**Schermo del terminale:**
```
C:\Users\TuoNome\Desktop\webapp_secure> _
```

**✅ CHECKPOINT**: Sei nella cartella giusta

---

## 🎬 SCENA 4: LOGIN SU HEROKU (1 minuto)

**Digita:**
```bash
heroku login
```

**Cosa succede:**
```
┌─────────────────────────────────────────┐
│  heroku: Press any key to open up      │
│  the browser to login or q to exit:    │
└─────────────────────────────────────────┘
```

**Premi un tasto qualsiasi** → Si apre il browser

**Nel browser:**
```
┌─────────────────────────────────────────┐
│  🟣 HEROKU                              │
│                                          │
│  [ Log In to Heroku CLI ]               │
│                                          │
│  Email: _______________                 │
│  Password: __________                   │
│                                          │
│       [ LOG IN ]                        │
└─────────────────────────────────────────┘
```

**Fai login** → Torna al terminale

**Terminale conferma:**
```
✓ Logged in as tuaemail@example.com
```

**✅ CHECKPOINT**: Sei loggato

---

## 🎬 SCENA 5: CREA L'APP (2 minuti)

**Digita:**
```bash
heroku create bilancio-mvp-2024
```

(Puoi scegliere un nome diverso, deve essere univoco)

**Cosa succede:**
```
Creating ⬢ bilancio-mvp-2024... done
https://bilancio-mvp-2024.herokuapp.com/ | 
https://git.heroku.com/bilancio-mvp-2024.git
```

**✅ CHECKPOINT**: Vedi il link della tua app

---

## 🎬 SCENA 6: INIZIALIZZA GIT (1 minuto)

**Digita (una riga alla volta):**
```bash
git init
git add .
git commit -m "Deploy bilancio processor"
```

**Cosa vedi:**
```
Initialized empty Git repository in...
[main (root-commit) abc1234] Deploy bilancio processor
 5 files changed, 500 insertions(+)
 create mode 100644 app.py
 create mode 100644 Procfile
 ...
```

**✅ CHECKPOINT**: File committati

---

## 🎬 SCENA 7: DEPLOY! (3 minuti)

**Digita:**
```bash
git push heroku main
```

(Se dice "master not found", usa: `git push heroku master`)

**Cosa succede (MAGIA! ✨):**
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Compressing objects: 100% (4/4), done.
Writing objects: 100% (5/5), 1.2 KiB | 1.2 MiB/s, done.

remote: Compressing source files... done.
remote: Building source:
remote: -----> Building on the Heroku-22 stack
remote: -----> Using buildpack: heroku/python
remote: -----> Python app detected
remote: -----> Installing python-3.11.7
remote: -----> Installing pip 23.3.2
remote: -----> Installing requirements with pip
remote:        Collecting Flask==3.1.2
remote:        Collecting pdfplumber==0.11.7
remote:        ...
remote:        Successfully installed Flask-3.1.2 pandas-2.3.3...
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: -----> Compressing...
remote:        Done: 52.3M
remote: -----> Launching...
remote:        Released v1
remote:        https://bilancio-mvp-2024.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
```

**✅ CHECKPOINT**: Vedi "deployed to Heroku" ✓

---

## 🎬 SCENA 8: APRI L'APP! (30 secondi)

**Digita:**
```bash
heroku open
```

**Si apre il browser con la TUA app!**

```
┌──────────────────────────────────────────┐
│  🔒 Accesso Riservato                    │
│     Bilancio Processor MVP               │
│                                           │
│  🛡️ AREA PRIVATA                        │
│                                           │
│  Username: [_______________]             │
│  Password: [_______________]             │
│                                           │
│           [ Accedi ]                     │
└──────────────────────────────────────────┘
```

**Login con:**
- Username: `admin`
- Password: `BilancioMVP2024!`

**Dopo il login:**
```
┌──────────────────────────────────────────┐
│  🚀 Bilancio Processor MVP    [👤][Esci] │
├──────────────────────────────────────────┤
│                                           │
│   Carica il tuo bilancino di verifica    │
│                                           │
│  ┌────────────────────────────────────┐  │
│  │          📄                         │  │
│  │  Trascina qui il tuo file          │  │
│  │  o clicca per selezionarlo         │  │
│  │                                     │  │
│  │  PDF o Excel • Max 10MB            │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
```

---

## 🎉 FINE! L'APP È ONLINE!

**URL della tua app:**
```
https://bilancio-mvp-2024.herokuapp.com
```

**Puoi accedere da:**
- 💻 PC
- 📱 Smartphone
- 🌍 Ovunque nel mondo

**È privata e protetta!** 🔒

---

## 📝 RECAP COMANDI USATI

```bash
cd Desktop/webapp_secure          # 1. Vai nella cartella
heroku login                       # 2. Login Heroku
heroku create nome-app            # 3. Crea app
git init                          # 4. Inizializza git
git add .                         # 5. Aggiungi file
git commit -m "Deploy"            # 6. Commit
git push heroku main              # 7. DEPLOY!
heroku open                       # 8. Apri app
```

---

## 🔧 SE QUALCOSA VA STORTO

**Comando magico per vedere gli errori:**
```bash
heroku logs --tail
```

Questo mostra gli ultimi log in tempo reale.

**Problemi comuni:**

1️⃣ **"App name is already taken"**
   Soluzione: Usa un nome diverso
   ```bash
   heroku create altro-nome-univoco
   ```

2️⃣ **"No such app"**
   Soluzione: L'app non è stata creata, ripeti step 5

3️⃣ **"Application error"**
   Soluzione: Controlla i log con `heroku logs --tail`

---

## 🎯 COSA HAI OTTENUTO

✅ Web app online 24/7
✅ Protetta da login
✅ URL personalizzato
✅ HTTPS sicuro (SSL)
✅ Accessibile da ovunque
✅ Upload e processing funzionanti
✅ Download Excel automatico

**COSTO: 0€** (piano gratuito Heroku)

---

## 📸 CONDIVIDI IL LINK

Ora puoi dare il link ai tuoi clienti:

```
https://tua-app.herokuapp.com

Username: admin
Password: BilancioMVP2024!
```

(Ricordati di cambiare le credenziali in app.py!)

---

## 🚀 PROSSIMO LIVELLO

Vuoi aggiungere:
- ✅ Più utenti?
- ✅ Storico file elaborati?
- ✅ Custom domain (es: bilancio.tuosito.it)?
- ✅ Email di notifica?

Dimmi e lo implementiamo! 🎯

---

**🎉 CONGRATULAZIONI! HAI LA TUA WEB APP ONLINE! 🎉**
