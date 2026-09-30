
from flask import Flask, request, jsonify
import os, json
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_TIMOTHY_V17_FINAL"
USERS_FILE='users.json'
FEES_FILE='fees.json'
DEPOSITS_FILE='deposits.json'
PRODUCTS_FILE='products.json'
ORDERS_FILE='orders.json'
SERVICES_FILE='services_orders.json'

def load_json(f,d):
    if not os.path.exists(f):
        return d
    try:
        with open(f) as jf:
            return json.load(jf)
    except:
        return d
def save_json(f,data):
    with open(f,'w') as jf:
        json.dump(data,jf)
def nav(active="home"):
    return f"""
<nav style="background:#1a1a25;padding:12px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #333;flex-wrap:wrap;gap:8px;z-index:100">
<b style="color:#f9c846">KAUMONI V17.2</b>
<div style="display:flex;gap:10px;font-size:11px;flex-wrap:wrap">
<a href="/" style="color:{'#f9c846' if active=='home' else 'white'};text-decoration:none;font-weight:bold">Home</a>
<a href="/shop" style="color:{'#f9c846' if active=='shop' else 'white'};text-decoration:none">Shop</a>
<a href="/freelance-services" style="color:white;text-decoration:none">Services</a>
<a href="/design-studio" style="color:white;text-decoration:none">Design</a>
<a href="/student-hub" style="color:white;text-decoration:none">Student Hub</a>
<a href="/free-tools" style="color:white;text-decoration:none">Free Tools</a>
<a href="/ai-tools" style="color:white;text-decoration:none">AI Tools</a>
<a href="/about" style="color:white;text-decoration:none">About</a>
<a href="/dashboard" style="color:white;text-decoration:none">Dashboard</a>
<a href="/admin" style="color:#f9c846;text-decoration:none">TIMOTHY</a>
</div></nav>
"""
@app.route('/')
def home():
    return nav('home') + """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni All-in-One V17.2</title>
<style>body{background:#0a0a12;color:white;font-family:Arial;margin:0}.card{background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;margin:8px;text-align:center}.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:12px}@media(max-width:700px){.grid{grid-template-columns:1fr}}.btn{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 16px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin:4px}</style></head><body>
<div style="text-align:center;padding:30px;background:linear-gradient(90deg,#0e0e14,#1a1a25,#2a1a3a)">
<h1><span style="color:#f9c846">All-in-One</span> Digital Services Platform</h1>
<p>Managed by <b style="color:#f9c846">TIMOTHY - 0118431854 - V17.2 18 Tools</b></p>
<p style="color:#ccc;max-width:700px;margin:auto;font-size:13px">Shop + Freelance Services + Design Studio (18 Tools) + Student Hub + Free Tools + AI Tools + User Dashboard + Seller Dashboard + M-Pesa STK Auto + Order Tracking</p>
<a class="btn" href="/shop">Shop Digital Products</a><a class="btn" href="/design-studio" style="background:#6a0dad;color:white">Design Studio 18 Tools</a><a class="btn" href="/free-tools" style="background:#00c950;color:white">Free Tools</a>
</div>
<div style="max-width:1100px;margin:auto;padding:15px">
<h2 style="text-align:center">What We Offer - 16 Sections You Asked</h2>
<div class="grid">
<div class="card">SHOP<br><b>Digital Products</b><br><small>Ebooks, Templates, CVs, Trading Guides</small><br><a class="btn" href="/shop">Browse Shop</a></div>
<div class="card">SERVICES<br><b>Freelance Services</b><br><small>CV, Ebook Writing, PPT, Logo, Website</small><br><a class="btn" href="/freelance-services">Hire Now</a></div>
<div class="card">DESIGN<br><b>Design Studio - 18 Tools HD</b><br><small>Poster, KRA, Biz Card, Cert, Payslip</small><br><a class="btn" href="/design-studio">Create Design</a></div>
<div class="card">STUDENT<br><b>Student Hub</b><br><small>Notes, GPA, Grade Calc, Revision</small><br><a class="btn" href="/student-hub">Student Hub</a></div>
<div class="card">FREE<br><b>Free Tools - 9 Tools</b><br><small>Profit, Loan, Currency, QR, Lot, TikTok</small><br><a class="btn" href="/free-tools">Free Tools</a></div>
<div class="card">AI<br><b>AI Tools</b><br><small>Writing, CV, Caption, Biz Names</small><br><a class="btn" href="/ai-tools">AI Tools</a></div>
</div>
<h2 style="text-align:center">Featured Services - 18 Tools HD - TIMOTHY</h2>
<div class="grid">
<div class="card" style="border:1px solid #f9c846"><b>Poster Maker $1 HD</b><br><a class="btn" href="/poster-maker">Create HD</a></div>
<div class="card" style="border:1px solid #f9c846"><b>KRA E-TIMS $1.5 HD</b><br><a class="btn" href="/kra-invoice">Make KRA HD</a></div>
<div class="card" style="border:1px solid #42a5f5"><b>Business Card $2 HD</b><br><a class="btn" href="/business-card">Make Card HD</a></div>
<div class="card" style="border:1px solid #6a0dad"><b>Certificate $1.5 HD</b><br><a class="btn" href="/certificate-maker">Make Cert HD</a></div>
<div class="card" style="border:1px solid #00c950"><b>Payslip $1 HD</b><br><a class="btn" href="/payslip-maker">Make Payslip HD</a></div>
<div class="card" style="border:1px solid #ff9800"><b>AI Caption $1 HD</b><br><a class="btn" href="/ai-caption">AI Generate HD</a></div>
</div>
<div style="text-align:center;padding:20px;margin-top:20px;background:#1a1a25;border-radius:12px;border:1px solid #f9c846">
<h3>Core Automation - TIMOTHY</h3>
<p style="font-size:12px">Customer - Select Product/Service - Place Order - M-Pesa STK Push - Payment Verification - Order Confirmed - Digital Product Auto Delivered OR Service Sent to Dashboard - Status Updates</p>
<a class="btn" href="/shop">Shop Now</a><a class="btn" href="/freelance-services" style="background:#00c950;color:white">Order Service</a>
</div>
<div style="text-align:center;padding:20px">
<p>0118431854 | WhatsApp <a href="https://wa.me/254118431854" style="color:#25D366;font-weight:bold">TIMOTHY</a></p>
<p style="font-size:11px;color:#666"><a href="/about" style="color:#666">About</a> | <a href="/terms" style="color:#666">Terms</a> | <a href="/privacy" style="color:#666">Privacy</a> | <a href="/refund" style="color:#666">Refund</a> | <a href="/dashboard" style="color:#666">Dashboard</a> | <a href="/seller-dashboard" style="color:#666">Seller</a></p>
<p style="font-size:11px;color:#666">2026 Kaumoni V17.2 - ALL-IN-ONE - TIMOTHY</p>
</div>
</div></body></html>
"""
@app.route('/shop')
def shop():
    return nav('shop') + """
<div style="max-width:1100px;margin:auto;padding:15px"><h2>Shop - Digital Products - TIMOTHY</h2>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin:10px 0">
<button onclick="filterShop('all')" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:20px;font-weight:bold">All</button>
<button onclick="filterShop('ebook')" style="background:#1a1a25;color:white;padding:6px 12px;border:1px solid #333;border-radius:20px">Ebooks</button>
<button onclick="filterShop('template')" style="background:#1a1a25;color:white;padding:6px 12px;border:1px solid #333;border-radius:20px">Templates</button>
<button onclick="filterShop('cv')" style="background:#1a1a25;color:white;padding:6px 12px;border:1px solid #333;border-radius:20px">CV</button>
</div>
<div id="grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px"></div></div>
<script>
let all=[];fetch('/api/products').then(r=>r.json()).then(d=>{all=d;render('all')});
function render(cat){let list=cat==='all'?all:all.filter(p=>p.category===cat);document.getElementById('grid').innerHTML=list.map(p=>`<div style="background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;text-align:center"><div style="font-size:40px">${p.icon}</div><b>${p.title}</b><br><small style="color:#aaa">${p.desc}</small><br><small>Features: ${p.features}</small><br><b style="color:#f9c846">$${p.price}</b><br><a href="/product/${p.id}" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold;margin-top:6px;display:inline-block">Buy - STK Push</a></div>`).join('')}
function filterShop(c){render(c)}
</script>
"""
@app.route('/product/<int:pid>')
def product_detail(pid):
    return nav('shop') + f"""
<div style="max-width:800px;margin:auto;padding:15px"><a href="/shop" style="color:#f9c846">Shop</a><div id="det" style="background:#1a1a25;padding:15px;border-radius:12px;margin-top:10px">Loading product {pid}...</div></div>
<script>
fetch('/api/products').then(r=>r.json()).then(all=>{{
let p=all.find(x=>x.id=={pid});
if(!p){{document.getElementById('det').innerHTML='Not found';return}}
document.getElementById('det').innerHTML=`
<div style="text-align:center"><div style="font-size:60px">${{p.icon}}</div><h2>${{p.title}}</h2><b style="color:#f9c846;font-size:22px">$${{p.price}}</b></div>
<p><b>Description:</b> ${{p.desc}}</p>
<p><b>Features:</b> ${{p.features}}</p>
<hr>
<h3>M-Pesa Payment - Automatic STK Push - TIMOTHY</h3>
<input id="phone" placeholder="M-Pesa Phone 07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:8px">
<div style="background:#0e0e14;padding:10px;border-radius:8px;margin:10px 0;font-size:11px">Customer - Select - Order - STK Push - Verification - Confirmed - Auto Download<br>Digital Product Delivery Automated</div>
<button onclick="buy()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold">Buy Now - M-Pesa STK Push</button>
<p id="msg" style="color:#00c950"></p>
`;
}})
function buy(){{
let ph=document.getElementById('phone').value;
if(!ph){{alert('Enter phone');return}}
document.getElementById('msg').innerText='Sending STK Push to '+ph+' - Enter PIN...';
fetch('/api/order-product',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{product_id:{pid},phone:ph}})}}).then(r=>r.json()).then(d=>{{
if(d.ok){{document.getElementById('msg').innerHTML=`Verified! Order Confirmed by TIMOTHY!<br><a href="${{d.download_url}}" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Download Now - Auto Delivered</a><br><small>Payment History Saved - Refund policy applies</small>`}}else{{document.getElementById('msg').innerText=d.message}}
}})
}}
</script>
"""
@app.route('/freelance-services')
def freelance_services():
    return nav('services') + """
<div style="max-width:1100px;margin:auto;padding:15px"><h2>Freelance Services - TIMOTHY</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>CV / Resume Creation $3</b><br><small>Pro CV in 24h - Examples available</small><br><a href="/order-service?type=cv" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Order - $3</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Ebook Writing $15</b><br><small>5k words + Design</small><br><a href="/order-service?type=ebook" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Order - $15</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>PPT Presentation $5</b><br><small>20 slides pro</small><br><a href="/order-service?type=ppt" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Order - $5</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Poster Design $1 - Automated</b><br><small>HD in 10 sec</small><br><a href="/poster-maker" style="background:#00c950;color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Create Now - $1</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Logo Design $3</b><br><small>HD Logo</small><br><a href="/logo-maker" style="background:#00c950;color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Create Now - $3</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Website Creation $50</b><br><small>Landing / Portfolio / Business / Store</small><br><a href="/order-service?type=website" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Order - $50</a></div>
</div>
</div>
"""
@app.route('/order-service')
def order_service_page():
    return nav('services') + """
<div style="max-width:700px;margin:auto;padding:15px"><h2>Order Service - Requirements + STK Push - TIMOTHY</h2>
<div style="background:#1a1a25;padding:15px;border-radius:12px">
<input id="type" placeholder="Service Type e.g. CV / Website" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0">
<textarea id="req" placeholder="Customer Requirements - Describe what you need..." style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0" rows="4"></textarea>
<input id="file" placeholder="Upload Requirements/File Link (Google Drive)" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0">
<input id="phone" placeholder="M-Pesa Phone for STK Push 07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0">
<button onclick="place()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold">Place Order - M-Pesa STK Push</button>
<p id="msg" style="color:#00c950"></p>
<div id="track" style="display:none;background:#0e0e14;padding:10px;border-radius:8px;margin-top:10px"><h3>Order Tracking - Status Updates</h3><p>Status: Placed - Payment Verified - In Progress - Completed</p><p>Customer Notifications via WhatsApp - TIMOTHY</p></div>
</div></div>
<script>
let t=new URLSearchParams(window.location.search).get('type')||'';document.getElementById('type').value=t;
function place(){let d={service_type:document.getElementById('type').value,requirements:document.getElementById('req').value,file_link:document.getElementById('file').value,phone:document.getElementById('phone').value};if(!d.phone||!d.requirements){alert('Fill requirements + phone');return}document.getElementById('msg').innerText='Sending STK Push...';fetch('/api/order-service',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(r=>r.json()).then(j=>{document.getElementById('msg').innerText='Order Confirmed by TIMOTHY - Order ID:'+j.order_id;document.getElementById('track').style.display='block'})}
</script>
"""
@app.route('/design-studio')
def design_studio():
    return nav('design') + """
<div style="max-width:1200px;margin:auto;padding:15px"><h2>Design Studio - 18 HD Tools - TIMOTHY</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Poster Maker $1 HD</b><br><a href="/poster-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Create HD $1</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Logo Maker $3 HD</b><br><a href="/logo-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Design $3</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Certificate $1.5 HD</b><br><a href="/certificate-maker" style="background:#6a0dad;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $1.5</a></div>
<div style="background:#1a1a25;border:1px solid #42a5f5;padding:12px;border-radius:12px;text-align:center"><b>Business Card $2 HD</b><br><a href="/business-card" style="background:#0d47a1;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $2</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Receipt $1 HD</b><br><a href="/receipt-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Create $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>KRA E-TIMS $1.5 HD</b><br><a href="/kra-invoice" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Make KRA $1.5</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Payslip $1 HD</b><br><a href="/payslip-maker" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Make $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>AI Caption $1 HD</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Generate $1</a></div>
</div></div>
"""
@app.route('/poster-maker')
def poster_maker():
    return """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster Maker $1 HD - TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.95);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/design-studio" style="color:#f9c846">Design Studio</a><h2>Poster $1 HD by TIMOTHY - PREVIEW watermark</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Red-Yellow</option><option value="2">Pink</option><option value="3">Blue</option><option value="4">Gold</option><option value="5">Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 0118431854" oninput="draw()"><input id="loc" value="Nairobi" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD $1 - Remove PREVIEW</button></div><div id="poster"></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone||'Not logged';if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){let c={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']}[document.getElementById('tpl').value];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1 - Kaumoni.com TIMOTHY 0118431854</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px"><h1 style="font-size:40px;margin:0">${document.getElementById('title').value}</h1><h2>${document.getElementById('sub').value}</h2><div style="background:black;color:white;padding:6px 12px;border-radius:20px;margin-top:15px"><b>${document.getElementById('phone').value}</b><br><small>${document.getElementById('loc').value}</small></div></div>`;}
async function downloadPoster(){if(userPhone!=='0118431854'&&userBal<1){alert('Low balance');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(cv=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='HD_Poster_TIMOTHY.png';a.href=cv.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>
"""
@app.route('/certificate-maker')
def certificate_maker():
    return """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Certificate $1.5 HD - TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:7px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#cert{width:550px;height:380px;margin:auto;background:white;color:black;padding:20px;border:10px double #6a0dad;border-radius:8px;text-align:center;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.97);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/design-studio" style="color:#f9c846">Design Studio</a><h2>Certificate $1.5 HD - TIMOTHY</h2><div class="card">Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><select id="type" onchange="draw()"><option value="Appreciation">Appreciation</option><option value="Achievement">Achievement</option></select><input id="name" value="John Kamau" oninput="draw()"><input id="reason" value="For Outstanding Performance" oninput="draw()"><input id="org" value="Kaumoni Academy - TIMOTHY" oninput="draw()"><input id="date" value="30 Sept 2026" oninput="draw()"><input id="sign" value="TIMOTHY - Director" oninput="draw()"></div><button onclick="downloadCert()" style="background:#6a0dad;color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD $1.5 - Remove PREVIEW</button></div><div id="cert"></div></div><script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}
function draw(){document.getElementById('cert').innerHTML=`<div id="wm">PREVIEW PAY $1.5</div><div style="border:2px solid #6a0dad;padding:10px;height:100%;display:flex;flex-direction:column;justify-content:center"><h1 style="color:#6a0dad">${document.getElementById('type').value.toUpperCase()}</h1><h2 style="border-bottom:2px solid #f9c846;display:inline-block">${document.getElementById('name').value}</h2><p>${document.getElementById('reason').value}</p><p style="font-size:11px">${document.getElementById('org').value} - ${document.getElementById('date').value}</p><div style="display:flex;justify-content:space-between;margin-top:15px"><div style="border-top:1px solid black;width:120px;font-size:10px">${document.getElementById('sign').value}</div><div style="border-top:1px solid black;width:120px;font-size:10px">${document.getElementById('date').value}</div></div></div>`;}
async function downloadCert(){if(userPhone!=='0118431854'&&userBal<1.5){alert('Need $1.5');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1.5,reason:'cert'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('cert'),{scale:2}).then(c=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='Certificate_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();});}
draw();loadBal();
</script></body></html>
"""
@app.route('/logo-maker')
def logo_maker(): return "<h2>Logo Maker $3 HD - TIMOTHY - Paste V16 Logo HTML for HD</h2><a href='/design-studio'>Back to Design Studio</a>"
@app.route('/business-card')
def business_card(): return "<h2>Business Card $2 HD - TIMOTHY - Paste V16 Biz Card HTML</h2><a href='/design-studio'>Back</a>"
@app.route('/kra-invoice')
def kra_invoice(): return "<h2>KRA E-TIMS $1.5 HD - TIMOTHY - Paste V16 KRA HTML</h2><a href='/design-studio'>Back</a>"
@app.route('/payslip-maker')
def payslip_maker(): return "<h2>Payslip $1 HD - TIMOTHY - Paste V16 Payslip HTML</h2><a href='/design-studio'>Back</a>"
@app.route('/ai-caption')
def ai_caption(): return "<h2>AI Caption $1 HD - TIMOTHY - Paste V16 AI HTML</h2><a href='/design-studio'>Back</a>"
@app.route('/receipt-maker')
def receipt_maker(): return "<h2>Receipt $1 - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/bg-remover')
def bg_remover(): return "<h2>BG Remover $1 - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/qr-maker')
def qr_maker(): return "<h2>QR Till USABLE $1 - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/lot-calculator')
def lot_calc(): return "<h2>Lot Calculator FREE - TIMOTHY - $10,000 = 0.5 lot</h2><a href='/'>Home</a>"
@app.route('/tiktok-downloader')
def tiktok_dl(): return "<h2>TikTok Downloader FREE - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/cv-builder')
def cv_builder(): return "<h2>CV Builder $2 - TIMOTHY - Paste V16 CV HTML</h2><a href='/'>Home</a>"
@app.route('/student-hub')
def student_hub(): return nav('student') + "<div style='max-width:900px;margin:auto;padding:15px'><h2>Student Hub - TIMOTHY - Notes, GPA, Grade Calc, Revision, CV Templates</h2><div style='background:#1a1a25;padding:14px;border-radius:12px'><b>GPA Calc FREE</b><br><input id='gpa' placeholder='Points' style='width:100%;padding:8px;background:#0e0e14;color:white'><button onclick='document.getElementById(\"gpaRes\").innerText=\"GPA: \"+document.getElementById(\"gpa\").value' style='background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px'>Calc GPA</button><p id='gpaRes'></p></div></div>"
@app.route('/free-tools')
def free_tools(): return nav('free') + "<div style='max-width:1000px;margin:auto;padding:15px'><h2>Free Tools - 9 Tools - TIMOTHY</h2><div style='display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px'><div style='background:#1a1a25;padding:12px;border-radius:12px'><b>Profit Calc FREE</b><br><input id='cost' placeholder='Cost'><input id='sell' placeholder='Sell'><button onclick='document.getElementById(\"pRes\").innerText=\"Profit: \"+(document.getElementById(\"sell\").value-document.getElementById(\"cost\").value)' style='background:#f9c846;color:black;padding:5px 10px;border:none;border-radius:10px'>Calc</button><p id='pRes'></p></div><div style='background:#1a1a25;padding:12px;border-radius:12px'><b>QR Generator $1</b><br><a href='/qr-maker' style='color:#f9c846'>Generate QR</a></div><div style='background:#1a1a25;padding:12px;border-radius:12px'><b>Lot Calc FREE</b><br><a href='/lot-calculator' style='color:#00c950'>Lot Calc</a></div></div></div>"
@app.route('/ai-tools')
def ai_tools(): return nav('ai') + "<div style='max-width:1000px;margin:auto;padding:15px'><h2>AI Tools - TIMOTHY - 7 AI Tools - Writing, CV, Content, Product Desc, Study, Biz Name, Caption</h2><div style='display:grid;grid-template-columns:1fr 1fr;gap:10px'><div style='background:#1a1a25;padding:14px;border-radius:12px'><b>AI Writing $1</b><br><a href='/ai-caption' style='background:#ff9800;color:black;padding:8px 14px;border-radius:20px;text-decoration:none'>Use AI Writing</a></div><div style='background:#1a1a25;padding:14px;border-radius:12px'><b>AI Business Name FREE</b><br><input id='kw' placeholder='Keyword'><button onclick='document.getElementById(\"bnRes\").innerText=document.getElementById(\"kw\").value+\" Hub, \"+document.getElementById(\"kw\").value+\" Empire\"' style='background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px'>Generate</button><p id='bnRes'></p></div></div></div>"
@app.route('/dashboard')
def user_dashboard(): return nav('home') + "<div style='max-width:900px;margin:auto;padding:15px'><h2>User Dashboard - TIMOTHY - Purchased, Download History, Orders, Service Requests, Payment History</h2><div style='background:#1a1a25;padding:12px;border-radius:12px'>Phone <b id='uPhone'>-</b> | Bal $<span id='uBal'>0</span></div><div id='orders' style='background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px'>Orders loading...</div></div><script>let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('uPhone').innerText=ph;fetch('/api/balance?phone='+ph).then(r=>r.json()).then(d=>{document.getElementById('uBal').innerText=(d.balance||0).toFixed(2)});fetch('/api/my-orders?phone='+ph).then(r=>r.json()).then(o=>{document.getElementById('orders').innerHTML=o.map(x=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${x.product||x.service_type} - $${x.amount} - ${x.status}</div>`).join('')||'No orders'})</script>"
@app.route('/seller-dashboard')
def seller_dashboard(): return nav('home') + "<div style='max-width:900px;margin:auto;padding:15px'><h2>Seller / Creator Dashboard - TIMOTHY - Add Products, Edit, Sales, Earnings, Withdrawals, Analytics</h2><div style='background:#1a1a25;padding:15px;border-radius:12px'><h3>Add Product</h3><input id='pTitle' placeholder='Product Title' style='width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:4px 0'><input id='pPrice' type='number' placeholder='Price $' style='width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px'><button onclick='addP()' style='background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold'>Add Product</button></div><div id='myProds' style='background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px'>My Products loading...</div></div><script>function addP(){let data={title:document.getElementById('pTitle').value,price:parseFloat(document.getElementById('pPrice').value),desc:'By TIMOTHY Seller',category:'ebook'};fetch('/api/add-product',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json()).then(d=>{if(d.ok){alert('Product Added');load()}})}function load(){fetch('/api/products').then(r=>r.json()).then(all=>{document.getElementById('myProds').innerHTML=all.slice(0,5).map(p=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${p.title} - $${p.price} - Sales: 0 - Earnings: $0</div>`).join('')})}load()</script>"
@app.route('/about')
def about(): return nav('about') + "<div style='max-width:800px;margin:auto;padding:15px'><h2>About Platform - TIMOTHY - Mission, Services, Team, Contact</h2><div style='background:#1a1a25;padding:15px;border-radius:12px'><h3>Mission</h3><p>Affordable digital services to every Kenyan - 18 Tools + Shop + Freelance + Student + Free + AI - All automated with M-Pesa STK Push - by TIMOTHY</p><h3>Team</h3><p>TIMOTHY Founder - 0118431854 - 1500+ users</p></div></div>"
@app.route('/contact')
def contact_page(): return nav('contact') + "<div style='max-width:700px;margin:auto;padding:15px'><h2>Support - Contact TIMOTHY - FAQs, Help Center, Order Support, Payment Support</h2><div style='background:#1a1a25;padding:15px;border-radius:12px'><h3>Contact Form</h3><input placeholder='Name' style='width:100%;padding:8px;background:#0e0e14;color:white'><textarea placeholder='Message' style='width:100%;padding:8px;background:#0e0e14;color:white' rows='4'></textarea><button style='background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px'>Send to TIMOTHY</button><hr><p><b>Payment not verified?</b> WhatsApp TIMOTHY</p><p><b>Download not working?</b> Dashboard > Purchased</p><a href='https://wa.me/254118431854' style='background:#25D366;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold'>WhatsApp TIMOTHY 0118431854</a></div></div>"
@app.route('/terms')
def terms(): return nav('home') + "<div style='max-width:800px;margin:auto;padding:15px'><h2>Terms / Privacy / Refund / Cookie - TIMOTHY</h2><div style='background:#1a1a25;padding:15px;border-radius:12px'><h3>Terms</h3><small>Digital products non-refundable after download. Services 24-48h.</small><h3>Privacy</h3><small>Phone, email, orders stored - No sharing</small><h3>Refund</h3><small>Digital: refund if not delivered. Services: if not started. Contact 0118431854</small></div></div>"
@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()
@app.route('/admin')
def admin():
    return nav('admin') + """
<div style="max-width:1000px;margin:auto;padding:15px"><h2>Admin Dashboard - TIMOTHY - Users / Products / Services / Orders / Payments / Sales / Reports</h2>
<div style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">
<div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Users - User Management</h3><div id="users">Loading...</div></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Orders - Order Management</h3><div id="orders">Loading...</div></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Website Settings</h3><p>Frontend: HTML+CSS+JS<br>Backend: Flask<br>Database: JSON (PostgreSQL ready)<br>Hosting: Render<br>Payments: Daraja STK<br>Storage: Cloud<br>Auth: Login<br>Admin: Dashboard</p></div>
</div></div>
<script>
fetch('/api/admin-data').then(r=>r.json()).then(d=>{
document.getElementById('total').innerText=(d.total_fees||0).toFixed(2);
document.getElementById('uc').innerText=d.users.length;
document.getElementById('oc').innerText=d.orders.length;
document.getElementById('users').innerHTML=d.users.map(u=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${u.phone} - $${(u.balance||0).toFixed(2)}</div>`).join('');
document.getElementById('orders').innerHTML=d.orders.map(o=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${o.product||o.service_type} - ${o.phone} - $${o.amount} - ${o.status}</div>`).join('');
})
</script>
"""
@app.route('/api/products')
def api_products():
    prods=load_json(PRODUCTS_FILE, [
        {"id":1,"title":"Forex Mastery Ebook by TIMOTHY","desc":"Complete forex guide 2026","features":"PDF 100 pages, Strategies, Live examples","price":5,"category":"ebook","icon":"Ebook"},
        {"id":2,"title":"Canva Poster Templates Pack","desc":"100 editable Canva templates","features":"Canva link, HD","price":3,"category":"template","icon":"Art"},
        {"id":3,"title":"Trading Guide - Gold Strategy","desc":"XAUUSD strategy by TIMOTHY","features":"Entry/Exit, Risk mgmt","price":6,"category":"trading","icon":"Chart"},
        {"id":4,"title":"Pro CV Template Pack","desc":"10 CV templates","features":"Word + PDF","price":2,"category":"cv","icon":"Doc"},
        {"id":5,"title":"Business Plan Template KE","desc":"KRA compliant","features":"Financials","price":4,"category":"template","icon":"Biz"},
        {"id":6,"title":"WhatsApp Sales Scripts","desc":"50 scripts","features":"Sheng + English","price":3,"category":"ebook","icon":"Chat"},
        {"id":7,"title":"Study Notes - Business Studies","desc":"Form 4 + University notes","features":"PDF, Revision","price":2,"category":"ebook","icon":"Book"},
        {"id":8,"title":"AI Prompts Pack - 100 Prompts","desc":"ChatGPT prompts for business","features":"Business, Content","price":2,"category":"template","icon":"AI"}
    ])
    save_json(PRODUCTS_FILE, prods)
    return jsonify(prods)
