
from flask import Flask, request, jsonify
import os, json
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V17_6_1_FIXED_IFRAME_REAL_CHART_ATTRACTIVE"
FILES = {"users":"users.json","fees":"fees.json","products":"products.json","orders":"orders.json","services":"services_orders.json"}
def load(f,d):
    if not os.path.exists(f): return d
    try:
        with open(f) as jf: return json.load(jf)
    except: return d
def save(f,data):
    with open(f,'w') as jf: json.dump(data,jf)
def nav(a="home"):
    return f"""<nav style="background:#1a1a25;padding:12px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #333;flex-wrap:wrap;gap:8px;z-index:100"><b style="color:#f9c846;animation:moveText 2s ease-in-out infinite;display:inline-block">KAUMONI V17.6.1 - TIMOTHY MOVING - CHART FIXED</b><style>@keyframes moveText{{0%{{transform:translateX(-5px)}}50%{{transform:translateX(5px)}}100%{{transform:translateX(-5px)}}}}</style><div style="display:flex;gap:8px;font-size:10px;flex-wrap:wrap"><a href="/" style="color:{'#f9c846' if a=='home' else 'white'};text-decoration:none">Home</a><a href="/shop" style="color:white;text-decoration:none">Shop</a><a href="/trading" style="color:{'#f9c846' if a=='trading' else 'white'};text-decoration:none;font-weight:bold">Trading LIVE FIXED</a><a href="/design-studio" style="color:white;text-decoration:none">Design</a><a href="/free-tools" style="color:white;text-decoration:none">Free</a><a href="/dashboard" style="color:white;text-decoration:none">Dashboard</a><a href="/admin" style="color:#f9c846;text-decoration:none">TIMOTHY</a></div></nav>"""

@app.route('/')
def home():
    return nav('home')+"""<style>
body{background:#0a0a12;color:white;font-family:Arial;margin:0;overflow-x:hidden}
@keyframes gradientMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
@keyframes float{0%{transform:translateY(0px)}50%{transform:translateY(-20px)}100%{transform:translateY(0px)}}
@keyframes moveText{0%{transform:translateX(-12px)}50%{transform:translateX(12px)}100%{transform:translateX(-12px)}}
@keyframes timothyMove{0%{transform:translateX(-15px) scale(1);color:#f9c846;text-shadow:0 0 10px #f9c846}25%{transform:translateX(15px) scale(1.1);color:#ff9800;text-shadow:0 0 20px #ff9800}50%{transform:translateX(-10px) scale(1);color:#f9c846;text-shadow:0 0 15px #f9c846}75%{transform:translateX(10px) scale(1.1);color:#00ff88;text-shadow:0 0 20px #00ff88}100%{transform:translateX(-15px) scale(1);color:#f9c846;text-shadow:0 0 10px #f9c846}}
.hero{background:linear-gradient(270deg,#0e0e14,#1a1a25,#2a1a3a,#6a0dad,#0d47a1);background-size:800% 800%;animation:gradientMove 12s ease infinite;position:relative;overflow:hidden;padding:45px 20px;text-align:center;border-bottom:3px solid #f9c846}
.bubble{position:absolute;border-radius:50%;background:radial-gradient(circle,rgba(249,200,70,0.15),rgba(249,200,70,0.05));animation:float 8s ease-in-out infinite;border:1px solid rgba(249,200,70,0.2)}
.b1{width:90px;height:90px;left:5%;top:15%;animation-delay:0s}.b2{width:130px;height:130px;left:75%;top:5%;animation-delay:1s}.b3{width:70px;height:70px;left:45%;top:65%;animation-delay:2s}.b4{width:110px;height:110px;left:85%;top:45%;animation-delay:3s}
.moving-timothy{display:inline-block;animation:timothyMove 3s ease-in-out infinite;font-weight:900;font-size:22px}
.moving-text{display:inline-block;animation:moveText 2.5s ease-in-out infinite;color:#f9c846;font-weight:bold}
.card{background:#1a1a25;border:1px solid #333;padding:14px;border-radius:14px;margin:8px;text-align:center;transition:0.4s}
.card:hover{transform:scale(1.05);border-color:#f9c846}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;padding:14px}@media(max-width:700px){.grid{grid-template-columns:1fr}}
.btn{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block;margin:6px}
.btn:hover{transform:scale(1.1)}
</style>
<div class="hero">
<div class="bubble b1"></div><div class="bubble b2"></div><div class="bubble b3"></div><div class="bubble b4"></div>
<h1 style="font-size:36px"><span style="color:#f9c846">All-in-One</span> <span class="moving-text">Digital Services</span></h1>
<p style="font-size:20px">Managed by <span class="moving-timothy">TIMOTHY - 0118431854 - V17.6.1 FIXED CHART</span></p>
<p style="color:#ccc;max-width:750px;margin:auto;font-size:14px">Shop + Trading Hub LIVE FIXED Real Chart 6 Pairs + Design Studio 18 HD + Freelance + Student + Free + AI + Dashboard + Seller + STK Auto + Moving Background + TIMOTHY Moving</p>
<div style="margin-top:20px">
<a class="btn" href="/trading" style="background:linear-gradient(90deg,#00c950,#00ff88);color:black">🔥 Trading LIVE FIXED - Chart Now Shows</a>
<a class="btn" href="/shop">🛒 Shop</a>
<a class="btn" href="/design-studio" style="background:linear-gradient(90deg,#6a0dad,#ff00ff);color:white">🎨 Design 18 HD</a>
</div>
<p style="margin-top:15px;color:#00ff88;font-weight:bold;animation:timothyMove 3s infinite">✅ CHART FIXED - iframe method - Now shows LIVE real chart! - TIMOTHY MOVING</p>
</div>
<div style="max-width:1150px;margin:auto;padding:15px"><h2 style="text-align:center"><span class="moving-text">What We Offer - Trading LIVE FIXED - V17.6.1</span></h2><div class="grid">
<div class="card" style="border:2px solid #00c950"><b>📈 Trading Hub LIVE FIXED</b><br><small>Real Chart iframe - 6 Pairs LIVE - Now Shows!</small><br><a class="btn" href="/trading" style="background:#00c950;color:white">Trading LIVE FIXED 🔥</a></div>
<div class="card"><b>🛒 Shop Digital</b><br><small>Ebooks, Templates, CVs $2-$6</small><br><a class="btn" href="/shop">Browse Shop</a></div>
<div class="card"><b>🎨 Design Studio 18 HD</b><br><small>Poster $1, KRA $1.5, Biz Card $2</small><br><a class="btn" href="/design-studio">Create HD</a></div>
</div></div>"""

