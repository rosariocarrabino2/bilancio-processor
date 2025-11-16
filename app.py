import os
import re
import io
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, send_file
from werkzeug.utils import secure_filename
import pdfplumber
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from functools import wraps

app = Flask(__name__)
app.secret_key = 'bilancio_mvp_secret_key_2024'

# Configurazione
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
ALLOWED_EXTENSIONS = {'pdf', 'xlsx', 'xls'}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Credenziali (versione semplificata senza hash)
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'BilancioMVP2024!'

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'logged_in' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_bilancio_from_pdf(pdf_path):
    """Estrae dati dal PDF del bilancino di verifica"""
    data = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
                
            lines = text.split('\n')
            
            for line in lines:
                line = line.strip()
                if not line or len(line) < 10:
                    continue
                
                # Pattern per identificare righe con conti
                amount_match = re.search(r'([\d.,]+)\s*$', line)
                if amount_match:
                    amount_str = amount_match.group(1)
                    amount = float(amount_str.replace('.', '').replace(',', '.'))
                    
                    # Estrai codice conto
                    code_match = re.match(r'^(\d+)', line)
                    if code_match:
                        code = code_match.group(1)
                        
                        # Descrizione è tutto tra il codice e l'importo
                        desc_start = len(code)
                        desc_end = amount_match.start()
                        description = line[desc_start:desc_end].strip()
                        
                        # Determina se SP o CE
                        tipo = 'Stato Patrimoniale'
                        if code.startswith(('5', '6', '7', '8', '9')):
                            tipo = 'Conto Economico'
                        
                        data.append({
                            'Codice': code,
                            'Descrizione': description,
                            'Tipo': tipo,
                            'Amount': amount
                        })
    
    return pd.DataFrame(data)

def create_excel_output(df, output_path):
    """Crea file Excel con 3 sheets"""
    wb = Workbook()
    
    # Sheet 1: Bilancino Pulito
    ws1 = wb.active
    ws1.title = "Bilancino Pulito"
    
    headers = ['Codice', 'Descrizione', 'Tipo', 'Amount']
    ws1.append(headers)
    
    # Stile header
    for cell in ws1[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    # Aggiungi dati
    for _, row in df.iterrows():
        ws1.append([row['Codice'], row['Descrizione'], row['Tipo'], row['Amount']])
    
    # Sheet 2: Mapping
    ws2 = wb.create_sheet("Mapping")
    mapping_headers = ['Codice', 'Descrizione', 'Tipo', 'Amount', 'Cluster I', 'Cluster II']
    ws2.append(mapping_headers)
    
    for cell in ws2[1]:
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
        cell.alignment = Alignment(horizontal="center")
    
    for _, row in df.iterrows():
        ws2.append([row['Codice'], row['Descrizione'], row['Tipo'], row['Amount'], '', ''])
    
    # Sheet 3: Headline
    ws3 = wb.create_sheet("Headline")
    ws3.append(["STATO PATRIMONIALE"])
    ws3.append([])
    ws3.append(["Voce", "Importo"])
    
    ws3.append(["CONTO ECONOMICO"])
    ws3.append([])
    ws3.append(["Voce", "Importo"])
    
    # Formatta Headline
    ws3['A1'].font = Font(bold=True, size=14)
    ws3['A4'].font = Font(bold=True, size=14)
    
    # Salva
    wb.save(output_path)

@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        
        # Verifica credenziali (comparazione diretta)
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Credenziali non valide')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'success': False, 'error': 'Nessun file caricato'})
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'Nessun file selezionato'})
    
    if not allowed_file(file.filename):
        return jsonify({'success': False, 'error': 'Formato file non supportato'})
    
    try:
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_id = f"{timestamp}_{filename}"
        input_path = os.path.join(UPLOAD_FOLDER, file_id)
        file.save(input_path)
        
        ext = filename.rsplit('.', 1)[1].lower()
        if ext == 'pdf':
            df = extract_bilancio_from_pdf(input_path)
        else:
            return jsonify({'success': False, 'error': 'Formato Excel non ancora supportato'})
        
        if df.empty:
            return jsonify({'success': False, 'error': 'Impossibile estrarre dati dal file'})
        
        output_filename = f"elaborato_{file_id.replace('.pdf', '.xlsx')}"
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        create_excel_output(df, output_path)
        
        df_sp = df[df['Tipo'] == 'Stato Patrimoniale']
        df_ce = df[df['Tipo'] == 'Conto Economico']
        totale = df['Amount'].sum()
        
        stats = {
            'total_conti': len(df),
            'conti_sp': len(df_sp),
            'conti_ce': len(df_ce),
            'totale': float(totale),
            'quadra': abs(totale) < 0.10
        }
        
        return jsonify({
            'success': True,
            'file_id': output_filename,
            'stats': stats
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download/<file_id>')
@login_required
def download_file(file_id):
    try:
        file_path = os.path.join(OUTPUT_FOLDER, file_id)
        return send_file(file_path, as_attachment=True, download_name=f"bilancio_elaborato.xlsx")
    except Exception as e:
        return jsonify({'error': str(e)}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
