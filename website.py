
from flask import Flask, request, jsonify, send_from_directory
import os, json
from werkzeug.utils import secure_filename
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'ebooks_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
USERS_FILE = 'users.json'
DEPOSITS_FILE = 'deposits.json'
FEES_FILE = 'fees.json'

def load_json(f, default):
    if not os.path.exists(f):
        return default
    try:
        with open(f) as jf:
            return json.load(jf)
    except:
        return default

def save_json(f, data):
    with open(f,'w') as jf:
        json.dump(data, jf)

TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>TIMO TRADING V5</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:8px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:10px;border-radius:8px;margin-top:8px}button{padding:8px 14px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}select,input{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}#tv_chart{height:400px}.topnav{background:#1a1a25;padding:10px;display:flex;gap:8px;overflow:auto}.topnav a{color:#f9c846;text-decoration:none;font-weight:bold;padding:6px 10px;border:1px solid #333;border-radius:5px;white-space:nowrap}.login{position:fixed;top:0;left:0;width:100%;height:100%;background:#0e0e14;z-index:100;display:flex;justify-content:center;align-items:center}</style></head><body>
<div id="loginBox" class="login"><div class="card" style="width:90%;max-width:350px;border:1px solid #f9c846"><h3 style="color:#f9c846">🔐 Login</h3><p style="font-size:12px;color:#aaa">Enter phone - balance saved on server</p><input id="phoneInput" placeholder="07XXXXXXXX" style="width:100%"><button onclick="login()" style="background:#f9c846;color:black;width:100%;margin-top:10px">Login / Register</button></div></div>
<div class="topnav"><a href="/">🏠 Home</a><a href="/trade">📈 Trade</a><a href="/poster-maker">🎨 Poster</a><a href="/receipt-maker">🧾 Receipt</a><a href="/cv-builder">📄 CV</a><a href="/logo-maker">💼 Logo</a><a href="/admin">👑 Admin</a></div>
<h3 style="color:#f9c846">TIMO TRADING V5 - REAL MONEY</h3><div>Hi: <b id="userPhone">-</b> | Bal: $<span id="bal">0</span> <button onclick="logout()" style="background:#333;color:white;padding:4px 8px;font-size:10px">Logout</button> | Price: <span id="price">-</span></div><div class="card"><button onclick="openDep()" style="background:#00c950;color:white">💰 Deposit M-Pesa</button><button onclick="loadBal()" style="background:#333;color:white">Refresh</button><span id="feeInfo" style="float:right;color:#f9c846;font-size:12px"></span></div><div class="card">Pair: <select id="pair" onchange="changePair()"></select> <input id="newPair" placeholder="SOLUSDT" style="width:80px"> <button onclick="addPair()" style="background:#f9c846;color:black">+ Add</button></div><div id="tv_chart" class="card"></div><div class="card"><input id="amt" type="number" value="10" style="width:60px"> $ <button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button> <button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button> <small style="color:#aaa">20% fee on profit to Kaumoni</small></div><div id="open"></div>
<div id="depBox" class="card" style="display:none;border:1px solid #00c950"><h4>Deposit M-Pesa</h4><p>Pay to Till: <b>YOUR_TILL_HERE</b> (edit code!)</p><input id="mpesaCode" placeholder="M-Pesa Code QGH..."><input id="depAmt" type="number" placeholder="Amount $"><button onclick="requestDep()" style="background:#00c950;width:100%;margin-top:6px">Submit</button><p id="depStatus" style="font-size:12px"></p></div>
<script>let pair='BTCUSDT',currentPrice=0;let trades=JSON.parse(localStorage.getItem('trades_v5')||'[]');let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"]');let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;function login(){let p=document.getElementById('phoneInput').value.trim();if(p.length<9){alert('Enter phone');return;}localStorage.setItem('userPhone_v5',p);userPhone=p;document.getElementById('loginBox').style.display='none';loadBal();}function logout(){localStorage.removeItem('userPhone_v5');location.reload();}async function loadBal(){if(!userPhone){document.getElementById('loginBox').style.display='flex';return;}document.getElementById('userPhone').innerText=userPhone;let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('bal').innerText=userBal.toFixed(2);document.getElementById('feeInfo').innerText='Fee to Kaumoni: $'+(d.total_fee||0);}function openDep(){document.getElementById('depBox').style.display='block';}async function requestDep(){let code=document.getElementById('mpesaCode').value, amt=parseFloat(document.getElementById('depAmt').value);if(!code||!amt)return alert('Fill');let res=await fetch('/api/deposit-request',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,code:code,amount:amt})});let d=await res.json();document.getElementById('depStatus').innerText=d.message;}function tvSymbol(s){let m={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT'};return m[s]||'BINANCE:'+s;}function loadChart(){document.getElementById('tv_chart').innerHTML='';new TradingView.widget({"autosize":true,"symbol":tvSymbol(pair),"interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","container_id":"tv_chart","backgroundColor":"#1a1a25"});}function loadPairSelect(){let sel=document.getElementById('pair');sel.innerHTML='';pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p.replace('USDT','/USD');sel.appendChild(o);});pair=pairsList[0];sel.value=pair;loadChart();fetchPrice();}function addPair(){let np=document.getElementById('newPair').value.toUpperCase().trim();if(!np)return;if(!np.endsWith('USDT'))np=np+'USDT';if(pairsList.includes(np))return;pairsList.push(np);localStorage.setItem('pairsList',JSON.stringify(pairsList));loadPairSelect();}async function fetchPrice(){try{let r=await fetch('https://api.binance.com/api/v3/ticker/price?symbol='+pair);let d=await r.json();currentPrice=parseFloat(d.price);document.getElementById('price').innerText=currentPrice.toFixed(5);}catch(e){}}function changePair(){pair=document.getElementById('pair').value;loadChart();fetchPrice();}async function openTrade(t){let amt=parseFloat(document.getElementById('amt').value);if(amt>userBal){alert('Low bal $'+userBal+' - Deposit first');openDep();return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:amt,reason:'open_trade'})});let d=await res.json();if(!d.ok){alert(d.message);return;}trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice});localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}async function closeTrade(id){let tr=trades.find(x=>x.id===id);if(!tr)return;let diff=currentPrice-tr.open;if(tr.type==='SELL')diff=-diff;let profit=(diff/tr.open)*tr.amount*100;let ret=tr.amount+profit;let fee=0;if(profit>0){fee=profit*0.20;ret-=fee;await fetch('/api/add-fee',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,fee:fee})});}await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:ret})});trades=trades.filter(x=>x.id!==id);localStorage.setItem('trades_v5',JSON.stringify(trades));loadBal();render();}function render(){document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open;if(t.type==='SELL')diff=-diff;let fl=(diff/t.open)*t.amount*100;return '<div class="card">'+t.pair+' '+t.type+' $'+t.amount+' <b style="color:'+(fl>=0?'#26a69a':'#ef5350')+'">'+fl.toFixed(2)+'</b> <button onclick="closeTrade('+t.id+')" style="background:orange">CLOSE</button></div>';}).join('');}setInterval(fetchPrice,3000);if(userPhone){document.getElementById('loginBox').style.display='none';loadBal();}loadPairSelect();setInterval(render,1000);</script></body></html>
"""

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni V5</title><style>body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:15px}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:15px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:16px;border-radius:12px;text-align:center}a.btn{display:block;background:#f9c846;color:black;padding:8px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:8px;font-size:13px}.wallet{background:linear-gradient(135deg,#f9c846,#ff9800);color:black;padding:12px;border-radius:12px}</style></head><body>
<h1 style="color:#f9c846;margin:0">KAUMONI V5 - REAL MONEY</h1><p style="color:#888;font-size:12px">Balance on SERVER - share safely!</p><div class="wallet"><b>💰 Balance:</b> $ <span id="bal">0</span> | Phone: <span id="phone">Not logged</span><br><small><a href="/admin" style="color:black;font-weight:bold">👑 Admin</a></small></div>
<div class="grid">
<div class="card"><div style="font-size:28px">📈</div><h3>Trading</h3><p>20% fee to you</p><a class="btn" href="/trade">Trade</a></div>
<div class="card"><div style="font-size:28px">🎨</div><h3>Poster</h3><p>$1</p><a class="btn" href="/poster-maker">Create</a></div>
<div class="card"><div style="font-size:28px">🧾</div><h3>Receipt</h3><p>$1</p><a class="btn" href="/receipt-maker">Make</a></div>
<div class="card"><div style="font-size:28px">📄</div><h3>CV</h3><p>$2</p><a class="btn" href="/cv-builder">Build</a></div>
<div class="card"><div style="font-size:28px">💼</div><h3>Logo</h3><p>$3</p><a class="btn" href="/logo-maker">Design</a></div>
<div class="card"><div style="font-size:28px">📡</div><h3>Signals</h3><p>$10</p><a class="btn" href="/signals">Join</a></div>
<div class="card"><div style="font-size:28px">📚</div><h3>Ebooks</h3><p>Sell</p><a class="btn" href="/ebooks">Store</a></div>
<div class="card"><div style="font-size:28px">✉️</div><h3>Cover</h3><p>$1</p><a class="btn" href="/cover-letter">Write</a></div>
</div><div class="card" style="margin-top:15px"><input id="loginPhone" placeholder="07XXXXXXXX" style="width:70%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px"><button onclick="login()" style="background:#f9c846;color:black;padding:8px 12px;border:none;border-radius:5px;font-weight:bold">Login</button></div><script>let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('phone').innerText=ph||'Not logged';async function check(){if(!ph)return;let res=await fetch('/api/balance?phone='+ph);let d=await res.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}function login(){let p=document.getElementById('loginPhone').value;if(!p)return;localStorage.setItem('userPhone_v5',p);location.reload();}check();</script></body></html>
"""

POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster V5</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px;margin:0}input,select{width:100%;padding:9px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box}.gallery{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:15px}.mini{width:100%;height:140px;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:5px;box-sizing:border-box;border-radius:6px;font-size:10px;overflow:hidden}.history-card{background:#1a1a25;padding:8px;border-radius:8px;border:1px solid #333}</style></head><body><a href="/" style="color:#f9c846">← Home</a> <a href="/admin" style="color:#f9c846;float:right">👑 Admin</a><h2 style="color:#f9c846">🎨 Poster V5 - Pay $1</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px"><div><div class="card"><p>Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">🔥 Sale - Red</option><option value="2">✨ Salon - Pink</option><option value="3">⛪ Church - Blue</option><option value="4">🎉 Event - Yellow</option><option value="5">🍔 Food - Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XXXXXXXX" oninput="draw()"><input id="loc" value="Nairobi CBD" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%">📥 Pay $1 & Download HD</button><button onclick="shareCurrent()" style="background:#25D366;color:white;width:100%;margin-top:6px">📲 Share WA</button></div><div id="poster"></div></div><h3 style="color:#f9c846;margin-top:25px">📚 Saved (<span id="count">0</span>)</h3><div id="gallery" class="gallery"></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){if(!userPhone){alert('Login first');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let t=document.getElementById('tpl').value;let title=document.getElementById('title').value;let sub=document.getElementById('sub').value;let phone=document.getElementById('phone').value;let loc=document.getElementById('loc').value;let colors={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']};let c=colors[t];document.getElementById('poster').innerHTML=`<div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px;box-sizing:border-box"><h1 style="font-size:42px;margin:0;text-transform:uppercase">${title}</h1><h2 style="margin:10px 0;font-size:20px">${sub}</h2><div style="background:black;color:white;padding:8px 15px;border-radius:20px;margin-top:20px"><b>${phone}</b><br><small>${loc}</small></div></div>`;}async function downloadPoster(){if(userBal<1){alert('Low bal $'+userBal+' - Deposit in /trade');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await res.json();if(!d.ok){alert(d.message);return;}let title=document.getElementById('title').value;let posterEl=document.getElementById('poster');html2canvas(posterEl,{scale:2}).then(canvas=>{let link=document.createElement('a');link.download=title+'_poster.png';link.href=canvas.toDataURL();link.click();saveHistory();loadBal();});}function shareCurrent(){let posterEl=document.getElementById('poster');html2canvas(posterEl,{scale:2}).then(canvas=>{canvas.toBlob(blob=>{let file=new File([blob],'poster.png',{type:'image/png'});if(navigator.canShare && navigator.canShare({files:[file]})){navigator.share({files:[file],title:'Poster',text:document.getElementById('title').value});}else{window.open('https://wa.me/?text='+encodeURIComponent(document.getElementById('title').value+' '+window.location.href),'_blank');}},'image/png');});}function saveHistory(){let hist=JSON.parse(localStorage.getItem('poster_history')||'[]');hist.unshift({id:Date.now(),title:document.getElementById('title').value,date:new Date().toLocaleString(),tpl:document.getElementById('tpl').value});localStorage.setItem('poster_history',JSON.stringify(hist));renderGallery();}function renderGallery(){let hist=JSON.parse(localStorage.getItem('poster_history')||'[]');document.getElementById('count').innerText=hist.length;let colors={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']};document.getElementById('gallery').innerHTML=hist.map(h=>{let c=colors[h.tpl]||colors[1];return `<div class="history-card"><div class="mini" style="background:linear-gradient(135deg,${c[0]},${c[1]})"><b>${h.title}</b></div><small>${h.date}</small></div>`}).join('')||'<p>No posters</p>';}draw();renderGallery();loadBal();</script></body></html>"""

CV_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>CV V5</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,textarea{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:4px 0}.card{background:#1a1a25;padding:12px;border-radius:8px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold}#preview{background:white;color:black;padding:20px;border-radius:8px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">📄 CV V5 - Pay $2</h2><div class="card">Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></div><div style="display:grid;grid-template-columns:1fr 1fr;gap:15px"><div><div class="card"><input id="name" value="Timo" oninput="update()"><input id="title" value="Trader" oninput="update()"><textarea id="summary" oninput="update()">Experienced...</textarea></div><button onclick="downloadCV()" style="background:#00c950;color:white;width:100%">Pay $2 & Download</button></div><div id="preview"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;document.getElementById('uBal').innerText=userBal.toFixed(2);}function update(){document.getElementById('preview').innerHTML=`<h1>${document.getElementById('name').value}</h1><b>${document.getElementById('title').value}</b><p>${document.getElementById('summary').value}</p>`;}async function downloadCV(){if(userBal<2){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:2,reason:'cv'})});let d=await res.json();if(!d.ok){alert(d.message);return;}let el=document.getElementById('preview');html2canvas(el,{scale:2}).then(c=>{let a=document.createElement('a');a.download='CV.png';a.href=c.toDataURL();a.click();});loadBal();}update();loadBal();</script></body></html>"""

COVER_HTML = CV_HTML.replace('CV V5','Cover V5').replace('📄','✉️').replace('Pay $2','Pay $1').replace("'cv'","'cover'").replace('2,reason','1,reason')
LOGO_HTML = CV_HTML.replace('CV V5','Logo V5').replace('📄','💼').replace('Pay $2','Pay $3').replace("'cv'","'logo'").replace('2,reason','3,reason')
SIGNALS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Signals V5</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:10px;margin:8px 0}button{padding:10px;border:none;border-radius:6px;font-weight:bold}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">📡 VIP Signals - $10</h2><div class="card">Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></div><div class="card"><button onclick="join()" style="background:#f9c846;color:black;width:100%">Pay $10 & Join VIP</button><p id="status"></p></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;document.getElementById('uBal').innerText=userBal.toFixed(2);}async function join(){if(userBal<10){alert('Deposit');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}document.getElementById('status').innerText='VIP Active!';loadBal();}loadBal();</script></body></html>"""

EBOOK_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ebooks V5</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:10px;margin:8px 0}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}input{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">📚 Ebooks V5</h2><div class="card">Phone: <b id="uPhone">-</b> Bal: $<span id="uBal">0</span></div><div id="ebookList">Loading...</div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){let res=await fetch('/api/balance?phone='+userPhone);let d=await res.json();userBal=d.balance||0;document.getElementById('uPhone').innerText=userPhone;document.getElementById('uBal').innerText=userBal.toFixed(2);}async function loadEbooks(){let res=await fetch('/api/ebooks');let data=await res.json();document.getElementById('ebookList').innerHTML=data.map(e=>`<div class="card"><h3>${e.title} - $${e.price}</h3><button onclick="buyEbook('${e.filename}','${e.title}',${e.price})" style="background:#00c950;color:white">Buy $${e.price}</button></div>`).join('')||'No ebooks';}async function buyEbook(filename,title,price){if(userBal<price){alert('Low bal');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:price,reason:'ebook'})});let d=await res.json();if(!d.ok){alert(d.message);return;}window.location='/download/'+filename;loadBal();}loadBal();loadEbooks();</script></body></html>"""

ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin V5</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px;margin:0}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:8px 0}.big{font-size:22px;font-weight:bold;color:#f9c846} button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2 style="color:#f9c846">👑 ADMIN V5 - REAL MONEY</h2><div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><div>Total Fees (Server)</div><div class="big" id="total">$0</div><div id="userCount">0 users</div></div><div class="card" style="border:1px solid #00c950"><h3>💰 Pending Deposits</h3><div id="depList">Loading...</div></div><div class="card"><h3>👥 Users</h3><div id="usersList">Loading...</div></div><div class="card"><button onclick="load()" style="background:#f9c846;color:black">Refresh</button></div><script>async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText='$'+(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} - Bal: $${u.balance} - Fees: $${u.total_fee||0}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add $</button></div>`).join('')||'No users';document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div class="card" style="background:#2a2a3a"><b>${d.phone}</b> - $${d.amount} - Code: ${d.code} - ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white;margin-top:5px">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';}async function approveDep(idx){let res=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function rejectDep(idx){let res=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:idx})});let d=await res.json();alert(d.message);load();}async function addBal(phone){let amt=prompt('Amount to add to '+phone);if(!amt)return;let res=await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:phone,amount:parseFloat(amt)})});let d=await res.json();alert(d.message);load();}load();setInterval(load,5000);</script></body></html>
"""

@app.route('/')
def home(): return HOME_HTML
@app.route('/trade')
def trade(): return TRADING_HTML
@app.route('/poster-maker')
def poster(): return POSTER_HTML
@app.route('/receipt-maker')
def receipt(): return POSTER_HTML.replace('Poster V5','Receipt V5').replace('🎨','🧾').replace('Pay $1 & Download HD','Pay $1 & Download Receipt')
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

@app.route('/api/balance')
def api_balance():
    phone = request.args.get('phone')
    users = load_json(USERS_FILE, {})
    u = users.get(phone, {"phone":phone,"balance":0,"total_fee":0})
    return jsonify(u)

@app.route('/api/deposit-request', methods=['POST'])
def api_deposit_request():
    data = request.get_json()
    deposits = load_json(DEPOSITS_FILE, [])
    deposits.append({"phone":data['phone'],"code":data['code'],"amount":float(data['amount']),"status":"pending","time":str(datetime.now())})
    save_json(DEPOSITS_FILE, deposits)
    users = load_json(USERS_FILE, {})
    if data['phone'] not in users:
        users[data['phone']] = {"phone":data['phone'],"balance":0,"total_fee":0,"joined":str(datetime.now())}
        save_json(USERS_FILE, users)
    return jsonify({"ok":True,"message":"Request sent! Admin will approve after M-Pesa check."})

@app.route('/api/add-balance', methods=['POST'])
def api_add_balance():
    data = request.get_json()
    users = load_json(USERS_FILE, {})
    phone = data['phone']
    if phone not in users:
        users[phone] = {"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance'] = float(users[phone].get('balance',0)) + float(data['amount'])
    save_json(USERS_FILE, users)
    return jsonify({"ok":True,"message":f"Added ${data['amount']} to {phone}"})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data = request.get_json()
    users = load_json(USERS_FILE, {})
    phone = data['phone']
    amt = float(data['amount'])
    if phone not in users or float(users[phone].get('balance',0)) < amt:
        return jsonify({"ok":False,"message":f"Low balance. Have ${users.get(phone,{}).get('balance',0)}, need ${amt}. Deposit first."})
    users[phone]['balance'] -= amt
    if 'poster' in data.get('reason','') or 'cv' in data.get('reason','') or 'logo' in data.get('reason','') or 'vip' in data.get('reason','') or 'ebook' in data.get('reason','') or 'cover' in data.get('reason','') or 'receipt' in data.get('reason',''):
        users[phone]['total_fee'] = users[phone].get('total_fee',0) + amt
        fees = load_json(FEES_FILE, {"total":0})
        fees['total'] = fees.get('total',0) + amt
        save_json(FEES_FILE, fees)
    save_json(USERS_FILE, users)
    return jsonify({"ok":True,"message":"Deducted","balance":users[phone]['balance']})

@app.route('/api/add-fee', methods=['POST'])
def api_add_fee():
    data = request.get_json()
    fees = load_json(FEES_FILE, {"total":0})
    fees['total'] = fees.get('total',0) + float(data['fee'])
    save_json(FEES_FILE, fees)
    users = load_json(USERS_FILE, {})
    if data['phone'] in users:
        users[data['phone']]['total_fee'] = users[data['phone']].get('total_fee',0) + float(data['fee'])
        save_json(USERS_FILE, users)
    return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users = load_json(USERS_FILE, {})
    deposits = load_json(DEPOSITS_FILE, [])
    fees = load_json(FEES_FILE, {"total":0})
    return jsonify({"users":list(users.values()),"deposits":deposits,"total_fees":fees.get('total',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    data = request.get_json()
    idx = int(data['index'])
    deposits = load_json(DEPOSITS_FILE, [])
    if idx >= len(deposits): return jsonify({"message":"Invalid"})
    dep = deposits[idx]
    if dep['status']!= 'pending': return jsonify({"message":"Already processed"})
    users = load_json(USERS_FILE, {})
    phone = dep['phone']
    if phone not in users:
        users[phone] = {"phone":phone,"balance":0,"total_fee":0}
    users[phone]['balance'] += float(dep['amount'])
    save_json(USERS_FILE, users)
    deposits[idx]['status'] = 'approved'
    save_json(DEPOSITS_FILE, deposits)
    return jsonify({"message":f"Approved! Added ${dep['amount']} to {phone}"})

@app.route('/api/reject-deposit', methods=['POST'])
def api_reject():
    data = request.get_json()
    idx = int(data['index'])
    deposits = load_json(DEPOSITS_FILE, [])
    deposits[idx]['status'] = 'rejected'
    save_json(DEPOSITS_FILE, deposits)
    return jsonify({"message":"Rejected"})

@app.route('/api/ebooks')
def api_ebooks():
    files = []
    if os.path.exists(UPLOAD_FOLDER):
        for f in os.listdir(UPLOAD_FOLDER):
            if f.endswith('.json'):
                with open(os.path.join(UPLOAD_FOLDER,f)) as jf:
                    files.append(json.load(jf))
    return jsonify(files)

@app.route('/upload_ebook', methods=['POST'])
def upload_ebook():
    title = request.form.get('title')
    price = request.form.get('price')
    file = request.files.get('file')
    if not file or not file.filename.endswith('.pdf'):
        return jsonify({"ok":False,"message":"Only PDF"})
    filename = secure_filename(title.replace(' ','_')+'_'+file.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(path)
    meta = {"title":title,"price":float(price),"filename":filename}
    with open(os.path.join(UPLOAD_FOLDER, filename+'.json'),'w') as jf:
        json.dump(meta,jf)
    return jsonify({"ok":True,"message":"Uploaded!"})

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