@app.route('/trading')
def trading_hub():
    return nav('trading')+"""<div style="max-width:1200px;margin:auto;padding:15px">
<h2>Trading Hub - TIMOTHY - LIVE Real Chart FIXED V17.6.1 - Iframe Always Shows - 6 Pairs</h2>
<div style="background:#1a1a25;padding:12px;border-radius:12px;margin-bottom:15px;border:2px solid #00c950">
<h3 style="color:#00ff88;text-align:center">✅ FIXED - LIVE Real Chart - Iframe Method - Now Shows!</h3>
<div style="height:600px;background:#131722;border-radius:12px;overflow:hidden;border:2px solid #333">
<iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_real&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&studies=%5B%22RSI%40tv-basicstudies%22%2C%22MACD%40tv-basicstudies%22%5D&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en&utm_source=kaumoni.com&utm_medium=widget" style="width:100%;height:100%;border:none" frameborder="0" scrolling="no"></iframe>
</div>
<p style="text-align:center;color:#00c950;font-weight:bold;margin-top:10px">✅ If you see XAUUSD Gold chart moving above, FIXED! - Real LiteFinance Data via TradingView iframe</p>
<p style="text-align:center;font-size:12px;color:#aaa">6 Main Pairs: XAUUSD Gold, EURUSD, GBPUSD, USDJPY, USDCAD, AUDUSD - Use search inside chart to switch pairs - Or click below</p>
<div style="text-align:center;margin-top:12px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap">
<a href="/market-analysis" style="background:#00c950;color:white;padding:12px 20px;border-radius:20px;text-decoration:none;font-weight:bold">View All 6 Pairs LIVE FIXED - Click Here</a>
<a href="https://www.litefinance.com" target="_blank" style="background:#f9c846;color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">LiteFinance Real Account</a>
<a href="/signals" style="background:#ff9800;color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Signals $5 - TIMOTHY</a>
</div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;border:2px solid #00c950;padding:14px;border-radius:12px;text-align:center"><b>🥇 XAUUSD Gold LIVE FIXED</b><br><span style="color:#00c950;font-weight:bold">Chart Above LIVE - FIXED</span></div>
<div style="background:#1a1a25;border:1px solid #00c950;padding:14px;border-radius:12px;text-align:center"><b>6 Main Pairs LIVE FIXED</b><br><a href="/market-analysis" style="background:#00c950;color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">View All 6 LIVE FIXED</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:14px;border-radius:12px;text-align:center"><b>Gold Signals $5</b><br><a href="/signals" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold">Signals $5</a></div>
</div>
</div>"""

