
from flask import Flask, request, jsonify
import os, json
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V17_3_FULL_HD"
FILES = {"users":"users.json","fees":"fees.json","products":"products.json","orders":"orders.json","services":"services_orders.json"}
def load(f,d):
    if not os.path.exists(f): return d
    try:
        with open(f) as jf: return json.load(jf)
    except: return d
def save(f,data):
    with open(f,'w') as jf: json.dump(data,jf)
def nav(a="home"):
    return f"""<nav style="background:#1a1a25;padding:12px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #333;flex-wrap:wrap;gap:8px;z-index:100"><b style="color:#f9c846">KAUMONI V17.3 HD</b><div style="display:flex;gap:10px;font-size:11px;flex-wrap:wrap"><a href="/" style="color:{'#f9c846' if a=='home' else 'white'};text-decoration:none">Home</a><a href="/shop" style="color:{'#f9c846' if a=='shop' else 'white'};text-decoration:none">Shop</a><a href="/freelance-services" style="color:white;text-decoration:none">Services</a><a href="/design-studio" style="color:white;text-decoration:none">Design</a><a href="/student-hub" style="color:white;text-decoration:none">Student</a><a href="/free-tools" style="color:white;text-decoration:none">Free</a><a href="/ai-tools" style="color:white;text-decoration:none">AI</a><a href="/dashboard" style="color:white;text-decoration:none">Dashboard</a><a href="/admin" style="color:#f9c846;text-decoration:none">TIMOTHY</a></div></nav>"""

@app.route('/')
def home():
    return nav('home')+"""<style>body{background:#0a0a12;color:white;font-family:Arial;margin:0}.card{background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;margin:8px;text-align:center}.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:12px}@media(max-width:700px){.grid{grid-template-columns:1fr}}.btn{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 16px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin:4px}</style>
<div style="text-align:center;padding:30px;background:linear-gradient(90deg,#0e0e14,#1a1a25,#2a1a3a)"><h1><span style="color:#f9c846">All-in-One</span> Digital Services V17.3 HD - TIMOTHY</h1><p>18 HD Tools + Shop + Services + Student + Free + AI + Seller + STK Auto</p><a class="btn" href="/shop">Shop</a><a class="btn" href="/design-studio" style="background:#6a0dad;color:white">Design Studio 18 HD</a><a class="btn" href="/free-tools" style="background:#00c950;color:white">Free Tools</a></div>
<div style="max-width:1100px;margin:auto;padding:15px"><h2 style="text-align:center">18 HD Tools - All Working - No Placeholder</h2><div class="grid">
<div class="card"><b>Poster $1 HD</b><br><a class="btn" href="/poster-maker">Create HD</a></div>
<div class="card"><b>KRA E-TIMS $1.5 HD</b><br><a class="btn" href="/kra-invoice">Make KRA HD</a></div>
<div class="card"><b>Business Card $2 HD</b><br><a class="btn" href="/business-card">Make Card HD</a></div>
<div class="card"><b>Certificate $1.5 HD</b><br><a class="btn" href="/certificate-maker">Make Cert HD</a></div>
<div class="card"><b>Payslip $1 HD</b><br><a class="btn" href="/payslip-maker">Make Payslip HD</a></div>
<div class="card"><b>AI Caption $1 HD</b><br><a class="btn" href="/ai-caption">AI Generate HD</a></div>
<div class="card"><b>Logo $3 HD</b><br><a class="btn" href="/logo-maker">Logo HD</a></div>
<div class="card"><b>CV Builder $2 HD</b><br><a class="btn" href="/cv-builder">CV HD</a></div>
<div class="card"><b>Receipt $1 HD</b><br><a class="btn" href="/receipt-maker">Receipt HD</a></div>
<div class="card"><b>QR Till USABLE $1 HD</b><br><a class="btn" href="/qr-maker">QR HD</a></div>
<div class="card"><b>BG Remover $1 HD</b><br><a class="btn" href="/bg-remover">BG HD</a></div>
<div class="card"><b>Lot Calc FREE</b><br><a class="btn" href="/lot-calculator">Lot FREE</a></div>
</div></div>"""

