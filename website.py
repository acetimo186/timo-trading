
from flask import Flask, request, jsonify
import os, json
from datetime import datetime

app = Flask(__name__)
app.secret_key = "KAUMONI_TIMOTHY_V17"

USERS_FILE='users.json'
FEES_FILE='fees.json'

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
<nav style="background:#1a1a25;padding:12px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #333;flex-wrap:wrap;gap:8px">
<b style="color:#f9c846">KAUMONI V17</b>
<div style="display:flex;gap:10px;font-size:11px;flex-wrap:wrap">
<a href="/" style="color:{'#f9c846' if active=='home' else 'white'};text-decoration:none">Home</a>
<a href="/shop" style="color:{'#f9c846' if active=='shop' else 'white'};text-decoration:none">Shop</a>
<a href="/freelance-services" style="color:white;text-decoration:none">Services</a>
<a href="/design-studio" style="color:white;text-decoration:none">Design</a>
<a href="/student-hub" style="color:white;text-decoration:none">Student Hub</a>
<a href="/free-tools" style="color:white;text-decoration:none">Free Tools</a>
<a href="/ai-tools" style="color:white;text-decoration:none">AI Tools</a>
<a href="/about" style="color:white;text-decoration:none">About</a>
<a href="/admin" style="color:#f9c846;text-decoration:none">TIMOTHY</a>
</div></nav>
"""

@app.route('/')
def home():
    return f"""<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni V17</title>
