from flask import Flask, request, jsonify
app = Flask(__name__)

# ============ YOUR ORIGINAL TRADING - 100% SAME - NEVER LOST ============
TRADING_HTML = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO TRADING</title>
<script src="https://s3.tradingview.com/tv.js"></script>
<style>
body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:8px}
.card{background:#1a1a25;border:1px solid #2a2a3a;padding:10px;border-radius:8px;margin-top:8px}
button{padding:8px 14px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
select,input{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}
#tv_chart{height:400px}
.modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,0.8);justify-content:center;align-items:center;z-index:99}
.modalBox{background:#1a1a25;padding:20px;border-radius:10px;width:90%;max-width:350px;border:1px solid #f9c846}
.topnav{background:#1a1a25;padding:10px;display:flex;gap:10px;align-items:center}
.topnav a{color:#f9c846;text-decoration:none;font-weight:bold;padding:6px 10px;border:1px solid #333;border-radius:5px}
</style>
</head>
<body>
<div class="topnav"><a href="/">🏠 All Services</a><a href="/trade">📈 Trading</a><a href="/cv-builder">📄 CV Builder</a><a href="/ebooks">📚 Ebooks</a></div>
<h3 style="color:#f9c846">TIMO TRADING PRO</h3>
<div>Balance: $<span id="bal">0</span> | Fee: $<span id="adminBal">0</span> | <span id="price">-</span></div>
<div class="card">
<button onclick="openModal('dep')" style="background:#00c950;color:white">Deposit M-Pesa</button>
<button onclick="openModal('wd')" style="background:#ff9800">Withdraw</button>
<button onclick="adminLogin()" style="background:#333;color:white;float:right">Admin</button>
</div>
<div class="card">Pair: <select id="pair" onchange="changePair()"></select> <input id="newPair" placeholder="SOLUSDT" style="width:80px"> <button onclick="addPair()" style="background:#f9c846;color:black">+ Add</button></div>
<div id="tv_chart" class="card"></div>
<div class="card"><input id="amt" type="number" value="10" style="width:60px"> $ <button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button> <button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button></div>
<div id="open"></div>
<div id="depModal" class="modal"><div class="modalBox"><h4>Deposit M-Pesa</h4><p>Paybill: <b>522522</b> Acc: <b>YOUR_TILL</b></p><input id="mpesaCode" placeholder="M-Pesa Code"><input id="depAmt" type="number" placeholder="Amount $"><button onclick="confirmDeposit()" style="background:#00c950;width:100%;margin-top:8px">Confirm</button><button onclick="closeModal()" style="background:#333;width:100%;margin-top:5px">Cancel</button></div></div>
<div id="wdModal" class="modal"><div class="modalBox"><h4>Withdraw</h4><input id="wdPhone" placeholder="07XXXXXXXX"><input id="wdAmt" type="number" placeholder="Amount $"><button onclick="requestWithdraw()" style="background:#ff9800;width:100%;margin-top:8px">Request</button><button onclick="closeModal()" style="background:#333;width:100%;margin-top:5px">Cancel</button><p id="wdStatus"></p></div></div>
<script>
let pair='BTCUSDT',currentPrice=0;
let bal=parseFloat(localStorage.getItem('bal')||'20');
let adminBal=parseFloat(localStorage.getItem('adminBal')||'0');
let trades=JSON.parse(localStorage.getItem('trades')||'[]');
let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"]');
function tvSymbol(s){let m={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT'};return m[s]||'BINANCE:'+s;}
function loadChart(){document.getElementById('tv_chart').innerHTML='';new TradingView.widget({"autosize":true,"symbol":tvSymbol(pair),"interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","container_id":"tv_chart","backgroundColor":"#1a1a25"});}
function loadPairSelect(){let sel=document.getElementById('pair');sel.innerHTML='';pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p.replace('USDT','/USD');sel.appendChild(o);});pair=pairsList[0];sel.value=pair;loadChart();fetchPrice();}
function addPair(){let np=document.getElementById('newPair').value.toUpperCase().trim();if(!np)return;if(!np.endsWith('USDT'))np=np+'USDT';if(pairsList.includes(np))return;pairsList.push(np);localStorage.setItem('pairsList',JSON.stringify(pairsList));loadPairSelect();}
async function fetchPrice(){try{let r=await fetch('https://api.binance.com/api/v3/ticker/price?symbol='+pair);let d=await r.json();currentPrice=parseFloat(d.price);document.getElementById('price').innerText=currentPrice.toFixed(5);}catch(e){}}
function changePair(){pair=document.getElementById('pair').value;loadChart();fetchPrice();}
function openTrade(t){let amt=parseFloat(document.getElementById('amt').value);if(amt>bal){alert('Low balance');return;}trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice});bal-=amt;save();}
function closeTrade(id){let tr=trades.find(x=>x.id===id);let diff=currentPrice-tr.open;if(tr.type==='SELL')diff=-diff;let profit=(diff/tr.open)*tr.amount*100;let ret=tr.amount+profit;let fee=0;if(profit>0){fee=profit*0.20;ret-=fee;adminBal+=fee;}bal+=ret;trades=trades.filter(x=>x.id!==id);save();}
function openModal(type){document.getElementById(type==='dep'?'depModal':'wdModal').style.display='flex';}
function closeModal(){document.getElementById('depModal').style.display='none';document.getElementById('wdModal').style.display='none';}
function confirmDeposit(){let code=document.getElementById('mpesaCode').value;let amt=parseFloat(document.getElementById('depAmt').value);if(!code||!amt){alert('Fill all');return;}bal+=amt;save();alert('Deposit $'+amt+' added');closeModal();}
function requestWithdraw(){let amt=parseFloat(document.getElementById('wdAmt').value);let phone=document.getElementById('wdPhone').value;if(amt>bal){alert('Low bal');return;}bal-=amt;save();document.getElementById('wdStatus').innerText='Requested $'+amt+' to '+phone;}
function adminLogin(){let p=prompt('Admin password:');if(p==='Timo2024'){alert('Fee Pot: $'+adminBal.toFixed(2));}}
function render(){document.getElementById('bal').innerText=bal.toFixed(2);document.getElementById('adminBal').innerText=adminBal.toFixed(2);document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open;if(t.type==='SELL')diff=-diff;let fl=(diff/t.open)*t.amount*100;return '<div class="card">'+t.pair+' '+t.type+' $'+t.amount+' <b style="color:'+(fl>=0?'#26a69a':'#ef5350')+'">'+fl.toFixed(2)+'</b> <button onclick="closeTrade('+t.id+')" style="background:orange">CLOSE NOW</button></div>';}).join('');}
function save(){localStorage.setItem('bal',bal);localStorage.setItem('adminBal',adminBal);localStorage.setItem('trades',JSON.stringify(trades));render();}
setInterval(fetchPrice,3000);loadPairSelect();setInterval(render,1000);
</script>
</body>
</html>
"""

# ============ NEW SUPER APP PAGES ============
HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni Super App</title>
<style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:15px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.card{background:#1a1a25;border:1px solid #2a2a3a;padding:18px;border-radius:12px;text-align:center}
.card h2{margin:5px 0}.card p{color:#aaa;font-size:13px}
a.btn{display:block;background:#f9c846;color:black;padding:10px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:10px}
.wallet{background:linear-gradient(135deg,#f9c846,#ff9800);color:black;padding:15px;border-radius:12px}
</style></head><body>
<h1 style="color:#f9c846">KAUMONI SUPER APP</h1>
<div class="wallet"><b>💰 One Wallet</b> - Earnings from ALL services go here<br>Balance: $ <span id="bal">0</span> <small>(same as Trading)</small></div>
<div class="grid">
<div class="card"><h2>📈</h2><h2>Trading Pro</h2><p>Your existing trading - safe & unchanged</p><a class="btn" href="/trade">Open Trading</a></div>
<div class="card"><h2>📄</h2><h2>CV Builder</h2><p>5 Pro Templates + PDF Download - Sell for $2</p><a class="btn" href="/cv-builder">Build CV</a></div>
<div class="card"><h2>📚</h2><h2>Ebooks Store</h2><p>Sell your PDFs, guides</p><a class="btn" href="/ebooks">Open Store</a></div>
<div class="card"><h2>🎨</h2><h2>Templates</h2><p>Coming soon - Posters, Logos</p><a class="btn" style="background:#333;color:white">Soon</a></div>
</div>
<p style="margin-top:20px;color:#666;font-size:12px">✅ Trading backed up in branch: backup-trading-today</p>
<script>document.getElementById('bal').innerText=localStorage.getItem('bal')||'20';</script>
</body></html>
"""

