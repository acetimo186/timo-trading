
import os
from flask import Flask, request, redirect, render_template_string, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime
import random
import threading
import time

app = Flask(__name__)
app.secret_key = 'musila-secret-key-2024-ONLINE'
MPESA_NUMBER = "0118431854"
MPESA_NAME = "MUSILA"

def db():
    con = sqlite3.connect('trading.db')
    con.row_factory = sqlite3.Row
    con.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT, demo_balance REAL DEFAULT 1000, live_balance REAL DEFAULT 0, profit REAL DEFAULT 0, fee REAL DEFAULT 0, bot_running INTEGER DEFAULT 0)''')
    con.execute('''CREATE TABLE IF NOT EXISTS deposits (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, status TEXT DEFAULT 'Pending', date TEXT)''')
    con.execute('''CREATE TABLE IF NOT EXISTS trades (id INTEGER PRIMARY KEY, user_id INTEGER, amount REAL, result TEXT, profit REAL, date TEXT)''')
    return con

LOGIN_HTML = '''
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>MUSILA AI - Login</title>
<style>body{background:#0a0a0a;color:white;font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}.box{background:#1a1a1a;padding:30px;border-radius:15px;width:320px;text-align:center;border:1px solid #333}input{width:90%;padding:12px;margin:10px 0;border-radius:8px;border:none;background:#2a2a2a;color:white}button{width:95%;padding:12px;background:#00ff88;color:black;font-weight:bold;border:none;border-radius:8px;cursor:pointer;margin-top:10px}a{color:#00ff88;text-decoration:none}</style>
</head><body><div class="box"><h2>MUSILA AI TRADING</h2><p>Login</p><form method="POST"><input name="email" placeholder="Email" required><input name="password" type="password" placeholder="Password" required><button type="submit">Login</button></form><br><a href="/register">Create Account - Get $1000 Free</a></div></body></html>
'''

REGISTER_HTML = '''
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>MUSILA AI - Register</title>
<style>body{background:#0a0a0a;color:white;font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}.box{background:#1a1a1a;padding:30px;border-radius:15px;width:320px;text-align:center;border:1px solid #333}input{width:90%;padding:12px;margin:10px 0;border-radius:8px;border:none;background:#2a2a2a;color:white}button{width:95%;padding:12px;background:#00ff88;color:black;font-weight:bold;border:none;border-radius:8px;cursor:pointer;margin-top:10px}a{color:#00ff88;text-decoration:none}</style>
</head><body><div class="box"><h2>MUSILA AI TRADING</h2><p>Get $1000 Demo Free</p><form method="POST"><input name="email" placeholder="Email" required><input name="password" type="password" placeholder="Password" required><button type="submit">Register</button></form><br><a href="/login">Already have account? Login</a></div></body></html>
'''

DASHBOARD_HTML = '''
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>Dashboard</title>
<style>body{background:#0a0a0a;color:white;font-family:Arial;margin:0;padding:15px}.top{display:flex;justify-content:space-between}.card{background:#1a1a1a;border-radius:15px;padding:15px;margin:10px;text-align:center;flex:1}.live{border:2px solid #00ff88;color:#00ff88}.bal{font-size:22px;font-weight:bold;margin-top:10px}.btn{padding:12px 20px;border-radius:10px;border:none;font-weight:bold;cursor:pointer;margin:5px}.start{background:#00ff88;color:black}.stop{background:#333;color:white}.deposit{background:#0099ff;color:white;width:100%;padding:15px;border-radius:12px;margin-top:15px;font-weight:bold}.profit{color:#00ff88}</style></head><body>
<div class="top"><h3>MUSILA AI</h3><div>{{email}} | <a href="/logout" style="color:#ff5555">Logout</a></div></div>
<div style="display:flex;flex-wrap:wrap"><div class="card"><div>DEMO</div><div class="bal">${{ "%.2f"|format(demo) }}</div></div><div class="card live"><div>LIVE</div><div class="bal">${{ "%.2f"|format(live) }}</div></div><div class="card"><div>PROFIT</div><div class="bal profit">${{ "%.2f"|format(profit) }}</div><div style="font-size:12px;margin-top:5px">Fee: ${{ "%.2f"|format(fee) }}</div></div></div>
<p>Bot: {% if bot %}<span style="color:#00ff88">RUNNING</span>{% else %}<span style="color:#ff5555">STOPPED</span>{% endif %}</p>
<form method="POST" action="/bot" style="display:inline"><button name="action" value="start" class="btn start">Start Bot</button></form>
<form method="POST" action="/bot" style="display:inline"><button name="action" value="stop" class="btn stop">Stop</button></form>
<form method="POST" action="/deposit"><button class="deposit">DEPOSIT<br>0118431854 - MUSILA</button></form>
<div style="display:flex;gap:10px;margin-top:15px"><div class="card" style="flex:1">WITHDRAW<br><small>Min $10</small></div></div><br><center><a href="/admin" style="color:#888">Admin Panel</a></center>
<div style="margin-top:20px"><h4>Recent Trades</h4>{% for t in trades %}<div style="background:#1a1a1a;padding:10px;margin:5px;border-radius:8px;display:flex;justify-content:space-between"><span>{{t['date']}}</span><span>{{t['result']}}</span><span style="color:{% if t['profit']>0 %}#00ff88{% else %}#ff5555{% endif %}">${{t['profit']}}</span></div>{% endfor %}</div>
</body></html>
'''

@app.route('/')
def home(): return redirect('/login')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form['email'].lower().strip()
        con=db(); user=con.execute('SELECT * FROM users WHERE email=?',(email,)).fetchone(); con.close()
        if user and check_password_hash(user['password'], request.form['password']):
            session['uid']=user['id']; session['email']=user['email']
            return redirect('/dashboard')
    return render_template_string(LOGIN_HTML)
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        email=request.form['email'].lower().strip()
        try:
            con=db(); con.execute('INSERT INTO users (email,password) VALUES (?,?)',(email, generate_password_hash(request.form['password']))); con.commit()
            uid=con.execute('SELECT id FROM users WHERE email=?',(email,)).fetchone()['id']; con.close()
            session['uid']=uid; session['email']=email
            return redirect('/dashboard')
        except: pass
    return render_template_string(REGISTER_HTML)
@app.route('/dashboard')
def dashboard():
    if 'uid' not in session: return redirect('/login')
    con=db(); u=con.execute('SELECT * FROM users WHERE id=?',(session['uid'],)).fetchone()
    trades=con.execute('SELECT * FROM trades WHERE user_id=? ORDER BY id DESC LIMIT 20',(session['uid'],)).fetchall(); con.close()
    if not u: return redirect('/logout')
    return render_template_string(DASHBOARD_HTML, email=session['email'], demo=u['demo_balance'], live=u['live_balance'], profit=u['profit'], fee=u['fee'], bot=u['bot_running'], trades=trades)
@app.route('/bot', methods=['POST'])
def bot_toggle():
    if 'uid' not in session: return redirect('/login')
    con=db(); con.execute('UPDATE users SET bot_running=? WHERE id=?',(1 if request.form['action']=='start' else 0, session['uid'])); con.commit(); con.close()
    return redirect('/dashboard')
@app.route('/deposit', methods=['POST'])
def deposit():
    if 'uid' not in session: return redirect('/login')
    con=db(); con.execute('INSERT INTO deposits (user_id,amount,status,date) VALUES (?,?,?,?)',(session['uid'], 0, 'Pending - Pay 0118431854 MUSILA', datetime.now().strftime('%Y-%m-%d %H:%M'))); con.commit(); con.close()
    return '<h2 style="background:#0a0a0a;color:white;padding:50px;text-align:center">Send M-Pesa to 0118431854 - MUSILA<br><br><a href="/dashboard" style="color:#00ff88">Back</a></h2>'
@app.route('/logout')
def logout(): session.clear(); return redirect('/login')
@app.route('/admin')
def admin():
    if 'uid' not in session: return redirect('/login')
    con=db(); users=con.execute('SELECT * FROM users').fetchall(); deps=con.execute('SELECT deposits.*, users.email FROM deposits JOIN users ON deposits.user_id=users.id ORDER BY deposits.id DESC').fetchall(); con.close()
    html='<body style="background:#111;color:white;font-family:Arial;padding:20px"><h2>Admin Panel - MUSILA</h2><a href="/dashboard" style="color:#00ff88">Back</a><h3>Users</h3>'
    for u in users: html+=f"{u['email']} - DEMO ${u['demo_balance']} LIVE ${u['live_balance']} Profit ${u['profit']}<br>"
    html+='<h3>Deposits</h3>'
    for d in deps: html+=f"{d['email']} - {d['status']} - {d['date']}<br>"
    return html+'</body>'

def bot_worker():
    while True:
        try:
            con=db(); users=con.execute('SELECT * FROM users WHERE bot_running=1').fetchall()
            for u in users:
                profit = round(random.uniform(-5, 15),2)
                new_demo = u['demo_balance']+profit; fee = u['fee']+ (profit*0.1 if profit>0 else 0); new_profit = u['profit']+profit
                con.execute('UPDATE users SET demo_balance=?, profit=?, fee=? WHERE id=?',(new_demo, new_profit, fee, u['id']))
                con.execute('INSERT INTO trades (user_id,amount,result,profit,date) VALUES (?,?,?,?,?)',(u['id'], 10, 'WIN' if profit>0 else 'LOSS', profit, datetime.now().strftime('%H:%M:%S')))
            con.commit(); con.close()
        except: pass
        time.sleep(5)
threading.Thread(target=bot_worker, daemon=True).start()

if __name__=='__main__':
    print('M-Pesa 0118431854 MUSILA READY - ONLINE MODE')
    port=int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port, debug=False)
