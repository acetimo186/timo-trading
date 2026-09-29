
from flask import Flask, request, jsonify, send_from_directory
import os, json
from datetime import datetime

app = Flask(__name__)
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

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni - Animated 8 Tools</title>
<style>
*{box-sizing:border-box}
body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:0;overflow-x:hidden}
nav{background:rgba(26,26,37,0.9);backdrop-filter:blur(10px);padding:12px 20px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:50;border-bottom:1px solid #2a2a3a}
nav b{color:#f9c846;font-size:22px;animation:glow 2s infinite}
@keyframes glow{0%,100%{text-shadow:0 0 5px #f9c846}50%{text-shadow:0 0 20px #f9c846,0 0 30px #ff9800}}
.hero{padding:40px 20px 30px 20px;text-align:center;background:linear-gradient(270deg,#0e0e14,#1a1a25,#2a1a3a,#1a2a25);background-size:600% 600%;animation:gradientMove 8s ease infinite;position:relative;overflow:hidden}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.hero h1{font-size:40px;margin:10px 0;line-height:1.1;animation:slideDown 1s ease}
.hero h1 span{background:linear-gradient(90deg,#f9c846,#ff9800,#00c950,#60a5fa);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;animation:colorShift 3s infinite;background-size:200%}
@keyframes colorShift{0%{filter:hue-rotate(0deg)}100%{filter:hue-rotate(360deg)}}
@keyframes slideDown{from{transform:translateY(-30px);opacity:0}to{transform:translateY(0);opacity:1}}
.floating{position:absolute;font-size:22px;animation:float 6s ease-in-out infinite;opacity:0.6}
.f1{top:15%;left:8%;animation-delay:0s}.f2{top:25%;right:12%;animation-delay:1s}.f3{top:65%;left:15%;animation-delay:2s}.f4{top:70%;right:8%;animation-delay:3s}
@keyframes float{0%,100%{transform:translateY(0) rotate(0deg)}50%{transform:translateY(-18px) rotate(8deg)}}
.btn-main{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:14px 28px;border:none;border-radius:30px;font-weight:bold;font-size:16px;text-decoration:none;display:inline-block;margin:8px;animation:pulse 2s infinite;box-shadow:0 4px 20px rgba(249,200,70,0.4);transition:0.3s}
.btn-main:hover{transform:scale(1.05)}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.btn-sec{background:rgba(30,30,45,0.8);border:1px solid #333;color:white;padding:10px 20px;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:6px}
.marquee{background:#1a1a25;border-top:1px solid #2a2a3a;border-bottom:1px solid #2a2a3a;padding:8px 0;overflow:hidden;white-space:nowrap}
.marquee span{display:inline-block;animation:scroll 22s linear infinite;color:#f9c846;font-weight:bold;font-size:13px}
@keyframes scroll{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}
.card{background:linear-gradient(135deg,#1a1a25,#1e1e2d);border:1px solid #2a2a3a;padding:16px;border-radius:16px;text-align:center;transition:0.4s;position:relative;overflow:hidden}
.card::before{content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;background:linear-gradient(120deg,transparent,rgba(249,200,70,0.1),transparent);transform:rotate(25deg);animation:shine 3s infinite}
@keyframes shine{0%{transform:translateX(-100%) rotate(25deg)}100%{transform:translateX(100%) rotate(25deg)}}
.card:hover{transform:translateY(-6px);border-color:#f9c846;box-shadow:0 10px 30px rgba(249,200,70,0.2)}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:10px}
@media(max-width:600px){.grid{grid-template-columns:1fr}.hero h1{font-size:30px}}
.wallet{background:linear-gradient(90deg,#f9c846,#ff9800,#f9c846);background-size:200%;animation:gradientMove 3s linear infinite;color:black;padding:12px;border-radius:12px;margin:12px;font-weight:bold}
.stat{font-size:26px;font-weight:900;color:#f9c846}
.dot{width:8px;height:8px;background:#00c950;border-radius:50%;display:inline-block;animation:blink 1s infinite}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.2}}
/* AUTO SLIDER */
.slider{width:340px;height:200px;margin:20px auto;position:relative;overflow:hidden;border-radius:12px;border:2px solid #2a2a3a;box-shadow:0 8px 25px rgba(0,0,0,0.5)}
.slide{position:absolute;width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;transition:all 0.8s ease;transform:translateX(100%);opacity:0}
.slide.active{transform:translateX(0);opacity:1}
</style></head><body>
<nav><b>KAUMONI</b><div><a href="/trade" style="color:white;text-decoration:none;margin:0 8px;font-size:13px">📈 Trade</a><a href="/admin" style="color:#f9c846;text-decoration:none;font-weight:bold">👑 Admin</a></div></nav>

<div class="hero">
<div class="floating f1">🎨</div><div class="floating f2">📈</div><div class="floating f3">💼</div><div class="floating f4">✨</div>
<h1>Create <span>Pro Posters</span> in 10 Sec</h1>
<p style="color:#aaa;font-size:14px;max-width:500px;margin:8px auto">Kenya's #1 Animated Toolkit • <span class="dot"></span> <b style="color:#00c950" id="online">2,341 users online</b> • Auto HD Posters</p>

<!-- AUTO SLIDING POSTER PREVIEWS -->
<div class="slider" id="slider">
<div class="slide active" style="background:linear-gradient(135deg,#ff3b3b,#ff9a00)"><h1 style="margin:0;font-size:36px">MEGA SALE!</h1><p style="background:white;color:black;padding:4px 12px;border-radius:20px;margin:6px 0;font-weight:bold">50% OFF</p><small>Salon • Nairobi</small></div>
<div class="slide" style="background:linear-gradient(135deg,#ff69b4,#ffb6d9)"><h1 style="margin:0;font-size:34px">BEAUTY PALACE</h1><p style="background:black;color:white;padding:4px 12px;border-radius:20px;margin:6px 0">Braids - Ksh 500</p><small>Call: 07XX</small></div>
<div class="slide" style="background:linear-gradient(135deg,#1e3a8a,#60a5fa)"><h1 style="margin:0;font-size:32px">SUNDAY SERVICE</h1><p style="background:#f9c846;color:black;padding:4px 12px;border-radius:20px;margin:6px 0;font-weight:bold">Welcome All!</p><small>8AM - 12PM</small></div>
<div class="slide" style="background:linear-gradient(135deg,#f9c846,#ff9800)"><h1 style="margin:0;font-size:34px">GRAND OPENING</h1><p style="background:black;color:white;padding:4px 12px;border-radius:20px;margin:6px 0">New Shop Nairobi</p><small>20% Off First Week</small></div>
<div class="slide" style="background:linear-gradient(135deg,#00c950,#a8ff78);color:black"><h1 style="margin:0;font-size:34px">BURGER FEST</h1><p style="background:black;color:white;padding:4px 12px;border-radius:20px;margin:6px 0">Buy 1 Get 1 Free</p><small>Today Only</small></div>
</div>

<div style="margin-top:10px">
<a class="btn-main" href="#tools">🚀 Explore 8 Tools →</a><br>
<a class="btn-sec" href="/trade">📈 Live Trading Chart</a>
</div>
<p style="font-size:11px;color:#666;margin-top:10px">⚡ No watermark after pay • M-Pesa Till: YOUR_TILL_HERE • Instant HD</p>
</div>

<div class="marquee"><span>🔥 POSTER Ksh 150 • RECEIPT Ksh 150 • CV Ksh 300 • LOGO Ksh 500 • COVER Ksh 150 • TRADING 20% Fee • VIP Ksh 1500 • E-BOOKS From 500 • Till: YOUR_TILL_HERE • 2000+ Businesses • </span></div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;padding:10px;text-align:center">
<div class="card" style="padding:10px"><div class="stat" id="c1">0</div><small style="color:#aaa;font-size:11px">Posters Made</small></div>
<div class="card" style="padding:10px"><div class="stat" id="c2">0</div><small style="color:#aaa;font-size:11px">Happy Users</small></div>
<div class="card" style="padding:10px"><div class="stat"><span class="dot"></span> LIVE</div><small style="color:#aaa;font-size:11px">Trading</small></div>
</div>

<div id="tools" style="padding:10px"><h2 style="text-align:center">✨ Our 8 Magic Tools</h2>
<div class="grid">
<div class="card"><div style="font-size:32px">🎨</div><h3>Poster Maker</h3><b style="color:#f9c846">Ksh 150</b><br><a href="/service/poster" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">🧾</div><h3>Receipt Maker</h3><b style="color:#f9c846">Ksh 150</b><br><a href="/service/receipt" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">📄</div><h3>CV Builder</h3><b style="color:#f9c846">Ksh 300</b><br><a href="/service/cv" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">💼</div><h3>Logo Maker</h3><b style="color:#f9c846">Ksh 500</b><br><a href="/service/logo" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">✉️</div><h3>Cover Letter</h3><b style="color:#f9c846">Ksh 150</b><br><a href="/service/cover" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card" style="border:1px solid #00c950"><div style="font-size:32px">📈</div><h3>Trading</h3><b style="color:#00c950">20% Fee</b><br><a href="/service/trading" class="btn-main" style="padding:8px 16px;background:#00c950;color:white;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">📡</div><h3>VIP Signals</h3><b style="color:#f9c846">Ksh 1500</b><br><a href="/service/signals" class="btn-main" style="padding:8px 16px;font-size:13px;margin-top:8px">View Guide</a></div>
<div class="card"><div style="font-size:32px">📚</div><h3>E-Books</h3><b style="color:#f9c846">From 500</b><br><a href="/service/ebooks" class="btn-main" style="padding:8px 16px;background:#333;color:white;margin-top:8px">View Guide</a></div>
</div></div>

<div style="padding:20px;text-align:center"><div class="wallet" style="max-width:400px;margin:10px auto"><b>Bal:</b> $ <span id="bal">0</span> | <span id="phone">Not logged</span> <span class="dot"></span></div>
<div class="card" style="max-width:400px;margin:auto"><input id="loginPhone" placeholder="Phone" style="width:36%;padding:10px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><input id="loginPass" type="password" placeholder="Pass" style="width:36%;padding:10px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><button onclick="login()" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 14px;border:none;border-radius:6px;font-weight:bold;cursor:pointer">Login</button><p id="loginMsg" style="color:#ff5555;font-size:12px"></p></div></div>

<footer style="text-align:center;padding:20px;color:#666;font-size:11px">Kaumoni V8 Animated © 2026 | Till YOUR_TILL_HERE | Admin 0118431854 FREE</footer>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:25px;right:25px;background:#25D366;color:white;padding:16px 22px;border-radius:50px;font-weight:bold;z-index:999999;text-decoration:none;box-shadow:0 8px 25px rgba(0,0,0,0.6);animation:pulse 2s infinite">💬 WhatsApp</a>

<script>
let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('phone').innerText=ph||'Not logged';
async function check(){if(!ph)return;let res=await fetch('/api/balance?phone='+ph);let d=await res.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}
async function login(){let p=document.getElementById('loginPhone').value.trim();let pw=document.getElementById('loginPass').value.trim();if(!p||!pw){document.getElementById('loginMsg').innerText='Enter phone and pass';return;}let res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await res.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);location.reload();}
let n1=0,n2=0;setInterval(()=>{if(n1<2341){n1+=11;document.getElementById('c1').innerText=n1}if(n2<1876){n2+=9;document.getElementById('c2').innerText=n2}},40);
let cur=0;let slides=document.querySelectorAll('.slide');setInterval(()=>{slides[cur].classList.remove('active');cur=(cur+1)%slides.length;slides[cur].classList.add('active');},2200);
check();
</script></body></html>"""

POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.95);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Poster $1</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Sale Red</option><option value="2">Salon Pink</option><option value="3">Church Blue</option><option value="4">Event Yellow</option><option value="5">Food Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XXXXXXXX" oninput="draw()"><input id="loc" value="Nairobi CBD" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%">Download HD $1</button></div><div id="poster"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){if(!userPhone){alert('Login first');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let t=document.getElementById('tpl').value;let title=document.getElementById('title').value;let sub=document.getElementById('sub').value;let phone=document.getElementById('phone').value;let loc=document.getElementById('loc').value;let colors={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']};let c=colors[t];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px;box-sizing:border-box"><h1 style="font-size:42px;margin:0">${title}</h1><h2 style="margin:10px 0;font-size:20px">${sub}</h2><div style="background:black;color:white;padding:8px 15px;border-radius:20px;margin-top:20px"><b>${phone}</b><br><small>${loc}</small></div></div>`;}async function downloadPoster(){if(userPhone!=='0118431854' && userBal<1){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await res.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm) wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(canvas=>{if(wm) wm.style.display='block';let a=document.createElement('a');a.download='HD.png';a.href=canvas.toDataURL();a.click();if(userPhone!=='0118431854') loadBal();});}draw();loadBal();</script></body></html>"""

TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:8px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:10px;border-radius:8px;margin-top:8px}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}select,input{padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}#tv_chart{height:400px}.login{position:fixed;top:0;left:0;width:100%;height:100%;background:#0e0e14;z-index:100;display:flex;justify-content:center;align-items:center}</style></head><body><div id="loginBox" class="login"><div class="card" style="width:90%;max-width:350px;border:1px solid #f9c846"><h3>Login</h3><input id="phoneInput" placeholder="Phone" style="width:100%;margin-bottom:6px"><input id="passInput" type="password" placeholder="Password" style="width:100%"><button onclick="login()" style="background:#f9c846;color:black;width:100%;margin-top:10px">Login</button><p id="loginMsg" style="color:#ff5555;font-size:12px"></p></div></div><div><a href="/" style="color:#f9c846">← Home</a> <b>TRADING</b> Hi <b id="userPhone">-</b> Bal $<span id="bal">0</span> <button onclick="logout()" style="background:#333;color:white;padding:4px 8px;font-size:10px">Logout</button></div><div class="card"><button onclick="openDep()" style="background:#00c950;color:white">Deposit Till YOUR_TILL_HERE</button></div><div class="card">Pair <select id="pair" onchange="changePair()"></select></div><div id="tv_chart" class="card"></div><div class="card"><input id="amt" type="number" value="10" style="width:60px"> $ <button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button> <button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button></div><div id="open"></div><div id="depBox" class="card" style="display:none;border:1px solid #00c950"><h4>Deposit</h4><input id="mpesaCode" placeholder="Code"><input id="depAmt" type="number" placeholder="$"><button onclick="requestDep()" style="background:#00c950;width:100%;margin-top:6px">Submit</button><p id="depStatus"></p></div><script>let pair='BTCUSDT',currentPrice=0;let trades=JSON.parse(localStorage.getItem('trades_v5')||'[]');let pairsList=["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"];let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function login(){let p=document.getElementById('phoneInput').value.trim();let pw=document.getElementById('passInput').value.trim();let res=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await res.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);userPhone=p;document.getElementById('loginBox').style.display='none';loadBal();}function logout(){localStorage.removeItem('userPhone_v5');location.reload();}async function loadBal(){if(!userPhone){document.getElementById('loginBox').style.display='flex';return;}document.getElementById('userPhone').innerText=userPhone;let res=await fetch('/api/balance?phone='+userPhone);let dd=await res.json();userBal=dd.balance||0;document.getElementById('bal').innerText=userPhone==='0118431854'?'999 FREE':userBal.toFixed(2);}function openDep(){document.getElementById('depBox').style.display='block';}async function requestDep(){let code=document.getElementById('mpesaCode').value, amt=parseFloat(document.getElementById('depAmt').value);let res=await fetch('/api/deposit-request',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,code:code,amount:amt})});let d=await res.json();document.getElementById('depStatus').innerText=d.message;}function tvSymbol(s){let m={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT'};return m[s]||'BINANCE:'+s;}function loadChart(){document.getElementById('tv_chart').innerHTML='';new TradingView.widget({"autosize":true,"symbol":tvSymbol(pair),"interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","container_id":"tv_chart","backgroundColor":"#1a1a25"});}function loadPairSelect(){let sel=document.getElementById('pair');sel.innerHTML='';pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p;sel.appendChild(o);});loadChart();}async function fetchPrice(){try{let r=await fetch('https://api.binance.com/api/v3/ticker/price?symbol='+pair);let d=await r.json();currentPrice=parseFloat(d.price);}catch(e){}}function changePair(){pair=document.getElementById('pair').value;loadChart();fetchPrice();}async function openTrade(t){let amt=parseFloat(document.getElementById('amt').value);if(userPhone!=='0118431854' && amt>userBal){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:amt,reason:'open_trade'})});let d=await res.json();if(!d.ok){alert(d.message);return;}trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice});localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}async function closeTrade(id){let tr=trades.find(x=>x.id===id);if(!tr)return;let diff=currentPrice-tr.open;if(tr.type==='SELL')diff=-diff;let profit=(diff/tr.open)*tr.amount*100;let ret=tr.amount+profit;let fee=0;if(profit>0){fee=profit*0.20;ret-=fee;await fetch('/api/add-fee',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,fee:fee})});}await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:ret})});trades=trades.filter(x=>x.id!==id);localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}function render(){document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open;if(t.type==='SELL')diff=-diff;let fl=(diff/t.open)*t.amount*100;return '<div class="card">'+t.pair+' '+t.type+' $'+t.amount+' <b>'+fl.toFixed(2)+'</b> <button onclick="closeTrade('+t.id+')" style="background:orange">CLOSE</button></div>';}).join('');}setInterval(fetchPrice,3000);if(userPhone){document.getElementById('loginBox').style.display='none';loadBal();}loadPairSelect();setInterval(render,1000);</script></body></html>
"""

ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:8px 0}.big{font-size:22px;font-weight:bold;color:#f9c846}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>ADMIN V8 Animated</h2><div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><div>Total Fees</div><div class="big" id="total">$0</div><div id="userCount">0 users</div></div><div class="card"><h3>Pending Deposits</h3><div id="depList">Loading...</div></div><div class="card"><h3>Users</h3><div id="usersList">Loading...</div></div><script>async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText='$'+(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} - $${u.balance}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add $</button></div>`).join('');document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div class="card" style="background:#2a2a3a"><b>${d.phone}</b> - $${d.amount} - ${d.code} - ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white;margin-top:5px">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';}async function approveDep(idx){let res=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function rejectDep(idx){let res=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function addBal(phone){let amt=prompt('Amount');if(!amt)return;let res=await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:phone,amount:parseFloat(amt)})});let d=await res.json();alert(d.message);load();}load();setInterval(load,5000);</script></body></html>
"""

GUIDE_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Guide</title><style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:0}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;border-bottom:1px solid #2a2a3a}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.container{padding:20px;max-width:600px;margin:auto}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:16px;border-radius:12px;margin:12px 0;text-align:left}.btn-main{background:#f9c846;color:black;padding:14px 28px;border:none;border-radius:30px;font-weight:bold;font-size:16px;text-decoration:none;display:inline-block;margin:8px 0;width:90%;text-align:center}.badge{background:#f9c846;color:black;padding:4px 10px;border-radius:20px;font-size:12px;font-weight:bold}.step{background:#1e1e2d;border-left:3px solid #f9c846;padding:10px;margin:8px 0;border-radius:0 8px 8px 0}</style></head><body>
<nav><a href="/">← Back Home</a><b id="gname">Tool Guide</b><span></span></nav>
<div class="container"><div style="text-align:center;padding:20px 0"><div style="font-size:60px" id="gicon">🎨</div><h1 id="gtitle">Poster Maker</h1><span class="badge" id="gprice">Ksh 150</span><p style="color:#aaa;font-size:14px" id="gdesc">Description</p><a class="btn-main" id="gbtn" href="/poster-maker">Start Now</a></div>
<div class="card"><h3>🎁 What You Get</h3><p style="color:#ccc;font-size:14px" id="gwhat">What</p></div>
<div class="card"><h3>📋 Inside Guide</h3><p style="color:#ddd;background:#0e0e14;padding:10px;border-radius:8px;font-size:13px" id="ginside">Inside</p></div>
<div class="card"><h3>🪜 Steps</h3><div id="gsteps"></div></div>
<div class="card" style="border:1px solid #f9c846"><h3>💰 Payment</h3><p style="font-size:13px;color:#aaa">Till: YOUR_TILL_HERE<br>Deposit in /trade, admin approves in /admin. BLUE watermark disappears after pay. Admin 0118431854 FREE.</p></div>
<div style="text-align:center"><a class="btn-main" id="gbtn2" href="/poster-maker">Start Now</a><br><a href="/" style="color:#666;font-size:13px;text-decoration:none">← All Tools</a></div></div>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:25px;right:25px;background:#25D366;color:white;padding:16px 22px;border-radius:50px;font-weight:bold;z-index:999999;text-decoration:none;">💬 WhatsApp</a>
<script>
const data={
poster:{icon:"🎨",name:"Poster Maker",price:"Ksh 150 / $1",to:"/poster-maker",desc:"Create professional business posters in 10 seconds. No design skills needed.",what:"You get HD poster without watermark ready for WhatsApp Status, Facebook, print.",inside:"Inside you will find: 5 color templates, Title editor, Offer editor, Phone and Location box, Live preview 350x500, BLUE PAY watermark, Download HD button.",steps:["1. Choose template: Sale Red, Salon Pink, Church Blue","2. Type title MEGA SALE!, offer 50% OFF, phone, location","3. See LIVE BLUE preview with watermark PREVIEW PAY $1","4. Pay $1 from balance - watermark disappears","5. Click Download HD - Clean image saved"]},
receipt:{icon:"🧾",name:"Receipt Maker",price:"Ksh 150 / $1",to:"/receipt-maker",desc:"Generate professional receipts for your shop.",what:"HD receipt with shop name, customer, item, price. No watermark after pay.",inside:"Inside: Business name input, Customer name, Item sold, Price input, Live receipt preview white paper style, Download HD $1.",steps:["Enter Business Name","Enter Customer and Item","Live preview with BLUE watermark","Pay $1 and download clean"]},
cv:{icon:"📄",name:"CV Builder",price:"Ksh 300 / $2",to:"/cv-builder",desc:"Build HR-approved professional CV that gets you hired. ATS friendly.",what:"You get HD CV image ready to print or send to HR. Professional layout.",inside:"Inside: Name input, Job Title input, Summary textarea, Experience and Skills fields, Live white CV preview, Download HD $2 button.",steps:["Enter Full Name and Job Title","Enter Summary, Experience, Skills","Live CV preview with BLUE watermark PAY $2","Pay $2 - watermark removed","Download HD CV to apply"]},
logo:{icon:"💼",name:"Logo Maker",price:"Ksh 500 / $3",to:"/logo-maker",desc:"Design modern business logo for shop in seconds.",what:"HD square logo 350x350 perfect for WhatsApp profile, business cards.",inside:"Inside: Business name input, Tagline input, Square logo preview box, Download $3.",steps:["Enter Business Name e.g. KAUMONI","Enter Tagline e.g. TRADING","Live square logo preview with watermark","Pay $3 to remove watermark","Download HD logo"]},
cover:{icon:"✉️",name:"Cover Letter",price:"Ksh 150 / $1",to:"/cover-letter",desc:"Write winning cover letter that makes HR call you.",what:"HD Cover Letter image ready to attach with CV.",inside:"Inside: Name input, Letter textarea, Live preview, Download $1.",steps:["Enter Your Name","Type cover letter text","Preview with PAY watermark","Pay $1 and download clean HD"]},
trading:{icon:"📈",name:"Trading Platform",price:"20% Profit Fee Only",to:"/trade",desc:"Trade Forex, Crypto, Gold live with real TradingView chart.",what:"Live trading with BUY/SELL, profit calc, 20% fee goes to admin when profit.",inside:"Inside: TradingView dark chart, Pair selector EURUSD BTCUSDT, BUY green SELL red buttons, Amount input, Open trades list with live P/L, Balance top, Deposit box with M-Pesa code.",steps:["Login with phone + password","Deposit via M-Pesa Till - Admin approves in /admin","Choose pair EURUSD GBPUSD BTCUSDT ETHUSDT XAUUSDT","Enter amount $10 and click BUY or SELL","See live profit/loss, click CLOSE. If profit 20% fee auto deducted","Balance updates instantly"]},
signals:{icon:"📡",name:"VIP Signals",price:"Ksh 1500 / $10",to:"/signals",desc:"Get daily trading signals with 80% win rate.",what:"After paying $10 you become VIP. See VIP Active and get WhatsApp group link.",inside:"Inside: Balance display, Join VIP $10 button, Status text VIP Active. Admin adds you manually to WhatsApp.",steps:["Check balance - Need $10","Click Join VIP $10 - $10 deducted","See VIP Active message","Contact admin on WhatsApp 0118431854 to be added to VIP group"]},
ebooks:{icon:"📚",name:"E-Books Store",price:"From Ksh 500",to:"/ebooks",desc:"Buy business and trading ebooks - Learn how to make money.",what:"After paying ebook PDF downloads automatically.",inside:"Inside: List of ebooks from folder, Each with title price Buy button, Auto download after pay.",steps:["Browse list of ebooks","Check your balance","Click Buy - Amount deducted","PDF auto downloads","Read and learn"]}
};
let key=window.location.pathname.split('/').pop();
let d=data[key]||data.poster;
document.getElementById('gicon').innerText=d.icon;
document.getElementById('gname').innerText=d.name;
document.getElementById('gtitle').innerText=d.name;
document.getElementById('gprice').innerText=d.price;
document.getElementById('gdesc').innerText=d.desc;
document.getElementById('gwhat').innerText=d.what;
document.getElementById('ginside').innerText=d.inside;
document.getElementById('gbtn').href=d.to;
document.getElementById('gbtn2').href=d.to;
document.getElementById('gbtn').innerText="Start "+d.name+" Now";
document.getElementById('gbtn2').innerText="Start "+d.name+" - "+d.price;
let stepsDiv=document.getElementById('gsteps');
stepsDiv.innerHTML=d.steps.map(s=>`<div class="step">${s}</div>`).join('');
</script></body></html>"""

@app.route('/')
def home(): return HOME_HTML.replace("YOUR_TILL_HERE", MPESA_TILL)
@app.route('/service/<key>')
def service_page_route(key): return GUIDE_HTML.replace("YOUR_TILL_HERE", MPESA_TILL)
@app.route('/trade')
def trade(): return TRADING_HTML.replace("YOUR_TILL_HERE", MPESA_TILL)
@app.route('/poster-maker')
def poster(): return POSTER_HTML
@app.route('/receipt-maker')
def receipt(): return POSTER_HTML.replace("Poster $1","Receipt $1").replace("MEGA SALE!","Kaumoni Shop Receipt")
@app.route('/cv-builder')
def cv(): return POSTER_HTML.replace("Poster $1","CV Builder $2 - Use full version after deploy").replace("MEGA SALE!","Timo Kaumoni - CV")
@app.route('/cover-letter')
def cover(): return POSTER_HTML.replace("Poster $1","Cover Letter $1")
@app.route('/logo-maker')
def logo(): return POSTER_HTML.replace("Poster $1","Logo Maker $3")
@app.route('/signals')
def signals(): return "<html><body style='background:#0e0e14;color:white;font-family:Arial;padding:20px'><a href='/' style='color:#f9c846'>← Home</a><h2>VIP Signals $10</h2><p>Phone <b id='uPhone'>-</b> Bal $<span id='uBal'>0</span></p><button onclick='join()' style='background:#f9c846;padding:10px;border:none;border-radius:6px;font-weight:bold;width:100%'>Join VIP $10</button><p id='status'></p><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;document.getElementById('uBal').innerText=userPhone==='0118431854'?'999 FREE':userBal.toFixed(2);}async function join(){if(userPhone!=='0118431854'&&userBal<10){alert('Need $10');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}document.getElementById('status').innerText='VIP Active!';}loadBal();</script></body></html>"
@app.route('/ebooks')
def ebooks(): return signals()
@app.route('/admin')
def admin(): return ADMIN_HTML

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); password=data['password'].strip()
    users=load_json(USERS_FILE, {})
    if phone==ADMIN_PHONE:
        if password!=ADMIN_PASSWORD: return jsonify({"ok":False,"message":"Wrong admin password!"})
        if phone not in users: users[phone]={"phone":phone,"password":password,"balance":999,"total_fee":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":999})
    if phone in users:
        if users[phone].get('password') and users[phone].get('password')!=password: return jsonify({"ok":False,"message":"Wrong password"})
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
    data=request.get_json(); users=load_json(USERS_FILE, {}); phone=data['phone']
    if phone not in users: users[phone]={"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance']=float(users[phone].get('balance',0))+float(data['amount']); save_json(USERS_FILE, users); return jsonify({"ok":True,"message":"Added"})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load_json(USERS_FILE, {}); phone=data['phone']; amt=float(data['amount'])
    if phone==ADMIN_PHONE: return jsonify({"ok":True,"balance":999})
    if phone not in users or float(users[phone].get('balance',0))<amt: return jsonify({"ok":False,"message":"Low balance"})
    users[phone]['balance']-=amt
    if any(x in data.get('reason','') for x in ['poster','cv','logo','vip','ebook','cover','receipt']): users[phone]['total_fee']=users[phone].get('total_fee',0)+amt; fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+amt; save_json(FEES_FILE, fees)
    save_json(USERS_FILE, users); return jsonify({"ok":True,"balance":users[phone]['balance']})

@app.route('/api/add-fee', methods=['POST'])
def api_add_fee():
    data=request.get_json()
    if data['phone']==ADMIN_PHONE: return jsonify({"ok":True})
    fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+float(data['fee']); save_json(FEES_FILE, fees)
    users=load_json(USERS_FILE, {});
    if data['phone'] in users: users[data['phone']]['total_fee']=users[data['phone']].get('total_fee',0)+float(data['fee']); save_json(USERS_FILE, users)
    return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {}); deposits=load_json(DEPOSITS_FILE, []); fees=load_json(FEES_FILE, {"total":0}); return jsonify({"users":list(users.values()),"deposits":deposits,"total_fees":fees.get('total',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    data=request.get_json(); idx=int(data['index']); deposits=load_json(DEPOSITS_FILE, []); dep=deposits[idx]
    if dep['status']!='pending': return jsonify({"message":"Already processed"})
    users=load_json(USERS_FILE, {}); phone=dep['phone']
    if phone not in users: users[phone]={"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance']+=float(dep['amount']); save_json(USERS_FILE, users); deposits[idx]['status']='approved'; save_json(DEPOSITS_FILE, deposits); return jsonify({"message":"Approved!"})

@app.route('/api/reject-deposit', methods=['POST'])
def api_reject():
    data=request.get_json(); idx=int(data['index']); deposits=load_json(DEPOSITS_FILE, []); deposits[idx]['status']='rejected'; save_json(DEPOSITS_FILE, deposits); return jsonify({"message":"Rejected"})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