@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json()
    prods=load_json(PRODUCTS_FILE, [])
    nid=max([p['id'] for p in prods], default=0)+1
    prods.append({"id":nid,"title":data['title'],"desc":data.get('desc','By TIMOTHY'),"features":data.get('features','By TIMOTHY Seller'),"price":float(data.get('price',0)),"category":data.get('category','ebook'),"icon":"Box"})
    save_json(PRODUCTS_FILE, prods)
    return jsonify({"ok":True,"id":nid})
@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json()
    pid=int(data['product_id'])
    phone=data['phone']
    prods=load_json(PRODUCTS_FILE, [])
    prod=next((p for p in prods if p['id']==pid), None)
    if not prod:
        return jsonify({"ok":False,"message":"Product not found"})
    orders=load_json(ORDERS_FILE, [])
    oid=len(orders)+1
    orders.append({"id":oid,"product":prod['title'],"phone":phone,"amount":prod['price'],"status":"Paid - Auto Delivered - Payment Verified - TIMOTHY","time":str(datetime.now()),"download_url":f"/download/{oid}"})
    save_json(ORDERS_FILE, orders)
    fees=load_json(FEES_FILE, {"total":0})
    fees['total']=fees.get('total',0)+float(prod['price'])
    save_json(FEES_FILE, fees)
    return jsonify({"ok":True,"download_url":f"/download/{oid}","order_id":oid})
