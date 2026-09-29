from flask import Flask, request, jsonify, send_from_directory
import os, json
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'ebooks_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
USERS_FILE = 'users.json'
DEPOSITS_FILE = 'deposits.json'
FEES_FILE = 'fees.json'

ADMIN_PHONE = "0118431854"
ADMIN_PASSWORD = "KAUMONI20r4."
MPESA_TILL = "YOUR_TILL_HERE"

def load_json(f, default):
    if not os.path.exists(f): return default
    try:
        with open(f) as jf: return json.load(jf)
    except: return default
def save_json(f, data):
    with open(f,'w') as jf: json.dump(data, jf)

# --- SERVICE GUIDE PAGES DATA ---
SERVICES = {
"poster": {"icon":"🎨","name":"Poster Maker","price":"Ksh 150 / $1","to":"/poster-maker","color":"#f9c846",
"desc":"Create professional business posters in 10 seconds. No design skills needed. Used by salons, shops, churches, events.",
"what":"You get HD poster without watermark, ready to post on WhatsApp Status, Facebook, print.",
"steps":["1. Choose template: Sale Red, Salon Pink, Church Blue, Event Yellow, Food Green","2. Type your title (e.g. MEGA SALE!), offer (50% OFF), phone, location","3. See LIVE BLUE preview with watermark PREVIEW PAY $1","4. Pay $1 from your balance (Till "+MPESA_TILL+") - watermark disappears","5. Click Download HD - Clean image saved to your phone"],
"inside":"Inside you will find: 5 color templates, big title editor, subtitle, phone & location box, live preview box (350x500), BLUE pay watermark, Download HD button."},
"receipt": {"icon":"🧾","name":"Receipt Maker","price":"Ksh 150 / $1","to":"/receipt-maker","color":"#f9c846",
"desc":"Generate professional receipts for your shop, salon, or business. Looks like real printed receipt.",
"what":"HD receipt image with your shop name, customer name, item, price. No watermark after pay.",
"steps":["1. Enter Business Name, Customer Name, Item Sold, Price","2. Live preview shows receipt with BLUE PAY watermark","3. Pay $1 from balance","4. Download clean receipt to send to customer on WhatsApp"],
"inside":"Inside: Business name input, customer input, item input, price input, live receipt preview (white paper style), Download HD $1."},
"cv": {"icon":"📄","name":"CV Builder","price":"Ksh 300 / $2","to":"/cv-builder","color":"#f9c846",
"desc":"Build HR-approved professional CV that gets you hired. ATS friendly, clean design.",
"what":"You get HD CV image (also can print to PDF). Professional layout with your name, title, summary.",
"steps":["1. Enter Full Name, Job Title (e.g. Cashier, Driver)","2. Enter Summary, Experience, Skills (text area)","3. Live CV preview with BLUE watermark PAY $2","4. Pay $2 - watermark removed","5. Download HD CV to apply for jobs"],
"inside":"Inside: Name input, Title input, Summary textarea, Experience & Education fields, Live white CV preview, Download HD $2 button."},
"logo": {"icon":"💼","name":"Logo Maker","price":"Ksh 500 / $3","to":"/logo-maker","color":"#f9c846",
"desc":"Design a modern business logo for your shop, brand, company in seconds.",
"what":"HD logo (350x350 square) perfect for WhatsApp profile, business cards, signboard.",
"steps":["1. Enter Business Name (e.g. KAUMONI)","2. Enter Tagline (e.g. TRADING)","3. Live square logo preview with watermark","4. Pay $3 to remove watermark","5. Download HD logo"],
"inside":"Inside: Business name input, Tagline input, Square logo preview box, color gold style, Download $3."},
"cover": {"icon":"✉️","name":"Cover Letter Builder","price":"Ksh 150 / $1","to":"/cover-letter","color":"#f9c846",
"desc":"Write winning cover letter that makes HR call you. For any job application.",
"what":"HD Cover Letter image ready to attach with your CV.",
"steps":["1. Enter Your Name","2. Type or paste cover letter text","3. Preview with PAY watermark","4. Pay $1 and download clean HD"],
"inside":"Inside: Name input, Letter textarea, Live preview of letter, Download HD $1."},
"trading": {"icon":"📈","name":"Trading Platform","price":"20% Profit Fee Only","to":"/trade","color":"#00c950",
"desc":"Trade Forex, Crypto (BTC, ETH), Gold (XAUUSD) live with real TradingView chart. Like Binomo but you own it.",
"what":"Live trading with BUY/SELL, profit calculation, 20% fee goes to admin when you profit. Demo with real Binance price.",
"steps":["1. Login with phone + password","2. Deposit via M-Pesa Till "+MPESA_TILL+" - Admin approves in /admin","3. Choose pair: EURUSD, GBPUSD, BTCUSDT, ETHUSDT, XAUUSD","4. Enter amount $10 and click BUY or SELL","5. See live profit/loss, click CLOSE to close. If profit, 20% fee auto deducted as your profit","6. Balance updates instantly"],
"inside":"Inside: TradingView chart (dark), Pair selector, BUY green / SELL red buttons, Amount input, Open trades list with live P/L, Balance top, Deposit box with M-Pesa code submission, Logout."},
"signals": {"icon":"📡","name":"VIP Signals","price":"Ksh 1500 / $10","to":"/signals","color":"#f9c846",
"desc":"Get daily trading signals with 80% win rate. We send you when to BUY/SELL.",
"what":"After paying $10, you become VIP. Status shows VIP Active and you get WhatsApp group link.",
"steps":["1. Check balance - Need $10","2. Click Join VIP $10 - $10 deducted from balance","3. See VIP Active message","4. Contact admin on WhatsApp 0118431854 to be added to VIP group"],
"inside":"Inside: Balance display, Join VIP $10 button, Status text (VIP Active). After payment admin adds you manually to WhatsApp."},
"ebooks": {"icon":"📚","name":"E-Books Store","price":"From Ksh 500 / $3","to":"/ebooks","color":"#f9c846",
"desc":"Buy business and trading ebooks - Learn how to make money, trade, start business.",
"what":"After paying, ebook PDF downloads automatically to your phone.",
"steps":["1. Browse list of ebooks (title + price)","2. Check your balance","3. Click Buy $price - Amount deducted","4. PDF auto downloads via /download/ filename","5. Read and learn"],
"inside":"Inside: List of ebooks from ebooks_files folder, Each with title, price, Buy button, Auto download after pay."}
}