<style>body{{background:#0a0a12;color:white;font-family:Arial;margin:0}}.card{{background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;margin:8px;text-align:center}}.grid{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;padding:12px}}@media(max-width:700px){{.grid{{grid-template-columns:1fr}}}}.btn{{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 16px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin:4px}}</style></head><body>
{nav('home')}
<div style="text-align:center;padding:30px;background:linear-gradient(90deg,#0e0e14,#1a1a25,#2a1a3a)">
<h1><span style="color:#f9c846">All-in-One</span> Digital Services</h1>
<p>Managed by <b style="color:#f9c846">TIMOTHY - 0118431854</b> - 18 Tools + Shop + Services</p>
<a class="btn" href="/shop">Shop</a><a class="btn" href="/design-studio" style="background:#6a0dad;color:white">Design Studio</a><a class="btn" href="/free-tools" style="background:#00c950;color:white">Free Tools</a>
</div>
<div style="max-width:1100px;margin:auto;padding:15px">
<h2 style="text-align:center">What We Offer</h2>
<div class="grid">
<div class="card">🛒<br><b>Shop Digital Products</b><br><small>Ebooks, Templates, CVs</small><br><a class="btn" href="/shop">Browse Shop</a></div>
<div class="card">💼<br><b>Freelance Services</b><br><small>CV, PPT, Websites</small><br><a class="btn" href="/freelance-services">Hire Now</a></div>
<div class="card">🎨<br><b>Design Studio - 18 Tools</b><br><small>Poster, Logo, KRA, Biz Card</small><br><a class="btn" href="/design-studio">Create Design</a></div>
<div class="card">🎓<br><b>Student Hub</b><br><small>GPA, Notes, Revision</small><br><a class="btn" href="/student-hub">Student Hub</a></div>
<div class="card">🛠️<br><b>Free Tools</b><br><small>Profit, Loan, QR, Lot</small><br><a class="btn" href="/free-tools">Free Tools</a></div>
<div class="card">🤖<br><b>AI Tools</b><br><small>AI Caption, Writing, Names</small><br><a class="btn" href="/ai-tools">AI Tools</a></div>
</div>
<h2 style="text-align:center">Featured - Your 18 Tools Still Here</h2>
<div class="grid">
<div class="card"><b>Poster Maker $1</b><br><a class="btn" href="/poster-maker">Create</a></div>
<div class="card"><b>KRA E-TIMS $1.5</b><br><a class="btn" href="/kra-invoice">Make KRA</a></div>
<div class="card"><b>Business Card $2</b><br><a class="btn" href="/business-card">Make Card</a></div>
<div class="card"><b>Certificate $1.5</b><br><a class="btn" href="/certificate-maker">Make Cert</a></div>
<div class="card"><b>Payslip $1</b><br><a class="btn" href="/payslip-maker">Make Payslip</a></div>
<div class="card"><b>AI Caption $1</b><br><a class="btn" href="/ai-caption">Generate</a></div>
</div>
<div style="text-align:center;padding:20px;margin-top:20px;background:#1a1a25;border-radius:12px">
<h3>Contact TIMOTHY - 0118431854</h3>
<a href="https://wa.me/254118431854" style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">WhatsApp</a>
<p style="font-size:11px;color:#666"><a href="/about" style="color:#666">About</a> | <a href="/terms" style="color:#666">Terms</a> | <a href="/privacy" style="color:#666">Privacy</a></p>
<p style="font-size:11px;color:#666">© 2026 Kaumoni V17 - TIMOTHY - Deploy Fixed</p>
</div>
</div></body></html>"""

@app.route('/shop')
def shop():
    return f"""{nav('shop')}<div style="max-width:1000px;margin:auto;padding:15px"><h2>Shop - Digital Products by TIMOTHY</h2>
<div class="grid" id="grid"></div></div>
<script>fetch('/api/products').then(r=>r.json()).then(d=>{{document.getElementById('grid').innerHTML=d.map(p=>`<div style="background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;text-align:center"><div style="font-size:40px">${{p.icon}}</div><b>${{p.title}}</b><br><small>${{p.desc}}</small><br><b style="color:#f9c846">$${{p.price}}</b><br><a href="/product/${{p.id}}" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold;margin-top:6px;display:inline-block">Buy - STK Push</a></div>`).join('')}})</script>
"""

@app.route('/product/<pid>')
def product(pid):
    return f"""{nav('shop')}<div style="max-width:700px;margin:auto;padding:15px"><a href="/shop" style="color:#f9c846">← Shop</a><div id="det" style="background:#1a1a25;padding:15px;border-radius:12px;margin-top:10px">Loading...</div></div>
<script>
let id={pid};fetch('/api/products').then(r=>r.json()).then(all=>{{let p=all.find(x=>x.id==id);document.getElementById('det').innerHTML=`<div style="text-align:center"><div style="font-size:60px">${{p.icon}}</div><h2>${{p.title}}</h2><b style="color:#f9c846;font-size:22px">$${{p.price}}</b></div><p>${{p.desc}}</p><p>Features: ${{p.features}}</p><hr><h3>M-Pesa STK Push - Auto Delivery</h3><input id="phone" placeholder="07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:8px"><button onclick="buy()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold;margin-top:8px">Buy Now - STK Push</button><p id="msg" style="color:#00c950"></p>`}})
function buy(){{let ph=document.getElementById('phone').value;if(!ph){{alert('Enter phone');return;}}document.getElementById('msg').innerText='Sending STK to '+ph+'...';fetch('/api/order-product',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{product_id:{pid},phone:ph}})}}).then(r=>r.json()).then(d=>{{if(d.ok){{document.getElementById('msg').innerHTML=`✅ Verified by TIMOTHY! <a href="${{d.download_url}}" style="background:#00c950;color:white;padding:8px 14px;border-radius:20px;text-decoration:none">Download Now</a>`}}else{{document.getElementById('msg').innerText=d.message}}}})}}
</script>
"""

@app.route('/design-studio')
def design_studio():
    return f"""{nav()}<div style="max-width:1100px;margin:auto;padding:15px"><h2>Design Studio - 18 Tools - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Poster $1</b><br><a href="/poster-maker" style="color:#f9c846">Create</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Logo $3</b><br><a href="/logo-maker" style="color:#f9c846">Create</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>KRA E-TIMS $1.5</b><br><a href="/kra-invoice" style="color:#f9c846">Create</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Biz Card $2</b><br><a href="/business-card" style="color:#f9c846">Create</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Certificate $1.5</b><br><a href="/certificate-maker" style="color:#f9c846">Create</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px;text-align:center"><b>Payslip $1</b><br><a href="/payslip-maker" style="color:#f9c846">Create</a></div>
</div></div>
"""

@app.route('/freelance-services')
def services():
    return f"""{nav()}<div style="max-width:900px;margin:auto;padding:15px"><h2>Freelance Services - TIMOTHY</h2>