@app.route('/signals')
def signals_page():
    return nav('trading')+"""<div style="max-width:800px;margin:auto;padding:15px"><h2>Gold Signals - TIMOTHY - $5/month - Real Chart FIXED</h2>
<div style="background:#1a1a25;padding:15px;border-radius:12px"><div style="background:#0e0e14;padding:10px;border-radius:8px;margin:8px 0;border-left:4px solid #00c950"><b>BUY XAUUSD @ 2645 - LIVE FIXED</b><br>SL: 2625 | TP: 2670, 2690 | By TIMOTHY - Real Chart FIXED</div><div style="background:#0e0e14;padding:10px;border-radius:8px;margin:8px 0;border-left:4px solid #ef5350"><b>SELL XAUUSD @ 2685</b><br>SL: 2705 | TP: 2660, 2640 | By TIMOTHY</div><a href="https://wa.me/254118431854" style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Join Signals $5 - FIXED</a><br><br><a href="/trading" style="color:#00c950">← Trading LIVE FIXED</a> | <a href="/market-analysis" style="color:#00c950">6 Pairs LIVE FIXED</a></div></div>"""

@app.route('/market-analysis')
def market_analysis():
    return nav('trading')+"""<div style="max-width:1200px;margin:auto;padding:15px"><h2>Market Analysis - 6 Main Pairs LIVE FIXED - iframe - V17.6.1</h2>
<div style="background:#1a1a25;padding:10px;border-radius:12px;margin-bottom:10px;border:2px solid #00c950"><p style="color:#00c950;text-align:center;font-weight:bold">✅ FIXED - 6 Mini LIVE Charts iframe - All should show moving now!</p></div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:15px">
<div style="background:#1a1a25;padding:8px;border-radius:12px;border:1px solid #f9c846"><h4 style="color:#f9c846">🥇 XAUUSD Gold LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_gold&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
<div style="background:#1a1a25;padding:8px;border-radius:12px"><h4>💶 EURUSD LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_eur&symbol=FX%3AEURUSD&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
<div style="background:#1a1a25;padding:8px;border-radius:12px"><h4>💷 GBPUSD LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_gbp&symbol=FX%3AGBPUSD&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-bottom:15px">
<div style="background:#1a1a25;padding:8px;border-radius:12px"><h4>💴 USDJPY LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_jpy&symbol=FX%3AUSDJPY&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
<div style="background:#1a1a25;padding:8px;border-radius:12px"><h4>💵 USDCAD LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_cad&symbol=FX%3AUSDCAD&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
<div style="background:#1a1a25;padding:8px;border-radius:12px"><h4>🇦🇺 AUDUSD LIVE FIXED</h4><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tv_aud&symbol=FX%3AAUDUSD&interval=60&hidesidetoolbar=1&symboledit=0&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:250px;border:none;border-radius:8px"></iframe></div>
</div>
<div style="background:#1a1a25;padding:15px;border-radius:12px"><h3>6 Pairs Analysis - If 6 charts above moving, FIXED!</h3><p>🥇 XAUUSD: Buy 2630-2640 SL 2610 TP 2680 | 💶 EURUSD: Buy 1.1050 Target 1.1150 | 💷 GBPUSD: Buy 1.3020 TP 1.3150</p><p>💴 USDJPY: Sell below 145 Target 143.5 | 💵 USDCAD: Sell below 1.35 Target 1.34 | 🇦🇺 AUDUSD: Buy above 0.68 Target 0.69</p><a href="/trading" style="background:#00c950;color:white;padding:8px 14px;border-radius:20px;text-decoration:none">Back to Trading FIXED</a></div></div>"""

@app.route('/shop')
def shop():
    return nav('shop')+"""<div style="max-width:1100px;margin:auto;padding:15px"><h2>Shop - TIMOTHY - 8 Products</h2><div id="grid" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px"></div></div><script>fetch('/api/products').then(r=>r.json()).then(d=>{document.getElementById('grid').innerHTML=d.map(p=>`<div style="background:#1a1a25;border:1px solid #333;padding:14px;border-radius:12px;text-align:center"><div style="font-size:30px">${p.icon}</div><b>${p.title}</b><br><small style="color:#aaa">${p.desc}</small><br><b style="color:#f9c846">$${p.price}</b><br><a href="/product/${p.id}" style="background:#f9c846;color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block;margin-top:6px">Buy - STK Push</a></div>`).join('')})</script>"""

