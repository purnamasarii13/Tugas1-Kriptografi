from flask import Flask, render_template, request, redirect, url_for, flash, session
from crypto.algorithms import caesar, vigenere, affine, hill, playfair, parse_matrix
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'ganti-secret-key-produksi'

CIPHERS = {
    'caesar': 'Caesar Cipher',
    'vigenere': 'Vigenère Cipher',
    'affine': 'Affine Cipher',
    'hill': 'Hill Cipher',
    'playfair': 'Playfair Cipher'
}

@app.route('/')
def index():
    return render_template('index.html', ciphers=CIPHERS)

@app.route('/cipher/<name>', methods=['GET','POST'])
def cipher(name):
    if name not in CIPHERS: return redirect(url_for('index'))
    result=None; formula=None; steps=[]; extra=None; form={}
    if request.method=='POST':
        form=request.form.to_dict(); mode=form.get('mode','encrypt'); text=form.get('text','')
        try:
            if not text.strip(): raise ValueError('Teks tidak boleh kosong.')
            if name=='caesar': result,formula,steps,extra=caesar(text,int(form.get('shift',0)),mode)
            elif name=='vigenere': result,formula,steps,extra=vigenere(text,form.get('key',''),mode)
            elif name=='affine': result,formula,steps,extra=affine(text,int(form.get('a',0)),int(form.get('b',0)),mode)
            elif name=='hill':
                n=int(form.get('size',2)); matrix=parse_matrix(form.get('matrix',''), n)
                result,formula,steps,extra=hill(text,matrix,mode)
            elif name=='playfair': result,formula,steps,extra=playfair(text,form.get('key',''),mode)
            item={'time':datetime.now().strftime('%d-%m-%Y %H:%M'), 'cipher':CIPHERS[name], 'mode':mode, 'input':text, 'output':result}
            hist=session.get('history',[]); hist.insert(0,item); session['history']=hist[:30]
        except Exception as e:
            flash(str(e),'danger')
    return render_template('cipher.html', name=name, title=CIPHERS[name], result=result, formula=formula, steps=steps, extra=extra, form=form)

@app.route('/history')
def history():
    return render_template('history.html', history=session.get('history',[]))

@app.route('/clear-history')
def clear_history():
    session.pop('history',None); flash('History berhasil dihapus.','success'); return redirect(url_for('history'))

if __name__ == '__main__':
    app.run(debug=True)
