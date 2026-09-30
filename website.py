
from flask import Flask, request, jsonify
import os, json, requests, random
from datetime import datetime
app = Flask(__name__)
USERS_FILE='users.json';DEPOSITS_FILE='deposits.json';FEES_FILE='fees.json';SIGNALS_FILE='signals.json';REFS_FILE='referrals.json'
ADMIN_PHONE="0118431854";ADMIN_PASSWORD="KAUMONI20r4."
def load_json(f,d):
    if not os.path.exists(f): return d
    try:
        with open(f) as jf: return json.load(jf)
    except: return d
def save_json(f,data):
    with open(f,'w') as jf: json.dump(data,jf)
def get_trend(pair):
    try:
        url=f"https://data-api.binance.vision/api/v3/klines?symbol={pair}&interval=1h&limit=55"
        r=requests.get(url,timeout=10).json()
        if isinstance(r,list) and len(r)>50:
            closes=[float(x[4]) for x in r];sma20=sum(closes[-20:])/20;sma50=sum(closes[-50:])/50;price=closes[-1]
            trend="BUY" if sma20>sma50 else "SELL"
            return {"trend":trend,"price":price,"sma20":sma20,"sma50":sma50,"note":"Live trend"}
    except: pass
    fb={"BTCUSDT":65200,"ETHUSDT":3200,"EURUSDT":1.0850,"GBPUSDT":1.27,"XAUUSDT":2345.5}.get(pair,2340)
    return {"trend":"BUY","price":fb,"sma20":fb-2,"sma50":fb-8,"note":"Check TV"}

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni V16 - 18 Tools TIMOTHY</title>
<style>
*{box-sizing:border-box}body{background:#0a0a12;color:white;font-family:Arial;margin:0;overflow-x:hidden}
nav{background:rgba(26,26,37,0.95);backdrop-filter:blur(10px);padding:12px 20px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #2a2a3a;z-index:100}nav b{color:#f9c846}
.btn-main{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:11px 20px;border:none;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:4px;animation:pulse 2s infinite;font-size:12px}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.hero{background:linear-gradient(270deg,#0e0e14,#1a1a25,#2a1a3a,#4a1a6a,#0e0e14,#1a2a5a);background-size:800% 800%;animation:gradMove 12s ease infinite;text-align:center;padding:28px 15px}
@keyframes gradMove{0%{background-position:0% 50%}25%{background-position:100% 50%}50%{background-position:50% 100%}75%{background-position:0% 100%}100%{background-position:0% 50%}}
.moving-name{font-size:18px;font-weight:bold;color:#f9c846;display:inline-block;animation:nameMove 3s ease-in-out infinite;background:linear-gradient(90deg,#f9c846,#ff9800,#f9c846);background-size:200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
@keyframes nameMove{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px) scale(1.1)}}
.marquee{width:100%;overflow:hidden;white-space:nowrap;background:rgba(0,0,0,0.4);padding:10px 0;border-top:1px solid #f9c846;border-bottom:1px solid #f9c846;margin:15px 0}
.marquee-track{display:inline-block;animation:marquee 40s linear infinite}
@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.price-tag{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:4px 11px;border-radius:20px;font-weight:bold;margin:0 7px;font-size:11px}
.slider{width:340px;height:180px;margin:18px auto;position:relative;overflow:hidden;border-radius:14px;border:2px solid #f9c846}
.slide{position:absolute;width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;transition:0.8s;transform:translateX(100%);opacity:0}
.slide.active{transform:translateX(0);opacity:1}
.card{background:linear-gradient(135deg,#1a1a25,#222235);border:1px solid #2a2a3a;padding:12px;border-radius:14px;margin:6px;text-align:center;transition:0.3s}
.card:hover{transform:translateY(-4px);border-color:#f9c846}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px;padding:12px}@media(max-width:1000px){.grid{grid-template-columns:1fr 1fr 1fr}}@media(max-width:700px){.grid{grid-template-columns:1fr 1fr}}@media(max-width:500px){.grid{grid-template-columns:1fr}}
.wallet{background:linear-gradient(90deg,#f9c846,#ff9800);background-size:200% 200%;animation:gradMove 3s linear infinite;color:black;padding:12px;border-radius:12px;margin:12px;font-weight:bold}
.new-badge{background:#00c950;color:white;padding:2px 7px;border-radius:10px;font-size:9px;margin-left:4px;animation:pricePop 1s infinite}
@keyframes pricePop{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
.ref-box{background:linear-gradient(135deg,#1a1a25,#2a2a4a);border:2px dashed #f9c846;padding:12px;border-radius:12px;margin:12px auto;max-width:600px;text-align:center}
</style></head><body>
<nav><b>KAUMONI V16</b><div><a href="/trade" style="color:white;text-decoration:none;margin:0 6px">📈 Trade</a><a href="/admin" style="color:#f9c846;font-weight:bold;text-decoration:none">👑 TIMOTHY</a></div></nav>
<div class="hero">
<h1>Create <span style="color:#f9c846">Pro Designs</span> in 10 Seconds</h1>
<p>Managed by <span class="moving-name">TIMOTHY - Trusted Admin</span> <span style="display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:3px 10px;border-radius:20px;font-weight:bold;margin-left:6px">ONLINE ✅ 18 TOOLS</span></p>
<p style="color:#ccc;font-size:13px;max-width:700px;margin:10px auto">Now 18 Tools! Certificate + Payslip + Biz Card + AI Caption ADDED! Same moving background kept!</p>
<div class="slider" id="slider">
<div class="slide active" style="background:linear-gradient(135deg,#6a0dad,#f9c846)"><h2>📜 NEW! Certificate $1.5</h2><small>Schools, Churches, NGOs</small></div>
<div class="slide" style="background:linear-gradient(135deg,#0d47a1,#42a5f5)"><h2>💳 NEW! Business Card $2</h2><small>Front + Back HD</small></div>
<div class="slide" style="background:linear-gradient(135deg,#1b5e20,#66bb6a)"><h2>💰 NEW! Payslip $1</h2><small>SME Monthly Recurring</small></div>
<div class="slide" style="background:linear-gradient(135deg,#ff6f00,#ffca28);color:black"><h2>🤖 NEW! AI Caption $1</h2><small>Sheng to Poster Auto</small></div>
</div>
<div class="marquee"><div class="marquee-track">
<span class="price-tag">📜 Certificate $1.5 NEW</span><span class="price-tag">💳 Biz Card $2 NEW</span><span class="price-tag">💰 Payslip $1 NEW</span><span class="price-tag">🤖 AI Caption $1 NEW</span><span class="price-tag">🧾 KRA E-TIMS $1.5</span><span class="price-tag">💸 Referral $1</span><span class="price-tag">🎵 TikTok FREE</span><span class="price-tag">🎨 Poster $1</span><span class="price-tag">📱 QR USABLE $1</span><span class="price-tag">✂️ BG Remover $1</span>
<span class="price-tag">📜 Certificate $1.5 NEW</span><span class="price-tag">💳 Biz Card $2 NEW</span><span class="price-tag">💰 Payslip $1 NEW</span><span class="price-tag">🤖 AI Caption $1 NEW</span><span class="price-tag">🧾 KRA E-TIMS $1.5</span><span class="price-tag">💸 Referral $1</span><span class="price-tag">🎵 TikTok FREE</span><span class="price-tag">🎨 Poster $1</span><span class="price-tag">📱 QR USABLE $1</span><span class="price-tag">✂️ BG Remover $1</span>
</div></div>
<div class="ref-box"><h3 style="color:#f9c846">💸 Earn $1 Per Friend - Referral</h3><div style="background:#0e0e14;padding:8px;border-radius:8px;word-break:break-all;font-size:12px;border:1px solid #f9c846"><span id="refLink">Login to get link</span></div><button onclick="copyRef()" style="background:#f9c846;color:black;padding:7px 14px;border:none;border-radius:20px;font-weight:bold;margin-top:8px">📋 Copy</button><p style="font-size:11px;color:#00c950">Refs: <span id="refCount">0</span> | Earned $<span id="refEarn">0</span></p></div>
<a class="btn-main" href="#tools">🚀 Explore 18 Tools</a>
</div>
<div id="tools" style="padding:15px;max-width:1200px;margin:auto">
<h2 style="text-align:center">💎 18 Premium Tools - V16 by TIMOTHY</h2>
<div class="grid">
<div class="card" style="border:2px solid #f9c846"><div style="font-size:28px">📜</div><h3 style="font-size:13px">Certificate <span class="new-badge" style="background:#6a0dad">NEW</span></h3><b style="color:#f9c846">$1.5</b><br><a href="/certificate-maker" class="btn-main" style="background:#6a0dad;color:white">Make Cert</a></div>
<div class="card" style="border:2px solid #42a5f5"><div style="font-size:28px">💳</div><h3 style="font-size:13px">Biz Card <span class="new-badge" style="background:#0d47a1">NEW</span></h3><b style="color:#42a5f5">$2</b><br><a href="/business-card" class="btn-main" style="background:#0d47a1;color:white">Make Card</a></div>
<div class="card" style="border:2px solid #00c950"><div style="font-size:28px">💰</div><h3 style="font-size:13px">Payslip <span class="new-badge">NEW</span></h3><b style="color:#00c950">$1</b><br><a href="/payslip-maker" class="btn-main" style="background:#00c950;color:white">Make Payslip</a></div>
<div class="card" style="border:2px solid #ff9800"><div style="font-size:28px">🤖</div><h3 style="font-size:13px">AI Caption <span class="new-badge" style="background:#ff9800;color:black">NEW</span></h3><b style="color:#ff9800">$1</b><br><a href="/ai-caption" class="btn-main" style="background:#ff9800;color:black">Generate</a></div>
<div class="card"><div style="font-size:28px">🎨</div><h3 style="font-size:13px">Poster</h3><b style="color:#f9c846">$1</b><br><a href="/poster-maker" class="btn-main">Create</a></div>
<div class="card"><div style="font-size:28px">🧾</div><h3 style="font-size:13px">Receipt</h3><b style="color:#f9c846">$1</b><br><a href="/receipt-maker" class="btn-main">Create</a></div>
<div class="card"><div style="font-size:28px">🧾</div><h3 style="font-size:13px">KRA E-TIMS</h3><b style="color:#f9c846">$1.5</b><br><a href="/kra-invoice" class="btn-main">Make KRA</a></div>
<div class="card"><div style="font-size:28px">📄</div><h3 style="font-size:13px">CV Builder</h3><b style="color:#f9c846">$2</b><br><a href="/cv-builder" class="btn-main">Build CV</a></div>
<div class="card"><div style="font-size:28px">💼</div><h3 style="font-size:13px">Logo Maker</h3><b style="color:#f9c846">$3</b><br><a href="/logo-maker" class="btn-main">Design</a></div>
<div class="card"><div style="font-size:28px">✂️</div><h3 style="font-size:13px">BG Remover</h3><b style="color:#00c950">$1</b><br><a href="/bg-remover" class="btn-main" style="background:#00c950;color:white">Remove</a></div>
<div class="card"><div style="font-size:28px">📱</div><h3 style="font-size:13px">QR Till</h3><b style="color:#00c950">$1</b><br><a href="/qr-maker" class="btn-main" style="background:#00c950;color:white">Make QR</a></div>
<div class="card"><div style="font-size:28px">📊</div><h3 style="font-size:13px">Lot Calc</h3><b style="color:#00c950">FREE</b><br><a href="/lot-calculator" class="btn-main" style="background:#00c950;color:white">Calc</a></div>
<div class="card"><div style="font-size:28px">🎵</div><h3 style="font-size:13px">TikTok DL</h3><b style="color:#ff0050">FREE</b><br><a href="/tiktok-downloader" class="btn-main" style="background:#ff0050;color:white">Download</a></div>
<div class="card"><div style="font-size:28px">💸</div><h3 style="font-size:13px">Referral</h3><b style="color:#f9c846">$1/friend</b><br><a href="#refBox" class="btn-main" style="background:#f9c846;color:black">Get Link</a></div>
<div class="card"><div style="font-size:28px">📈</div><h3 style="font-size:13px">Trading</h3><b style="color:#00c950">FREE</b><br><a href="/trade" class="btn-main" style="background:#00c950;color:white">Trade</a></div>
<div class="card"><div style="font-size:28px">📡</div><h3 style="font-size:13px">VIP Signals</h3><b style="color:#f9c846">$10</b><br><a href="/signals" class="btn-main">Join VIP</a></div>
<div class="card"><div style="font-size:28px">✉️</div><h3 style="font-size:13px">Cover Letter</h3><b style="color:#f9c846">$1</b><br><a href="/cover-letter" class="btn-main">Write</a></div>
<div class="card"><div style="font-size:28px">📚</div><h3 style="font-size:13px">E-Books</h3><b style="color:#f9c846">$2-6</b><br><a href="/ebooks" class="btn-main" style="background:#333;color:white">Browse</a></div>
</div>
</div>
<div style="text-align:center;padding:20px;background:linear-gradient(135deg,#1a1a25,#2a1a3a);margin-top:20px;border-top:1px solid #f9c846">
<h3>Managed by <span class="moving-name" style="font-size:22px">TIMOTHY</span> - 18 Tools V16</h3>
<div class="wallet" style="max-width:350px;margin:10px auto">Bal $<span id="bal">0</span> | <span id="phone">Not logged</span></div>
<div class="card" style="max-width:350px;margin:10px auto"><input id="loginPhone" placeholder="Phone" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><input id="loginPass" type="password" placeholder="Pass" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><button onclick="login()" style="background:#f9c846;color:black;padding:8px 12px;border:none;border-radius:6px;font-weight:bold">Login</button><p id="loginMsg" style="color:#ff5555;font-size:11px"></p></div>
<p style="font-size:11px;color:#666">© 2026 Kaumoni V16 - TIMOTHY - 18 Tools - Same Background</p>
</div>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:12px 18px;border-radius:50px;font-weight:bold;text-decoration:none;z-index:100">💬 TIMOTHY WhatsApp</a>
<script>
let ph=localStorage.getItem('userPhone_v5')||'';let refFromUrl=new URLSearchParams(window.location.search).get('ref');if(refFromUrl){localStorage.setItem('refBy',refFromUrl);}
document.getElementById('phone').innerText=ph||'Not logged';
async function check(){if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);let rr=await fetch('/api/referral-info?phone='+ph);let rd=await rr.json();document.getElementById('refLink').innerText=window.location.origin+'/?ref='+ph;document.getElementById('refCount').innerText=rd.count||0;document.getElementById('refEarn').innerText=(rd.earned||0).toFixed(2);}
function copyRef(){let t=document.getElementById('refLink').innerText;navigator.clipboard.writeText(t);alert('Copied by TIMOTHY: '+t);}
async function login(){let p=document.getElementById('loginPhone').value.trim();let pw=document.getElementById('loginPass').value.trim();let refBy=localStorage.getItem('refBy')||'';let r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw,refBy:refBy})});let d=await r.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);location.reload();}
let cur=0;let slides=document.querySelectorAll('.slide');setInterval(()=>{slides[cur].classList.remove('active');cur=(cur+1)%slides.length;slides[cur].classList.add('active');},2500);check();
</script></body></html>"""

CERT_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Certificate Maker by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px;margin:6px 0}#cert{width:550px;height:380px;margin:auto;background:white;color:black;padding:20px;border:10px double #6a0dad;border-radius:8px;text-align:center;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📜 Certificate Maker $1.5 - by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div>
<div class="card"><select id="type" onchange="draw()"><option value="Appreciation">Certificate of Appreciation</option><option value="Achievement">Certificate of Achievement</option><option value="Completion">Certificate of Completion</option><option value="Excellence">Certificate of Excellence</option></select><input id="name" value="John Kamau" oninput="draw()"><input id="reason" value="For Outstanding Performance" oninput="draw()"><input id="org" value="Kaumoni Academy - TIMOTHY" oninput="draw()"><input id="date" value="30 Sept 2026" oninput="draw()"><input id="sign" value="TIMOTHY - Director" oninput="draw()"></div>
<button onclick="downloadCert()" style="background:#6a0dad;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD Certificate $1.5</button>
</div><div id="cert"></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){
let type=document.getElementById('type').value;let name=document.getElementById('name').value;let reason=document.getElementById('reason').value;let org=document.getElementById('org').value;let date=document.getElementById('date').value;let sign=document.getElementById('sign').value;
document.getElementById('cert').innerHTML=`<div id="wm">PREVIEW PAY $1.5</div><div style="border:2px solid #6a0dad;padding:10px;height:100%;display:flex;flex-direction:column;justify-content:center"><div style="font-size:30px">🏆</div><h1 style="margin:5px 0;color:#6a0dad;font-size:22px">${type.toUpperCase()}</h1><p style="margin:5px 0;font-size:12px">This Certificate is Proudly Presented To</p><h2 style="margin:10px 0;font-size:26px;color:#1a1a25;border-bottom:2px solid #f9c846;display:inline-block;padding-bottom:5px">${name}</h2><p style="font-size:13px;margin:8px 0">${reason}</p><p style="font-size:11px;color:#666;margin:5px 0">Awarded by ${org}<br>Date: ${date}</p><div style="margin-top:15px;display:flex;justify-content:space-between"><div style="border-top:1px solid black;width:120px;font-size:10px">${sign}<br>Signature</div><div style="border-top:1px solid black;width:120px;font-size:10px">Date<br>${date}</div></div><small style="font-size:8px;color:#999">Generated by Kaumoni.com - TIMOTHY 0118431854</small></div>`;
}
async function downloadCert(){if(userPhone!=='0118431854'&&userBal<1.5){alert('Need $1.5');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1.5,reason:'cert'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('cert'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='Certificate_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>"""

BIZCARD_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Business Card by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px;margin:6px 0}.bc{width:380px;height:220px;margin:10px auto;border-radius:12px;padding:18px;display:flex;flex-direction:column;justify-content:center;position:relative;overflow:hidden;color:white}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:20px;font-weight:900;padding:8px 16px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>💳 Business Card $2 - Front + Back - TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div>
<div class="card"><input id="name" value="TIMOTHY K." oninput="draw()"><input id="biz" value="KAUMONI SHOP" oninput="draw()"><input id="role" value="CEO & Founder" oninput="draw()"><input id="phone" value="0118431854" oninput="draw()"><input id="email" value="kaumoni@gmail.com" oninput="draw()"><input id="loc" value="Nairobi, Kenya" oninput="draw()"><select id="style" onchange="draw()"><option value="1">Black Gold - TIMOTHY</option><option value="2">Blue White</option><option value="3">Green White</option></select></div>
<button onclick="downloadCard()" style="background:#0d47a1;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD Front+Back $2</button>
</div><div><div id="front" class="bc"></div><div id="back" class="bc" style="background:#f9f9f9;color:black;border:1px solid #ddd"></div></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){
let name=document.getElementById('name').value;let biz=document.getElementById('biz').value;let role=document.getElementById('role').value;let phone=document.getElementById('phone').value;let email=document.getElementById('email').value;let loc=document.getElementById('loc').value;let st=document.getElementById('style').value;
let bg='linear-gradient(135deg,#0e0e14,#1a1a25)';let col='#f9c846';if(st=='2'){bg='linear-gradient(135deg,#0d47a1,#42a5f5)';col='white';}if(st=='3'){bg='linear-gradient(135deg,#00c950,#a8ff78)';col='black';}
document.getElementById('front').style.background=bg;
document.getElementById('front').innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="border:2px solid ${col};width:50px;height:50px;border-radius:50%;display:flex;justify-content:center;align-items:center;font-weight:bold;font-size:20px;color:${col}">${biz.charAt(0)}</div><h2 style="margin:8px 0 2px;color:${col}">${name}</h2><small style="color:${col}">${role}</small><h3 style="margin:8px 0 0">${biz}</h3>`;
document.getElementById('back').innerHTML=`<div style="text-align:center"><h3 style="margin:0">${biz}</h3><small style="color:#666">${role}</small><hr><div style="text-align:left;font-size:11px;margin-top:10px">📞 ${phone}<br>✉️ ${email}<br>📍 ${loc}<br><br><small style="background:#0e0e14;color:#f9c846;padding:3px 8px;border-radius:10px">Kaumoni.com - TIMOTHY 0118431854</small></div></div>`;
}
async function downloadCard(){if(userPhone!=='0118431854'&&userBal<2){alert('Need $2');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:2,reason:'bizcard'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let f=document.getElementById('front');let b=document.getElementById('back');let wm=f.querySelector('#wm');if(wm)wm.style.display='none';html2canvas(f,{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='BizCard_Front_TIMOTHY.png';a.href=c.toDataURL();a.click();});setTimeout(()=>{html2canvas(b,{scale:2}).then(c=>{let a=document.createElement('a');a.download='BizCard_Back_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();});},800);}
draw();loadBal();
</script></body></html>"""

PAYSLIP_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Payslip by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px;margin:6px 0}#slip{width:400px;margin:auto;background:white;color:black;padding:18px;border-radius:8px;font-size:12px;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>💰 Payslip Maker $1 - TIMOTHY - Monthly Recurring!</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span> | SME Monthly Need!</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div>
<div class="card"><input id="company" value="Kaumoni Ltd" oninput="draw()"><input id="empName" value="John Kamau" oninput="draw()"><input id="empId" value="EMP001" oninput="draw()"><input id="role" value="Sales Exec" oninput="draw()"><input id="month" value="September 2026" oninput="draw()"><input id="basic" type="number" value="30000" oninput="draw()"><input id="allow" type="number" value="5000" oninput="draw()"><input id="deduct" type="number" value="3000" oninput="draw()"><input id="nssf" type="number" value="1080" oninput="draw()"><input id="nhif" type="number" value="750" oninput="draw()"></div>
<button onclick="downloadSlip()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD Payslip $1</button>
</div><div id="slip"></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){
let comp=document.getElementById('company').value;let emp=document.getElementById('empName').value;let eid=document.getElementById('empId').value;let role=document.getElementById('role').value;let month=document.getElementById('month').value;
let basic=parseFloat(document.getElementById('basic').value)||0;let allow=parseFloat(document.getElementById('allow').value)||0;let deduct=parseFloat(document.getElementById('deduct').value)||0;let nssf=parseFloat(document.getElementById('nssf').value)||0;let nhif=parseFloat(document.getElementById('nhif').value)||0;
let gross=basic+allow;let totalDed=deduct+nssf+nhif;let net=gross-totalDed;
document.getElementById('slip').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="text-align:center;border-bottom:2px solid black;padding-bottom:8px"><h2 style="margin:0">${comp}</h2><small>PAYSLIP - ${month}</small><br><small style="background:black;color:white;padding:2px 6px;border-radius:4px">Confidential - TIMOTHY Payroll</small></div>
<div style="margin:10px 0;font-size:11px"><b>Employee:</b> ${emp} (${eid})<br><b>Role:</b> ${role}<br><b>Month:</b> ${month}</div>
<table style="width:100%;border-collapse:collapse;font-size:11px"><tr style="background:#f9c846"><th style="border:1px solid black;padding:5px;text-align:left">Earnings</th><th style="border:1px solid black">Amount KSH</th></tr>
<tr><td style="border:1px solid #ccc;padding:4px">Basic Salary</td><td style="border:1px solid #ccc;text-align:right">${basic.toFixed(2)}</td></tr>
<tr><td style="border:1px solid #ccc;padding:4px">Allowances</td><td style="border:1px solid #ccc;text-align:right">${allow.toFixed(2)}</td></tr>
<tr style="background:#eee"><td style="border:1px solid black;padding:5px"><b>Gross Pay</b></td><td style="border:1px solid black;text-align:right"><b>${gross.toFixed(2)}</b></td></tr>
<tr style="background:#ffcccb"><th style="border:1px solid black;padding:5px;text-align:left">Deductions</th><th style="border:1px solid black"></th></tr>
<tr><td style="border:1px solid #ccc;padding:4px">Other Deductions</td><td style="border:1px solid #ccc;text-align:right">${deduct.toFixed(2)}</td></tr>
<tr><td style="border:1px solid #ccc;padding:4px">NSSF</td><td style="border:1px solid #ccc;text-align:right">${nssf.toFixed(2)}</td></tr>
<tr><td style="border:1px solid #ccc;padding:4px">NHIF/SHIF</td><td style="border:1px solid #ccc;text-align:right">${nhif.toFixed(2)}</td></tr>
<tr style="background:#ffcccb"><td style="border:1px solid black;padding:5px"><b>Total Deductions</b></td><td style="border:1px solid black;text-align:right"><b>${totalDed.toFixed(2)}</b></td></tr>
<tr style="background:#00c950;color:white"><td style="border:1px solid black;padding:8px"><b>NET PAY KSH</b></td><td style="border:1px solid black;text-align:right;font-size:14px"><b>${net.toFixed(2)}</b></td></tr>
</table><div style="margin-top:10px;font-size:9px;color:#666;text-align:center">Generated by Kaumoni.com - TIMOTHY 0118431854<br>This is computer generated payslip</div>`;
}
async function downloadSlip(){if(userPhone!=='0118431854'&&userBal<1){alert('Need $1');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'payslip'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('slip'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='Payslip_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>"""

AI_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>AI Caption by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,textarea,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:10px;margin:8px 0}#poster{width:360px;height:480px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;position:relative;overflow:hidden;border-radius:12px}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:22px;font-weight:900;padding:8px 16px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>🤖 AI Caption + Poster $1 - TIMOTHY - Sheng to Sales!</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div>
<div class="card"><textarea id="sheng" rows="3" placeholder="Andika kwa Sheng e.g. Niko na sale ya nguo, bei ni 1500 tu, call 07..." oninput="generateAI()">Niko na sale ya nguo Kali Sana! Bei ni 1500 tu!</textarea><select id="bizType" onchange="generateAI()"><option value="clothes">Nguo / Clothes</option><option value="food">Food / Chakula</option><option value="shoes">Viatu / Shoes</option><option value="phone">Phones</option><option value="salon">Salon / Beauty</option><option value="general">General Business</option></select><input id="phone" value="0118431854" oninput="generateAI()"><input id="loc" value="Nairobi CBD" oninput="generateAI()"></div>
<div class="card"><h3 style="color:#f9c846">🤖 AI Generated Caption</h3><div id="aiCaption" style="background:#0e0e14;padding:10px;border-radius:8px;font-size:12px;color:#ccc;min-height:80px">Type in Sheng above...</div><button onclick="copyCaption()" style="background:#333;color:white;margin-top:6px">📋 Copy Caption</button></div>
<button onclick="downloadAI()" style="background:#ff9800;color:black;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download AI Poster + Caption $1</button>
</div><div id="poster"></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;let currentTitle='';let currentOffer='';
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function generateAI(){
let sheng=document.getElementById('sheng').value.toLowerCase();let bizType=document.getElementById('bizType').value;let phone=document.getElementById('phone').value;let loc=document.getElementById('loc').value;
let title='MEGA SALE!';let offer='50% OFF Today!';let emoji='🔥';
if(sheng.includes('sale')||sheng.includes('bei')){title='🔥 MEGA SALE!';offer=sheng.match(/\\d+/)? 'KSH '+sheng.match(/\\d+/)[0]+' ONLY!' : 'Bei Poa Sana!';}
if(bizType==='clothes'){title='👗 NGUO KALI!';emoji='👗';offer='Mtumba Grade 1!';}
if(bizType==='food'){title='🍛 CHAKULA TAMU!';emoji='🍛';}
if(bizType==='shoes'){title='👟 VIATU KALI!';emoji='👟';}
if(bizType==='phone'){title='📱 SIMU KALI!';emoji='📱';}
if(bizType==='salon'){title='💇‍♀️ BEAUTY SALE!';emoji='💇‍♀️';}
currentTitle=title;currentOffer=offer;
let captions=[
`🔥 ${title} ${emoji}\\n\\n${sheng.toUpperCase()} 💥\\n\\n✅ Bei ni Poa\\n✅ Delivery Available\\n✅ Quality Guaranteed\\n\\n📞 Call/WhatsApp: ${phone}\\n📍 ${loc}\\n\\n#Kaumoni #Nairobi #Sale #Kenya - by TIMOTHY`,
`🚀 OFFER! OFFER! ${title}\\n\\nWatu wangu! ${sheng} 🎉\\n\\nUsikose! Limited Stock!\\n📞 ${phone} - ${loc}\\n\\nPata yako leo! - TIMOTHY`
];
let cap=captions[Math.floor(Math.random()*captions.length)];
document.getElementById('aiCaption').innerText=cap;
document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1 - TIMOTHY</div><div style="background:linear-gradient(135deg,#ff6f00,#ffca28);width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px;color:black"><div style="font-size:50px">${emoji}</div><h1 style="font-size:32px;margin:10px 0">${title}</h1><h2 style="background:black;color:#ffca28;padding:8px 16px;border-radius:20px;font-size:18px">${offer}</h2><p style="font-size:14px;margin:15px 0;background:white;padding:8px;border-radius:8px">${sheng}</p><div style="background:black;color:white;padding:8px 14px;border-radius:20px;margin-top:10px"><b>📞 ${phone}</b><br><small>📍 ${loc}</small></div><small style="margin-top:10px">AI by TIMOTHY - Kaumoni.com</small></div>`;
}
function copyCaption(){let t=document.getElementById('aiCaption').innerText;navigator.clipboard.writeText(t);alert('Caption Copied!');}
async function downloadAI(){if(userPhone!=='0118431854'&&userBal<1){alert('Need $1');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'ai'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='AI_Poster_TIMOTHY.png';a.href=c.toDataURL();a.click();copyCaption();loadBal();});}
generateAI();loadBal();
</script></body></html>"""

# Keep other HTMLs as before (poster, receipt, cv, logo, cover, ebooks, signals, admin, bg, qr, lot, kra, tiktok, trading)
POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.95);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Poster $1 by TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Red</option><option value="2">Pink</option><option value="3">Blue</option><option value="4">Yellow</option><option value="5">Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XX" oninput="draw()"><input id="loc" value="Nairobi" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $1</button></div><div id="poster"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let c={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']}[document.getElementById('tpl').value];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1 - Kaumoni.com TIMOTHY 0118431854</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px"><h1 style="font-size:40px;margin:0">${document.getElementById('title').value}</h1><h2>${document.getElementById('sub').value}</h2><div style="background:black;color:white;padding:6px 12px;border-radius:20px;margin-top:15px"><b>${document.getElementById('phone').value}</b><br><small>${document.getElementById('loc').value}</small></div></div>`;}async function downloadPoster(){if(userPhone!=='0118431854'&&userBal<1){alert('Low');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(cv=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='HD_TIMOTHY.png';a.href=cv.toDataURL();a.click();loadBal();});}draw();loadBal();</script></body></html>"""

RECEIPT_HTML = POSTER_HTML.replace("Poster $1 by TIMOTHY","Receipt $1 by TIMOTHY")
CV_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,textarea{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#preview{background:white;color:black;padding:20px;border-radius:8px;position:relative;overflow:hidden;min-height:450px}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>CV $2 by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><input id="name" value="Timo Kaumoni" oninput="update()"><input id="title" value="Sales & Trader" oninput="update()"><input id="phone" value="07XX" oninput="update()"><input id="email" value="timo@email.com" oninput="update()"><textarea id="summary" rows="2" oninput="update()">Hardworking - TIMOTHY trained</textarea><input id="exp" value="Kaumoni Ltd - Sales 2022-2024" oninput="update()"><input id="edu" value="UoN - BBA 2020" oninput="update()"><input id="skills" value="Sales, Trading, Canva" oninput="update()"></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $2</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){document.getElementById('preview').innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="border-left:4px solid #f9c846;padding-left:10px"><h1 style="margin:0;font-size:24px">${document.getElementById('name').value}</h1><b style="color:#f9c846">${document.getElementById('title').value}</b><p style="font-size:11px;color:#555">${document.getElementById('phone').value} | ${document.getElementById('email').value}</p></div><hr><p><b>SUMMARY</b><br><span style="font-size:12px">${document.getElementById('summary').value}</span></p><p><b>EXPERIENCE</b><br><span style="font-size:12px">${document.getElementById('exp').value}</span></p><p><b>EDUCATION</b><br><span style="font-size:12px">${document.getElementById('edu').value}</span></p><p><b>SKILLS</b><br><span style="font-size:12px">${document.getElementById('skills').value}</span></p>`;}async function downloadCV(){if(userPhone!=='0118431854'&&userBal<2){alert('Need $2');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:2,reason:'cv'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='CV_HD.png';a.href=c.toDataURL();a.click();loadBal();});}update();loadBal();</script></body></html>"""

LOGO_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Logo by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#preview{background:white;color:black;width:340px;height:340px;margin:auto;display:flex;flex-direction:column;justify-content:center;align-items:center;border-radius:16px;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:22px;font-weight:900;padding:8px 18px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Logo $3 by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><input id="biz" value="KAUMONI" oninput="update()"><input id="tag" value="TIMOTHY BRANDS" oninput="update()"><select id="style" onchange="update()"><option value="1">Gold Black</option><option value="2">Blue White</option><option value="3">Green White</option><option value="4">Red Yellow</option><option value="5">Purple Luxury</option></select></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $3</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){let biz=document.getElementById('biz').value;let tag=document.getElementById('tag').value;let st=document.getElementById('style').value;let bg='#0e0e14',col='#f9c846',bd='#f9c846';if(st=='2'){bg='#1e3a8a';col='white';bd='white';}if(st=='3'){bg='#00c950';col='white';bd='white';}if(st=='4'){bg='#ff3b3b';col='#ffcc00';bd='#ffcc00';}if(st=='5'){bg='#6a0dad';col='#f9c846';bd='#f9c846';}document.getElementById('preview').style.background=bg;document.getElementById('preview').innerHTML=`<div id="wm">PREVIEW PAY $3</div><div style="border:3px solid ${bd};padding:20px;border-radius:50%;width:120px;height:120px;display:flex;justify-content:center;align-items:center"><h1 style="font-size:36px;margin:0;color:${col}">${biz.charAt(0)}</h1></div><h1 style="font-size:28px;margin:12px 0 4px;color:${col}">${biz}</h1><b style="color:${col};letter-spacing:3px;font-size:10px">${tag}</b>`;}async function downloadCV(){if(userPhone!=='0118431854'&&userBal<3){alert('Need $3');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:3,reason:'logo'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='Logo_HD.png';a.href=c.toDataURL();a.click();loadBal();});}update();loadBal();</script></body></html>"""

COVER_HTML = CV_HTML.replace("CV $2 by TIMOTHY","Cover Letter $1 by TIMOTHY").replace("PREVIEW PAY $2","PREVIEW PAY $1")
EBOOKS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>E-Books by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:10px 0;display:flex;justify-content:space-between}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}</style></head><body><nav><a href="/">← Home</a><b>📚 E-BOOKS by TIMOTHY</b><span id="uPhone">-</span></nav><div style="max-width:700px;margin:auto"><div class="card" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black"><div>Bal $ <span id="uBal">0</span> | TIMOTHY Library</div></div><div class="grid" id="books"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;let books=[{id:1,title:"Forex Mastery by TIMOTHY",price:5},{id:2,title:"Canva Secrets by TIMOTHY",price:3},{id:3,title:"M-Pesa Guide",price:4},{id:4,title:"CV Jobs",price:2},{id:5,title:"WhatsApp Sales",price:3},{id:6,title:"Crypto Basics KE",price:6}];async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function render(){document.getElementById('books').innerHTML=books.map(b=>`<div class="card"><div><b>${b.title}</b><br><b style="color:#f9c846">$${b.price}</b></div><button onclick="buy(${b.id})" style="background:#f9c846;color:black">Buy</button></div>`).join('');}async function buy(id){let b=books.find(x=>x.id===id);if(userPhone!=='0118431854'&&userBal<b.price){alert('Need $'+b.price);return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:b.price,reason:'ebook'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let blob=new Blob([b.title],{type:'text/plain'});let a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=b.title+'.txt';a.click();loadBal();}render();loadBal();</script></body></html>"""

SIGNALS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIP by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px;margin:0}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;border-bottom:1px solid #2a2a3a;position:sticky;top:0}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:10px 0}.signal{background:#1e1e2d;border-left:3px solid #00c950;padding:10px;margin:8px 0;border-radius:0 8px 8px 0}</style></head><body><nav><a href="/">← Home</a><b>📡 VIP by TIMOTHY</b><span id="uPhone" style="font-size:11px">-</span></nav><div style="max-width:600px;margin:auto;padding:10px"><div class="card" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black"><b>Bal $ <span id="uBal">0</span></b></div><div id="notVip" class="card" style="border:2px dashed #f9c846;text-align:center"><h3>🔒 Join VIP $10 - By TIMOTHY</h3><button onclick="join()" style="background:#f9c846;color:black;width:100%;padding:12px">Join VIP Now</button></div><div id="vipArea" style="display:none"><h3>📈 Live Signals</h3><div id="signals">Loading...</div></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let isVip=localStorage.getItem('isVip_'+userPhone)==='true';
async function load(){if(!userPhone){alert('Login');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854')isVip=true;let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();document.getElementById('uBal').innerText=(d.balance||0).toFixed(2);if(isVip){document.getElementById('notVip').style.display='none';document.getElementById('vipArea').style.display='block';let sr=await fetch('/api/signals');let sj=await sr.json();document.getElementById('signals').innerHTML=sj.map(s=>`<div class="signal"><b>${s.pair} - ${s.type}</b><br><small>Entry ${s.entry} | TP ${s.tp} | SL ${s.sl}</small><br><small>${s.time}</small> <b style="float:right">${s.result}</b></div>`).join('')||'No signals';}}
async function join(){if(userPhone==='0118431854'){localStorage.setItem('isVip_'+userPhone,'true');location.reload();return;}let r=await fetch('/api/balance?phone='+userPhone);let dd=await r.json();if(dd.balance<10){alert('Need $10');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}localStorage.setItem('isVip_'+userPhone,'true');location.reload();}load();
</script></body></html>"""

ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin TIMOTHY V16</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:12px;border-radius:12px;margin:8px 0}button{padding:7px 12px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}input,select{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0;width:100%}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>ADMIN - TIMOTHY 👑 V16 - 18 Tools</h2>
<div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><b>Total Fees $<span id="total">0</span></b> | <span id="userCount">0 users</span></div>
<div class="card"><h3>📈 Active Signals</h3><div id="activeSigs">Loading...</div></div><div class="card"><h3>💸 Top Referrers</h3><div id="topRefs">Loading...</div></div><div class="card"><h3>Deposits</h3><div id="depList">Loading...</div></div><div class="card"><h3>Users</h3><div id="usersList">Loading...</div></div>
<script>
async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText=(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';
document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} $${(u.balance||0).toFixed(2)} Ref:${u.referred_by||'-'}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add</button></div>`).join('');
document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div style="background:#2a2a3a;padding:6px;margin:4px 0;border-radius:6px"><b>${d.phone}</b> $${d.amount} ${d.code} ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';
document.getElementById('topRefs').innerHTML=data.users.sort((a,b)=>(b.ref_count||0)-(a.ref_count||0)).slice(0,10).map(u=>`<div style="background:#2a2a3a;padding:5px;margin:3px 0;border-radius:5px">${u.phone} - ${u.ref_count||0} refs - $${(u.ref_earned||0).toFixed(2)}</div>`).join('')||'No refs';
loadSigs();}
async function loadSigs(){let r=await fetch('/api/signals');let s=await r.json();document.getElementById('activeSigs').innerHTML=s.map((sig,i)=>`<div style="background:#1e1e2d;padding:6px;margin:4px 0;border-radius:6px"><b>${sig.pair} ${sig.type}</b> ${sig.entry}<br><button onclick="closeWin(${i})" style="background:#00c950;color:white;font-size:10px">WIN</button> <button onclick="closeLoss(${i})" style="background:#ef5350;color:white;font-size:10px">LOSS</button> <button onclick="delSig(${i})" style="background:#333;color:white;font-size:10px">Del</button></div>`).join('')||'No signals';}
async function closeWin(i){let p=prompt('Win','+20$ ✅');if(!p)return;await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function closeLoss(i){let p=prompt('Loss','-10$ ❌');if(!p)return;await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function delSig(i){if(!confirm('Delete?'))return;await fetch('/api/delete-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});loadSigs();}
async function approveDep(i){let r=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function rejectDep(i){let r=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function addBal(ph){let amt=prompt('Amount $');if(!amt)return;await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:ph,amount:parseFloat(amt)})});load();}
load();
</script></body></html>"""

BG_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>BG Remover by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:10px;margin:8px 0}canvas{max-width:100%;border:2px solid #f9c846;border-radius:10px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>✂️ BG Remover $1 - TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><input type="file" id="file" accept="image/*"><select id="bgColor"><option value="white">White BG</option><option value="transparent">Transparent</option><option value="black">Black</option><option value="#f9c846">Gold</option></select><button onclick="removeBG()" style="background:#f9c846;color:black;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Remove BG $1</button><button onclick="download()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold;margin-top:6px">Download HD</button></div></div><div><canvas id="canvas"></canvas></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;let img=new Image();let paid=false;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
document.getElementById('file').addEventListener('change',e=>{let f=e.target.files[0];if(!f)return;let url=URL.createObjectURL(f);img.onload=()=>{let c=document.getElementById('canvas');c.width=img.width;c.height=img.height;let ctx=c.getContext('2d');ctx.drawImage(img,0,0);};img.src=url;});
async function removeBG(){if(userPhone!=='0118431854'&&userBal<1&&!paid){let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'bg'})});let d=await r.json();if(!d.ok){alert(d.message);return;}paid=true;loadBal();}
let c=document.getElementById('canvas');let ctx=c.getContext('2d');let imgData=ctx.getImageData(0,0,c.width,c.height);let data=imgData.data;let bg=document.getElementById('bgColor').value;
for(let i=0;i<data.length;i+=4){let r=data[i],g=data[i+1],b=data[i+2];if(r>220&&g>220&&b>220){if(bg==='transparent'){data[i+3]=0;}else if(bg==='white'){data[i]=255;data[i+1]=255;data[i+2]=255;}else if(bg==='black'){data[i]=0;data[i+1]=0;data[i+2]=0;}else if(bg==='#f9c846'){data[i]=249;data[i+1]=200;data[i+2]=70;}}}
ctx.putImageData(imgData,0,0);
if(bg!=='transparent'){let tmp=document.createElement('canvas');tmp.width=c.width;tmp.height=c.height;let tctx=tmp.getContext('2d');if(bg==='#f9c846')tctx.fillStyle='#f9c846';else tctx.fillStyle=bg;tctx.fillRect(0,0,tmp.width,tmp.height);tctx.drawImage(c,0,0);ctx.clearRect(0,0,c.width,c.height);ctx.drawImage(tmp,0,0);}
alert('BG Removed by TIMOTHY!');}
function download(){let c=document.getElementById('canvas');let a=document.createElement('a');a.download='BG_Removed_TIMOTHY.png';a.href=c.toDataURL();a.click();}
loadBal();
</script></body></html>"""

QR_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>QR Till USABLE by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:10px}#poster{width:350px;margin:auto;background:white;color:black;padding:20px;border-radius:12px;text-align:center;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:22px;font-weight:900;padding:8px 18px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📱 QR Till USABLE $1 - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><input id="biz" value="KAUMONI SHOP" oninput="draw()"><input id="till" value="5389841" oninput="draw()"><input id="phone" value="0118431854" oninput="draw()"><select id="qrType" onchange="draw()"><option value="till">USABLE: Till Number Only</option><option value="bg">USABLE: BG_TILL</option><option value="full">INFO: Full</option></select><input id="msg" value="Lipa na M-Pesa - TIMOTHY" oninput="draw()"></div><button onclick="downloadQR()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD Poster $1</button></div><div id="poster"></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){let biz=document.getElementById('biz').value;let till=document.getElementById('till').value;let ph=document.getElementById('phone').value;let msg=document.getElementById('msg').value;let type=document.getElementById('qrType').value;let qrText=till;if(type==='bg')qrText='BG_'+till;if(type==='full')qrText=`TILL:${till}|PHONE:${ph}|BIZ:${biz}`;document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="border:3px solid #f9c846;padding:15px;border-radius:12px"><h2 style="margin:0;color:#1a1a25">${biz}</h2><div id="qrcode" style="margin:10px auto;display:flex;justify-content:center"></div><h3 style="background:#1a1a25;color:#f9c846;padding:6px;border-radius:6px">TILL: ${till}</h3><p style="font-size:12px">${msg}</p></div>`;new QRCode(document.getElementById("qrcode"), {text:qrText,width:190,height:190});}
async function downloadQR(){if(userPhone!=='0118431854'&&userBal<1){alert('Need $1');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'qr'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='QR_Till_USABLE.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>"""

LOT_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lot Calc FREE by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:14px;border-radius:12px;margin:8px 0}.result{background:linear-gradient(90deg,#00c950,#00ff88);color:black;padding:14px;border-radius:10px;font-weight:bold;text-align:center;font-size:18px;margin-top:10px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📊 Lot Size Calculator FREE - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:800px;margin:auto"><div><div class="card"><label>Balance $</label><input id="bal" type="number" value="100" oninput="calc()"><label>Risk %</label><input id="risk" type="number" value="2" oninput="calc()"><label>Entry</label><input id="entry" type="number" value="2345.5" oninput="calc()"><label>SL</label><input id="sl" type="number" value="2335.5" oninput="calc()"><label>TP</label><input id="tp" type="number" value="2365.5" oninput="calc()"></div></div><div><div class="card"><h3 style="color:#f9c846">Result</h3><div id="res" class="result">Enter values</div><div id="details" style="margin-top:10px;font-size:13px;color:#ccc"></div></div></div></div><script>
function calc(){let bal=parseFloat(document.getElementById('bal').value)||0;let riskP=parseFloat(document.getElementById('risk').value)||0;let entry=parseFloat(document.getElementById('entry').value)||0;let sl=parseFloat(document.getElementById('sl').value)||0;let tp=parseFloat(document.getElementById('tp').value)||0;let riskAmt=bal*riskP/100;let slDist=Math.abs(entry-sl);let tpDist=Math.abs(tp-entry);let lot=riskAmt/(slDist*10);if(lot<0.01)lot=0.01;let rr=slDist>0?(tpDist/slDist).toFixed(2):0;document.getElementById('res').innerHTML=`Risk $${riskAmt.toFixed(2)} | Lot <b>${lot.toFixed(2)}</b><br>RR 1:${rr}`;document.getElementById('details').innerHTML=`Balance $${bal}<br><b style="color:#f9c846">Lot: ${lot.toFixed(2)}</b>`;}calc();
</script></body></html>"""

KRA_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>KRA E-TIMS by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px;margin:6px 0}#invoice{width:380px;margin:auto;background:white;color:black;padding:18px;border-radius:8px;font-size:12px;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>🧾 KRA E-TIMS $1.5 - TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div>
<div class="card"><b>Business</b><input id="bizName" value="KAUMONI SHOP" oninput="draw()"><input id="kraPin" value="A012345678Z" oninput="draw()"><input id="bizPhone" value="0118431854" oninput="draw()"><input id="cuNo" value="KRA CU: 123456789" oninput="draw()"></div>
<div class="card"><b>Customer</b><input id="custName" value="John Kamau" oninput="draw()"><input id="custPin" value="A987654321Y" oninput="draw()"></div>
<div class="card"><b>Items</b><input id="item1" value="Poster Design" oninput="draw()"><input id="qty1" type="number" value="1" oninput="draw()"><input id="price1" type="number" value="1000" oninput="draw()"><input id="item2" value="Logo" oninput="draw()"><input id="qty2" type="number" value="1" oninput="draw()"><input id="price2" type="number" value="500" oninput="draw()"><select id="vatRate" onchange="draw()"><option value="16">VAT 16%</option><option value="0">VAT 0%</option></select></div>
<button onclick="downloadKRA()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD KRA $1.5</button>
</div><div id="invoice"></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){let biz=document.getElementById('bizName').value;let pin=document.getElementById('kraPin').value;let phone=document.getElementById('bizPhone').value;let cu=document.getElementById('cuNo').value;let cust=document.getElementById('custName').value;let cpin=document.getElementById('custPin').value;let i1=document.getElementById('item1').value;let q1=parseFloat(document.getElementById('qty1').value)||0;let p1=parseFloat(document.getElementById('price1').value)||0;let i2=document.getElementById('item2').value;let q2=parseFloat(document.getElementById('qty2').value)||0;let p2=parseFloat(document.getElementById('price2').value)||0;let vatR=parseFloat(document.getElementById('vatRate').value)||0;let total=q1*p1+q2*p2;let vat=total*vatR/100;let grand=total+vat;document.getElementById('invoice').innerHTML=`<div id="wm">PREVIEW PAY $1.5</div><div style="text-align:center;border-bottom:2px solid black;padding-bottom:8px"><h2 style="margin:0">${biz}</h2><small>KRA PIN: ${pin} | Tel: ${phone}</small><br><small style="background:black;color:white;padding:2px 6px;border-radius:4px">${cu}</small><br><b style="color:#004AFF">KRA E-TIMS COMPLIANT</b></div><div style="margin:8px 0"><b>Customer:</b> ${cust} | PIN: ${cpin}<br><small>Date: ${new Date().toLocaleDateString()} | By TIMOTHY</small></div><table style="width:100%;border-collapse:collapse;font-size:11px"><tr style="background:black;color:white"><th style="padding:5px;border:1px solid black">Item</th><th style="border:1px solid black">Qty</th><th style="border:1px solid black">Price</th><th style="border:1px solid black">Total</th></tr><tr><td style="border:1px solid #ccc;padding:4px">${i1}</td><td style="border:1px solid #ccc;text-align:center">${q1}</td><td style="border:1px solid #ccc;text-align:right">${p1}</td><td style="border:1px solid #ccc;text-align:right">${(q1*p1).toFixed(2)}</td></tr><tr><td style="border:1px solid #ccc;padding:4px">${i2}</td><td style="border:1px solid #ccc;text-align:center">${q2}</td><td style="border:1px solid #ccc;text-align:right">${p2}</td><td style="border:1px solid #ccc;text-align:right">${(q2*p2).toFixed(2)}</td></tr><tr><td colspan="3" style="border:1px solid black;text-align:right;padding:4px"><b>Subtotal</b></td><td style="border:1px solid black;text-align:right"><b>${total.toFixed(2)}</b></td></tr><tr><td colspan="3" style="border:1px solid black;text-align:right;padding:4px">VAT ${vatR}%</td><td style="border:1px solid black;text-align:right">${vat.toFixed(2)}</td></tr><tr style="background:#f9c846"><td colspan="3" style="border:1px solid black;text-align:right;padding:6px"><b>GRAND TOTAL</b></td><td style="border:1px solid black;text-align:right"><b>${grand.toFixed(2)}</b></td></tr></table><div style="display:flex;justify-content:space-between;margin-top:10px"><div><small>Kaumoni - TIMOTHY<br>0118431854<br>KRA E-TIMS Compliant</small></div><div id="kraQr"></div></div>`;setTimeout(()=>{if(document.getElementById('kraQr')) new QRCode(document.getElementById('kraQr'),{text:`${biz}|${pin}|${grand}|${cu}|TIMOTHY`,width:70,height:70});},100);}
async function downloadKRA(){if(userPhone!=='0118431854'&&userBal<1.5){alert('Need $1.5');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1.5,reason:'kra'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('invoice'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='KRA_E-TIMS.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>"""

TIKTOK_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>TikTok DL FREE by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}input{width:100%;padding:10px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:8px;margin:6px 0}.card{background:#1a1a25;padding:14px;border-radius:12px;margin:10px 0}button{padding:12px;border:none;border-radius:8px;font-weight:bold;cursor:pointer;width:100%}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>🎵 TikTok Downloader FREE - TIMOTHY</h2><div style="max-width:600px;margin:auto"><div class="card"><input id="tiktokUrl" placeholder="Paste TikTok link"><button onclick="downloadTik()" style="background:linear-gradient(90deg,#ff0050,#00f2ea);color:white;padding:14px;font-size:16px">🎵 Download No Watermark FREE</button></div><div id="result"></div></div><script>
async function downloadTik(){let url=document.getElementById('tiktokUrl').value.trim();if(!url){alert('Paste link');return;}document.getElementById('result').innerHTML='<div class="card">⏳ Fetching...</div>';try{let apiUrl=`https://www.tikwm.com/api/?url=${encodeURIComponent(url)}`;let r=await fetch(apiUrl);let d=await r.json();if(d.code!=0||!d.data){throw 'Failed';}let videoUrl=d.data.play;let author=d.data.author.nickname;let title=d.data.title;document.getElementById('result').innerHTML=`<div class="card"><h3 style="color:#00c950">✅ Ready</h3><b>${author}</b><br><small>${title}</small><video controls style="width:100%;max-height:400px;border-radius:8px;margin-top:10px" src="${videoUrl}"></video><a href="${videoUrl}" target="_blank" download><button style="background:#00c950;color:white;margin-top:10px">📥 Download HD No Watermark</button></a></div>`;}catch(e){document.getElementById('result').innerHTML=`<div class="card" style="border:1px solid #ef5350"><h3 style="color:#ef5350">❌ Failed - Try another link or ssstik.io</h3></div>`;}}
</script></body></html>"""

TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading by TIMOTHY</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:8px}.card{background:#1a1a25;padding:10px;border-radius:8px;margin-top:8px}#tv_chart{height:400px}</style></head><body><a href="/" style="color:#f9c846">← Home</a> <b>Trading - TIMOTHY's Chart</b> Bal $<span id="bal">0</span><div id="tv_chart" class="card"></div><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","theme":"dark","container_id":"tv_chart"});async function load(){let ph=localStorage.getItem('userPhone_v5');if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}load();</script></body></html>"""

@app.route('/')
def home(): return HOME_HTML
@app.route('/trade')
def trade(): return TRADING_HTML
@app.route('/poster-maker')
def poster(): return POSTER_HTML
@app.route('/receipt-maker')
def receipt(): return RECEIPT_HTML
@app.route('/cv-builder')
def cv(): return CV_HTML
@app.route('/logo-maker')
def logo(): return LOGO_HTML
@app.route('/cover-letter')
def cover(): return COVER_HTML
@app.route('/signals')
def signals_page(): return SIGNALS_HTML
@app.route('/ebooks')
def ebooks_page(): return EBOOKS_HTML
@app.route('/admin')
def admin(): return ADMIN_HTML
@app.route('/bg-remover')
def bg_remover(): return BG_HTML
@app.route('/qr-maker')
def qr_maker(): return QR_HTML
@app.route('/lot-calculator')
def lot_calc(): return LOT_HTML
@app.route('/kra-invoice')
def kra_invoice(): return KRA_HTML
@app.route('/tiktok-downloader')
def tiktok_dl(): return TIKTOK_HTML
@app.route('/certificate-maker')
def cert_maker(): return CERT_HTML
@app.route('/business-card')
def biz_card(): return BIZCARD_HTML
@app.route('/payslip-maker')
def payslip_maker(): return PAYSLIP_HTML
@app.route('/ai-caption')
def ai_caption(): return AI_HTML

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); pwd=data['password'].strip(); refBy=data.get('refBy','').strip()
    users=load_json(USERS_FILE, {})
    if phone==ADMIN_PHONE:
        if pwd!=ADMIN_PASSWORD: return jsonify({"ok":False,"message":"Wrong admin pass"})
        if phone not in users: users[phone]={"phone":phone,"password":pwd,"balance":999,"total_fee":0,"ref_count":0,"ref_earned":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":999})
    if phone in users:
        if users[phone].get('password') and users[phone].get('password')!=pwd: return jsonify({"ok":False,"message":"Wrong password"})
        if not users[phone].get('password'): users[phone]['password']=pwd; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":users[phone].get('balance',0)})
    else:
        users[phone]={"phone":phone,"password":pwd,"balance":0,"total_fee":0,"referred_by":refBy if refBy!=phone else "", "ref_count":0,"ref_earned":0,"joined":str(datetime.now())}
        save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":0})

@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone')
    if phone==ADMIN_PHONE: return jsonify({"phone":phone,"balance":999})
    users=load_json(USERS_FILE, {}); return jsonify(users.get(phone, {"phone":phone,"balance":0}))

@app.route('/api/referral-info')
def api_ref_info():
    phone=request.args.get('phone'); users=load_json(USERS_FILE, {})
    u=users.get(phone, {}); return jsonify({"count":u.get('ref_count',0),"earned":u.get('ref_earned',0)})

@app.route('/api/deposit-request', methods=['POST'])
def api_dep_req():
    data=request.get_json(); deps=load_json(DEPOSITS_FILE, []); deps.append({"phone":data['phone'],"code":data['code'],"amount":float(data['amount']),"status":"pending","time":str(datetime.now())}); save_json(DEPOSITS_FILE, deps); return jsonify({"ok":True,"message":"Sent to TIMOTHY"})

@app.route('/api/add-balance', methods=['POST'])
def api_add_bal():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0,"ref_count":0,"ref_earned":0}
    users[ph]['balance']=float(users[ph].get('balance',0))+float(data['amount']); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']; amt=float(data['amount'])
    if ph==ADMIN_PHONE: return jsonify({"ok":True,"balance":999})
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({"ok":False,"message":"Low balance"})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+amt; save_json(FEES_FILE, fees); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {}); deps=load_json(DEPOSITS_FILE, []); fees=load_json(FEES_FILE, {"total":0}); refs=load_json(REFS_FILE, {"total_paid":0})
    return jsonify({"users":list(users.values()),"deposits":deps,"total_fees":fees.get('total',0),"referrals_total":refs.get('total_paid',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    idx=int(request.get_json()['index']); deps=load_json(DEPOSITS_FILE, []); dep=deps[idx]; users=load_json(USERS_FILE, {}); refs=load_json(REFS_FILE, {"total_paid":0})
    if dep['status']!='pending': return jsonify({"message":"Already"})
    ph=dep['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0,"ref_count":0,"ref_earned":0}
    users[ph]['balance']+=float(dep['amount']); save_json(USERS_FILE, users); deps[idx]['status']='approved'; save_json(DEPOSITS_FILE, deps)
    bonus_msg=None
    if float(dep['amount'])>=5 and users[ph].get('referred_by'):
        ref_phone=users[ph]['referred_by']
        if ref_phone in users and not users[ph].get('ref_bonus_given'):
            users[ref_phone]['balance']=float(users[ref_phone].get('balance',0))+1.0
            users[ref_phone]['ref_count']=int(users[ref_phone].get('ref_count',0))+1
            users[ref_phone]['ref_earned']=float(users[ref_phone].get('ref_earned',0))+1.0
            users[ph]['ref_bonus_given']=True
            refs['total_paid']=float(refs.get('total_paid',0))+1.0
            bonus_msg=ref_phone
            save_json(USERS_FILE, users); save_json(REFS_FILE, refs)
    return jsonify({"message":"Approved by TIMOTHY","ref_bonus":bonus_msg})

@app.route('/api/reject-deposit', methods=['POST'])
def api_reject():
    idx=int(request.get_json()['index']); deps=load_json(DEPOSITS_FILE, []); deps[idx]['status']='rejected'; save_json(DEPOSITS_FILE, deps); return jsonify({"message":"Rejected"})

@app.route('/api/signals')
def api_signals(): return jsonify(load_json(SIGNALS_FILE, []))

@app.route('/api/trend-suggest')
def api_trend_suggest():
    out=[];pairs_map={"BTCUSDT":"BTC/USD","ETHUSDT":"ETH/USD","EURUSDT":"EUR/USD","GBPUSDT":"GBP/USD","XAUUSDT":"XAUUSD GOLD"}
    for raw,name in pairs_map.items():
        t=get_trend(raw);price=t.get("price",0)
        if price==0: price={"BTC/USD":65200,"ETH/USD":3200,"EUR/USD":1.0850,"GBP/USD":1.27,"XAUUSD GOLD":2345.5}[name]
        out.append({"pair":name,"raw":raw,"trend":t.get("trend","BUY"),"price":round(float(price),2),"sma20":round(float(t.get("sma20",0)),2),"sma50":round(float(t.get("sma50",0)),2),"note":t.get("note","")})
    return jsonify(out)

@app.route('/api/add-signal', methods=['POST'])
def api_add_signal():
    data=request.get_json(); sigs=load_json(SIGNALS_FILE, []); sigs.insert(0,{"pair":data['pair'],"type":data['type'],"entry":data['entry'],"tp":data['tp'],"sl":data['sl'],"result":data.get('result','Running...'),"time":datetime.now().strftime("%Y-%m-%d %H:%M")+" by TIMOTHY"}); save_json(SIGNALS_FILE, sigs[:30]); return jsonify({"ok":True})

@app.route('/api/update-signal', methods=['POST'])
def api_update_signal():
    data=request.get_json(); idx=int(data['index']); sigs=load_json(SIGNALS_FILE, [])
    if 0 <= idx < len(sigs): sigs[idx]['result']=data['result']; save_json(SIGNALS_FILE, sigs)
    return jsonify({"ok":True})

@app.route('/api/delete-signal', methods=['POST'])
def api_delete_signal():
    idx=int(request.get_json()['index']); sigs=load_json(SIGNALS_FILE, [])
    if 0 <= idx < len(sigs): sigs.pop(idx); save_json(SIGNALS_FILE, sigs)
    return jsonify({"ok":True})

if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