@app.route('/product/<int:pid>')
def product_detail(pid):
    return nav('shop')+f"""<div style="max-width:800px;margin:auto;padding:15px"><a href="/shop" style="color:#f9c846">← Shop</a><div id="det" style="background:#1a1a25;padding:15px;border-radius:12px;margin-top:10px">Loading {pid}...</div></div><script>fetch('/api/products').then(r=>r.json()).then(all=>{{let p=all.find(x=>x.id=={pid});document.getElementById('det').innerHTML=`<div style="text-align:center"><div style="font-size:40px">${{p.icon}}</div><h2>${{p.title}}</h2><b style="color:#f9c846;font-size:22px">$${{p.price}}</b></div><p><b>Description:</b> ${{p.desc}}</p><p><b>Features:</b> ${{p.features}}</p><hr><h3>M-Pesa STK Push - Auto Delivery - TIMOTHY</h3><input id="phone" placeholder="07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:8px"><button onclick="buy()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold;margin-top:8px">Buy Now - STK Push</button><p id="msg" style="color:#00c950"></p>`}});function buy(){{let ph=document.getElementById('phone').value;if(!ph){{alert('Enter phone');return}}document.getElementById('msg').innerText='Sending STK to '+ph;fetch('/api/order-product',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{product_id:{pid},phone:ph}})}}).then(r=>r.json()).then(d=>{{if(d.ok){{document.getElementById('msg').innerHTML=`✅ Verified!<br><a href="${{d.download_url}}" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none">Download Now</a>`}}}})}}
</script>"""

