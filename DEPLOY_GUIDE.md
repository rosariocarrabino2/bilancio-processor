# 🔒 BILANCIO PROCESSOR - VERSIONE PRIVATA CON LOGIN

## 🎯 CREDENZIALI DI ACCESSO

**⚠️ IMPORTANTE - CAMBIA QUESTE CREDENZIALI!**

**Username**: `admin`
**Password**: `BilancioMVP2024!`

---

## 🚀 DEPLOY SU HEROKU (GRATIS) - GUIDA PASSO-PASSO

### STEP 1: Crea account Heroku (1 minuto)

1. Vai su: https://signup.heroku.com/
2. Compila il form:
   - Nome e Cognome
   - Email
   - Paese: Italy
   - Ruolo: Student (o altro)
   - Primary language: Python
3. Clicca su "CREATE FREE ACCOUNT"
4. Controlla la tua email e conferma l'account
5. Crea una password

✅ Account creato!

---

### STEP 2: Installa Heroku CLI (2 minuti)

**Windows:**
1. Scarica: https://cli-assets.heroku.com/heroku-x64.exe
2. Esegui l'installer
3. Segui le istruzioni

**Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

---

### STEP 3: Deploy l'applicazione (5 minuti)

1. **Apri il Terminale/Prompt dei comandi**

2. **Vai nella cartella webapp_secure:**
```bash
cd /path/to/webapp_secure
```

3. **Login su Heroku:**
```bash
heroku login
```
(Si aprirà il browser, clicca su "Log in")

4. **Crea l'app Heroku:**
```bash
heroku create nome-tua-app
```
(Sostituisci `nome-tua-app` con un nome univoco, es: `bilancio-processor-mvp`)

5. **Inizializza Git (se necessario):**
```bash
git init
git add .
git commit -m "Initial commit"
```

6. **Deploy su Heroku:**
```bash
git push heroku main
```
(Se hai un branch chiamato "master" invece di "main", usa: `git push heroku master`)

7. **Apri l'app:**
```bash
heroku open
```

✅ **L'APP È ONLINE!** 🎉

---

## 🔐 COME CAMBIARE USERNAME E PASSWORD

Apri il file `app.py` e cerca questa sezione (riga ~26):

```python
# ⚠️ CONFIGURAZIONE SICUREZZA - CAMBIA QUESTI VALORI!
USERS = {
    'admin': generate_password_hash('BilancioMVP2024!')  
}
```

**Per cambiare:**

1. **Username**: Sostituisci `'admin'` con il tuo username desiderato
2. **Password**: Sostituisci `'BilancioMVP2024!'` con la tua password

**Esempio:**
```python
USERS = {
    'marco': generate_password_hash('SuperSecret2024!'),
    'giulia': generate_password_hash('Password123!')  # Puoi aggiungere più utenti
}
```

Dopo aver modificato, fai il deploy di nuovo:
```bash
git add app.py
git commit -m "Update credentials"
git push heroku main
```

---

## 🎯 COME FUNZIONA

1. **Vai sul sito**: https://nome-tua-app.herokuapp.com
2. **Fai login** con username e password
3. **Carica il bilancino PDF**
4. **Attendi l'elaborazione** (2-5 secondi)
5. **Scarica l'Excel** elaborato

---

## 🔒 SICUREZZA

✅ **Login obbligatorio** - Nessuno può accedere senza credenziali
✅ **Password hashate** - Le password non sono salvate in chiaro
✅ **Sessioni sicure** - Token random per ogni sessione
✅ **HTTPS automatico** - Heroku fornisce SSL gratis
✅ **File temporanei** - I file caricati vengono eliminati automaticamente

---

## 📊 LIMITI PIANO GRATUITO HEROKU

- ✅ **550-1000 ore/mese gratis** (24/7 se verifichi la carta)
- ✅ **HTTPS incluso**
- ✅ **Custom domain** possibile
- ⚠️ **Sleep dopo 30 min di inattività** (primo caricamento lento ~10 sec)
- ⚠️ **Max 10MB per file**

---

## 🎨 PERSONALIZZAZIONE

### Cambiare il logo e i colori:

Nel file `app.py`, cerca le sezioni HTML e modifica:

**Logo**: 
- Login: cerca `<div class="logo">🔒</div>`
- Dashboard: cerca `<div class="logo-small">🚀</div>`

**Colori** (trova queste variabili CSS):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Sostituisci con i tuoi colori hex!

---

## 🛠️ TROUBLESHOOTING

**Problema: "Heroku: command not found"**
- Soluzione: Riavvia il terminale dopo aver installato Heroku CLI

**Problema: "App name already taken"**
- Soluzione: Scegli un altro nome univoco per la tua app

**Problema: "Application error"**
- Soluzione: Controlla i log con: `heroku logs --tail`

**Problema: "Non riesco a fare login"**
- Soluzione: Controlla di aver cambiato le credenziali correttamente

---

## 📱 ACCESSO DA MOBILE

L'interfaccia è **responsive** e funziona perfettamente su:
- 📱 iPhone / Android
- 💻 Tablet
- 🖥️ Desktop

---

## 🔄 AGGIORNARE L'APP

Ogni volta che modifichi il codice:

```bash
git add .
git commit -m "Descrizione modifiche"
git push heroku main
```

L'app si aggiornerà automaticamente in ~30 secondi!

---

## 🆘 SUPPORTO

**Documentazione Heroku**: https://devcenter.heroku.com/
**Tutorial video**: Cerca su YouTube "deploy flask app heroku"

---

## ✨ FEATURES IMPLEMENTATE

✅ Login protetto con password
✅ Dashboard privata
✅ Upload PDF drag & drop
✅ Processing automatico
✅ Download Excel
✅ Logout sicuro
✅ Sessioni gestite
✅ Design responsive
✅ HTTPS (SSL)

---

## 🚀 PROSSIMI STEP

Dopo il deploy, puoi aggiungere:
- [ ] Registrazione utenti
- [ ] Reset password via email
- [ ] Storico upload
- [ ] Multi-file batch processing
- [ ] API REST
- [ ] Custom domain

---

**🎉 Sei pronto per mettere online la tua app privata!**

Segui gli step e in 10 minuti avrai la tua app online e protetta! 🔒