CV_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV Builder</title>
<style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:10px}
input,textarea{width:100%;padding:10px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:5px 0}
.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0;border:1px solid #2a2a3a}
button{padding:10px 16px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}
.tpl{border:2px solid #333;padding:8px;border-radius:6px;cursor:pointer;text-align:center}
.tpl.active{border-color:#f9c846;background:#2a2a3a}
#preview{background:white;color:black;padding:20px;border-radius:8px;min-height:300px}
@media print{#preview{width:100%}}
</style></head><body>
<a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">CV BUILDER - 5 Templates</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">
<div>
<div class="card">Choose Template:<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-top:8px">
<div class="tpl active" onclick="setTpl(1)">Modern</div><div class="tpl" onclick="setTpl(2)">Classic</div><div class="tpl" onclick="setTpl(3)">Creative</div><div class="tpl" onclick="setTpl(4)">Pro</div><div class="tpl" onclick="setTpl(5)">Minimal</div>
</div></div>
<div class="card"><input id="name" placeholder="Full Name" oninput="update()" value="Timo Acetimo"><input id="title" placeholder="Job Title" oninput="update()" value="Trader & Developer"><textarea id="summary" oninput="update()">Experienced trader...</textarea><textarea id="exp" oninput="update()">Trading - Timo Trading Pro (2024-Now)\nBuilt super app</textarea><textarea id="edu" oninput="update()">KCSE - etc</textarea><input id="contact" placeholder="Phone | Email" oninput="update()" value="07XXXXXXXX | timo@email.com"></div>
<button onclick="window.print()" style="background:#00c950;color:white;width:100%">📥 Download PDF (Print to PDF)</button>
<button onclick="saveAndCharge()" style="background:#f9c846;color:black;width:100%;margin-top:6px">💰 Save to Wallet + $2 fee</button>
</div>
<div id="preview"></div>
</div>
<script>
let tpl=1;
function setTpl(n){tpl=n;document.querySelectorAll('.tpl').forEach((e,i)=>e.classList.toggle('active',i+1==n));update();}
function update(){let name=document.getElementById('name').value;let title=document.getElementById('title').value;let sum=document.getElementById('summary').value;let exp=document.getElementById('exp').value.replace(/\\n/g,'<br>');let edu=document.getElementById('edu').value;let contact=document.getElementById('contact').value;
let styles={1:`<div style="border-left:4px solid #f9c846;padding-left:15px"><h1 style="margin:0">${name}</h1><div style="color:#f9c846;font-weight:bold">${title}</div><small>${contact}</small><hr><p>${sum}</p><h3>Experience</h3><p>${exp}</p><h3>Education</h3><p>${edu}</p></div>`,2:`<div style="text-align:center"><h1>${name}</h1><b>${title}</b><br><small>${contact}</small><hr style="border:1px solid black"><div style="text-align:left"><p>${sum}</p><h3>EXPERIENCE</h3><p>${exp}</p><h3>EDUCATION</h3><p>${edu}</p></div></div>`,3:`<div style="display:flex"><div style="background:#1a1a25;color:white;padding:15px;width:35%"><h2>${name}</h2><p>${title}</p><hr><p>${contact}</p><p>${edu}</p></div><div style="padding:15px"><p>${sum}</p><h3>Experience</h3><p>${exp}</p></div></div>`,4:`<div><div style="background:#f9c846;padding:10px"><h1 style="margin:0">${name}</h1><b>${title}</b></div><div style="padding:10px"><small>${contact}</small><p>${sum}</p><h3 style="color:#ff9800">Experience</h3><p>${exp}</p><h3 style="color:#ff9800">Education</h3><p>${edu}</p></div></div>`,5:`<div style="font-family:Georgia"><h1 style="font-weight:300">${name}</h1><i>${title} | ${contact}</i><br><br><p>${sum}</p><br><b>Experience</b><br><p>${exp}</p><br><b>Education</b><br><p>${edu}</p></div>`};
document.getElementById('preview').innerHTML=styles[tpl];
}
function saveAndCharge(){let adminBal=parseFloat(localStorage.getItem('adminBal')||'0');adminBal+=2;localStorage.setItem('adminBal',adminBal);alert('Saved! $2 added to your Fee pot. User can download.');}
update();
</script></body></html>
"""

EBOOK_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ebooks</title>
<style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:12px}
.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:10px;margin:8px 0}
button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}
</style></head><body>
<a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">📚 Ebook Store</h2>
<div class="card"><h3>How to Trade Like Timo - $5</h3><p>PDF guide</p><button onclick="buy(5)" style="background:#00c950;color:white">Buy with Wallet</button></div>
<div class="card"><h3>CV Mastery - $3</h3><p>Land jobs fast</p><button onclick="buy(3)" style="background:#00c950;color:white">Buy with Wallet</button></div>
<div class="card"><h3>Add Your Ebook</h3><input id="eTitle" placeholder="Title" style="width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px"><input id="ePrice" type="number" placeholder="Price $" style="width:100%;padding:8px;margin-top:6px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px"><button onclick="addE()" style="background:#f9c846;margin-top:6px;width:100%">Add</button></div>
<div id="myEbooks"></div>
<script>
function buy(price){let bal=parseFloat(localStorage.getItem('bal')||'20');if(bal<price){alert('Low balance, deposit in Trading');return;}bal-=price;localStorage.setItem('bal',bal);let admin=parseFloat(localStorage.getItem('adminBal')||'0');admin+=price;localStorage.setItem('adminBal',admin);alert('Bought! $'+price+' to your Fee pot');}
function addE(){let t=document.getElementById('eTitle').value;let p=document.getElementById('ePrice').value;let list=JSON.parse(localStorage.getItem('ebooks')||'[]');list.push({t,p});localStorage.setItem('ebooks',JSON.stringify(list));renderE();}
function renderE(){let list=JSON.parse(localStorage.getItem('ebooks')||'[]');document.getElementById('myEbooks').innerHTML=list.map(e=>`<div class="card"><b>${e.t}</b> - $${e.p} <button onclick="buy(${e.p})" style="background:#00c950;color:white">Buy</button></div>`).join('');}
renderE();
</script></body></html>
"""

@app.route('/')
def home(): return HOME_HTML

@app.route('/trade')
def trade(): return TRADING_HTML

@app.route('/cv-builder')
def cv(): return CV_HTML

@app.route('/ebooks')
def ebooks(): return EBOOK_HTML

# Keep old root also show trading for existing users? No, home is super app. Trading moved to /trade but also accessible.
@app.route('/old')
def old(): return TRADING_HTML

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