def make_service_page(key):
    s=SERVICES[key]
    return f"""<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>{s['name']} Guide</title>
<style>
body{{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:0}}
nav{{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #2a2a3a}}
nav a{{color:#f9c846;text-decoration:none;font-weight:bold}}
.container{{padding:20px;max-width:600px;margin:auto}}
.card{{background:#1a1a25;border:1px solid #2a2a3a;padding:16px;border-radius:12px;margin:12px 0;text-align:left}}
.btn-main{{background:{s['color']};color:black;padding:14px 28px;border:none;border-radius:30px;font-weight:bold;font-size:16px;text-decoration:none;display:inline-block;margin:8px 0;width:90%;text-align:center}}
.badge{{background:{s['color']};color:black;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:bold}}
.step{{background:#1e1e2d;border-left:3px solid {s['color']};padding:10px;margin:8px 0;border-radius:0 8px 8px 0}}
</style></head><body>
<nav><a href="/">← Back Home</a><b style="color:{s['color']}">{s['icon']} {s['name']}</b><span></span></nav>
<div class="container">
<div style="text-align:center;padding:20px 0">
<div style="font-size:60px">{s['icon']}</div>
<h1>{s['name']}</h1>
<span class="badge">{s['price']}</span>
<p style="color:#aaa;font-size:14px;margin-top:10px">{s['desc']}</p>
<a class="btn-main" href="{s['to']}">🚀 Start {s['name']} Now →</a>
<p style="font-size:11px;color:#666">Till: {MPESA_TILL} | Admin 0118431854 FREE</p>
</div>

<div class="card">
<h3>🎁 What You Will Get</h3>
<p style="color:#ccc;font-size:14px">{s['what']}</p>
</div>

<div class="card">
<h3>📋 Inside Guide - What Happens Inside?</h3>
<p style="font-size:13px;color:#aaa">When you click Start, you will enter the tool. Here is exactly what you will see:</p>
<p style="font-size:13px;color:#ddd;background:#0e0e14;padding:10px;border-radius:8px">{s['inside']}</p>
</div>

<div class="card">
<h3>🪜 Step-by-Step How To Use</h3>
{''.join(f'<div class="step">{step}</div>' for step in s['steps'])}
</div>

<div class="card" style="border:1px solid {s['color']}">
<h3>💰 How Payment Works</h3>
<p style="font-size:13px;color:#aaa">
1. You login with phone + password<br>
2. You deposit via M-Pesa Till <b style="color:white">{MPESA_TILL}</b><br>
3. Submit M-Pesa code in /trade page<br>
4. Admin approves in /admin → Balance added<br>
5. Inside tool, when you click Download, amount ({s['price']}) is deducted<br>
6. If you are admin (0118431854 + KAUMONI20r4.) it's FREE always<br>
7. Preview has BLUE watermark "PREVIEW PAY $X" - disappears after pay
</p>
</div>

<div style="text-align:center;margin:20px 0">
<a class="btn-main" href="{s['to']}">Start {s['name']} - {s['price']} →</a><br>
<a href="/" style="color:#666;font-size:13px;text-decoration:none">← Back to All Tools</a>
</div>
</div>

<a href="https://wa.me/254118431854?text=Hi%20I%20need%20help%20with%20{s['name']}" target="_blank"
style="position:fixed!important;bottom:25px!important;right:25px!important;background:#25D366!important;color:white!important;padding:16px 22px!important;border-radius:50px!important;font-weight:bold!important;z-index:999999!important;text-decoration:none!important;box-shadow:0 8px 25px rgba(0,0,0,0.6)!important;display:flex!important;align-items:center!important;gap:8px!important;">💬 WhatsApp Us</a>
</body></html>"""

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kaumoni - 8 Tools Kenya</title>
<style>
body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:0}
nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:50;border-bottom:1px solid #2a2a3a}
nav b{color:#f9c846;font-size:20px} nav a{color:white;text-decoration:none;margin:0 8px;font-size:13px}
.hero{padding:40px 20px;text-align:center;background:radial-gradient(circle at top,#2a2a3a 0%,#0e0e14 70%)}
.hero h1{font-size:36px;margin:10px 0}.hero h1 span{color:#f9c846}
.btn-main{background:#f9c846;color:black;padding:12px 22px;border:none;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:6px;font-size:14px}
.card{background:#1a1a25;border:1px solid #2a2a3a;padding:16px;border-radius:12px;text-align:center}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:10px}
@media(max-width:600px){.grid{grid-template-columns:1fr}}
.wallet{background:linear-gradient(135deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px;margin:12px}
input{padding:10px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px}
</style></head><body>
<nav><b>KAUMONI</b><div><a href="/trade">Trade</a><a href="/admin">Admin</a></div></nav>
<div class="hero">
<h1>Kenya's <span>8-in-1</span> Business Tools</h1>
<p style="color:#aaa;font-size:14px;max-width:500px;margin:auto">Posters, Receipts, CVs, Logos, Trading, Signals - All with M-Pesa Till YOUR_TILL_HERE</p>
<a class="btn-main" href="#tools">View All 8 Tools ↓</a>
</div>
<div id="tools" style="padding:10px">
<h2 style="text-align:center">Our Tools - Click to See Guide</h2>
<div class="grid">
<div class="card"><div style="font-size:32px">🎨</div><h3>Poster Maker</h3><p style="font-size:11px;color:#aaa">Sale, Salon, Church</p><b style="color:#f9c846">Ksh 150</b><br><a href="/service/poster" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">🧾</div><h3>Receipt Maker</h3><p style="font-size:11px;color:#aaa">Pro Receipts</p><b style="color:#f9c846">Ksh 150</b><br><a href="/service/receipt" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">📄</div><h3>CV Builder</h3><p style="font-size:11px;color:#aaa">HR Approved</p><b style="color:#f9c846">Ksh 300</b><br><a href="/service/cv" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">💼</div><h3>Logo Maker</h3><p style="font-size:11px;color:#aaa">Brand Logos</p><b style="color:#f9c846">Ksh 500</b><br><a href="/service/logo" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">✉️</div><h3>Cover Letter</h3><p style="font-size:11px;color:#aaa">Job Letters</p><b style="color:#f9c846">Ksh 150</b><br><a href="/service/cover" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card" style="border:1px solid #00c950"><div style="font-size:32px">📈</div><h3>Trading Platform</h3><p style="font-size:11px;color:#aaa">Forex Crypto Gold Live</p><b style="color:#00c950">20% Fee</b><br><a href="/service/trading" class="btn-main" style="padding:8px 16px;background:#00c950;color:white;margin-top:8px">View Guide</a></div>
<div class="card" style="border:1px solid #f9c846"><div style="font-size:32px">📡</div><h3>VIP Signals</h3><p style="font-size:11px;color:#aaa">80% Win Daily</p><b style="color:#f9c846">Ksh 1500</b><br><a href="/service/signals" class="btn-main" style="padding:8px 16px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">📚</div><h3>E-Books Store</h3><p style="font-size:11px;color:#aaa">Business Guides</p><b style="color:#f9c846">From 500</b><br><a href="/service/ebooks" class="btn-main" style="padding:8px 16px;background:#333;color:white;margin-top:8px">View Guide</a></div>
</div>
</div>
<div style="padding:20px;text-align:center">
<div class="wallet" style="max-width:400px;margin:10px auto"><b>💰 Balance:</b> $ <span id="bal">0</span> | <span id="phone">Not logged</span></div>
<div class="card" style="max-width:400px;margin:auto">
<input id="loginPhone" placeholder="Phone 07..." style="width:36%"><input id="loginPass" type="password" placeholder="Password" style="width:36%"><button onclick="login()" style="background:#f9c846;color:black;padding:10px 12px;border:none;border-radius:5px;font-weight:bold">Login</button>
<p id="loginMsg" style="color:#ff5555;font-size:12px"></p>
</div>
</div>
<footer style="text-align:center;padding:20px;color:#666;font-size:11px">Kaumoni V7.3 © 2026 | 8 Tools Guide | Till: YOUR_TILL_HERE</footer>
<a href="https://wa.me/254118431854?text=Hi%20Kaumoni" target="_blank" style="position:fixed!important;bottom:25px!important;right:25px!important;background:#25D366!important;color:white!important;padding:16px 22px!important;border-radius:50px!important;font-weight:bold!important;z-index:999999!important;text-decoration:none!important;box-shadow:0 8px 25px rgba(0,0,0,0.6)!important;">💬 WhatsApp Us</a>
<script>
let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('phone').innerText=ph||'Not logged';
async function check(){if(!ph)return;let res=await fetch('/api/balance?phone='+ph);let d=await res.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}
async function login(){let p=document.getElementById('loginPhone').value.trim();let pw=document.getElementById('loginPass').value.trim();if(!p||!pw){document.getElementById('loginMsg').innerText='Enter phone and password';return;}let res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await res.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);location.reload();}check();
</script></body></html>
"""

# Keep your other tools HTML same as V7.2 (shortened here for space - reuse previous)
TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:8px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:10px;border-radius:8px;margin-top:8px}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}select,input{padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}#tv_chart{height:400px}.topnav{background:#1a1a25;padding:10px;display:flex;gap:8px;overflow:auto}.topnav a{color:#f9c846;text-decoration:none;font-weight:bold;padding:6px 10px;border:1px solid #333;border-radius:5px;white-space:nowrap}.login{position:fixed;top:0;left:0;width:100%;height:100%;background:#0e0e14;z-index:100;display:flex;justify-content:center;align-items:center}</style></head><body>
<div id="loginBox" class="login"><div class="card" style="width:90%;max-width:350px;border:1px solid #f9c846"><h3>🔐 Login</h3><input id="phoneInput" placeholder="Phone" style="width:100%;margin-bottom:6px"><input id="passInput" type="password" placeholder="Password" style="width:100%"><button onclick="login()" style="background:#f9c846;color:black;width:100%;margin-top:10px">Login</button><p id="loginMsg" style="color:#ff5555;font-size:12px"></p></div></div>
<div class="topnav"><a href="/">🏠 Home</a><a href="/trade">📈 Trade</a><a href="/poster-maker">🎨 Poster</a><a href="/admin">👑 Admin</a></div>
<h3 style="color:#f9c846">TIMO TRADING V7.3</h3><div>Hi: <b id="userPhone">-</b> | Bal: $<span id="bal">0</span> <button onclick="logout()" style="background:#333;color:white;padding:4px 8px;font-size:10px">Logout</button></div><div class="card"><button onclick="openDep()" style="background:#00c950;color:white">💰 Deposit Till YOUR_TILL_HERE</button></div><div class="card">Pair: <select id="pair" onchange="changePair()"></select></div><div id="tv_chart" class="card"></div><div class="card"><input id="amt" type="number" value="10" style="width:60px"> $ <button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button> <button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button></div><div id="open"></div><div id="depBox" class="card" style="display:none;border:1px solid #00c950"><h4>Deposit</h4><input id="mpesaCode" placeholder="Code"><input id="depAmt" type="number" placeholder="$"><button onclick="requestDep()" style="background:#00c950;width:100%;margin-top:6px">Submit</button><p id="depStatus"></p></div>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:14px 20px;border-radius:50px;font-weight:bold;z-index:999999;text-decoration:none;">💬 WhatsApp</a>
<script>let pair='BTCUSDT',currentPrice=0;let trades=JSON.parse(localStorage.getItem('trades_v5')||'[]');let pairsList=["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"];let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function login(){let p=document.getElementById('phoneInput').value.trim();let pw=document.getElementById('passInput').value.trim();let res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await res.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);userPhone=p;document.getElementById('loginBox').style.display='none';loadBal();}function logout(){localStorage.removeItem('userPhone_v5');location.reload();}async function loadBal(){if(!userPhone){document.getElementById('loginBox').style.display='flex';return;}document.getElementById('userPhone').innerText=userPhone;let res=await fetch('/api/balance?phone='+userPhone);let dd=await res.json();userBal=dd.balance||0;document.getElementById('bal').innerText=userPhone==='0118431854'?'999 FREE':userBal.toFixed(2);}function openDep(){document.getElementById('depBox').style.display='block';}async function requestDep(){let code=document.getElementById('mpesaCode').value, amt=parseFloat(document.getElementById('depAmt').value);let res=await fetch('/api/deposit-request',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,code:code,amount:amt})});let d=await res.json();document.getElementById('depStatus').innerText=d.message;}function tvSymbol(s){let m={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT'};return m[s]||'BINANCE:'+s;}function loadChart(){document.getElementById('tv_chart').innerHTML='';new TradingView.widget({"autosize":true,"symbol":tvSymbol(pair),"interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","container_id":"tv_chart","backgroundColor":"#1a1a25"});}function loadPairSelect(){let sel=document.getElementById('pair');sel.innerHTML='';pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p;sel.appendChild(o);});loadChart();}async function fetchPrice(){try{let r=await fetch('https://api.binance.com/api/v3/ticker/price?symbol='+pair);let d=await r.json();currentPrice=parseFloat(d.price);}catch(e){}}function changePair(){pair=document.getElementById('pair').value;loadChart();fetchPrice();}async function openTrade(t){let amt=parseFloat(document.getElementById('amt').value);if(userPhone!=='0118431854' && amt>userBal){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:amt,reason:'open_trade'})});let d=await res.json();if(!d.ok){alert(d.message);return;}trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice});localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}async function closeTrade(id){let tr=trades.find(x=>x.id===id);if(!tr)return;let diff=currentPrice-tr.open;if(tr.type==='SELL')diff=-diff;let profit=(diff/tr.open)*tr.amount*100;let ret=tr.amount+profit;let fee=0;if(profit>0){fee=profit*0.20;ret-=fee;await fetch('/api/add-fee',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,fee:fee})});}await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:ret})});trades=trades.filter(x=>x.id!==id);localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}function render(){document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open;if(t.type==='SELL')diff=-diff;let fl=(diff/t.open)*t.amount*100;return '<div class="card">'+t.pair+' '+t.type+' $'+t.amount+' <b>'+fl.toFixed(2)+'</b> <button onclick="closeTrade('+t.id+')" style="background:orange">CLOSE</button></div>';}).join('');}setInterval(fetchPrice,3000);if(userPhone){document.getElementById('loginBox').style.display='none';loadBal();}loadPairSelect();setInterval(render,1000);</script></body></html>
"""

POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px;margin:0}input,select{width:100%;padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-30deg);font-size:38px;font-weight:900;color:#004AFF;border:5px solid #004AFF;background:rgba(255,255,255,0.85);padding:12px 22px;white-space:nowrap;z-index:10;pointer-events:none}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>🎨 Poster - Ksh 150</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px"><div><div class="card"><p>Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Sale Red</option><option value="2">Salon Pink</option><option value="3">Church Blue</option><option value="4">Event Yellow</option><option value="5">Food Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XXXXXXXX" oninput="draw()"><input id="loc" value="Nairobi CBD" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%">📥 Download HD $1</button></div><div id="poster"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){if(!userPhone){alert('Login first');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let t=document.getElementById('tpl').value;let title=document.getElementById('title').value;let sub=document.getElementById('sub').value;let phone=document.getElementById('phone').value;let loc=document.getElementById('loc').value;let colors={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']};let c=colors[t];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px;box-sizing:border-box"><h1 style="font-size:42px;margin:0">${title}</h1><h2 style="margin:10px 0;font-size:20px">${sub}</h2><div style="background:black;color:white;padding:8px 15px;border-radius:20px;margin-top:20px"><b>${phone}</b><br><small>${loc}</small></div></div>`;}async function downloadPoster(){if(userPhone!=='0118431854' && userBal<1){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await res.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm) wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(canvas=>{if(wm) wm.style.display='block';let a=document.createElement('a');a.download='HD.png';a.href=canvas.toDataURL();a.click();if(userPhone!=='0118431854') loadBal();});}draw();loadBal();</script></body></html>"""

# Reuse other simple tools from V7.2 (receipt, cv, logo, cover, signals, ebooks, admin)
RECEIPT_HTML = POSTER_HTML.replace("Poster","Receipt").replace("poster","receipt")
CV_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,textarea{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold}#preview{background:white;color:black;padding:20px;border-radius:8px;position:relative;overflow:hidden;min-height:300px}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-30deg);font-size:34px;font-weight:900;color:#004AFF;border:5px solid #004AFF;background:rgba(255,255,255,0.9);padding:12px 20px;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📄 CV Builder $2</h2><div class="card">Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px"><div><div class="card"><input id="name" value="Timo Kaumoni" oninput="update()"><input id="title" value="Trader & Designer" oninput="update()"><textarea id="summary" oninput="update()">Experienced.</textarea></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%">Download HD $2</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){document.getElementById('preview').innerHTML=`<div id="wm">PREVIEW PAY $2</div><h1>${document.getElementById('name').value}</h1><b>${document.getElementById('title').value}</b><p>${document.getElementById('summary').value}</p>`;}async function downloadCV(){if(userPhone!=='0118431854' && userBal<2){alert('Need $2');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:2,reason:'cv'})});let d=await res.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm) wm.style.display='none';html2canvas(document.getElementById('preview'),{scale:2}).then(c=>{if(wm) wm.style.display='block';let a=document.createElement('a');a.download='CV_HD.png';a.href=c.toDataURL();a.click();if(userPhone!=='0118431854') loadBal();});}update();loadBal();</script></body></html>"""
COVER_HTML = CV_HTML.replace("CV Builder $2","Cover Letter $1").replace("reason:'cv'","reason:'cover'").replace("2","1")
LOGO_HTML = CV_HTML.replace("CV Builder $2","Logo Maker $3").replace("reason:'cv'","reason:'logo'").replace("$2","$3")
RECEIPT_HTML = CV_HTML.replace("CV Builder $2","Receipt Maker $1").replace("reason:'cv'","reason:'receipt'").replace("$2","$1")
SIGNALS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Signals</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:10px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📡 VIP Signals $10</h2><div class="card">Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></div><div class="card"><button onclick="join()" style="background:#f9c846;color:black;width:100%">Join VIP $10</button><p id="status"></p></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}async function join(){if(userPhone!=='0118431854' && userBal<10){alert('Need $10');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}document.getElementById('status').innerText='VIP Active!';if(userPhone!=='0118431854') loadBal();}loadBal();</script></body></html>"""
EBOOK_HTML = SIGNALS_HTML.replace("VIP Signals $10","Ebooks Store").replace("Join VIP","Buy Ebook")
ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin V7.3</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:8px 0}.big{font-size:22px;font-weight:bold;color:#f9c846} button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>👑 ADMIN V7.3 - Guide Pages Added</h2><div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><div>Total Fees</div><div class="big" id="total">$0</div><div id="userCount">0 users</div></div><div class="card" style="border:1px solid #00c950"><h3>💰 Pending Deposits</h3><div id="depList">Loading...</div></div><div class="card"><h3>👥 Users</h3><div id="usersList">Loading...</div></div><script>async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText='$'+(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} ${u.phone==='0118431854'?'👑':''} - $${u.balance} - Fees:$${u.total_fee||0}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add $</button></div>`).join('');document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div class="card" style="background:#2a2a3a"><b>${d.phone}</b> - $${d.amount} - ${d.code} - ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white;margin-top:5px">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';}async function approveDep(idx){let res=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function rejectDep(idx){let res=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function addBal(phone){let amt=prompt('Amount to add');if(!amt)return;let res=await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:phone,amount:parseFloat(amt)})});let d=await res.json();alert(d.message);load();}load();setInterval(load,5000);</script></body></html>
"""

@app.route('/')
def home(): return HOME_HTML.replace("YOUR_TILL_HERE", MPESA_TILL)
@app.route('/service/<key>')
def service_detail(key):
    if key not in SERVICES: return "Service not found", 404
    return make_service_page(key).replace("YOUR_TILL_HERE", MPESA_TILL)

@app.route('/trade')
def trade(): return TRADING_HTML.replace("YOUR_TILL_HERE", MPESA_TILL)
@app.route('/poster-maker')
def poster(): return POSTER_HTML
@app.route('/receipt-maker')
def receipt(): return RECEIPT_HTML
@app.route('/cv-builder')
def cv(): return CV_HTML
@app.route('/cover-letter')
def cover(): return COVER_HTML
@app.route('/logo-maker')
def logo(): return LOGO_HTML
@app.route('/signals')
def signals(): return SIGNALS_HTML
@app.route('/ebooks')
def ebooks(): return EBOOK_HTML
@app.route('/admin')
def admin(): return ADMIN_HTML

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); password=data['password'].strip()
    users=load_json(USERS_FILE, {})
    if phone==ADMIN_PHONE:
        if password!=ADMIN_PASSWORD: return jsonify({"ok":False,"message":"❌ Wrong admin password!"})
        if phone not in users: users[phone]={"phone":phone,"password":password,"balance":999,"total_fee":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":999})
    if phone in users:
        if users[phone].get('password') and users[phone].get('password')!=password: return jsonify({"ok":False,"message":"❌ Wrong password"})
        if not users[phone].get('password'): users[phone]['password']=password; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":users[phone].get('balance',0)})
    else: users[phone]={"phone":phone,"password":password,"balance":0,"total_fee":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users); return jsonify({"ok":True,"balance":0})

@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone')
    if phone==ADMIN_PHONE: return jsonify({"phone":phone,"balance":999,"total_fee":0})
    users=load_json(USERS_FILE, {}); u=users.get(phone, {"phone":phone,"balance":0,"total_fee":0}); return jsonify(u)

@app.route('/api/deposit-request', methods=['POST'])
def api_deposit_request():
    data=request.get_json(); deposits=load_json(DEPOSITS_FILE, []); deposits.append({"phone":data['phone'],"code":data['code'],"amount":float(data['amount']),"status":"pending","time":str(datetime.now())}); save_json(DEPOSITS_FILE, deposits); return jsonify({"ok":True,"message":"Sent! Admin will approve in /admin"})

@app.route('/api/add-balance', methods=['POST'])
def api_add_balance():
    data=request.get_json(); users=load_json(USERS_FILE, {}); phone=data['phone'];
    if phone not in users: users[phone]={"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance']=float(users[phone].get('balance',0))+float(data['amount']); save_json(USERS_FILE, users); return jsonify({"ok":True,"message":f"Added ${data['amount']}"})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load_json(USERS_FILE, {}); phone=data['phone']; amt=float(data['amount'])
    if phone==ADMIN_PHONE: return jsonify({"ok":True,"balance":999})
    if phone not in users or float(users[phone].get('balance',0))<amt: return jsonify({"ok":False,"message":f"Low balance. Till {MPESA_TILL}"})
    users[phone]['balance']-=amt
    if any(x in data.get('reason','') for x in ['poster','cv','logo','vip','ebook','cover','receipt']): users[phone]['total_fee']=users[phone].get('total_fee',0)+amt; fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+amt; save_json(FEES_FILE, fees)
    save_json(USERS_FILE, users); return jsonify({"ok":True,"balance":users[phone]['balance']})

@app.route('/api/add-fee', methods=['POST'])
def api_add_fee():
    data=request.get_json(); if data['phone']==ADMIN_PHONE: return jsonify({"ok":True})
    fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+float(data['fee']); save_json(FEES_FILE, fees)
    users=load_json(USERS_FILE, {});
    if data['phone'] in users: users[data['phone']]['total_fee']=users[data['phone']].get('total_fee',0)+float(data['fee']); save_json(USERS_FILE, users)
    return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {}); deposits=load_json(DEPOSITS_FILE, []); fees=load_json(FEES_FILE, {"total":0}); return jsonify({"users":list(users.values()),"deposits":deposits,"total_fees":fees.get('total',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    data=request.get_json(); idx=int(data['index']); deposits=load_json(DEPOSITS_FILE, []);
    if idx>=len(deposits): return jsonify({"message":"Invalid"}); dep=deposits[idx]
    if dep['status']!='pending': return jsonify({"message":"Already processed"})
    users=load_json(USERS_FILE, {}); phone=dep['phone']
    if phone not in users: users[phone]={"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance']+=float(dep['amount']); save_json(USERS_FILE, users); deposits[idx]['status']='approved'; save_json(DEPOSITS_FILE, deposits); return jsonify({"message":f"Approved! Added ${dep['amount']}"})

@app.route('/api/reject-deposit', methods=['POST'])
def api_reject():
    data=request.get_json(); idx=int(data['index']); deposits=load_json(DEPOSITS_FILE, []); deposits[idx]['status']='rejected'; save_json(DEPOSITS_FILE, deposits); return jsonify({"message":"Rejected"})

@app.route('/api/ebooks')
def api_ebooks():
    files=[];
    if os.path.exists(UPLOAD_FOLDER):
        for f in os.listdir(UPLOAD_FOLDER):
            if f.endswith('.json'):
                with open(os.path.join(UPLOAD_FOLDER,f)) as jf: files.append(json.load(jf))
    return jsonify(files)

@app.route('/download/<filename>')
def download_file(filename): return send_from_directory(UPLOAD_FOLDER, filename)

if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