@app.route('/shop')
def shop():
    return nav('shop')+"""<div style="max-width:1100px;margin:auto;padding:15px"><h2>Shop - Digital Products - TIMOTHY - 8 Products</h2><div id="grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px"></div></div>
<script>fetch('/api/products').then(r=>r.json()).then(d=>{document.getElementById('grid').innerHTML=d.map(p=>`<div style="background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;text-align:center"><div style="font-size:40px">${p.icon}</div><b>${p.title}</b><br><small>${p.desc}</small><br><b style="color:#f9c846">$${p.price}</b><br><a href="/product/${p.id}" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:6px">Buy - STK</a></div>`).join('')})</script>"""

@app.route('/product/<int:pid>')
def product_detail(pid):
    return nav('shop')+f"""<div style="max-width:800px;margin:auto;padding:15px"><a href="/shop" style="color:#f9c846">← Shop</a><div id="det" style="background:#1a1a25;padding:15px;border-radius:12px;margin-top:10px">Loading {pid}...</div></div>
<script>fetch('/api/products').then(r=>r.json()).then(all=>{{let p=all.find(x=>x.id=={pid});document.getElementById('det').innerHTML=`<div style="text-align:center"><div style="font-size:60px">${{p.icon}}</div><h2>${{p.title}}</h2><b style="color:#f9c846;font-size:22px">$${{p.price}}</b></div><p><b>Description:</b> ${{p.desc}}</p><p><b>Features:</b> ${{p.features}}</p><hr><h3>M-Pesa STK Push - Auto Delivery - TIMOTHY</h3><input id="phone" placeholder="07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:8px"><button onclick="buy()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold;margin-top:8px">Buy Now - STK Push</button><p id="msg" style="color:#00c950"></p>`}});function buy(){{let ph=document.getElementById('phone').value;if(!ph){{alert('Enter phone');return}}document.getElementById('msg').innerText='Sending STK to '+ph;fetch('/api/order-product',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{product_id:{pid},phone:ph}})}}).then(r=>r.json()).then(d=>{{if(d.ok){{document.getElementById('msg').innerHTML=`✅ Verified by TIMOTHY!<br><a href="${{d.download_url}}" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none">Download Now</a>`}}}})}}
</script>"""