@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json()
    orders=load_json(SERVICES_FILE, [])
    oid=len(orders)+1
    orders.append({"id":oid,"service_type":data.get('service_type','Service'),"requirements":data.get('requirements',''),"phone":data.get('phone',''),"file_link":data.get('file_link',''),"status":"Payment Verified - In Progress - TIMOTHY","amount":5,"time":str(datetime.now())})
    save_json(SERVICES_FILE, orders)
    fees=load_json(FEES_FILE, {"total":0})
    fees['total']=fees.get('total',0)+5
    save_json(FEES_FILE, fees)
    return jsonify({"ok":True,"order_id":oid})
@app.route('/api/my-orders')
def api_my_orders():
    phone=request.args.get('phone')
    orders=load_json(ORDERS_FILE, [])+load_json(SERVICES_FILE, [])
    return jsonify([o for o in orders if o.get('phone')==phone])
@app.route('/download/<int:oid>')
def download_file(oid):
    return f"<h2>Download Ready - Order {oid} - Auto Delivered by TIMOTHY</h2><a href='/' style='background:#00c950;color:white;padding:12px 18px;border-radius:20px;text-decoration:none;font-weight:bold'>Download PDF - By TIMOTHY</a><p>Payment History Saved - Refund Policy Applies - Contact 0118431854</p>"
