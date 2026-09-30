
from flask import Flask, request, jsonify
import os, json, requests
from datetime import datetime
app = Flask(__name__)
USERS_FILE='users.json';DEPOSITS_FILE='deposits.json';FEES_FILE='fees.json';SIGNALS_FILE='signals.json'
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
    try:
        if "XAU" in pair:
            rg=requests.get("https://api.gold-api.com/price/XAU",timeout=8).json()
            price=float(rg.get('price',2345));return {"trend":"BUY","price":price,"sma20":price-5,"sma50":price-12,"note":"Gold live bullish"}
        if "EUR" in pair:
            re=requests.get("https://api.exchangerate.host/convert?from=EUR&to=USD",timeout=8).json()
            price=float(re.get('result',1.0850) or 1.0850);return {"trend":"BUY","price":price,"sma20":1.084,"sma50":1.082,"note":"EUR live"}
        if "GBP" in pair:
            re=requests.get("https://api.exchangerate.host/convert?from=GBP&to=USD",timeout=8).json()
            price=float(re.get('result',1.27) or 1.27);return {"trend":"BUY","price":price,"sma20":1.269,"sma50":1.265,"note":"GBP live"}
    except: pass
    fb={"BTCUSDT":65200,"ETHUSDT":3200,"EURUSDT":1.0850,"GBPUSDT":1.27,"XAUUSDT":2345.5}.get(pair,2340)
    return {"trend":"BUY","price":fb,"sma20":fb-2,"sma50":fb-8,"note":"Check TV"}

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni V14.1 - 11 Tools TIMOTHY</title>
<style>
*{box-sizing:border-box}body{background:#0a0a12;color:white;font-family:Arial;margin:0;overflow-x:hidden}
nav{background:rgba(26,26,37,0.95);backdrop-filter:blur(10px);padding:12px 20px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #2a2a3a;z-index:100}nav b{color:#f9c846}
.btn-main{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:13px 26px;border:none;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:6px;animation:pulse 2s infinite;box-shadow:0 4px 15px rgba(249,200,70,0.4)}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}
.hero{background:linear-gradient(270deg,#0e0e14,#1a1a25,#2a1a3a,#4a1a6a,#0e0e14,#1a2a5a);background-size:800% 800%;animation:gradMove 12s ease infinite;text-align:center;padding:30px 15px}
@keyframes gradMove{0%{background-position:0% 50%}25%{background-position:100% 50%}50%{background-position:50% 100%}75%{background-position:0% 100%}100%{background-position:0% 50%}}
.moving-name{font-size:18px;font-weight:bold;color:#f9c846;display:inline-block;animation:nameMove 3s ease-in-out infinite;background:linear-gradient(90deg,#f9c846,#ff9800,#f9c846);background-size:200%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
@keyframes nameMove{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(-5px) scale(1.1)}}
.marquee{width:100%;overflow:hidden;white-space:nowrap;background:rgba(0,0,0,0.4);padding:10px 0;border-top:1px solid #f9c846;border-bottom:1px solid #f9c846;margin:15px 0}
.marquee-track{display:inline-block;animation:marquee 30s linear infinite}
@keyframes marquee{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.price-tag{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:4px 12px;border-radius:20px;font-weight:bold;margin:0 10px;font-size:13px;animation:pricePop 1.5s ease-in-out infinite}
@keyframes pricePop{0%,100%{transform:scale(1)}50%{transform:scale(1.15)}}
.slider{width:340px;height:180px;margin:18px auto;position:relative;overflow:hidden;border-radius:14px;border:2px solid #f9c846;box-shadow:0 0 25px rgba(249,200,70,0.4)}
.slide{position:absolute;width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;transition:0.8s;transform:translateX(100%);opacity:0}
.slide.active{transform:translateX(0);opacity:1}
.card{background:linear-gradient(135deg,#1a1a25,#222235);border:1px solid #2a2a3a;padding:16px;border-radius:14px;margin:8px;text-align:center;transition:0.3s}
.card:hover{transform:translateY(-5px);border-color:#f9c846;box-shadow:0 10px 30px rgba(249,200,70,0.2)}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;padding:12px}@media(max-width:900px){.grid{grid-template-columns:1fr 1fr}}@media(max-width:600px){.grid{grid-template-columns:1fr}}
.wallet{background:linear-gradient(90deg,#f9c846,#ff9800);background-size:200% 200%;animation:gradMove 3s linear infinite;color:black;padding:12px;border-radius:12px;margin:12px;font-weight:bold}
.pricing-move{font-size:11px;color:#f9c846;animation:slideText 3s ease-in-out infinite;display:inline-block}
@keyframes slideText{0%,100%{transform:translateX(0)}50%{transform:translateX(6px)}}
.timothy-badge{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:3px 10px;border-radius:20px;font-weight:bold;animation:nameMove 2s infinite;margin-left:6px}
.testimonials-wrap{background:linear-gradient(90deg,#0e0e14,#1a1a25);border-top:1px solid #2a2a3a;border-bottom:1px solid #2a2a3a;padding:20px 0;margin:20px 0;overflow:hidden}
.testi-title{text-align:center;font-size:20px;margin-bottom:12px}
.testi-track{display:flex;animation:testiScroll 40s linear infinite;width:max-content}
@keyframes testiScroll{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
.testi-card{min-width:280px;max-width:280px;background:#1e1e2d;border:1px solid #2a2a3a;border-radius:12px;padding:14px;margin:0 10px;flex-shrink:0}
.faq-item{background:#1a1a25;border:1px solid #2a2a3a;border-radius:10px;margin:8px 0;overflow:hidden}
.faq-q{padding:12px;font-weight:bold;cursor:pointer;display:flex;justify-content:space-between;background:#222235}
.faq-a{padding:12px;font-size:13px;color:#bbb;display:none}.faq-item.active.faq-a{display:block}
.new-badge{background:#00c950;color:white;padding:2px 8px;border-radius:10px;font-size:10px;margin-left:5px;animation:pricePop 1s infinite}
</style></head><body>
<nav><b>KAUMONI V14.1</b><div><a href="/trade" style="color:white;text-decoration:none;margin:0 8px">📈 Trade</a><a href="/admin" style="color:#f9c846;font-weight:bold;text-decoration:none">👑 TIMOTHY</a></div></nav>
<div class="hero">
<h1>Create <span style="color:#f9c846">Pro Designs</span> in 10 Seconds</h1>
<p style="font-size:16px">Managed by <span class="moving-name">TIMOTHY - Trusted Admin</span> <span class="timothy-badge">ONLINE ✅</span></p>
<p style="color:#ccc;font-size:13px;max-width:650px;margin:10px auto">Now 11 Tools! Same moving background! QR Till Now 100% USABLE - M-Pesa Scan Auto-Fills!</p>
<div class="slider" id="slider">
<div class="slide active" style="background:linear-gradient(135deg,#ff3b3b,#ff9a00)"><h2>🔥 MEGA SALE! 50% OFF</h2><small>Poster $1 by TIMOTHY</small></div>
<div class="slide" style="background:linear-gradient(135deg,#00c950,#a8ff78);color:black"><h2>✨ BG Remover $1</h2><small>Remove background 2 sec</small></div>
<div class="slide" style="background:linear-gradient(135deg,#1e3a8a,#60a5fa)"><h2>📱 QR Till $1 USABLE!</h2><small>M-Pesa Scan Works Now!</small></div>
<div class="slide" style="background:linear-gradient(135deg,#ff69b4,#ffb6d9)"><h2>📊 Lot Calculator FREE</h2><small>Forex risk manager</small></div>
</div>
<div class="marquee"><div class="marquee-track">
<span class="price-tag">🎨 Poster $1</span><span class="price-tag">🧾 Receipt $1</span><span class="price-tag">📄 CV $2</span><span class="price-tag">💼 Logo $3</span><span class="price-tag">✂️ BG Remover $1</span><span class="price-tag">📱 QR Till $1 USABLE!</span><span class="price-tag">📊 Lot Calc FREE</span><span class="price-tag">📈 Trading 20%</span><span class="price-tag">📡 VIP $10 by TIMOTHY</span><span class="price-tag">📚 E-Books $2-$6</span>
<span class="price-tag">🎨 Poster $1</span><span class="price-tag">🧾 Receipt $1</span><span class="price-tag">📄 CV $2</span><span class="price-tag">💼 Logo $3</span><span class="price-tag">✂️ BG Remover $1</span><span class="price-tag">📱 QR Till $1 USABLE!</span><span class="price-tag">📊 Lot Calc FREE</span><span class="price-tag">📈 Trading 20%</span><span class="price-tag">📡 VIP $10 by TIMOTHY</span><span class="price-tag">📚 E-Books $2-$6</span>
</div></div>
<a class="btn-main" href="#tools">🚀 Explore 11 Tools Now</a>
<div style="margin-top:12px;font-size:12px;color:#00c950;animation:slideText 2s infinite">✅ QR Till Now USABLE - Customer scans with M-Pesa App & Till Auto-Fills! ✅</div>
</div>
<div id="tools" style="padding:15px;max-width:1000px;margin:auto">
<h2 style="text-align:center">💎 11 Premium Tools</h2>
<div class="grid">
<div class="card"><div style="font-size:32px">🎨</div><h3>Poster Maker</h3><div class="pricing-move">Only $1</div><br><b style="color:#f9c846">$1</b><br><a href="/poster-maker" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Create Now</a></div>
<div class="card"><div style="font-size:32px">🧾</div><h3>Receipt Maker</h3><div class="pricing-move">Only $1</div><br><b style="color:#f9c846">$1</b><br><a href="/receipt-maker" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Create Now</a></div>
<div class="card"><div style="font-size:32px">📄</div><h3>CV Builder</h3><div class="pricing-move">Only $2</div><br><b style="color:#f9c846">$2</b><br><a href="/cv-builder" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Build CV</a></div>
<div class="card"><div style="font-size:32px">💼</div><h3>Logo Maker</h3><div class="pricing-move">Only $3</div><br><b style="color:#f9c846">$3</b><br><a href="/logo-maker" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Design Logo</a></div>
<div class="card"><div style="font-size:32px">✉️</div><h3>Cover Letter</h3><div class="pricing-move">Only $1</div><br><b style="color:#f9c846">$1</b><br><a href="/cover-letter" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Write Now</a></div>
<div class="card" style="border:2px solid #00c950"><div style="font-size:32px">✂️</div><h3>BG Remover <span class="new-badge">NEW</span></h3><div class="pricing-move">Only $1</div><br><b style="color:#00c950">$1</b><br><a href="/bg-remover" class="btn-main" style="padding:7px 16px;background:#00c950;color:white;font-size:11px;margin-top:8px">Remove BG</a></div>
<div class="card" style="border:2px solid #00c950;box-shadow:0 0 15px rgba(0,201,80,0.4)"><div style="font-size:32px">📱</div><h3>QR Till USABLE! <span class="new-badge">FIXED</span></h3><div class="pricing-move">Only $1 • M-Pesa Scan Works!</div><br><b style="color:#00c950">$1 USABLE</b><br><a href="/qr-maker" class="btn-main" style="padding:7px 16px;background:#00c950;color:white;font-size:11px;margin-top:8px">Make QR</a></div>
<div class="card" style="border:2px solid #f9c846"><div style="font-size:32px">📊</div><h3>Lot Calculator <span class="new-badge" style="background:#f9c846;color:black">FREE</span></h3><div class="pricing-move" style="color:#00c950">FREE</div><br><b style="color:#00c950">FREE</b><br><a href="/lot-calculator" class="btn-main" style="padding:7px 16px;background:#f9c846;color:black;font-size:11px;margin-top:8px">Calculate</a></div>
<div class="card" style="border:1px solid #00c950"><div style="font-size:32px">📈</div><h3>Live Trading</h3><div class="pricing-move" style="color:#00c950">20% Fee</div><br><b style="color:#00c950">FREE Start</b><br><a href="/trade" class="btn-main" style="padding:7px 16px;background:#00c950;color:white;font-size:11px;margin-top:8px">Trade Now</a></div>
<div class="card" style="border:1px solid #f9c846"><div style="font-size:32px">📡</div><h3>VIP Signals</h3><div class="pricing-move">Only $10 • By TIMOTHY</div><br><b style="color:#f9c846">$10</b><br><a href="/signals" class="btn-main" style="padding:7px 16px;font-size:11px;margin-top:8px">Join VIP</a></div>
<div class="card"><div style="font-size:32px">📚</div><h3>E-Books</h3><div class="pricing-move">$2-$6</div><br><b style="color:#f9c846">$2-$6</b><br><a href="/ebooks" class="btn-main" style="padding:7px 16px;background:#333;color:white;font-size:11px;margin-top:8px">Browse</a></div>
</div>
</div>
<div class="testimonials-wrap">
<div class="testi-title">⭐ What Kenyans Say About <span class="moving-name">TIMOTHY</span> ⭐</div>
<div class="testi-track">
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>James - Nairobi</b><br><small>"QR Till USABLE now! My customer scanned with M-Pesa and Till auto-filled! TIMOTHY fixed it!"</small><br><small style="color:#00c950">- QR Till USABLE $1</small></div>
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>Grace - Mombasa</b><br><small>"BG Remover $1 saved me 300 bob at cyber. TIMOTHY is best!"</small><br><small style="color:#f9c846">- BG Remover</small></div>
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>Brian - Kisumu</b><br><small>"Lot Calc FREE stopped me blowing. TIMOTHY cares!"</small><br><small style="color:#f9c846">- Lot Calculator</small></div>
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>James - Nairobi</b><br><small>"QR Till USABLE now! My customer scanned with M-Pesa and Till auto-filled! TIMOTHY fixed it!"</small><br><small style="color:#00c950">- QR Till USABLE $1</small></div>
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>Grace - Mombasa</b><br><small>"BG Remover $1 saved me 300 bob at cyber. TIMOTHY is best!"</small><br><small style="color:#f9c846">- BG Remover</small></div>
<div class="testi-card"><div style="color:#f9c846">★★★★★</div><b>Brian - Kisumu</b><br><small>"Lot Calc FREE stopped me blowing. TIMOTHY cares!"</small><br><small style="color:#f9c846">- Lot Calculator</small></div>
</div>
</div>
<div style="max-width:700px;margin:20px auto;padding:15px">
<h2 style="text-align:center">❓ FAQs About <span class="moving-name">TIMOTHY</span></h2>
<div class="faq-item active" onclick="this.classList.toggle('active')"><div class="faq-q">📱 Is QR Till USABLE now? <span>▼</span></div><div class="faq-a">YES! Now FIXED! Select <b>Till Number Only</b> or <b>BG_TILL</b> - QR contains only till number. Customer opens M-Pesa App > Lipa na M-Pesa > Scan QR > Till auto-fills! No typing! By TIMOTHY.</div></div>
<div class="faq-item" onclick="this.classList.toggle('active')"><div class="faq-q">👑 Who is TIMOTHY? <span>▼</span></div><div class="faq-a">I am <b>TIMOTHY</b> - Founder V14.1 - 11 tools - QR now USABLE! Online 7am-11pm - 0118431854</div></div>
<div class="faq-item" onclick="this.classList.toggle('active')"><div class="faq-q">💰 All 11 prices? <span>▼</span></div><div class="faq-a">Poster $1, Receipt $1, CV $2, Logo $3, Cover $1, BG Remover $1, QR Till $1 USABLE FIXED, Lot Calc FREE, Trading FREE, VIP $10, E-Books $2-$6</div></div>
</div>
<div style="text-align:center;padding:20px;background:linear-gradient(135deg,#1a1a25,#2a1a3a);margin-top:20px;border-top:1px solid #f9c846">
<h3>Managed by <span class="moving-name" style="font-size:24px">TIMOTHY</span> - 11 Tools - QR USABLE</h3>
<div class="wallet" style="max-width:350px;margin:10px auto">Bal $<span id="bal">0</span> | <span id="phone">Not logged</span></div>
<div class="card" style="max-width:350px;margin:10px auto"><input id="loginPhone" placeholder="Phone" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><input id="loginPass" type="password" placeholder="Pass" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><button onclick="login()" style="background:#f9c846;color:black;padding:8px 12px;border:none;border-radius:6px;font-weight:bold">Login</button><p id="loginMsg" style="color:#ff5555;font-size:11px"></p></div>
<p style="font-size:11px;color:#666">© 2026 Kaumoni V14.1 - TIMOTHY - QR USABLE Fixed</p>
</div>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:14px 20px;border-radius:50px;font-weight:bold;text-decoration:none;z-index:100">💬 TIMOTHY WhatsApp</a>
<script>
let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('phone').innerText=ph||'Not logged';
async function check(){if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}
async function login(){let p=document.getElementById('loginPhone').value.trim();let pw=document.getElementById('loginPass').value.trim();let r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await r.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);location.reload();}
let cur=0;let slides=document.querySelectorAll('.slide');setInterval(()=>{slides[cur].classList.remove('active');cur=(cur+1)%slides.length;slides[cur].classList.add('active');},2500);check();
</script></body></html>"""

BG_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>BG Remover by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:10px;margin:8px 0}canvas{max-width:100%;border:2px solid #f9c846;border-radius:10px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>✂️ BG Remover $1 - by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><input type="file" id="file" accept="image/*"><select id="bgColor"><option value="white">White BG (ID Photo)</option><option value="transparent">Transparent</option><option value="black">Black</option><option value="#f9c846">Gold - TIMOTHY</option></select><button onclick="removeBG()" style="background:#f9c846;color:black;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Remove BG $1</button><button onclick="download()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold;margin-top:6px">Download HD</button></div></div><div><canvas id="canvas"></canvas></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;let img=new Image();let paid=false;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
document.getElementById('file').addEventListener('change',e=>{let f=e.target.files[0];if(!f)return;let url=URL.createObjectURL(f);img.onload=()=>{let c=document.getElementById('canvas');c.width=img.width;c.height=img.height;let ctx=c.getContext('2d');ctx.drawImage(img,0,0);};img.src=url;});
async function removeBG(){if(userPhone!=='0118431854'&&userBal<1&&!paid){let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'bgremover'})});let d=await r.json();if(!d.ok){alert(d.message);return;}paid=true;loadBal();}
let c=document.getElementById('canvas');let ctx=c.getContext('2d');let imgData=ctx.getImageData(0,0,c.width,c.height);let data=imgData.data;let bg=document.getElementById('bgColor').value;
for(let i=0;i<data.length;i+=4){let r=data[i],g=data[i+1],b=data[i+2];if(r>220&&g>220&&b>220){if(bg==='transparent'){data[i+3]=0;}else if(bg==='white'){data[i]=255;data[i+1]=255;data[i+2]=255;}else if(bg==='black'){data[i]=0;data[i+1]=0;data[i+2]=0;}else if(bg==='#f9c846'){data[i]=249;data[i+1]=200;data[i+2]=70;}}}
ctx.putImageData(imgData,0,0);
if(bg!=='transparent'){let tmp=document.createElement('canvas');tmp.width=c.width;tmp.height=c.height;let tctx=tmp.getContext('2d');if(bg==='#f9c846')tctx.fillStyle='#f9c846';else tctx.fillStyle=bg;tctx.fillRect(0,0,tmp.width,tmp.height);tctx.drawImage(c,0,0);ctx.clearRect(0,0,c.width,c.height);ctx.drawImage(tmp,0,0);}
alert('BG Removed by TIMOTHY!');}
function download(){let c=document.getElementById('canvas');let a=document.createElement('a');a.download='BG_Removed_TIMOTHY.png';a.href=c.toDataURL();a.click();}
loadBal();
</script></body></html>"""

QR_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>QR Till USABLE by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:10px}#poster{width:350px;margin:auto;background:white;color:black;padding:20px;border-radius:12px;text-align:center;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:22px;font-weight:900;padding:8px 18px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📱 QR Till USABLE $1 - by TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><input id="biz" value="KAUMONI SHOP" oninput="draw()"><input id="till" value="123456" oninput="draw()" placeholder="Till Number e.g. 123456"><input id="phone" value="0118431854" oninput="draw()"><select id="qrType" onchange="draw()"><option value="till">USABLE: Till Number Only (M-Pesa Scan Auto-Fills)</option><option value="bg">USABLE: BG_TILL Format (Buy Goods)</option><option value="full">INFO: Full Business Info (Not auto-pay)</option></select><input id="msg" value="Lipa na M-Pesa - TIMOTHY" oninput="draw()"><p style="font-size:10px;color:#00c950">✅ USABLE: If you select Till Only, customer scans with M-Pesa App > Lipa na M-Pesa > QR and Till auto-fills!</p></div><button onclick="downloadQR()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD Poster $1</button></div><div id="poster"></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){
let biz=document.getElementById('biz').value;let till=document.getElementById('till').value;let ph=document.getElementById('phone').value;let msg=document.getElementById('msg').value;let type=document.getElementById('qrType').value;
let qrText = till;
if(type==='bg') qrText = 'BG_' + till;
if(type==='full') qrText = `TILL:${till}|PHONE:${ph}|BIZ:${biz}`;
document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="border:3px solid #f9c846;padding:15px;border-radius:12px"><h2 style="margin:0;color:#1a1a25">${biz}</h2><div id="qrcode" style="margin:10px auto;display:flex;justify-content:center"></div><h3 style="background:#1a1a25;color:#f9c846;padding:6px;border-radius:6px">TILL: ${till}</h3><p style="font-size:12px">${msg}</p><p style="font-size:11px;color:#666">Phone: ${ph}</p><small style="background:${type==='till'||type==='bg'?'#00c950':'#666'};color:white;padding:4px 10px;border-radius:10px">${type==='till'||type==='bg'?'✅ USABLE - M-Pesa Scan Works':'ℹ️ INFO Only'}</small><br><small style="font-size:9px;color:#999">By TIMOTHY - Scan to Pay</small></div>`;
new QRCode(document.getElementById("qrcode"), {text:qrText,width:190,height:190});
}
async function downloadQR(){if(userPhone!=='0118431854'&&userBal<1){alert('Need $1');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'qr'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='QR_Till_USABLE_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>"""

LOT_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Lot Calculator FREE by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:14px;border-radius:12px;margin:8px 0}.result{background:linear-gradient(90deg,#00c950,#00ff88);color:black;padding:14px;border-radius:10px;font-weight:bold;text-align:center;font-size:18px;margin-top:10px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>📊 Lot Size Calculator FREE - by TIMOTHY</h2><p style="color:#aaa;font-size:12px">Avoid blowing account! TIMOTHY's risk manager</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;max-width:800px;margin:auto"><div><div class="card"><label>Account Balance $</label><input id="bal" type="number" value="100" oninput="calc()"><label>Risk % (1-3)</label><input id="risk" type="number" value="2" oninput="calc()"><label>Pair</label><select id="pair" onchange="calc()"><option value="XAUUSD">XAUUSD GOLD</option><option value="EURUSD">EURUSD</option><option value="BTCUSD">BTCUSD</option><option value="GBPUSD">GBPUSD</option></select><label>Entry Price</label><input id="entry" type="number" value="2345.5" oninput="calc()"><label>Stop Loss Price</label><input id="sl" type="number" value="2335.5" oninput="calc()"><label>Take Profit</label><input id="tp" type="number" value="2365.5" oninput="calc()"></div></div><div><div class="card"><h3 style="color:#f9c846">Result by TIMOTHY</h3><div id="res" class="result">Enter values</div><div id="details" style="margin-top:10px;font-size:13px;color:#ccc"></div><a href="/signals" style="display:block;background:#f9c846;color:black;padding:12px;border-radius:8px;text-align:center;font-weight:bold;text-decoration:none;margin-top:10px">📡 Join VIP $10</a></div></div></div>
<script>
function calc(){
let bal=parseFloat(document.getElementById('bal').value)||0;let riskP=parseFloat(document.getElementById('risk').value)||0;
let entry=parseFloat(document.getElementById('entry').value)||0;let sl=parseFloat(document.getElementById('sl').value)||0;let tp=parseFloat(document.getElementById('tp').value)||0;
let riskAmt=bal*riskP/100;let slDist=Math.abs(entry-sl);let tpDist=Math.abs(tp-entry);
let lot = riskAmt / (slDist * 10);if(lot<0.01)lot=0.01;
let rr = slDist>0? (tpDist/slDist).toFixed(2) : 0;
document.getElementById('res').innerHTML=`Risk $${riskAmt.toFixed(2)} | Lot <b>${lot.toFixed(2)}</b><br>SL ${slDist.toFixed(2)} | RR 1:${rr}`;
document.getElementById('details').innerHTML=`Balance $${bal}<br>Risk ${riskP}% = $${riskAmt.toFixed(2)}<br>SL ${slDist.toFixed(2)}<br><b style="color:${rr>=2?'#00c950':'#ef5350'}">RR 1:${rr} ${rr>=2?'✅ Good':'❌ Bad'}</b><br><br><b style="color:#f9c846">Lot: ${lot.toFixed(2)}</b>`;
}
calc();
</script></body></html>"""

POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.95);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Poster $1 by TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Red</option><option value="2">Pink</option><option value="3">Blue</option><option value="4">Yellow</option><option value="5">Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XX" oninput="draw()"><input id="loc" value="Nairobi" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $1</button></div><div id="poster"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let c={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']}[document.getElementById('tpl').value];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px"><h1 style="font-size:40px;margin:0">${document.getElementById('title').value}</h1><h2>${document.getElementById('sub').value}</h2><div style="background:black;color:white;padding:6px 12px;border-radius:20px;margin-top:15px"><b>${document.getElementById('phone').value}</b><br><small>${document.getElementById('loc').value}</small></div></div>`;}async function downloadPoster(){if(userPhone!=='0118431854'&&userBal<1){alert('Low');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(cv=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='HD_TIMOTHY.png';a.href=cv.toDataURL();a.click();loadBal();});}draw();loadBal();</script></body></html>"""

RECEIPT_HTML = POSTER_HTML.replace("Poster $1 by TIMOTHY","Receipt $1 by TIMOTHY")
CV_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,textarea{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#preview{background:white;color:black;padding:20px;border-radius:8px;position:relative;overflow:hidden;min-height:450px}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>CV $2 by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><input id="name" value="Timo Kaumoni" oninput="update()"><input id="title" value="Sales & Trader" oninput="update()"><input id="phone" value="07XX" oninput="update()"><input id="email" value="timo@email.com" oninput="update()"><textarea id="summary" rows="2" oninput="update()">Hardworking - TIMOTHY trained</textarea><input id="exp" value="Kaumoni Ltd - Sales 2022-2024" oninput="update()"><input id="edu" value="UoN - BBA 2020" oninput="update()"><input id="skills" value="Sales, Trading, Canva" oninput="update()"></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $2</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){document.getElementById('preview').innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="border-left:4px solid #f9c846;padding-left:10px"><h1 style="margin:0;font-size:24px">${document.getElementById('name').value}</h1><b style="color:#f9c846">${document.getElementById('title').value}</b><p style="font-size:11px;color:#555">${document.getElementById('phone').value} | ${document.getElementById('email').value}</p></div><hr><p><b>SUMMARY</b><br><span style="font-size:12px">${document.getElementById('summary').value}</span></p><p><b>EXPERIENCE</b><br><span style="font-size:12px">${document.getElementById('exp').value}</span></p><p><b>EDUCATION</b><br><span style="font-size:12px">${document.getElementById('edu').value}</span></p><p><b>SKILLS</b><br><span style="font-size:12px">${document.getElementById('skills').value}</span></p>`;}async function downloadCV(){if(userPhone!=='0118431854'&&userBal<2){alert('Need $2');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:2,reason:'cv'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='CV_HD.png';a.href=c.toDataURL();a.click();loadBal();});}update();loadBal();</script></body></html>"""

LOGO_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Logo by TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#preview{background:white;color:black;width:340px;height:340px;margin:auto;display:flex;flex-direction:column;justify-content:center;align-items:center;border-radius:16px;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:22px;font-weight:900;padding:8px 18px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Logo $3 by TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><input id="biz" value="KAUMONI" oninput="update()"><input id="tag" value="TIMOTHY BRANDS" oninput="update()"><select id="style" onchange="update()"><option value="1">Gold Black</option><option value="2">Blue White</option><option value="3">Green White</option><option value="4">Red Yellow</option><option value="5">Purple Luxury</option></select></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $3</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){let biz=document.getElementById('biz').value;let tag=document.getElementById('tag').value;let st=document.getElementById('style').value;let bg='#0e0e14',col='#f9c846',bd='#f9c846';if(st=='2'){bg='#1e3a8a';col='white';bd='white';}if(st=='3'){bg='#00c950';col='white';bd='white';}if(st=='4'){bg='#ff3b3b';col='#ffcc00';bd='#ffcc00';}if(st=='5'){bg='#6a0dad';col='#f9c846';bd='#f9c846';}document.getElementById('preview').style.background=bg;document.getElementById('preview').innerHTML=`<div id="wm">PREVIEW PAY $3</div><div style="border:3px solid ${bd};padding:20px;border-radius:50%;width:120px;height:120px;display:flex;justify-content:center;align-items:center"><h1 style="font-size:36px;margin:0;color:${col}">${biz.charAt(0)}</h1></div><h1 style="font-size:28px;margin:12px 0 4px;color:${col}">${biz}</h1><b style="color:${col};letter-spacing:3px;font-size:10px">${tag}</b>`;}async function downloadCV(){if(userPhone!=='0118431854'&&userBal<3){alert('Need $3');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:3,reason:'logo'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='Logo_HD.png';a.href=c.toDataURL();a.click();loadBal();});}update();loadBal();</script></body></html>"""

COVER_HTML = CV_HTML.replace("CV $2 by TIMOTHY","Cover Letter $1 by TIMOTHY").replace("PREVIEW PAY $2","PREVIEW PAY $1")
EBOOKS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>E-Books by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:10px 0;display:flex;justify-content:space-between}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}@media(max-width:600px){.grid{grid-template-columns:1fr}}</style></head><body><nav><a href="/">← Home</a><b>📚 E-BOOKS by TIMOTHY</b><span id="uPhone">-</span></nav><div style="max-width:700px;margin:auto"><div class="card" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black"><div>Bal $ <span id="uBal">0</span> | TIMOTHY Library</div></div><div class="grid" id="books"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;let books=[{id:1,title:"Forex Mastery by TIMOTHY",price:5},{id:2,title:"Canva Secrets by TIMOTHY",price:3},{id:3,title:"M-Pesa Guide",price:4},{id:4,title:"CV Jobs",price:2},{id:5,title:"WhatsApp Sales",price:3},{id:6,title:"Crypto Basics KE",price:6}];async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function render(){document.getElementById('books').innerHTML=books.map(b=>`<div class="card"><div><b>${b.title}</b><br><b style="color:#f9c846">$${b.price}</b></div><button onclick="buy(${b.id})" style="background:#f9c846;color:black">Buy</button></div>`).join('');}async function buy(id){let b=books.find(x=>x.id===id);if(userPhone!=='0118431854'&&userBal<b.price){alert('Need $'+b.price);return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:b.price,reason:'ebook'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let blob=new Blob([b.title],{type:'text/plain'});let a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=b.title+'.txt';a.click();loadBal();}render();loadBal();</script></body></html>"""

SIGNALS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIP by TIMOTHY</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px;margin:0}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;border-bottom:1px solid #2a2a3a;position:sticky;top:0}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:10px 0}.signal{background:#1e1e2d;border-left:3px solid #00c950;padding:10px;margin:8px 0;border-radius:0 8px 8px 0}</style></head><body>
<nav><a href="/">← Home</a><b>📡 VIP by TIMOTHY</b><span id="uPhone" style="font-size:11px">-</span></nav>
<div style="max-width:600px;margin:auto;padding:10px">
<div class="card" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black"><b>Bal $ <span id="uBal">0</span></b> | Admin TIMOTHY</div>
<div id="notVip" class="card" style="border:2px dashed #f9c846;text-align:center"><h3>🔒 Join VIP $10 - By TIMOTHY</h3><button onclick="join()" style="background:#f9c846;color:black;width:100%;padding:12px">Join VIP Now</button></div>
<div id="vipArea" style="display:none"><div class="card" style="border:1px solid #00c950;background:rgba(0,201,80,0.1);text-align:center"><h3 style="color:#00c950">✅ VIP ACTIVE - TIMOTHY Online</h3></div><h3>📈 Live Signals from TIMOTHY</h3><div id="signals">Loading...</div></div>
</div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let isVip=localStorage.getItem('isVip_'+userPhone)==='true';
async function load(){if(!userPhone){alert('Login');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854')isVip=true;let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();document.getElementById('uBal').innerText=(d.balance||0).toFixed(2);if(isVip){document.getElementById('notVip').style.display='none';document.getElementById('vipArea').style.display='block';let sr=await fetch('/api/signals');let sj=await sr.json();if(sj.length==0)document.getElementById('signals').innerHTML='<p style=color:#666>No signals - TIMOTHY will post soon</p>';else document.getElementById('signals').innerHTML=sj.map(s=>`<div class="signal" style="border-left-color:${s.result.includes('✅')?'#00c950':s.result.includes('❌')?'#ef5350':'#f9c846'}"><b>${s.pair} - ${s.type}</b> <span style="background:${s.type==='BUY'?'#00c950':'#ef5350'};color:white;padding:2px 8px;border-radius:10px;font-size:11px">${s.type}</span><br><small>Entry ${s.entry} | TP ${s.tp} | SL ${s.sl}</small><br><small style="color:#aaa">${s.time}</small> <b style="float:right;color:${s.result.includes('✅')?'#00c950':s.result.includes('❌')?'#ef5350':'#f9c846'}">${s.result}</b></div>`).join('');}}
async function join(){if(userPhone==='0118431854'){localStorage.setItem('isVip_'+userPhone,'true');location.reload();return;}let r=await fetch('/api/balance?phone='+userPhone);let dd=await r.json();if(dd.balance<10){alert('Need $10');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}localStorage.setItem('isVip_'+userPhone,'true');location.reload();}load();
</script></body></html>"""

ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin TIMOTHY V14.1</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:12px;border-radius:12px;margin:8px 0}button{padding:7px 12px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}input,select{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0;width:100%}.suggest{background:#1e1e2d;border-left:3px solid #f9c846;padding:8px;margin:6px 0;border-radius:0 8px 8px 0}.sig{background:#1e1e2d;padding:8px;margin:6px 0;border-radius:8px;border-left:3px solid #00c950}.moving-name{font-size:18px;font-weight:bold;color:#f9c846;display:inline-block;animation:nameMove 3s ease-in-out infinite}@keyframes nameMove{0%,100%{transform:translateY(0)}50%{transform:translateY(-5px) scale(1.05)}}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>ADMIN - <span class="moving-name">TIMOTHY 👑 V14.1 QR USABLE</span></h2>
<div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><b>Total Fees $<span id="total">0</span></b> | <span id="userCount">0 users</span> | <span class="moving-name" style="color:black">TIMOTHY ONLINE ✅</span></div>
<div class="card" style="border:2px solid #f9c846"><h3>🤖 SEMI-AUTO by TIMOTHY</h3><button onclick="checkTrend()" style="background:#f9c846;color:black;width:100%;padding:12px">🔍 Check Trend Now</button><div id="trendBox">Click</div></div>
<div class="card" style="border:1px solid #00c950"><h3>📡 Post Signal</h3><input id="sPair" placeholder="Pair"><select id="sType"><option>BUY</option><option>SELL</option></select><input id="sEntry" placeholder="Entry"><input id="sTp" placeholder="TP"><input id="sSl" placeholder="SL"><input id="sResult" value="Running..."><button onclick="postSig()" style="background:#00c950;color:white;width:100%;padding:12px">📤 Send to VIP</button><p id="sMsg" style="color:#00c950"></p></div>
<div class="card"><h3>📈 Active - WIN/LOSS</h3><div id="activeSigs">Loading...</div></div>
<div class="card"><h3>Deposits</h3><div id="depList">Loading...</div></div>
<div class="card"><h3>Users</h3><div id="usersList">Loading...</div></div>
<script>
async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText=(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} $${(u.balance||0).toFixed(2)}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add</button></div>`).join('');document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div style="background:#2a2a3a;padding:6px;margin:4px 0;border-radius:6px"><b>${d.phone}</b> $${d.amount} ${d.code} ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';loadSigs();}
async function loadSigs(){let r=await fetch('/api/signals');let s=await r.json();if(s.length==0){document.getElementById('activeSigs').innerHTML='<small style=color:#666>No signals</small>';return;}document.getElementById('activeSigs').innerHTML=s.map((sig,i)=>`<div class="sig"><b>${sig.pair} ${sig.type}</b> Entry ${sig.entry} TP ${sig.tp} SL ${sig.sl}<br><small>${sig.time} - <b style="color:${sig.result.includes('✅')?'#00c950':sig.result.includes('❌')?'#ef5350':'#f9c846'}">${sig.result}</b></small><br><div style="margin-top:6px"><button onclick="closeWin(${i})" style="background:#00c950;color:white;font-size:11px">✅ WIN</button> <button onclick="closeLoss(${i})" style="background:#ef5350;color:white;font-size:11px">❌ LOSS</button> <button onclick="delSig(${i})" style="background:#333;color:white;font-size:11px">🗑 Delete</button></div></div>`).join('');}
async function checkTrend(){document.getElementById('trendBox').innerHTML='Checking...';let r=await fetch('/api/trend-suggest');let d=await r.json();document.getElementById('trendBox').innerHTML=d.map(t=>`<div class="suggest"><b>${t.pair}</b> - $${t.price}<br>Suggest: <b style="color:${t.trend==='BUY'?'#00c950':'#ef5350'}">${t.trend}</b> - ${t.note}<br><small>SMA20 ${t.sma20} vs SMA50 ${t.sma50}</small><br><button onclick="quickPost('${t.pair}','${t.trend}','${t.price}')" style="background:#f9c846;color:black;padding:5px 10px;font-size:11px;margin-top:5px">Use This</button></div>`).join('');}
function quickPost(pair,trend,price){document.getElementById('sPair').value=pair;document.getElementById('sType').value=trend;document.getElementById('sEntry').value=price;let p=parseFloat(price);if(isNaN(p))p=2345;if(trend==='BUY'){document.getElementById('sTp').value=(p*1.006).toFixed(2);document.getElementById('sSl').value=(p*0.997).toFixed(2);}else{document.getElementById('sTp').value=(p*0.994).toFixed(2);document.getElementById('sSl').value=(p*1.003).toFixed(2);}}
async function postSig(){let data={pair:document.getElementById('sPair').value,type:document.getElementById('sType').value,entry:document.getElementById('sEntry').value,tp:document.getElementById('sTp').value,sl:document.getElementById('sSl').value,result:document.getElementById('sResult').value||'Running...'};if(!data.pair||!data.entry){alert('Fill');return;}let res=await fetch('/api/add-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});await res.json();document.getElementById('sMsg').innerText='✅ Sent by TIMOTHY!';loadSigs();}
async function closeWin(i){let p=prompt('Win e.g. +20$ ✅','+20$ ✅');if(!p)return;await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function closeLoss(i){let p=prompt('Loss e.g. -10$ ❌','-10$ ❌');if(!p)return;await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function delSig(i){if(!confirm('Delete?'))return;await fetch('/api/delete-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});loadSigs();}
async function approveDep(i){let r=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function rejectDep(i){let r=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function addBal(ph){let amt=prompt('Amount $');if(!amt)return;await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:ph,amount:parseFloat(amt)})});load();}
load();setInterval(loadSigs,5000);
</script></body></html>"""

TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading by TIMOTHY</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:8px}.card{background:#1a1a25;padding:10px;border-radius:8px;margin-top:8px}#tv_chart{height:400px}</style></head><body><a href="/" style="color:#f9c846">← Home</a> <b>Trading - TIMOTHY's Chart</b> Bal $<span id="bal">0</span> | <a href="/lot-calculator" style="color:#00c950;text-decoration:none;font-weight:bold">📊 FREE Lot Calc</a><div id="tv_chart" class="card"></div><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","theme":"dark","container_id":"tv_chart"});async function load(){let ph=localStorage.getItem('userPhone_v5');if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}load();</script></body></html>"""

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

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); pwd=data['password'].strip()
    users=load_json(USERS_FILE, {})
    if phone==ADMIN_PHONE:
        if pwd!=ADMIN_PASSWORD: return jsonify({"ok":False,"message":"Wrong admin pass"})
        if phone not in users: users[phone]={"phone":phone,"password":pwd,"balance":999,"total_fee":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":999})
    if phone in users:
        if users[phone].get('password') and users[phone].get('password')!=pwd: return jsonify({"ok":False,"message":"Wrong password"})
        if not users[phone].get('password'): users[phone]['password']=pwd; save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":users[phone].get('balance',0)})
    else: users[phone]={"phone":phone,"password":pwd,"balance":0,"total_fee":0,"joined":str(datetime.now())}; save_json(USERS_FILE, users); return jsonify({"ok":True,"balance":0})

@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone')
    if phone==ADMIN_PHONE: return jsonify({"phone":phone,"balance":999})
    users=load_json(USERS_FILE, {}); return jsonify(users.get(phone, {"phone":phone,"balance":0}))

@app.route('/api/deposit-request', methods=['POST'])
def api_dep_req():
    data=request.get_json(); deps=load_json(DEPOSITS_FILE, []); deps.append({"phone":data['phone'],"code":data['code'],"amount":float(data['amount']),"status":"pending","time":str(datetime.now())}); save_json(DEPOSITS_FILE, deps); return jsonify({"ok":True,"message":"Sent to TIMOTHY"})

@app.route('/api/add-balance', methods=['POST'])
def api_add_bal():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0}
    users[ph]['balance']=float(users[ph].get('balance',0))+float(data['amount']); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']; amt=float(data['amount'])
    if ph==ADMIN_PHONE: return jsonify({"ok":True,"balance":999})
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({"ok":False,"message":"Low balance - deposit"})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+amt; save_json(FEES_FILE, fees); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {}); deps=load_json(DEPOSITS_FILE, []); fees=load_json(FEES_FILE, {"total":0}); return jsonify({"users":list(users.values()),"deposits":deps,"total_fees":fees.get('total',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    idx=int(request.get_json()['index']); deps=load_json(DEPOSITS_FILE, []); dep=deps[idx]; users=load_json(USERS_FILE, {})
    if dep['status']!='pending': return jsonify({"message":"Already"})
    ph=dep['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0}
    users[ph]['balance']+=float(dep['amount']); save_json(USERS_FILE, users); deps[idx]['status']='approved'; save_json(DEPOSITS_FILE, deps); return jsonify({"message":"Approved by TIMOTHY"})

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