<p>CV $3 | Ebook Writing $15 | PPT $5 | Website $50 | Poster $1 | Logo $3</p>
<a href="/order-service" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Order Service - STK Push</a></div>
"""

@app.route('/order-service')
def order_service():
    return f"""{nav()}<div style="max-width:700px;margin:auto;padding:15px"><h2>Order Service - STK Push - TIMOTHY</h2>
<div style="background:#1a1a25;padding:15px;border-radius:12px">
<input id="type" placeholder="Service Type e.g. CV" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0">
<textarea id="req" placeholder="Requirements" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0" rows="4"></textarea>
<input id="phone" placeholder="M-Pesa Phone 07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0">
<button onclick="place()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold">Place Order - STK Push</button>
<p id="msg" style="color:#00c950"></p>
</div></div>
<script>
function place(){{let d={{service_type:document.getElementById('type').value,requirements:document.getElementById('req').value,phone:document.getElementById('phone').value}};fetch('/api/order-service',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(d)}}).then(r=>r.json()).then(j=>{{document.getElementById('msg').innerText='✅ Order Confirmed by TIMOTHY - ID:'+j.order_id+' - Tracking: In Progress'}})}}
</script>
"""

@app.route('/student-hub')
def student_hub():
    return f"""{nav()}<div style="max-width:900px;margin:auto;padding:15px"><h2>Student Hub - GPA / Grade Calc - TIMOTHY</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<div style="background:#1a1a25;padding:14px;border-radius:12px"><b>GPA Calc FREE</b><br><input id="gpa" placeholder="Points e.g. 3.5" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px"><button onclick="document.getElementById('gpaRes').innerText='GPA: '+document.getElementById('gpa').value" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Calc GPA</button><p id="gpaRes"></p></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px"><b>Grade Calc FREE</b><br><input id="marks" placeholder="Marks 0-100" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px"><button onclick="let m=document.getElementById('marks').value;let g=m>=70?'A':m>=60?'B':m>=50?'C':'D';document.getElementById('gradeRes').innerText='Grade: '+g" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Get Grade</button><p id="gradeRes"></p></div>
</div></div>
"""

@app.route('/free-tools')
def free_tools():
    return f"""{nav()}<div style="max-width:1000px;margin:auto;padding:15px"><h2>Free Tools - 9 Tools - TIMOTHY</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Profit Calc FREE</b><br><input id="cost" placeholder="Cost"><input id="sell" placeholder="Sell"><button onclick="document.getElementById('pRes').innerText='Profit: '+(document.getElementById('sell').value-document.getElementById('cost').value)" style="background:#f9c846;color:black;padding:5px 10px;border:none;border-radius:10px">Calc</button><p id="pRes"></p></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><b>QR Generator $1</b><br><a href="/qr-maker" style="color:#f9c846">Generate QR</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Lot Calculator FREE</b><br><a href="/lot-calculator" style="color:#00c950">Lot Calc</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Invoice $1</b><br><a href="/kra-invoice" style="color:#f9c846">Invoice Gen</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px"><b>TikTok DL FREE</b><br><a href="/tiktok-downloader" style="color:#ff0050">Download</a></div>
</div></div>
"""

@app.route('/ai-tools')
def ai_tools():
    return f"""{nav()}<div style="max-width:1000px;margin:auto;padding:15px"><h2>AI Tools - TIMOTHY</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<div style="background:#1a1a25;padding:14px;border-radius:12px"><b>AI Caption $1</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Use AI</a></div>
<div style="background:#1a1a25;padding:14px;border-radius:12px"><b>AI Business Name FREE</b><br><input id="kw" placeholder="Keyword e.g. fashion" style="width:100%;padding:8px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px"><button onclick="document.getElementById('bnRes').innerText=document.getElementById('kw').value+' Hub, '+document.getElementById('kw').value+' Empire, Elite '+document.getElementById('kw').value" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px;margin-top:5px">Generate Names</button><p id="bnRes"></p></div>
</div></div>
"""

@app.route('/about')
def about():
    return f"""{nav()}<div style="max-width:800px;margin:auto;padding:15px"><h2>About - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><p>Mission: Affordable digital services to every Kenyan. 18 Tools + Shop + Freelance.</p><p>Team: TIMOTHY Founder - 0118431854 - 1500+ users</p><p>Contact: WhatsApp 0118431854</p></div></div>
