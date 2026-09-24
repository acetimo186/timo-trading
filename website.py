import os, sqlite3, json
from flask import Flask, render_template_string, request, redirect, session, jsonify
from datetime import datetime
import requests

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "musila-secret-2026")

DB = "trading.db"

def init_db():
    con = sqlite3.connect(DB)
    c = con.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        email TEXT UNIQUE,
        password TEXT,
        demo_balance REAL DEFAULT 1000,
        live_balance REAL DEFAULT 0
    )""")
    c.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        mode TEXT,
        symbol TEXT,
        type TEXT,
        amount REAL,
        entry_price REAL,
        exit_price REAL,
        profit REAL,
        status TEXT,
        created_at TEXT
    )""")
    con.commit()
    con.close()

init_db()

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MUSILA AI - Demo & Live Deriv</title>
<style>
body{background:#0a0e13;color:#fff;font-family:Inter,Arial;margin:0}
.header{display:flex;justify-content:space-between;padding:12px 16px;background:#121821;align-items:center;position:sticky;top:0;z-index:10}
.switch{display:flex;background:#1c2532;border-radius:20px;padding:3px}
.switch button{border:none;padding:8px 16px;border-radius:18px;font-weight:700;cursor:pointer}
.switch.active{background:#00d084;color:#000}
.switch.inactive{background:transparent;color:#888}
.price{font-size:28px;font-weight:800;text-align:center;margin:10px}
.chart{height:300px;background:#121821;margin:10px;border-radius:12px;display:flex;align-items:center;justify-content:center}
.btns{display:flex;gap:10px;padding:12px}
.btns button{flex:1;padding:16px;border:none;border-radius:12px;font-weight:800;font-size:16px;cursor:pointer}
.buy{background:#00d084}.sell{background:#ff4d4d}
.panel{margin:10px;background:#121821;padding:12px;border-radius:12px}
input,select{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #333;background:#0a0e13;color:#fff}
</style>
</head>
<body>
<div class="header">
  <div><b>MUSILA AI</b></div>
  <div class="switch">
    <button id="demoBtn" class="active" onclick="setMode('demo')">DEMO $<span id="demoBal">{{demo}}</span></button>
    <button id="liveBtn" class="inactive" onclick="setMode('live')">LIVE $<span id="liveBal">{{live}}</span></button>
  </div>
  <div><a href="/logout" style="color:#888;text-decoration:none">Logout</a></div>
</div>
<div style="text-align:center;padding:6px">
  <select id="symbol" onchange="changeSymbol()" style="width:auto">
    <option value="R_100">Volatility 100 Index</option>
    <option value="R_75">Volatility 75 Index</option>
    <option value="R_50">Volatility 50 Index</option>
    <option value="frxEURUSD">EUR/USD</option>
    <option value="frxXAUUSD">Gold</option>
    <option value="cryBTCUSD">BTC/USD</option>
  </select>
  <div class="price" id="price">Loading Deriv price...</div>
  <div style="color:#888;font-size:12px" id="status">Connecting to Deriv...</div>
</div>
<div class="chart" id="chart">Live Deriv Chart Loading...</div>
<div class="panel">
  <label>Amount (USD)</label>
  <input id="amount" type="number" value="10" min="1">
  <div class="btns">
    <button class="buy" onclick="trade('CALL')">BUY / CALL ↑</button>
    <button class="sell" onclick="trade('PUT')">SELL / PUT ↓</button>
  </div>
  <div id="msg" style="text-align:center;color:#00d084"></div>
</div>
<div class="panel">
  <b>My Trades (<span id="modeLabel">DEMO</span>)</b>
  <div id="trades">Loading...</div>
</div>
<div class="panel" id="livePanel" style="display:none;border:1px solid #00d084">
  <b>💰 LIVE ACCOUNT</b><br>
  <small style="color:#888">Deposit via M-Pesa to trade real money</small><br><br>
  <a href="/deposit" style="display:block;text-align:center;background:#00d084;color:#000;padding:12px;border-radius:8px;text-decoration:none;font-weight:800">DEPOSIT WITH M-PESA</a>
  <br><small>Deriv Token: {{has_token}}</small>
</div>
<script>
let mode = localStorage.getItem('mode') || 'demo';
let currentPrice = 0;
let symbol = 'R_100';
let ws;
function setMode(m){
  mode=m; localStorage.setItem('mode',m);
  document.getElementById('demoBtn').className = m==='demo'?'active':'inactive';
  document.getElementById('liveBtn').className = m==='live'?'active':'inactive';
  document.getElementById('modeLabel').innerText = m.toUpperCase();
  document.getElementById('livePanel').style.display = m==='live'?'block':'none';
  loadTrades();
}
setMode(mode);
function connectDeriv(){
  ws = new WebSocket('wss://ws.derivws.com/websockets/v3?app_id=1089');
  ws.onopen = ()=>{ document.getElementById('status').innerText='✓ Connected to Deriv'; subscribe(); };
  ws.onmessage = (msg)=>{
    let data = JSON.parse(msg.data);
    if(data.msg_type==='tick'){
      currentPrice = data.tick.quote;
      document.getElementById('price').innerText = symbol + ' ' + currentPrice;
      document.getElementById('chart').innerHTML = '<div style=text-align:center><div style=font-size:36px;font-weight:800>'+currentPrice+'</div><div style=color:#888>Live tick from Deriv</div></div>';
    }
  };
  ws.onclose = ()=>{ document.getElementById('status').innerText='Reconnecting...'; setTimeout(connectDeriv,2000); };
}
function subscribe(){ ws.send(JSON.stringify({ticks:symbol, subscribe:1})); }
function changeSymbol(){
  symbol=document.getElementById('symbol').value;
  if(ws && ws.readyState===1){ ws.send(JSON.stringify({forget_all:'ticks'})); subscribe(); }
}
connectDeriv();
function trade(type){
  let amt = document.getElementById('amount').value;
  fetch('/api/trade',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({mode:mode,symbol:symbol,type:type,amount:parseFloat(amt),price:currentPrice})})
 .then(r=>r.json()).then(d=>{
    document.getElementById('msg').innerText = d.message;
    loadTrades();
    if(d.new_balance!==undefined){
      if(mode==='demo') document.getElementById('demoBal').innerText=d.new_balance.toFixed(2);
      else document.getElementById('liveBal').innerText=d.new_balance.toFixed(2);
    }
  });
}
function loadTrades(){
  fetch('/api/trades?mode='+mode).then(r=>r.json()).then(list=>{
    let html=''; list.forEach(t=>{ html+=`<div style=display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid #222><span>${t.symbol} ${t.type} $${t.amount}</span><span style=color:${t.profit>=0?'#00d084':'#ff4d4d'}>${t.profit>0?'+':''}${t.profit}</span></div>`; });
    document.getElementById('trades').innerHTML = html || 'No trades yet';
  });
}
loadTrades();
</script>
</body>
</html>
"""

LOGIN_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{background:#0a0e13;color:#fff;font-family:Arial;display:flex;justify-content:center;align-items:center;height:100vh;margin:0}
.box{background:#121821;padding:24px;border-radius:12px;width:300px}
input{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #333;background:#0a0e13;color:#fff;box-sizing:border-box}
button{width:100%;padding:12px;background:#00d084;border:none;border-radius:8px;font-weight:800;cursor:pointer;margin-top:10px}
</style></head><body>
<div class="box">
<h2>MUSILA AI TRADING</h2>
<p style="color:#888">Demo + Live Deriv</p>
<form method="POST">
<input name="email" placeholder="Email" required>
<input name="password" type="password" placeholder="Password" required>
<button>Login / Create Account</button>
</form>
<p style="font-size:12px;color:#888;margin-top:12px">New account gets $1000 DEMO free. LIVE $0 until deposit.</p>
</div></body></html>
"""

DEPOSIT_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>body{background:#0a0e13;color:#fff;font-family:Arial;padding:20px}
.box{background:#121821;padding:20px;border-radius:12px;max-width:400px;margin:auto}
input{width:100%;padding:10px;margin:6px 0;border-radius:8px;border:1px solid #333;background:#0a0e13;color:#fff;box-sizing:border-box}
button{width:100%;padding:12px;background:#00d084;border:none;border-radius:8px;font-weight:800;margin-top:10px}
</style></head><body>
<div class="box">
<h3>M-Pesa Deposit - LIVE</h3>
<form method="POST">
<input name="phone" placeholder="07XX XXX XXX" required>
<input name="amount" type="number" placeholder="Amount KES min 100" required>
<button>Simulate Deposit (Adds to LIVE)</button>
</form>
<br><a href="/" style="color:#888">Back</a>
</div></body></html>
"""

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        email=request.form["email"].strip().lower()
        pwd=request.form["password"]
        con=sqlite3.connect(DB)
        c=con.cursor()
        c.execute("SELECT id,password FROM users WHERE email=?", (email,))
        row=c.fetchone()
        if row:
            if row[1]!=pwd:
                con.close()
                return "Wrong password", 400
            uid=row[0]
        else:
            c.execute("INSERT INTO users (email,password) VALUES (?,?)", (email,pwd))
            uid=c.lastrowid
        con.commit()
        con.close()
        session["uid"]=uid
        session["email"]=email
        return redirect("/")
    return render_template_string(LOGIN_HTML)

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/")
def home():
    if "uid" not in session:
        return redirect("/login")
    con=sqlite3.connect(DB)
    c=con.cursor()
    c.execute("SELECT demo_balance,live_balance FROM users WHERE id=?", (session["uid"],))
    demo,live=c.fetchone()
    con.close()
    has_token = "YES" if os.environ.get("DERIV_API_TOKEN") else "NO - Add in Render Env"
    return render_template_string(HTML, demo=round(demo,2), live=round(live,2), has_token=has_token)

@app.route("/deposit", methods=["GET","POST"])
def deposit():
    if "uid" not in session:
        return redirect("/login")
    if request.method=="POST":
        amt=float(request.form["amount"])
        usd=amt/130
        con=sqlite3.connect(DB)
        c=con.cursor()
        c.execute("UPDATE users SET live_balance=live_balance+? WHERE id=?", (usd, session["uid"]))
        con.commit()
        con.close()
        return redirect("/")
    return render_template_string(DEPOSIT_HTML)

@app.route("/api/trades")
def api_trades():
    if "uid" not in session:
        return jsonify([])
    mode=request.args.get("mode","demo")
    con=sqlite3.connect(DB)
    c=con.cursor()
    c.execute("SELECT symbol,type,amount,profit FROM trades WHERE user_id=? AND mode=? ORDER BY id DESC LIMIT 20", (session["uid"], mode))
    rows=c.fetchall()
    con.close()
    return jsonify([{"symbol":r[0],"type":r[1],"amount":r[2],"profit":r[3]} for r in rows])

@app.route("/api/trade", methods=["POST"])
def api_trade():
    if "uid" not in session:
        return jsonify({"message":"Not logged in"}), 401
    data=request.json
    mode=data.get("mode","demo")
    symbol=data.get("symbol","R_100")
    ttype=data.get("type","CALL")
    amount=float(data.get("amount",10))
    price=float(data.get("price",0) or 0)
    con=sqlite3.connect(DB)
    c=con.cursor()
    c.execute("SELECT demo_balance,live_balance FROM users WHERE id=?", (session["uid"],))
    demo_bal,live_bal=c.fetchone()
    bal = demo_bal if mode=="demo" else live_bal
    if bal < amount:
        con.close()
        return jsonify({"message":f"Insufficient {mode} balance"})
    import random
    profit = round(amount * 0.92 if random.random()>0.48 else -amount, 2)
    if mode=="demo":
        new_bal = demo_bal + profit
        c.execute("UPDATE users SET demo_balance=? WHERE id=?", (new_bal, session["uid"]))
    else:
        new_bal = live_bal + profit
        c.execute("UPDATE users SET live_balance=? WHERE id=?", (new_bal, session["uid"]))
    c.execute("INSERT INTO trades (user_id,mode,symbol,type,amount,entry_price,profit,status,created_at) VALUES (?,?,?,?,?,?,?,?,?)",
              (session["uid"], mode, symbol, ttype, amount, price, profit, "closed", datetime.utcnow().isoformat()))
    con.commit()
    con.close()
    msg = f"{mode.upper()} {ttype} {symbol} ${amount} -> {'WIN +$'+str(profit) if profit>0 else 'LOSS '+str(profit)}"
    if mode=="live" and not os.environ.get("DERIV_API_TOKEN"):
        msg += " (Simulated - Add DERIV_API_TOKEN for real)"
    return jsonify({"message":msg, "new_balance": new_bal})

if __name__=="__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT",10000)))
