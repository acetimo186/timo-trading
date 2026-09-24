import os
import sqlite3
import random
from datetime import datetime
from flask import Flask, request, jsonify, session, render_template_string

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "timo-secret-2026")

DB = "trading.db"

def init_db():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        demo_balance REAL DEFAULT 1000,
        live_balance REAL DEFAULT 0,
        total_deposited REAL DEFAULT 0,
        created_at TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        mode TEXT,
        symbol TEXT,
        type TEXT,
        amount REAL,
        entry_price REAL,
        profit REAL,
        status TEXT,
        created_at TEXT
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS deposits (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount_kes REAL,
        amount_usd REAL,
        mpesa_code TEXT,
        status TEXT DEFAULT 'pending',
        created_at TEXT
    )""")
    con.commit()
    con.close()

init_db()

HTML_PAGE = """ <!DOCTYPE html> <html> <head> <meta name="viewport" content="width=device-width, initial-scale=1"> <title>Timo Trading AI</title> <style> body{background:#0e0e10;color:#fff;font-family:Arial;margin:0;padding:10px}.card{background:#1e1e22;padding:15px;border-radius:12px;margin-bottom:12px} button{padding:10px 18px;border:none;border-radius:8px;font-weight:bold;cursor:pointer}.buy{background:#0ecb81;color:#000}.sell{background:#f6465d;color:#fff} input,select{padding:10px;border-radius:6px;border:1px solid #444;background:#2a2a30;color:#fff;width:90%} #chart{height:420px;width:100%;background:#121214;border-radius:10px}.topbar{display:flex;justify-content:space-between;align-items:center}.badge{padding:4px 10px;border-radius:20px;font-size:12px}.demo{background:#2a2a5a}.live{background:#1a4d2e} </style> </head> <body> <div class="topbar"> <h2>🤖 Timo AI Bot</h2> <div><span id="modeBadge" class="badge demo">DEMO</span> <button onclick="logout()">Logout</button></div> </div> <div class="card"> <div>DEMO: $<span id="demoBal">1000</span> | LIVE: $<span id="liveBal">0.0</span></div> <div style="margin-top:8px"> Mode: <select id="modeSel" onchange="changeMode()"><option value="demo">DEMO</option><option value="live">LIVE</option></select> Symbol: <select id="symbolSel"><option value="Volatility 100 Index">V100</option><option value="Volatility 75 Index">V75</option><option value="Volatility 50 Index">V50</option><option value="EURUSD">EURUSD</option></select> Amount: <input id="amountInp" type="number" value="1" min="1" style="width:80px"> </div> <div style="margin-top:10px"> <button class="buy" onclick="trade('CALL')">BUY / CALL 📈</button> <button class="sell" onclick="trade('PUT')">SELL / PUT 📉</button> </div> <div id="msg" style="margin-top:10px;color:#0ecb81"></div> </div> <div class="card"> <h3>Live Chart - <span id="chartSymbol">V100</span></h3> <div id="tradingview_chart" style="height:420px;"></div> </div> <div class="card"> <h3>Deposit LIVE (M-Pesa)</h3> <p>Send to <b>0118431854</b> - Rate: KSh 100 = $1</p> <input id="kesAmt" placeholder="Amount KES e.g 1000"> <input id="mpesaCode" placeholder="M-Pesa Code e.g QGH..." style="margin-top:6px"> <button onclick="requestDeposit()" style="margin-top:6px;background:#ffcc00;color:#000">Request LIVE Credit</button> <p style="font-size:12px;color:#aaa">Admin will approve in /admin in seconds</p> </div> <script src="https://s3.tradingview.com/tv.js"></script> <script> let mode="demo"; function changeMode(){ mode=document.getElementById('modeSel').value; document.getElementById('modeBadge').innerText=mode.toUpperCase(); document.getElementById('modeBadge').className='badge '+(mode=='demo'?'demo':'live'); } document.getElementById('symbolSel').addEventListener('change', loadChart); function loadChart(){ let sym=document.getElementById('symbolSel').value; document.getElementById('chartSymbol').innerText=sym; let tvSym = sym.includes('V')? "CAPITALCOM:VIX100" : "FX:EURUSD"; if(sym.includes('75')) tvSym="CAPITALCOM:VIX75"; if(sym.includes('50')) tvSym="CAPITALCOM:VIX50"; new TradingView.widget({ "autosize": true, "symbol": tvSym, "interval": "1", "timezone": "Africa/Nairobi", "theme": "dark", "style": "1", "locale": "en", "container_id": "tradingview_chart" }); } loadChart(); async function loadBalances(){ let r=await fetch('/api/balances'); let d=await r.json(); if(d.demo_balance!=undefined){ document.getElementById('demoBal').innerText=d.demo_balance; document.getElementById('liveBal').innerText=d.live_balance; } } loadBalances(); async function trade(t){ let amount=parseFloat(document.getElementById('amountInp').value); let symbol=document.getElementById('symbolSel').value; let res=await fetch('/api/trade',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({mode,symbol,type:t,amount})}); let data=await res.json(); document.getElementById('msg').innerText=data.message; if(data.new_balance!=undefined){ if(mode=='demo') document.getElementById('demoBal').innerText=data.new_balance; else document.getElementById('liveBal').innerText=data.new_balance; } } async function requestDeposit(){ let kes=parseFloat(document.getElementById('kesAmt').value); let code=document.getElementById('mpesaCode').value; let r=await fetch('/api/deposit-request',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({kes,code})}); let d=await r.json(); alert(d.message); } async function logout(){ await fetch('/api/logout',{method:'POST'}); location.href='/login'; } </script> </body> </html> """

LOGIN_PAGE = """ <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style> body{background:#0e0e10;color:#fff;font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh}.card{background:#1e1e22;padding:25px;border-radius:12px;width:300px} input{width:95%;padding:10px;margin:6px 0;border-radius:6px;border:1px solid #444;background:#2a2a30;color:#fff} button{width:100%;padding:10px;background:#0ecb81;border:none;border-radius:8px;font-weight:bold;margin-top:8px} a{color:#0ecb81} </style></head><body> <div class="card"><h2>Login / Register</h2> <input id="u" placeholder="username"><input id="p" type="password" placeholder="password"> <button onclick="login()">Login</button><button onclick="register()" style="background:#444;color:#fff">Register</button> <div id="m" style="margin-top:10px;color:#f6465d"></div></div> <script> async function login(){let r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:document.getElementById('u').value,password:document.getElementById('p').value})});let d=await r.json();if(d.ok) location.href='/'; else document.getElementById('m').innerText=d.message} async function register(){let r=await fetch('/api/register',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({username:document.getElementById('u').value,password:document.getElementById('p').value})});let d=await r.json();document.getElementById('m').innerText=d.message; if(d.ok) setTimeout(()=>location.href='/',800)} </script></body></html> """

ADMIN_PAGE = """ <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><style> body{background:#111;color:#fff;font-family:Arial;padding:12px} table{width:100%;border-collapse:collapse;margin-top:12px}th,td{border:1px solid #444;padding:6px;font-size:13px} button{padding:6px 10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}.approve{background:#0ecb81}.reject{background:#f6465d;color:#fff}.card{background:#1e1e22;padding:12px;border-radius:10px;margin-bottom:12px} </style></head><body> <h2>Admin - Timo Trading</h2> <div class="card"><h3>Protection Settings</h3>Max Withdraw = 2x Deposit (Auto Enforced) | Max LIVE per user: $5 for safety until 18</div> <div class="card"><h3>Pending Deposits</h3><div id="deps"></div></div> <div class="card"><h3>All Users</h3><div id="users"></div></div> <script> async function load(){ let r=await fetch('/admin/api/deposits'); let d=await r.json(); let h='<table><tr><th>User</th><th>KES</th><th>USD</th><th>Code</th><th>Action</th></tr>'; d.forEach(x=>{h+=`<tr><td>${x.username} (${x.user_id})</td><td>${x.amount_kes}</td><td>${x.amount_usd}</td><td>${x.mpesa_code}</td><td><button class="approve" onclick="approve(${x.id},${x.user_id},${x.amount_usd})">Approve</button> <button class="reject" onclick="reject(${x.id})">Reject</button></td></tr>`}); h+='</table>'; document.getElementById('deps').innerHTML=h; let r2=await fetch('/admin/api/users'); let u=await r2.json(); let h2='<table><tr><th>ID</th><th>Username</th><th>Demo</th><th>Live</th><th>Deposited</th><th>Add Live</th></tr>'; u.forEach(x=>{h2+=`<tr><td>${x.id}</td><td>${x.username}</td><td>${x.demo_balance}</td><td>${x.live_balance}</td><td>${x.total_deposited}</td><td><input id="add_${x.id}" style="width:60px" placeholder="$"><button class="approve" onclick="addLive(${x.id})">Add</button></td></tr>`}); h2+='</table>'; document.getElementById('users').innerHTML=h2; } async function approve(id,uid,usd){ if(!confirm('Approve $'+usd+'?'))return; let r=await fetch('/admin/api/approve',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({deposit_id:id,user_id:uid,usd})}); let d=await r.json(); alert(d.message); load(); } async function reject(id){ let r=await fetch('/admin/api/reject',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({deposit_id:id})}); let d=await r.json(); alert(d.message); load(); } async function addLive(uid){ let amt=parseFloat(document.getElementById('add_'+uid).value); let r=await fetch('/admin/api/add-live',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({user_id:uid,amount:amt})}); let d=await r.json(); alert(d.message); load(); } load(); </script></body></html> """

@app.route('/')
def home():
    if 'uid' not in session:
        return render_template_string(LOGIN_PAGE)
    return render_template_string(HTML_PAGE)

@app.route('/login')
def login_page():
    return render_template_string(LOGIN_PAGE)

@app.route('/admin')
def admin_page():
    pwd = request.args.get('pwd') or request.headers.get('X-Admin-Pwd') or ""
    admin_pwd = os.environ.get("ADMIN_PASSWORD", "musila2024")
    if session.get('is_admin'):
        return render_template_string(ADMIN_PAGE)
    if pwd == admin_pwd:
        session['is_admin']=True
        return render_template_string(ADMIN_PAGE)
    return f""" <script> let p=prompt('Enter Admin Password:'); if(p) location.href='/admin?pwd='+p; else document.write('No password'); </script> """

@app.route('/api/register', methods=['POST'])
def api_register():
    data=request.json
    u=data.get('username','').strip()
    p=data.get('password','').strip()
    if not u or not p: return jsonify({"ok":False,"message":"Fill all"})
    con=sqlite3.connect(DB); c=con.cursor()
    try:
        c.execute("INSERT INTO users (username,password,created_at) VALUES (?,?,?)",(u,p,datetime.utcnow().isoformat()))
        con.commit()
        uid=c.lastrowid
        con.close()
        session['uid']=uid
        return jsonify({"ok":True,"message":"Registered! Login now"})
    except:
        con.close()
        return jsonify({"ok":False,"message":"Username exists"})

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.json
    u=data.get('username'); p=data.get('password')
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT id FROM users WHERE username=? AND password=?",(u,p))
    row=c.fetchone(); con.close()
    if row:
        session['uid']=row[0]
        return jsonify({"ok":True})
    return jsonify({"ok":False,"message":"Wrong username/password"})

@app.route('/api/logout', methods=['POST'])
def api_logout():
    session.clear()
    return jsonify({"ok":True})

@app.route('/api/balances')
def api_balances():
    if 'uid' not in session: return jsonify({})
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT demo_balance,live_balance FROM users WHERE id=?",(session['uid'],))
    row=c.fetchone(); con.close()
    if row: return jsonify({"demo_balance":row[0],"live_balance":row[1]})
    return jsonify({})

@app.route('/api/trade', methods=['POST'])
def api_trade():
    if 'uid' not in session: return jsonify({"message":"Login first"})
    data=request.json
    mode=data.get('mode','demo')
    symbol=data.get('symbol','Volatility 100 Index')
    ttype=data.get('type','CALL')
    amount=float(data.get('amount',1))
    if mode=='live' and amount>5:
        return jsonify({"message":"LIVE max $5 until 18 for safety"})
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT demo_balance,live_balance,total_deposited FROM users WHERE id=?",(session['uid'],))
    row=c.fetchone()
    if not row:
        con.close(); return jsonify({"message":"User not found"})
    demo_bal, live_bal, total_dep = row
    bal = demo_bal if mode=='demo' else live_bal
    if bal < amount:
        con.close()
        return jsonify({"message":f"Insufficient {mode} balance"})
    profit = round(amount*0.92 if random.random()>0.52 else -amount, 2)
    if mode=='live':
        new_bal_test = live_bal + profit
        if total_dep>0 and new_bal_test > total_dep*2 and profit>0:
            profit = round((total_dep*2)-live_bal,2)
            if profit<0: profit=0
    if mode=='demo':
        new_bal = demo_bal + profit
        c.execute("UPDATE users SET demo_balance=? WHERE id=?",(new_bal, session['uid']))
    else:
        new_bal = live_bal + profit
        c.execute("UPDATE users SET live_balance=? WHERE id=?",(new_bal, session['uid']))
    c.execute("INSERT INTO trades (user_id,mode,symbol,type,amount,entry_price,profit,status,created_at) VALUES (?,?,?,?,?,?,?,?,?)", (session['uid'], mode, symbol, ttype, amount, 0, profit, "closed", datetime.utcnow().isoformat()))
    con.commit(); con.close()
    msg = f"{mode.upper()} {ttype} {symbol} ${amount} -> {'WIN $'+str(profit) if profit>0 else 'LOSS '+str(profit)}"
    if mode=='live' and not os.environ.get("DERIV_API_TOKEN"):
        msg += " (Simulated - Protected 2x max)"
    return jsonify({"message":msg, "new_balance": new_bal})

@app.route('/api/deposit-request', methods=['POST'])
def api_deposit_request():
    if 'uid' not in session: return jsonify({"message":"Login first"})
    data=request.json
    kes=float(data.get('kes',0))
    code=data.get('code','').strip()
    if kes<100: return jsonify({"message":"Min KES 100"})
    usd=round(kes/100,2)
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("INSERT INTO deposits (user_id,amount_kes,amount_usd,mpesa_code,created_at) VALUES (?,?,?,?,?)", (session['uid'], kes, usd, code, datetime.utcnow().isoformat()))
    con.commit(); con.close()
    return jsonify({"message":f"Request sent: KES {kes} = ${usd}. Wait admin approval in 1 min"})

def admin_required():
    if session.get('is_admin'): return True
    return False

@app.route('/admin/api/deposits')
def admin_deposits():
    if not admin_required(): return jsonify([])
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT d.id,d.user_id,d.amount_kes,d.amount_usd,d.mpesa_code,u.username FROM deposits d JOIN users u ON u.id=d.user_id WHERE d.status='pending'")
    rows=c.fetchall(); con.close()
    return jsonify([{"id":r[0],"user_id":r[1],"amount_kes":r[2],"amount_usd":r[3],"mpesa_code":r[4],"username":r[5]} for r in rows])

@app.route('/admin/api/users')
def admin_users():
    if not admin_required(): return jsonify([])
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("SELECT id,username,demo_balance,live_balance,total_deposited FROM users ORDER BY id DESC")
    rows=c.fetchall(); con.close()
    return jsonify([{"id":r[0],"username":r[1],"demo_balance":r[2],"live_balance":r[3],"total_deposited":r[4]} for r in rows])

@app.route('/admin/api/approve', methods=['POST'])
def admin_approve():
    if not admin_required(): return jsonify({"message":"Not admin"})
    data=request.json
    dep_id=data.get('deposit_id'); uid=data.get('user_id'); usd=float(data.get('usd',0))
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("UPDATE deposits SET status='approved' WHERE id=?",(dep_id,))
    c.execute("UPDATE users SET live_balance=live_balance+?, total_deposited=total_deposited+? WHERE id=?",(usd,usd,uid))
    con.commit(); con.close()
    return jsonify({"message":f"Approved ${usd} to user {uid}"})

@app.route('/admin/api/reject', methods=['POST'])
def admin_reject():
    if not admin_required(): return jsonify({"message":"Not admin"})
    dep_id=request.json.get('deposit_id')
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("UPDATE deposits SET status='rejected' WHERE id=?",(dep_id,))
    con.commit(); con.close()
    return jsonify({"message":"Rejected"})

@app.route('/admin/api/add-live', methods=['POST'])
def admin_add_live():
    if not admin_required(): return jsonify({"message":"Not admin"})
    data=request.json
    uid=data.get('user_id'); amt=float(data.get('amount',0))
    con=sqlite3.connect(DB); c=con.cursor()
    c.execute("UPDATE users SET live_balance=live_balance+? WHERE id=?",(amt,uid))
    con.commit(); con.close()
    return jsonify({"message":f"Added ${amt}"})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
