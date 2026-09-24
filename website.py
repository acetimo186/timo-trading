from flask import Flask, render_template_string, request, redirect, session, jsonify
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = "timo_secret_2026"

# Simple in-memory DB (resets on Render restart - good for practice)
users = {"Admin": {"demo": 10000.0, "live": 0.0, "password": "Admin"}}

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TimoTrader - EUR/USD H1 REAL</title>
<style>
body { background:#0e0e0e; color:white; font-family:Arial; margin:0; padding:10px; }
.top { display:flex; justify-content:space-between; padding:10px; background:#1a1a1a; border-radius:10px; }
.balance { font-size:18px; font-weight:bold; color:#00ff88; }
.chart-box { margin-top:15px; background:#1a1a1a; border-radius:10px; padding:10px; height:520px; }
.btn { padding:12px 20px; border:none; border-radius:8px; font-weight:bold; cursor:pointer; margin:5px; width:48%; }
.buy { background:#00c853; color:white; }
.sell { background:#d50000; color:white; }
input { padding:12px; width:90%; border-radius:8px; border:none; margin:10px 0; background:#2a2a2a; color:white; }
.mode { padding:8px 15px; border-radius:20px; border:1px solid #555; background:#222; color:white; cursor:pointer; }
.mode.active { background:#ffeb3b; color:black; }
</style>
</head>
<body>

<div class="top">
  <div>EUR/USD <b style="color:#ffeb3b;">REAL H1</b> - Matches LiteFinance</div>
  <div class="balance">DEMO: ${{ "%.2f"|format(user.demo) }} | LIVE: ${{ "%.2f"|format(user.live) }}</div>
</div>

<div style="margin:10px 0;">
  <button class="mode {{ 'active' if mode=='demo' else '' }}" onclick="setMode('demo')">DEMO</button>
  <button class="mode {{ 'active' if mode=='live' else '' }}" onclick="setMode('live')">LIVE</button>
  <span style="margin-left:15px; font-size:12px; color:#aaa;">Real Chart • Nairobi Time • 1 Hour</span>
</div>

<div class="chart-box">
  <div id="tradingview_chart" style="height:500px;"></div>
</div>

<div style="background:#1a1a1a; border-radius:10px; padding:15px; margin-top:15px;">
  <h3>Trade EUR/USD H1</h3>
  <input id="amount" type="number" placeholder="Amount $ e.g 1" value="1" min="0.5">
  <div style="display:flex;">
    <button class="btn buy" onclick="trade('buy')">BUY (UP)</button>
    <button class="btn sell" onclick="trade('sell')">SELL (DOWN)</button>
  </div>
  <div id="result" style="margin-top:15px; font-weight:bold;"></div>
  <div style="font-size:11px; color:#888; margin-top:10px;">Chart = REAL EUR/USD H1 from market (matches LiteFinance). Trade result = Simulated 70% win for practice. No M-Pesa needed for solo.</div>
</div>

<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
<script>
// REAL EUR/USD 1 Hour Chart - Matches LiteFinance H1
new TradingView.widget({
  "autosize": true,
  "symbol": "FX:EURUSD",
  "interval": "60",
  "timezone": "Africa/Nairobi",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#0e0e0e",
  "enable_publishing": false,
  "hide_top_toolbar": false,
  "allow_symbol_change": false,
  "save_image": false,
  "container_id": "tradingview_chart"
});

function setMode(m){
  fetch('/set_mode?mode='+m).then(()=>location.reload());
}

function trade(type){
  let amt = document.getElementById('amount').value;
  document.getElementById('result').innerHTML = "Trading...";
  fetch('/trade', {
    method:'POST',
    headers:{'Content-Type':'application/json'},
    body: JSON.stringify({type:type, amount:amt})
  }).then(r=>r.json()).then(d=>{
    document.getElementById('result').innerHTML = d.message;
    setTimeout(()=>location.reload(), 1500);
  });
}
</script>

</body>
</html>
"""

ADMIN_HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>body{background:#111;color:white;font-family:Arial;padding:20px;} input{padding:10px;width:90%;margin:5px 0;border-radius:5px;border:none;background:#222;color:white;} button{padding:10px 20px;background:#ffeb3b;border:none;border-radius:5px;font-weight:bold;cursor:pointer;}</style>
</head><body>
<h2>Admin - Free LIVE Credit (No M-Pesa)</h2>
<p>Give yourself LIVE dollars FREE for solo practice</p>
<form method="POST">
<input name="username" placeholder="Username e.g Admin" required>
<input name="amount" type="number" placeholder="Amount $ e.g 10" required>
<button type="submit">Give LIVE Credit FREE</button>
</form>
<h3 style="margin-top:30px;">All Users:</h3>
{% for u, d in users.items() %}
<div style="background:#222;padding:10px;border-radius:8px;margin:5px 0;">{{u}} - DEMO: ${{d.demo}} | LIVE: ${{d.live}}</div>
{% endfor %}
<br><a href="/" style="color:#ffeb3b;">Back to Trading</a>
</body></html>
"""

@app.route('/')
def home():
    if 'user' not in session:
        session['user'] = 'Admin'
    if session['user'] not in users:
        users[session['user']] = {"demo": 10000.0, "live": 0.0, "password": ""}
    if 'mode' not in session:
        session['mode'] = 'demo'
    return render_template_string(HTML, user=users[session['user']], mode=session['mode'])

@app.route('/set_mode')
def set_mode():
    session['mode'] = request.args.get('mode','demo')
    return "ok"

@app.route('/trade', methods=['POST'])
def do_trade():
    data = request.json
    try:
        amount = float(data.get('amount',1))
    except:
        return jsonify({"message": "Invalid amount"})
    if amount <=0:
        return jsonify({"message": "Amount must be >0"})

    user = session.get('user','Admin')
    mode = session.get('mode','demo')

    if user not in users:
        return jsonify({"message": "Login first"})

    bal = users[user][mode]
    if bal < amount:
        return jsonify({"message": f"Low balance! You have ${bal:.2f} {mode.upper()}"})

    # 70% win simulation - chart is real, trade is simulated for practice
    win = random.random() < 0.70
    profit = amount * 0.70

    if win:
        users[user][mode] += profit
        msg = f"✅ WIN! +${profit:.2f} | Balance: ${users[user][mode]:.2f} | EUR/USD H1 REAL"
    else:
        users[user][mode] -= amount
        msg = f"❌ LOSS! -${amount:.2f} | Balance: ${users[user][mode]:.2f} | EUR/USD H1 REAL"

    return jsonify({"message": msg})

@app.route('/admin', methods=['GET','POST'])
def admin():
    if request.method == 'POST':
        uname = request.form.get('username','').strip()
        try:
            amt = float(request.form.get('amount',0))
        except:
            amt = 0
        if uname not in users:
            users[uname] = {"demo": 10000.0, "live": 0.0, "password": ""}
        users[uname]['live'] += amt
        return redirect('/admin')
    return render_template_string(ADMIN_HTML, users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