"""

@app.route('/terms')
def terms():
    return f"""{nav()}<div style="max-width:800px;margin:auto;padding:15px"><h2>Terms / Privacy / Refund - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><p><b>Terms:</b> Digital products non-refundable after download.</p><p><b>Privacy:</b> We store phone only, no sharing.</p><p><b>Refund:</b> Only if file not delivered, within 24h contact 0118431854</p></div></div>
"""

@app.route('/privacy')
def privacy(): return terms()
@app.route('/contact')
def contact(): return about()

# Tools placeholders - link to your previous V16 full HTML if you have
@app.route('/poster-maker')
def poster_maker(): return "<h2>Poster Maker $1 - TIMOTHY - Full HD tool from V16 - paste your V16 poster HTML here</h2><a href='/'>Home</a>"
@app.route('/kra-invoice')
def kra_invoice(): return "<h2>KRA E-TIMS $1.5 - TIMOTHY - Paste V16 KRA HTML</h2><a href='/'>Home</a>"
@app.route('/business-card')
def biz_card(): return "<h2>Biz Card $2 - TIMOTHY - Paste V16 Biz Card HTML</h2><a href='/'>Home</a>"
@app.route('/certificate-maker')
def cert(): return "<h2>Certificate $1.5 - TIMOTHY - Paste V16 Cert HTML</h2><a href='/'>Home</a>"
@app.route('/payslip-maker')
def payslip(): return "<h2>Payslip $1 - TIMOTHY - Paste V16 Payslip HTML</h2><a href='/'>Home</a>"
@app.route('/ai-caption')
def ai_caption(): return "<h2>AI Caption $1 - TIMOTHY - Paste V16 AI HTML</h2><a href='/'>Home</a>"
@app.route('/qr-maker')
def qr_maker(): return "<h2>QR Maker - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/lot-calculator')
def lot_calc(): return "<h2>Lot Calc FREE - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/tiktok-downloader')
def tiktok_dl(): return "<h2>TikTok DL FREE - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/logo-maker')
def logo_maker(): return "<h2>Logo Maker $3 - TIMOTHY</h2><a href='/'>Home</a>"
@app.route('/admin')
def admin(): return f"""{nav()}<div style="max-width:900px;margin:auto;padding:15px"><h2>Admin - TIMOTHY - V17</h2><div style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span></div><div id="users"></div></div>
<script>fetch('/api/admin-data').then(r=>r.json()).then(d=>{{document.getElementById('total').innerText=(d.total_fees||0).toFixed(2);document.getElementById('uc').innerText=d.users.length;document.getElementById('users').innerHTML=d.users.map(u=>`<div style="background:#1a1a25;padding:6px;margin:4px 0;border-radius:6px">${{u.phone}} - $${{(u.balance||0).toFixed(2)}}</div>`).join('')}})</script>
"""

@app.route('/api/products')
def api_products():
    return jsonify([
        {"id":1,"title":"Forex Mastery Ebook by TIMOTHY","desc":"Complete forex guide 2026","features":"PDF 100 pages, Strategies","price":5,"icon":"📘"},
        {"id":2,"title":"Canva Poster Templates","desc":"100 editable templates","features":"Canva link, HD","price":3,"icon":"🎨"},
        {"id":3,"title":"Trading Guide - Gold","desc":"XAUUSD strategy","features":"Entry/Exit, Risk mgmt","price":6,"icon":"📈"},
        {"id":4,"title":"Pro CV Template Pack","desc":"10 CV templates","features":"Word + PDF","price":2,"icon":"📄"},
        {"id":5,"title":"Business Plan KE","desc":"KRA compliant","features":"Financials","price":4,"icon":"💼"},
        {"id":6,"title":"WhatsApp Sales Scripts","desc":"50 scripts","features":"Sheng + English","price":3,"icon":"💬"}
    ])

@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json()
    return jsonify({"ok":True,"download_url":f"/download/{data['product_id']}","order_id":1})

@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    return jsonify({"ok":True,"order_id":123})

@app.route('/download/<oid>')
def download_file(oid):
    return f"<h2>Download Ready - Order {oid} - TIMOTHY - Auto Delivered</h2><a href='/' style='background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none'>Download PDF - Simulated</a>"

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {})
    fees=load_json(FEES_FILE, {"total":0})
    return jsonify({"users":list(users.values()),"total_fees":fees.get('total',0)})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