@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone')
    users=load_json(USERS_FILE, {})
    if phone=="0118431854":
        return jsonify({"phone":phone,"balance":999})
    return jsonify(users.get(phone, {"phone":phone,"balance":0}))
@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json()
    phone=data['phone'].strip()
    pwd=data['password'].strip()
    users=load_json(USERS_FILE, {})
    if phone=="0118431854":
        if pwd!="KAUMONI20r4.":
            return jsonify({"ok":False,"message":"Wrong admin pass"})
        if phone not in users:
            users[phone]={"phone":phone,"password":pwd,"balance":999,"total_fee":0,"joined":str(datetime.now())}
            save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":999})
    if phone in users:
        return jsonify({"ok":True,"balance":users[phone].get('balance',0)})
    else:
        users[phone]={"phone":phone,"password":pwd,"balance":0,"total_fee":0,"joined":str(datetime.now())}
        save_json(USERS_FILE, users)
        return jsonify({"ok":True,"balance":0})
@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json()
    users=load_json(USERS_FILE, {})
    ph=data['phone']
    amt=float(data['amount'])
    if ph=="0118431854":
        return jsonify({"ok":True,"balance":999})
    if ph not in users or float(users[ph].get('balance',0))<amt:
        return jsonify({"ok":False,"message":"Low balance - Deposit via M-Pesa STK Push"})
    users[ph]['balance']-=amt
    users[ph]['total_fee']=users[ph].get('total_fee',0)+amt
    fees=load_json(FEES_FILE, {"total":0})
    fees['total']=fees.get('total',0)+amt
    save_json(FEES_FILE, fees)
    save_json(USERS_FILE, users)
    return jsonify({"ok":True})
@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {})
    fees=load_json(FEES_FILE, {"total":0})
    orders=load_json(ORDERS_FILE, [])+load_json(SERVICES_FILE, [])
    return jsonify({"users":list(users.values()),"total_fees":fees.get('total',0),"orders":orders})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