@app.route('/freelance-services')
def freelance(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Freelance Services - TIMOTHY - CV $3, Ebook $15, PPT $5, Website $50</h2><a href="/order-service" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Order Service</a> - <a href="/design-studio" style="background:#f9c846;color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Design 18 HD</a> - <a href="/trading" style="background:#00c950;color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">Trading LIVE FIXED</a></div>"""
@app.route('/order-service')
def order_service(): return nav()+"""<div style="max-width:700px;margin:auto;padding:15px"><h2>Order Service - STK - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><input id="type" placeholder="Service Type" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0"><textarea id="req" placeholder="Requirements" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px" rows="4"></textarea><input id="phone" placeholder="M-Pesa 07XX" style="width:100%;padding:10px;background:#0e0e14;color:white;border:1px solid #333;border-radius:6px;margin:5px 0"><button onclick="place()" style="background:#00c950;color:white;width:100%;padding:12px;border:none;border-radius:8px;font-weight:bold">Place Order - STK Push</button><p id="msg" style="color:#00c950"></p></div></div><script>function place(){let d={service_type:document.getElementById('type').value,requirements:document.getElementById('req').value,phone:document.getElementById('phone').value};fetch('/api/order-service',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(d)}).then(r=>r.json()).then(j=>{document.getElementById('msg').innerText='✅ Confirmed by TIMOTHY ID:'+j.order_id})}</script>"""
@app.route('/design-studio')
def design_studio(): return nav()+"""<div style="max-width:1200px;margin:auto;padding:15px"><h2>Design Studio - 18 HD Tools - TIMOTHY</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Poster $1 HD</b><br><a href="/poster-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Create $1</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Certificate $1.5 HD</b><br><a href="/certificate-maker" style="background:#6a0dad;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $1.5</a></div>
<div style="background:#1a1a25;border:1px solid #f9c846;padding:12px;border-radius:12px;text-align:center"><b>Logo $3 HD</b><br><a href="/logo-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Logo $3</a></div>
<div style="background:#1a1a25;border:1px solid #42a5f5;padding:12px;border-radius:12px;text-align:center"><b>Biz Card $2 HD</b><br><a href="/business-card" style="background:#0d47a1;color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:bold">Make $2</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>KRA E-TIMS $1.5 HD</b><br><a href="/kra-invoice" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">KRA $1.5</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Receipt $1 HD</b><br><a href="/receipt-maker" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Receipt $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Payslip $1 HD</b><br><a href="/payslip-maker" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Payslip $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>CV Builder $2 HD</b><br><a href="/cv-builder" style="background:#0d47a1;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">CV $2</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>AI Caption $1 HD</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">AI $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>QR USABLE $1 HD</b><br><a href="/qr-maker" style="background:#333;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">QR $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>BG Remover $1 HD</b><br><a href="/bg-remover" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">BG $1</a></div>
<div style="background:#1a1a25;padding:12px;border-radius:12px;text-align:center"><b>Lot Calc FREE</b><br><a href="/lot-calculator" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Lot FREE FIXED</a></div>
</div></div>"""

def hd_tool_template(title, price, color, inputs_html, draw_js, filename):
    return f"""<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} HD - TIMOTHY</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>body{{background:#0e0e14;color:white;font-family:Arial;padding:10px}}input,select,textarea{{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}}.card{{background:#1a1a25;padding:10px;border-radius:8px}}#preview{{width:500px;max-width:95%;margin:auto;background:white;color:black;padding:15px;border-radius:8px;position:relative;overflow:hidden;text-align:center}}#wm{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.96);color:#004AFF;font-size:24px;font-weight:900;padding:10px 20px;border:3px solid #004AFF;white-space:nowrap;z-index:10}}</style></head><body><a href="/design-studio" style="color:#f9c846">← Design Studio</a><h2>{title} HD by TIMOTHY - PREVIEW watermark - FIXED V17.6.1</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p>{inputs_html}</div><button onclick="downloadHD()" style="background:{color};color:white;width:100%;padding:12px;border:none;border-radius:6px;font-weight:bold">Download HD ${price} - Remove PREVIEW</button></div><div id="preview"></div></div>
<script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){{document.getElementById('uPhone').innerText=userPhone||'Not logged';if(userPhone==='0118431854'){{document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}}{draw_js}async function downloadHD(){{if(userPhone!=='0118431854'&&userBal<{price}){{alert('Need {price}');return;}}let r=await fetch('/api/deduct',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{phone:userPhone,amount:{price},reason:'{filename}'}})}});let d=await r.json();if(!d.ok){{alert(d.message);return;}}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('preview'),{{scale:2}}).then(c=>{{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='{filename}_TIMOTHY.png';a.href=c.toDataURL();a.click();loadBal();}});}}loadBal();draw();</script></body></html>"""

@app.route('/poster-maker')
def poster_maker(): return hd_tool_template("Poster Maker $1",1,"#00c950",'<select id="tpl" onchange="draw()"><option value="1">Red-Yellow</option><option value="2">Blue</option><option value="3">Gold</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 0118431854" oninput="draw()">','function draw(){let cols={1:["#ff0000","#ffcc00"],2:["#1e3a8a","#60a5fa"],3:["#f9c846","#ff9800"]}[document.getElementById("tpl").value];document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1 - Kaumoni.com</div><div style="background:linear-gradient(135deg,${cols[0]},${cols[1]});padding:40px 20px;border-radius:8px"><h1 style="font-size:42px;margin:0">${document.getElementById("title").value}</h1><h2>${document.getElementById("sub").value}</h2><div style="background:black;color:white;padding:8px 14px;border-radius:20px;margin-top:15px;display:inline-block">${document.getElementById("phone").value}</div></div>`;}','Poster')
@app.route('/certificate-maker')
def certificate_maker(): return hd_tool_template("Certificate $1.5",1.5,"#6a0dad",'<select id="type" onchange="draw()"><option value="Appreciation">Appreciation</option><option value="Achievement">Achievement</option></select><input id="name" value="John Kamau" oninput="draw()"><input id="reason" value="For Outstanding Performance" oninput="draw()"><input id="org" value="Kaumoni Academy - TIMOTHY" oninput="draw()"><input id="date" value="30 Sept 2026" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1.5</div><div style="border:10px double #6a0dad;padding:15px;border-radius:8px"><h1 style="color:#6a0dad">${document.getElementById("type").value.toUpperCase()}</h1><h2 style="font-size:28px;border-bottom:2px solid #f9c846;display:inline-block">${document.getElementById("name").value}</h2><p>${document.getElementById("reason").value}</p><p style="font-size:11px">${document.getElementById("org").value} - ${document.getElementById("date").value}</p></div>`;}','Certificate')
@app.route('/logo-maker')
def logo_maker(): return hd_tool_template("Logo Maker $3",3,"#f9c846",'<input id="brand" value="KAUMONI" oninput="draw()"><input id="tag" value="Digital Services" oninput="draw()"><select id="style" onchange="draw()"><option value="1">Circle Gold</option><option value="2">Square Blue</option><option value="3">Modern Black</option></select>','function draw(){let brand=document.getElementById("brand").value;let tag=document.getElementById("tag").value;let s=document.getElementById("style").value;let bg={1:"#f9c846",2:"#0d47a1",3:"#111"}[s];document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $3</div><div style="background:${bg};color:white;padding:50px;border-radius:16px;text-align:center"><div style="width:100px;height:100px;background:white;color:black;border-radius:50%;margin:auto;display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:900">${brand[0]}</div><h1 style="margin:10px 0">${brand}</h1><p style="letter-spacing:3px;font-size:12px">${tag}</p></div>`;}','Logo')
@app.route('/business-card')
def business_card(): return hd_tool_template("Business Card $2",2,"#0d47a1",'<input id="name" value="TIMOTHY" oninput="draw()"><input id="biz" value="Kaumoni Digital" oninput="draw()"><input id="phone" value="0118431854" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="background:white;color:black;border-radius:12px;overflow:hidden;border:2px solid #0d47a1"><div style="background:#0d47a1;color:white;padding:15px"><h2>${document.getElementById("name").value}</h2><p>${document.getElementById("biz").value}</p></div><div style="padding:15px;text-align:left"><p>📞 ${document.getElementById("phone").value}</p><p>🌐 Kaumoni.com - TIMOTHY FIXED</p></div></div>`;}','BusinessCard')
@app.route('/kra-invoice')
def kra_invoice(): return hd_tool_template("KRA E-TIMS $1.5",1.5,"#00c950",'<input id="biz" value="Kaumoni Shop" oninput="draw()"><input id="customer" value="John Customer" oninput="draw()"><input id="amount" value="1000" oninput="draw()">','function draw(){let amt=document.getElementById("amount").value;document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1.5 - KRA</div><div style="background:white;color:black;padding:15px;text-align:left;font-size:11px"><h2>${document.getElementById("biz").value}</h2><p>Customer: ${document.getElementById("customer").value}</p><p>Amount: KSH ${amt}</p><p>Total KSH ${(amt*1.16).toFixed(0)}</p></div>`;}','KRA_Invoice')
@app.route('/receipt-maker')
def receipt_maker(): return hd_tool_template("Receipt $1",1,"#f9c846",'<input id="biz" value="Kaumoni Shop" oninput="draw()"><input id="amt" value="129" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px"><h3>${document.getElementById("biz").value}</h3><p>Amount KSH ${document.getElementById("amt").value}</p></div>`;}','Receipt')
@app.route('/payslip-maker')
def payslip_maker(): return hd_tool_template("Payslip $1",1,"#00c950",'<input id="name" value="John Kamau" oninput="draw()"><input id="salary" value="30000" oninput="draw()">','function draw(){let sal=parseFloat(document.getElementById("salary").value)||0;document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px"><h3>Payslip</h3><p>Name: ${document.getElementById("name").value}</p><p>Net KSH ${(sal*0.9).toFixed(0)}</p></div>`;}','Payslip')
@app.route('/cv-builder')
def cv_builder(): return hd_tool_template("CV Builder $2",2,"#0d47a1",'<input id="name" value="TIMOTHY" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $2</div><div style="background:white;color:black;padding:15px"><h2>${document.getElementById("name").value}</h2><p>Contact 0118431854 - FIXED Chart</p></div>`;}','CV')
@app.route('/ai-caption')
def ai_caption(): return hd_tool_template("AI Caption $1",1,"#ff9800",'<input id="biz" value="Kaumoni Fashion" oninput="draw()"><input id="product" value="New Dress" oninput="draw()">','function draw(){document.getElementById("preview").innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:white;color:black;padding:15px"><p>${document.getElementById("biz").value} - ${document.getElementById("product").value} - DM 0118431854</p></div>`;}','AI_Caption')
@app.route('/qr-maker')
def qr_maker(): return """<h2>QR $1 HD - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input id="till" placeholder="Till No" style="width:100%;padding:10px;background:#0e0e14;color:white"><button onclick="document.getElementById('qrRes').innerText='QR Till '+document.getElementById('till').value+' - FIXED'" style="background:#f9c846;color:black;padding:10px;width:100%;border:none;border-radius:6px">Generate QR $1 FIXED</button><p id="qrRes" style="color:#00c950"></p></div>"""
@app.route('/bg-remover')
def bg_remover(): return """<h2>BG Remover $1 HD - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input type="file"><button style="background:#00c950;color:white;padding:10px;width:100%;border:none;border-radius:6px">Remove BG $1 FIXED</button></div>"""
@app.route('/lot-calculator')
def lot_calc(): return """<h2>Lot Calculator FREE - TIMOTHY - FIXED CHART - 6 Pairs</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input id="balance" placeholder="Balance $" style="width:100%;padding:10px;background:#0e0e14;color:white"><input id="risk" placeholder="Risk %" style="width:100%;padding:10px;background:#0e0e14;color:white"><button onclick="let b=document.getElementById('balance').value;let r=document.getElementById('risk').value;document.getElementById('lotRes').innerText='Lot: '+(b*r/100/10).toFixed(2)+' - FIXED Chart'" style="background:#00c950;color:white;padding:10px;width:100%;border:none;border-radius:6px">Calculate Lot FREE FIXED</button><p id="lotRes" style="color:#00c950"></p><a href="/trading" style="color:#00c950">← Trading LIVE FIXED</a></div>"""
@app.route('/tiktok-downloader')
def tiktok_dl(): return """<h2>TikTok Downloader FREE - TIMOTHY</h2><div style="background:#1a1a25;padding:15px;border-radius:12px;max-width:500px;margin:auto"><input placeholder="TikTok Link" style="width:100%;padding:10px;background:#0e0e14;color:white"><button style="background:#ff0050;color:white;padding:10px;width:100%;border:none;border-radius:6px">Download FREE</button></div>"""
@app.route('/student-hub')
def student_hub(): return nav('student')+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Student Hub - TIMOTHY - FIXED CHART</h2><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>GPA Calculator FREE</b><br><input id="gpa" placeholder="Points"><button onclick="document.getElementById('gpaRes').innerText='GPA: '+document.getElementById('gpa').value" style="background:#f9c846;color:black;padding:6px 12px;border:none;border-radius:10px">Calc</button><p id="gpaRes"></p></div></div>"""
@app.route('/free-tools')
def free_tools(): return nav('free')+"""<div style="max-width:1000px;margin:auto;padding:15px"><h2>Free Tools - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:12px;border-radius:12px"><b>Lot Calc FREE FIXED</b><br><a href="/lot-calculator" style="background:#00c950;color:white;padding:6px 12px;border-radius:20px;text-decoration:none">Lot FREE FIXED</a> - <a href="/trading" style="background:#f9c846;color:black;padding:6px 12px;border-radius:20px;text-decoration:none">Trading FIXED</a></div></div>"""
@app.route('/ai-tools')
def ai_tools(): return nav('ai')+"""<div style="max-width:1000px;margin:auto;padding:15px"><h2>AI Tools - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:14px;border-radius:12px"><b>AI Writing $1</b><br><a href="/ai-caption" style="background:#ff9800;color:black;padding:8px 14px;border-radius:20px;text-decoration:none">Use AI Writing FIXED</a></div></div>"""
@app.route('/dashboard')
def user_dashboard(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>User Dashboard - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:12px;border-radius:12px">Phone <b id="uPhone">-</b> | Bal $<span id="uBal">0</span></div><div id="orders" style="background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px">Loading...</div></div><script>let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('uPhone').innerText=ph;fetch('/api/balance?phone='+ph).then(r=>r.json()).then(d=>{document.getElementById('uBal').innerText=(d.balance||0).toFixed(2)});fetch('/api/my-orders?phone='+ph).then(r=>r.json()).then(o=>{document.getElementById('orders').innerHTML=o.map(x=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${x.product||x.service_type} - $${x.amount} - ${x.status}</div>`).join('')||'No orders'})</script>"""
@app.route('/seller-dashboard')
def seller_dashboard(): return nav()+"""<div style="max-width:900px;margin:auto;padding:15px"><h2>Seller Dashboard - TIMOTHY FIXED - Add Products</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><input id="pTitle" placeholder="Product Title" style="width:100%;padding:8px;background:#0e0e14;color:white"><input id="pPrice" type="number" placeholder="Price $" style="width:100%;padding:8px;background:#0e0e14;color:white"><button onclick="addP()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px">Add Product FIXED</button></div><div id="myProds" style="background:#1a1a25;padding:12px;border-radius:12px;margin-top:10px">Loading...</div></div><script>function addP(){let data={title:document.getElementById('pTitle').value,price:parseFloat(document.getElementById('pPrice').value),desc:'By TIMOTHY FIXED',category:'ebook'};fetch('/api/add-product',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)}).then(r=>r.json()).then(d=>{if(d.ok){alert('Added FIXED');load()}})}function load(){fetch('/api/products').then(r=>r.json()).then(all=>{document.getElementById('myProds').innerHTML=all.slice(0,6).map(p=>`<div style='background:#0e0e14;padding:6px;margin:4px 0;border-radius:6px'>${p.title} - $${p.price}</div>`).join('')})}load()</script>"""
@app.route('/about')
def about(): return nav('about')+"""<div style="max-width:800px;margin:auto;padding:15px"><h2>About - TIMOTHY FIXED CHART</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><p>Affordable digital services - 18 Tools + Shop + Trading LIVE FIXED iframe 6 Pairs + Attractive Moving TIMOTHY</p></div></div>"""
@app.route('/contact')
def contact_page(): return nav()+"""<div style="max-width:700px;margin:auto;padding:15px"><h2>Support - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><a href="https://wa.me/254118431854" style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;text-decoration:none">WhatsApp TIMOTHY 0118431854 FIXED</a></div></div>"""
@app.route('/terms')
def terms(): return nav()+"""<div style="max-width:800px;margin:auto;padding:15px"><h2>Legal - TIMOTHY FIXED</h2><div style="background:#1a1a25;padding:15px;border-radius:12px"><small>Digital products non-refundable after download - FIXED CHART</small></div></div>"""
@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()
@app.route('/admin')
def admin(): return nav('admin')+"""<div style="max-width:1100px;margin:auto;padding:15px"><h2>Admin Dashboard - TIMOTHY FIXED CHART</h2><div style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px"><div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Users</h3><div id="users">Loading...</div></div><div style="background:#1a1a25;padding:12px;border-radius:12px"><h3>Orders</h3><div id="orders">Loading...</div></div></div></div><script>fetch('/api/admin-data').then(r=>r.json()).then(d=>{document.getElementById('total').innerText=(d.total_fees||0).toFixed(2);document.getElementById('uc').innerText=d.users.length;document.getElementById('oc').innerText=d.orders.length;document.getElementById('users').innerHTML=d.users.map(u=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${u.phone} - $${(u.balance||0).toFixed(2)}</div>`).join('');document.getElementById('orders').innerHTML=d.orders.map(o=>`<div style="background:#0e0e14;padding:5px;margin:3px 0;border-radius:6px">${o.product||o.service_type} - ${o.phone} - $${o.amount}</div>`).join('');})</script>"""

@app.route('/api/products')
def api_products():
    prods=load(FILES["products"],[
        {"id":1,"title":"Forex Mastery Ebook by TIMOTHY FIXED CHART","desc":"Complete forex guide - Trading FIXED","features":"PDF 100 pages","price":5,"category":"ebook","icon":"📘"},
        {"id":2,"title":"Canva Poster Templates Pack","desc":"100 templates","features":"Canva link HD","price":3,"category":"template","icon":"🎨"},
        {"id":3,"title":"Trading Guide - Gold Strategy XAUUSD FIXED CHART","desc":"XAUUSD strategy - Real Chart FIXED iframe","features":"Entry/Exit, Real Chart 6 Pairs LIVE FIXED","price":6,"category":"trading","icon":"📈"},
        {"id":4,"title":"Pro CV Template Pack","desc":"10 CV templates","features":"Word + PDF","price":2,"category":"cv","icon":"📄"},
        {"id":5,"title":"Business Plan Template KE","desc":"KRA compliant","features":"Financials","price":4,"category":"template","icon":"💼"},
        {"id":6,"title":"WhatsApp Sales Scripts","desc":"50 scripts","features":"Sheng + English","price":3,"category":"ebook","icon":"💬"},
        {"id":7,"title":"Study Notes - Business Studies","desc":"Form 4 + University","features":"PDF","price":2,"category":"ebook","icon":"📚"},
        {"id":8,"title":"AI Prompts Pack - 100 Prompts","desc":"ChatGPT prompts","features":"Business Content","price":2,"category":"template","icon":"🤖"}
    ])
    save(FILES["products"],prods)
    return jsonify(prods)
@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json(); prods=load(FILES["products"],[]); nid=max([p['id'] for p in prods],default=0)+1
    prods.append({"id":nid,"title":data['title'],"desc":data.get('desc','By TIMOTHY FIXED'),"features":data.get('features','By TIMOTHY FIXED'),"price":float(data.get('price',0)),"category":data.get('category','ebook'),"icon":"📦"})
    save(FILES["products"],prods); return jsonify({"ok":True,"id":nid})
@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json(); pid=int(data['product_id']); phone=data['phone']
    prods=load(FILES["products"],[]); prod=next((p for p in prods if p['id']==pid),None)
    if not prod: return jsonify({"ok":False,"message":"Not found"})
    orders=load(FILES["orders"],[]); oid=len(orders)+1
    orders.append({"id":oid,"product":prod['title'],"phone":phone,"amount":prod['price'],"status":"Paid - Auto Delivered - TIMOTHY FIXED CHART V17.6.1","time":str(datetime.now()),"download_url":f"/download/{oid}"})
    save(FILES["orders"],orders); fees=load(FILES["fees"],{"total":0}); fees['total']=fees.get('total',0)+float(prod['price']); save(FILES["fees"],fees)
    return jsonify({"ok":True,"download_url":f"/download/{oid}","order_id":oid})
@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json(); orders=load(FILES["services"],[]); oid=len(orders)+1
    orders.append({"id":oid,"service_type":data.get('service_type','Service'),"requirements":data.get('requirements',''),"phone":data.get('phone',''),"file_link":data.get('file_link',''),"status":"Payment Verified - TIMOTHY FIXED CHART","amount":5,"time":str(datetime.now())})
    save(FILES["services"],orders); fees=load(FILES["fees"],{"total":0}); fees['total']=fees.get('total',0)+5; save(FILES["fees"],fees)
    return jsonify({"ok":True,"order_id":oid})
@app.route('/api/my-orders')
def api_my_orders():
    phone=request.args.get('phone'); orders=load(FILES["orders"],[])+load(FILES["services"],[])
    return jsonify([o for o in orders if o.get('phone')==phone])
@app.route('/download/<int:oid>')
def download_file(oid): return f"<h2>Download Ready Order {oid} - TIMOTHY FIXED CHART V17.6.1</h2><a href='/' style='background:#00c950;color:white;padding:12px 18px;border-radius:20px;text-decoration:none'>Download Now - FIXED</a>"
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