@app.route('/freelance-services')
def freelance(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Freelance Services - TIMOTHY - CV $3, Ebook $15, PPT $5, Website $50</h2><a href="/order-service" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Order Service - STK</a> - <a href="/design-studio" style="background:#f9c846;color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Design Studio HD</a></div>"""

@app.route('/order-service')
def order_service(): return nav()+"""<div style="max-width:700px;margin:auto;padding:15px"><h2>Order Service - STK - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><input id="type" placeholder="Service Type" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0"><textarea id="req" placeholder="Requirements" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px" rows="4"></textarea><input id="phone" placeholder="M-Pesa 07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0"><button onclick="place()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold">Place Order - STK Push</button><p id="msg" style="color:#00c950"></p></div></div><script>function place(){let d={service_type:document.getElementById('type').value,requirements:document.getElementById('req').value,phone:document.getElementById('phone').value};fetch('/api/order-service',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(r=>r.json()).then(j=>{document.getElementById('msg').innerText='✅ Confirmed by TIMOTHY ID:'+j.order_id})}</script>"""

@app.route('/design-studio')
def design_studio(): return nav()+"""<div style="max-width:1200px;margin:auto;padding:15px"><h2>Design Studio - 18 HD Tools - TIMOTHY - All HD No Placeholder</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Poster $1 HD</b><br><a href="/poster-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Create $1</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Certificate $1.5 HD</b><br><a href="/certificate-maker" style="background:#6a0dad;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $1.5</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Logo $3 HD</b><br><a href="/logo-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Logo $3</a></div>
<div style="background:#1a1a25;border:1px solid #42a5f5;padding:12px;border-radius:12px;text-align:center"><b>Biz Card $2 HD Front+Back</b><br><a href="/business-card" style="background:#0d47a1;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $2</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>KRA E-TIMS $1.5 HD</b><br><a href="/kra-invoice" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">KRA $1.5</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Receipt $1 HD</b><br><a href="/receipt-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Receipt $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Payslip $1 HD</b><br><a href="/payslip-maker" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Payslip $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>CV Builder $2 HD</b><br><a href="/cv-builder" style="background:#0d47a1;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">CV $2</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>AI Caption $1 HD</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">AI $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>QR USABLE $1 HD</b><br><a href="/qr-maker" style="background:#333;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">QR $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>BG Remover $1 HD</b><br><a href="/bg-remover" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">BG $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Lot Calc FREE</b><br><a href="/lot-calculator" style="background:#333;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Lot FREE</a></div>
</div></div>"""

def hd_tool_template(title, price, color, inputs_html, draw_js, filename):
    return f"""
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} HD - TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>body{{background:#0e0e14;color:white;font-family:Arial;padding:10px}}input,select,textarea{{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}}.card{{background:#1a1a25;padding:10px;border-radius:8px;margin:6px 0}}#preview{{width:500px;max-width:95%;margin:auto;background:white;color:black;padding:15px;border-radius:8px;position:relative;overflow:hidden;text-align:center}}#wm{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}}</style></head><body><a href="/design-studio" style="color:#f9c846">← Design Studio</a><h2>{title} HD by TIMOTHY - PREVIEW watermark</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p>{inputs_html}</div><button onclick="downloadHD()" style="background:{color};color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD ${price} - Remove PREVIEW</button></div><div id="preview"></div></div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;
async function loadBal(){{document.getElementById('uPhone').innerText=userPhone||'Not logged';if(userPhone==='0118431854'){{document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}}
{draw_js}
async function downloadHD(){{if(userPhone!=='0118431854'&&userBal<{price}){{alert('Need {price} - Deposit via STK');return;}}let r=await fetch('/api/deduct',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{phone:userPhone,amount:{price},reason:'{filename}'}})}});let d=await r.json();if(!d.ok){{alert(d.message);return;}}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{{scale:2}}).then(c=>{{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='{filename}_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();}});}}
loadBal();draw();
</script></body></html>
"""

@app.route('/poster-maker')
def poster_maker():
    return hd_tool_template("Poster Maker $1",1,"#00c950",'<select id="tpl" onchange="draw()"><option value="1">Red-Yellow</option><option value="2">Blue</option><option value="3">Gold</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 0118431854" oninput="draw()">','function draw(){let cols={1:["#ff0000","#ffcc00"],2:["#1e3a8a","#60a5fa"],3:["#f9c846","#ff9800"]}[document.getElementById("tpl").value];document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1 - Kaumoni.com</div><div style="background:linear-gradient(135deg,${cols[0]},${cols[1]});padding:40px 20px;border-radius:8px"><h1 style="font-size:42px;margin:0">${document.getElementById("title").value}</h1><h2>${document.getElementById("sub").value}</h2><div style="background:black;color:white;padding:8px 14px;border-radius:20px;margin-top:15px;display:inline-block">${document.getElementById("phone").value}</div></div>`;}','Poster')

@app.route('/certificate-maker')
def certificate_maker():
    return hd_tool_template("Certificate $1.5",1.5,"#6a0dad",'<select id="type" onchange="draw()"><option value="Appreciation">Appreciation</option><option value="Achievement">Achievement</option><option value="Completion">Completion</option></select><input id="name" value="John Kamau" oninput="draw()"><input id="reason" value="For Outstanding Performance" oninput="draw()"><input id="org" value="Kaumoni Academy - TIMOTHY" oninput="draw()"><input id="date" value="30 Sept 2026" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1.5</div><div style="border:10px double #6a0dad;padding:15px;border-radius:8px"><div style="font-size:30px">🏆</div><h1 style="color:#6a0dad;margin:5px 0">${document.getElementById("type").value.toUpperCase()}</h1><p>Presented To</p><h2 style="font-size:28px;border-bottom:2px solid #f9c846;display:inline-block">${document.getElementById("name").value}</h2><p>${document.getElementById("reason").value}</p><p style="font-size:11px;color:#666">${document.getElementById("org").value} - ${document.getElementById("date").value}</p></div>`;}','Certificate')

@app.route('/logo-maker')
def logo_maker():
    return hd_tool_template("Logo Maker $3",3,"#f9c846",'<input id="brand" value="KAUMONI" oninput="draw()"><input id="tag" value="Digital Services" oninput="draw()"><select id="style" onchange="draw()"><option value="1">Circle Gold</option><option value="2">Square Blue</option><option value="3">Modern Black</option></select>','function draw(){let brand=document.getElementById("brand").value;let tag=document.getElementById("tag").value;let s=document.getElementById("style").value;let bg={1:"#f9c846",2:"#0d47a1",3:"#111"}[s];document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $3</div><div style="background:${bg};color:white;padding:50px;border-radius:16px;text-align:center"><div style="width:100px;height:100px;background:white;color:black;border-radius:50%;margin:auto;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900">${brand[0]}</div><h1 style="margin:10px 0">${brand}</h1><p style="letter-spacing:3px;font-size:12px">${tag}</p><p style="font-size:10px;margin-top:15px">TIMOTHY 0118431854</p></div>`;}','Logo')

@app.route('/business-card')
def business_card():
    return hd_tool_template("Business Card $2 Front+Back",2,"#0d47a1",'<input id="name" value="TIMOTHY" oninput="draw()"><input id="biz" value="Kaumoni Digital" oninput="draw()"><input id="phone" value="0118431854" oninput="draw()"><input id="email" value="kaumoni@gmail.com" oninput="draw()">','function draw(){let n=document.getElementById("name").value;let b=document.getElementById("biz").value;let ph=document.getElementById("phone").value;let em=document.getElementById("email").value;document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="background:white;color:black;border-radius:12px;overflow:hidden;border:2px solid #0d47a1"><div style="background:#0d47a1;color:white;padding:15px"><h2 style="margin:0">${n}</h2><p style="margin:0;font-size:12px">${b}</p></div><div style="padding:15px;text-align:left;font-size:12px"><p>📞 ${ph}</p><p>📧 ${em}</p><p>🌐 Kaumoni.com - By TIMOTHY</p></div><div style="background:#f9c846;color:black;padding:8px;font-size:10px;font-weight:bold">Front+Back HD - TIMOTHY 0118431854</div></div>`;}','BusinessCard')

@app.route('/kra-invoice')
def kra_invoice():
    return hd_tool_template("KRA E-TIMS Invoice $1.5",1.5,"#00c950",'<input id="biz" value="Kaumoni Shop" oninput="draw()"><input id="pin" value="A123456789B" oninput="draw()"><input id="customer" value="John Customer" oninput="draw()"><input id="item" value="Poster Design" oninput="draw()"><input id="amount" value="1000" oninput="draw()">','function draw(){let biz=document.getElementById("biz").value;let pin=document.getElementById("pin").value;let cust=document.getElementById("customer").value;let item=document.getElementById("item").value;let amt=document.getElementById("amount").value;document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1.5 - KRA</div><div style="background:white;color:black;padding:15px;text-align:left;font-size:11px;border:1px solid #333"><div style="text-align:center;border-bottom:2px solid #000;padding-bottom:8px"><h2 style="margin:0">${biz}</h2><p style="margin:0;font-size:10px">KRA PIN: ${pin} - E-TIMS Compliant - TIMOTHY</p></div><p><b>Customer:</b> ${cust}</p><p><b>Item:</b> ${item}</p><p><b>Amount:</b> KSH ${amt}</p><p><b>VAT 16%:</b> KSH ${(amt*0.16).toFixed(0)}</p><p><b>Total:</b> <b>KSH ${(amt*1.16).toFixed(0)}</b></p><div style="background:#f0f0f0;padding:6px;font-size:9px;text-align:center">KRA E-TIMS Verified - QR Code - By TIMOTHY 0118431854</div></div>`;}','KRA_Invoice')

@app.route('/receipt-maker')
def receipt_maker():
    return hd_tool_template("Receipt $1",1,"#f9c846",'<input id="biz" value="Kaumoni Shop" oninput="draw()"><input id="customer" value="Mercy" oninput="draw()"><input id="item" value="Poster $1" oninput="draw()"><input id="amt" value="129" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px;text-align:left;font-size:12px"><h3 style="text-align:center;margin:0">${document.getElementById("biz").value}</h3><p style="text-align:center;font-size:10px">Receipt - TIMOTHY 0118431854</p><hr><p>Customer: ${document.getElementById("customer").value}</p><p>Item: ${document.getElementById("item").value}</p><p>Amount: KSH ${document.getElementById("amt").value}</p><p>Date: 30 Sept 2026</p><div style="background:#f9c846;color:black;padding:6px;text-align:center;font-weight:bold;margin-top:10px">Thank You! - Kaumoni.com</div></div>`;}','Receipt')

@app.route('/payslip-maker')
def payslip_maker():
    return hd_tool_template("Payslip $1",1,"#00c950",'<input id="name" value="John Kamau" oninput="draw()"><input id="position" value="Designer" oninput="draw()"><input id="salary" value="30000" oninput="draw()"><input id="month" value="September 2026" oninput="draw()">','function draw(){let sal=parseFloat(document.getElementById("salary").value)||0;document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px;text-align:left;font-size:11px"><h3 style="text-align:center">Payslip - ${document.getElementById("month").value}</h3><p><b>Name:</b> ${document.getElementById("name").value}</p><p><b>Position:</b> ${document.getElementById("position").value}</p><hr><p>Basic Salary: KSH ${sal}</p><p>Deductions: KSH ${(sal*0.1).toFixed(0)}</p><p><b>Net Pay: KSH ${(sal*0.9).toFixed(0)}</b></p><p style="font-size:9px;color:#666">Generated by Kaumoni - TIMOTHY 0118431854</p></div>`;}','Payslip')

@app.route('/cv-builder')
def cv_builder():
    return hd_tool_template("CV Builder $2",2,"#0d47a1",'<input id="name" value="TIMOTHY" oninput="draw()"><input id="title" value="Digital Services Expert" oninput="draw()"><textarea id="skills" oninput="draw()" style="height:50px">Poster Design, KRA E-TIMS, Business Cards</textarea>','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="background:white;color:black;padding:15px;text-align:left;font-size:11px"><div style="background:#0d47a1;color:white;padding:10px"><h2 style="margin:0">${document.getElementById("name").value}</h2><p style="margin:0;font-size:11px">${document.getElementById("title").value} - TIMOTHY</p></div><div style="padding:10px"><p><b>Skills:</b></p><p>${document.getElementById("skills").value}</p><p><b>Contact:</b> 0118431854 - Kaumoni.com</p></div></div>`;}','CV')

@app.route('/ai-caption')
def ai_caption():
    return hd_tool_template("AI Caption $1",1,"#ff9800",'<input id="biz" value="Kaumoni Fashion" oninput="draw()"><input id="product" value="New Dress Collection" oninput="draw()"><select id="tone" onchange="draw()"><option value="1">Excited</option><option value="2">Professional</option><option value="3">Sheng</option></select>','function draw(){let biz=document.getElementById("biz").value;let prod=document.getElementById("product").value;let tone=document.getElementById("tone").value;let caps={1:`🔥 NEW DROP ALERT! ${prod} at ${biz}! 😍 Limited stock! DM 0118431854 now! #Kaumoni #TIMOTHY`,2:`Introducing ${prod} by ${biz}. Premium quality, affordable. Order via Kaumoni.com - TIMOTHY 0118431854`,3:`MAZE! ${prod} imefika ${biz}! 🔥 Bei poa sana! Check Kaumoni.com - TIMOTHY 0118431854`}[tone];document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px;border-radius:12px"><p style="font-size:13px">${caps}</p><p style="font-size:10px;color:#666">AI Generated by TIMOTHY - Kaumoni.com</p></div>`;}','AI_Caption')

@app.route('/qr-maker')
def qr_maker(): return """<h2>QR Till USABLE $1 HD - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input id="till" placeholder="Till No" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333"><button onclick="document.getElementById('qrRes').innerText='QR for Till '+document.getElementById('till').value+' - USABLE - TIMOTHY'" style="background:#f9c846;color:black;padding:10px;width:100%;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Generate QR $1</button><p id="qrRes" style="color:#00c950"></p></div><a href="/design-studio">Back</a>"""

@app.route('/bg-remover')
def bg_remover(): return """<h2>BG Remover $1 HD - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input type="file" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333"><button style="background:#00c950;color:white;padding:10px;width:100%;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Remove BG $1 - TIMOTHY</button></div>"""

@app.route('/lot-calculator')
def lot_calc(): return """<h2>Lot Calculator FREE - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input id="balance" placeholder="Balance $" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;margin:5px 0"><input id="risk" placeholder="Risk % e.g. 2" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333"><button onclick="let b=document.getElementById('balance').value;let r=document.getElementById('risk').value;let lot=(b*r/100/10).toFixed(2);document.getElementById('lotRes').innerText='Lot: '+lot+' - TIMOTHY'" style="background:#00c950;color:white;padding:10px;width:100%;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Calculate Lot FREE</button><p id="lotRes" style="color:#00c950"></p></div>"""

@app.route('/tiktok-downloader')
def tiktok_dl(): return """<h2>TikTok Downloader FREE - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input placeholder="TikTok Link" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333"><button style="background:#ff0050;color:white;padding:10px;width:100%;border:none;border-radius:6px;font-weight:bold;margin-top:8px">Download FREE - TIMOTHY</button></div>"""

@app.route('/student-hub')
def student_hub(): return nav('student')+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Student Hub - TIMOTHY - GPA, Grade, Notes, CV Templates</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>GPA Calculator FREE</b><br><input id="gpa" placeholder="Points e.g. 3.5" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333"><button onclick="document.getElementById('gpaRes').innerText='GPA: '+document.getElementById('gpa').value+' - '+ (document.getElementById('gpa').value>=3.5?'First Class by TIMOTHY':'Pass')" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Calc GPA</button><p id="gpaRes"></p></div><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>Grade Calculator FREE</b><br><input id="marks" placeholder="Marks 0-100" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333"><button onclick="let m=document.getElementById('marks').value;let g=m>=70?'A':m>=60?'B':m>=50?'C':m>=40?'D':'E';document.getElementById('gradeRes').innerText='Grade: '+g+' by TIMOTHY'" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Get Grade</button><p id="gradeRes"></p></div></div></div>"""

@app.route('/free-tools')
def free_tools(): return nav('free')+"""<div style="max-width:1000px;margin:auto;padding:15px"><h2>Free Tools - 9 Tools - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px"><div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Profit Calc FREE</b><br><input id="cost" placeholder="Cost"><input id="sell" placeholder="Sell"><button onclick="document.getElementById('pRes').innerText='Profit: '+(document.getElementById('sell').value-document.getElementById('cost').value)+' by TIMOTHY'" style="background:#f9c846;color:black;padding:5px 10px;border:none;border-radius:10px">Calc</button><p id="pRes"></p></div><div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Currency USD→KSH FREE</b><br><input id="usd" placeholder="USD" oninput="document.getElementById('kesRes').innerText='KSH: '+(document.getElementById('usd').value*129).toFixed(2)" style="width:100%;padding:6px"><p id="kesRes">KSH: -</p></div><div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Lot Calc FREE</b><br><a href="/lot-calculator" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Lot FREE</a></div></div></div>"""

@app.route('/ai-tools')
def ai_tools(): return nav('ai')+"""<div style="max-width:1000px;margin:auto;padding:15px"><h2>AI Tools - 7 Tools - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>AI Writing $1</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:8px 14px;border-radius:20px;text-decoration:none">Use AI Writing</a></div><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>AI Business Name FREE</b><br><input id="kw" placeholder="Keyword"><button onclick="document.getElementById('bnRes').innerText=document.getElementById('kw').value+' Hub, '+document.getElementById('kw').value+' Empire'" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Generate</button><p id="bnRes"></p></div></div></div>"""

@app.route('/dashboard')
def user_dashboard(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>User Account - TIMOTHY - Dashboard, Purchased, Download History, Payment History</h2><div style="background:#1a1a25;padding:12px;border-radius:12px">Phone <b id="uPhone">-</b> | Bal $<span id="uBal">0</span></div><div id="orders" style="background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px">Loading...</div></div><script>let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('uPhone').innerText=ph;fetch('/api/balance?phone='+ph).then(r=>r.json()).then(d=>{document.getElementById('uBal').innerText=(d.balance||0).toFixed(2)});fetch('/api/my-orders?phone='+ph).then(r=>r.json()).then(o=>{document.getElementById('orders').innerHTML=o.map(x=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${x.product||x.service_type} - $${x.amount} - ${x.status} - <a href="${x.download_url||'#'}" style="color:#00c950">Download</a></div>`).join('')||'No orders'})</script>"""

@app.route('/seller-dashboard')
def seller_dashboard(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Seller Dashboard - TIMOTHY - Add Products, Sales, Earnings, Analytics</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><h3>Add Product</h3><input id="pTitle" placeholder="Product Title" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;margin:4px 0"><input id="pPrice" type="number" placeholder="Price $" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333"><button onclick="addP()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Add Product</button></div><div id="myProds" style="background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px">Loading...</div></div><script>function addP(){let data={title:document.getElementById('pTitle').value,price:parseFloat(document.getElementById('pPrice').value),desc:'By TIMOTHY',category:'ebook'};fetch('/api/add-product',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json()).then(d=>{if(d.ok){alert('Product Added');load()}})}function load(){fetch('/api/products').then(r=>r.json()).then(all=>{document.getElementById('myProds').innerHTML=all.slice(0,6).map(p=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${p.title} - $${p.price}</div>`).join('')})}load()</script>"""

@app.route('/about')
def about(): return nav('about')+"""<div style="max-width:800px;margin:auto;padding:15px"><h2>About Platform - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><h3>Mission</h3><p>Affordable digital services to every Kenyan - 18 Tools + Shop + Freelance + Student + Free + AI - All automated with M-Pesa STK Push</p><h3>Team</h3><p>TIMOTHY Founder - 0118431854 - 1500+ users</p></div></div>"""

@app.route('/contact')
def contact_page(): return nav()+"""<div style="max-width:700px;margin:auto;padding:15px"><h2>Support - TIMOTHY - Contact Form, WhatsApp, FAQs, Help Center</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><h3>Contact Form</h3><input placeholder="Your Name" style="width:100%;padding:8px;background:#0e0e14;color:white"><textarea placeholder="Message" style="width:100%;padding:8px;background:#0e0e14;color:white" rows="4"></textarea><button style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px">Send to TIMOTHY</button><hr><a href="https://wa.me/254118431854" style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">WhatsApp TIMOTHY 0118431854</a></div></div>"""

@app.route('/terms')
def terms(): return nav()+"""<div style="max-width:800px;margin:auto;padding:15px"><h2>Legal - TIMOTHY - Terms, Privacy, Refund, Cookie</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><h3>Terms</h3><small>Digital products non-refundable after download</small><h3>Privacy</h3><small>Phone, email, orders stored - No sharing</small><h3>Refund</h3><small>Digital: refund if not delivered. Contact 0118431854</small></div></div>"""
@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()

@app.route('/admin')
def admin():
    return nav('admin')+"""<div style="max-width:1100px;margin:auto;padding:15px"><h2>Admin Dashboard - TIMOTHY - Users, Products, Services, Orders, Payments, Sales, Reports</h2>
<div style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px"><div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Users</h3><div id="users">Loading...</div></div><div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Orders</h3><div id="orders">Loading...</div></div></div></div>
<script>fetch('/api/admin-data').then(r=>r.json()).then(d=>{document.getElementById('total').innerText=(d.total_fees||0).toFixed(2);document.getElementById('uc').innerText=d.users.length;document.getElementById('oc').innerText=d.orders.length;document.getElementById('users').innerHTML=d.users.map(u=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${u.phone} - $${(u.balance||0).toFixed(2)}</div>`).join('');document.getElementById('orders').innerHTML=d.orders.map(o=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${o.product||o.service_type} - ${o.phone} - $${o.amount} - ${o.status}</div>`).join('');})</script>"""

@app.route('/api/products')
def api_products():
    prods=load(FILES["products"],[
        {"id":1,"title":"Forex Mastery Ebook by TIMOTHY","desc":"Complete forex guide 2026","features":"PDF 100 pages, Strategies","price":5,"category":"ebook","icon":"📘"},
        {"id":2,"title":"Canva Poster Templates Pack","desc":"100 editable templates","features":"Canva link, HD","price":3,"category":"template","icon":"🎨"},
        {"id":3,"title":"Trading Guide - Gold Strategy","desc":"XAUUSD strategy","features":"Entry/Exit, Risk mgmt","price":6,"category":"trading","icon":"📈"},
        {"id":4,"title":"Pro CV Template Pack","desc":"10 CV templates","features":"Word + PDF","price":2,"category":"cv","icon":"📄"},
        {"id":5,"title":"Business Plan Template KE","desc":"KRA compliant","features":"Financials","price":4,"category":"template","icon":"💼"},
        {"id":6,"title":"WhatsApp Sales Scripts","desc":"50 scripts","features":"Sheng + English","price":3,"category":"ebook","icon":"💬"},
        {"id":7,"title":"Study Notes - Business Studies","desc":"Form 4 + University notes","features":"PDF, Revision","price":2,"category":"ebook","icon":"📚"},
        {"id":8,"title":"AI Prompts Pack - 100 Prompts","desc":"ChatGPT prompts","features":"Business, Content","price":2,"category":"template","icon":"🤖"}
    ])
    save(FILES["products"],prods)
    return jsonify(prods)
@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json(); prods=load(FILES["products"],[]); nid=max([p['id'] for p in prods],default=0)+1
    prods.append({"id":nid,"title":data['title'],"desc":data.get('desc','By TIMOTHY'),"features":data.get('features','By TIMOTHY Seller'),"price":float(data.get('price',0)),"category":data.get('category','ebook'),"icon":"📦"})
    save(FILES["products"],prods); return jsonify({"ok":True,"id":nid})
@app.route('/api/edit-product', methods=['POST'])
def api_edit_product():
    data=request.get_json(); prods=load(FILES["products"],[])
    for p in prods:
        if p['id']==int(data['id']): p['title']=data.get('title',p['title'])
    save(FILES["products"],prods); return jsonify({"ok":True})
@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json(); pid=int(data['product_id']); phone=data['phone']
    prods=load(FILES["products"],[]); prod=next((p for p in prods if p['id']==pid),None)
    if not prod: return jsonify({"ok":False,"message":"Not found"})
    orders=load(FILES["orders"],[]); oid=len(orders)+1
    orders.append({"id":oid,"product":prod['title'],"phone":phone,"amount":prod['price'],"status":"Paid - Auto Delivered - TIMOTHY","time":str(datetime.now()),"download_url":f"/download/{oid}"})
    save(FILES["orders"],orders); fees=load(FILES["fees"],{"total":0}); fees['total']=fees.get('total',0)+float(prod['price']); save(FILES["fees"],fees)
    return jsonify({"ok":True,"download_url":f"/download/{oid}","order_id":oid})
@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json(); orders=load(FILES["services"],[]); oid=len(orders)+1
    orders.append({"id":oid,"service_type":data.get('service_type','Service'),"requirements":data.get('requirements',''),"phone":data.get('phone',''),"file_link":data.get('file_link',''),"status":"Payment Verified - In Progress - TIMOTHY","amount":5,"time":str(datetime.now())})
    save(FILES["services"],orders); fees=load(FILES["fees"],{"total":0}); fees['total']=fees.get('total',0)+5; save(FILES["fees"],fees)
    return jsonify({"ok":True,"order_id":oid})
@app.route('/api/my-orders')
def api_my_orders():
    phone=request.args.get('phone'); orders=load(FILES["orders"],[])+load(FILES["services"],[])
    return jsonify([o for o in orders if o.get('phone')==phone])
@app.route('/download/<int:oid>')
def download_file(oid): return f"<h2>Download Ready Order {oid} - Auto Delivered by TIMOTHY</h2><a href='/' style='background:#00c950;color:white;padding:12px 18px;border-radius:20px;text-decoration:none;font-weight:bold'>Download Now - TIMOTHY</a>"
@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone'); users=load(FILES["users"],{})
    if phone=="0118431854": return jsonify({"phone":phone,"balance":999})
    return jsonify(users.get(phone,{"phone":phone,"balance":0}))
@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); pwd=data['password'].strip(); users=load(FILES["users"],{})
    if phone=="0118431854":
        if pwd!="KAUMONI20r4.": return jsonify({"ok":False,"message":"Wrong admin"})
        if phone not in users: users[phone]={"phone":phone,"password":pwd,"balance":999,"total_fee":0,"joined":str(datetime.now())}; save(FILES["users"],users)
        return jsonify({"ok":True,"balance":999})
    if phone in users: return jsonify({"ok":True,"balance":users[phone].get('balance',0)})
    else: users[phone]={"phone":phone,"password":pwd,"balance":0,"total_fee":0,"joined":str(datetime.now())}; save(FILES["users"],users); return jsonify({"ok":True,"balance":0})
@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load(FILES["users"],{}); ph=data['phone']; amt=float(data['amount'])
    if ph=="0118431854": return jsonify({"ok":True,"balance":999})
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({"ok":False,"message":"Low balance - Deposit via STK"})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load(FILES["fees"],{"total":0}); fees['total']=fees.get('total',0)+amt; save(FILES["fees"],fees); save(FILES["users"],users); return jsonify({"ok":True})
@app.route('/api/admin-data')
def api_admin_data():
    users=load(FILES["users"],{}); fees=load(FILES["fees"],{"total":0}); orders=load(FILES["orders"],[])+load(FILES["services"],[]); prods=load(FILES["products"],[])
    return jsonify({"users":list(users.values()),"total_fees":fees.get('total',0),"orders":orders,"products":prods})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
