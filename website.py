from flask import Flask, request, jsonify
import os, json, requests
from datetime import datetime

app = Flask(__name__)
USERS_FILE = 'users.json'
DEPOSITS_FILE = 'deposits.json'
FEES_FILE = 'fees.json'
SIGNALS_FILE = 'signals.json'
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

def get_trend(pair):
    try:
        # Crypto from Binance
        if pair in ["BTCUSDT","ETHUSDT"]:
            r=requests.get(f'https://api.binance.com/api/v3/klines?symbol={pair}&interval=1h&limit=55',timeout=5).json()
            closes=[float(x[4]) for x in r]
            sma20=sum(closes[-20:])/20
            sma50=sum(closes[-50:])/50
            price=closes[-1]
            if sma20 > sma50: return {"trend":"BUY","price":price,"sma20":sma20,"sma50":sma50}
            else: return {"trend":"SELL","price":price,"sma20":sma20,"sma50":sma50}
        else:
            # For Forex/Gold - use TradingView idea: random but we say check chart
            return {"trend":"CHECK_CHART","price":0,"note":"Open TradingView to confirm"}
    except:
        return {"trend":"CHECK_CHART","price":0}

HOME_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Kaumoni V10 Semi-Auto</title>
<style>*{box-sizing:border-box}body{background:#0e0e14;color:white;font-family:Arial;margin:0}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:1px solid #2a2a3a}nav b{color:#f9c846}.btn-main{background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px 22px;border:none;border-radius:30px;font-weight:bold;text-decoration:none;display:inline-block;margin:6px;animation:pulse 2s infinite}@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.05)}}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:8px;text-align:center}.grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:10px}@media(max-width:600px){.grid{grid-template-columns:1fr}}.slider{width:340px;height:180px;margin:15px auto;position:relative;overflow:hidden;border-radius:12px;border:2px solid #2a2a3a}.slide{position:absolute;width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;transition:0.8s;transform:translateX(100%);opacity:0}.slide.active{transform:translateX(0);opacity:1}.wallet{background:linear-gradient(90deg,#f9c846,#ff9800);background-size:200%;animation:grad 3s linear infinite;color:black;padding:10px;border-radius:10px;margin:10px;font-weight:bold}@keyframes grad{0%{background-position:0%}100%{background-position:200%}}</style></head><body>
<nav><b>KAUMONI V10</b><div><a href="/trade" style="color:white;text-decoration:none;margin:0 8px">📈 Trade</a><a href="/admin" style="color:#f9c846;font-weight:bold;text-decoration:none">👑 Admin</a></div></nav>
<div style="text-align:center;padding:25px 15px;background:linear-gradient(270deg,#0e0e14,#1a1a25,#2a1a3a);background-size:400% 400%;animation:grad 8s ease infinite"><h1 style="font-size:32px">Create <span style="color:#f9c846">Pro Posters</span> in 10 Sec</h1>
<div class="slider" id="slider"><div class="slide active" style="background:linear-gradient(135deg,#ff3b3b,#ff9a00)"><h2>MEGA SALE! 50% OFF</h2></div><div class="slide" style="background:linear-gradient(135deg,#ff69b4,#ffb6d9)"><h2>BEAUTY PALACE</h2></div><div class="slide" style="background:linear-gradient(135deg,#1e3a8a,#60a5fa)"><h2>SUNDAY SERVICE</h2></div><div class="slide" style="background:linear-gradient(135deg,#00c950,#a8ff78);color:black"><h2>BURGER FEST</h2></div></div>
<a class="btn-main" href="#tools">🚀 Explore 8 Tools</a></div>
<div id="tools" style="padding:10px"><div class="grid"><div class="card"><div style="font-size:30px">🎨</div><h3>Poster</h3><b style="color:#f9c846">Ksh150</b><br><a href="/poster-maker" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">🧾</div><h3>Receipt</h3><b style="color:#f9c846">150</b><br><a href="/receipt-maker" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">📄</div><h3>CV</h3><b style="color:#f9c846">300</b><br><a href="/cv-builder" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">💼</div><h3>Logo</h3><b style="color:#f9c846">500</b><br><a href="/logo-maker" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">✉️</div><h3>Cover</h3><b style="color:#f9c846">150</b><br><a href="/cover-letter" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">📈</div><h3>Trading</h3><b style="color:#00c950">20% Fee</b><br><a href="/trade" class="btn-main" style="padding:6px 14px;background:#00c950;color:white;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">📡</div><h3>VIP Signals</h3><b style="color:#f9c846">1500</b><br><a href="/signals" class="btn-main" style="padding:6px 14px;font-size:12px">Open</a></div><div class="card"><div style="font-size:30px">📚</div><h3>E-Books</h3><b style="color:#f9c846">500</b><br><a href="/ebooks" class="btn-main" style="padding:6px 14px;background:#333;color:white;font-size:12px">Open</a></div></div></div>
<div style="text-align:center"><div class="wallet" style="max-width:350px;margin:auto">Bal $<span id="bal">0</span> | <span id="phone">Not logged</span></div><div class="card" style="max-width:350px;margin:10px auto"><input id="loginPhone" placeholder="Phone" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><input id="loginPass" type="password" placeholder="Pass" style="width:35%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px"><button onclick="login()" style="background:#f9c846;color:black;padding:8px 12px;border:none;border-radius:6px;font-weight:bold">Login</button><p id="loginMsg" style="color:#ff5555;font-size:11px"></p></div></div>
<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;right:20px;background:#25D366;color:white;padding:14px 20px;border-radius:50px;font-weight:bold;text-decoration:none">💬 WhatsApp</a>
<script>let ph=localStorage.getItem('userPhone_v5')||'';document.getElementById('phone').innerText=ph||'Not logged';async function check(){if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=(d.balance||0).toFixed(2);}async function login(){let p=document.getElementById('loginPhone').value.trim();let pw=document.getElementById('loginPass').value.trim();let r=await fetch('/api/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:p,password:pw})});let d=await r.json();if(!d.ok){document.getElementById('loginMsg').innerText=d.message;return;}localStorage.setItem('userPhone_v5',p);location.reload();}let cur=0;let slides=document.querySelectorAll('.slide');setInterval(()=>{slides[cur].classList.remove('active');cur=(cur+1)%slides.length;slides[cur].classList.add('active');},2000);check();</script></body></html>"""

POSTER_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Poster</title><script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}input,select{width:100%;padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:6px;margin:4px 0}.card{background:#1a1a25;padding:10px;border-radius:8px}#poster{width:350px;height:500px;margin:auto;background:white;color:black;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:20px;box-sizing:border-box;position:relative;overflow:hidden}#wm{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%) rotate(-20deg);background:rgba(255,255,255,0.95);color:#004AFF;font-size:26px;font-weight:900;padding:10px 22px;border:3px solid #004AFF;white-space:nowrap;z-index:10}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>Poster $1</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><div><div class="card"><p>Phone <b id="uPhone">-</b> Bal $<span id="uBal">0</span></p><select id="tpl" onchange="draw()"><option value="1">Red</option><option value="2">Pink</option><option value="3">Blue</option><option value="4">Yellow</option><option value="5">Green</option></select><input id="title" value="MEGA SALE!" oninput="draw()"><input id="sub" value="50% OFF" oninput="draw()"><input id="phone" value="Call: 07XX" oninput="draw()"><input id="loc" value="Nairobi" oninput="draw()"></div><button onclick="downloadPoster()" style="background:#00c950;color:white;width:100%;padding:10px;border:none;border-radius:6px;font-weight:bold">Download HD $1</button></div><div id="poster"></div></div><script>let userPhone=localStorage.getItem('userPhone_v5')||'';let userBal=0;async function loadBal(){document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854'){document.getElementById('uBal').innerText='999 FREE';userBal=999;return;}let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();userBal=d.balance||0;document.getElementById('uBal').innerText=userBal.toFixed(2);}function draw(){let c={1:['#ff0000','#ffcc00'],2:['#ff69b4','#ffb6d9'],3:['#1e3a8a','#60a5fa'],4:['#f9c846','#ff9800'],5:['#00c950','#90ee90']}[document.getElementById('tpl').value];document.getElementById('poster').innerHTML=`<div id="wm">PREVIEW PAY $1</div><div style="background:linear-gradient(135deg,${c[0]},${c[1]});width:100%;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px"><h1 style="font-size:40px;margin:0">${document.getElementById('title').value}</h1><h2>${document.getElementById('sub').value}</h2><div style="background:black;color:white;padding:6px 12px;border-radius:20px;margin-top:15px"><b>${document.getElementById('phone').value}</b><br><small>${document.getElementById('loc').value}</small></div></div>`;}async function downloadPoster(){if(userPhone!=='0118431854'&&userBal<1){alert('Low bal');return;}let r=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:1,reason:'poster'})});let d=await r.json();if(!d.ok){alert(d.message);return;}let wm=document.getElementById('wm');if(wm)wm.style.display='none';html2canvas(document.getElementById('poster'),{scale:2}).then(cv=>{if(wm)wm.style.display='block';let a=document.createElement('a');a.download='HD.png';a.href=cv.toDataURL();a.click();loadBal();});}draw();loadBal();</script></body></html>"""

RECEIPT_HTML = POSTER_HTML.replace("Poster $1","Receipt $1")
CV_HTML = POSTER_HTML.replace("Poster $1","CV $2")
LOGO_HTML = POSTER_HTML.replace("Poster $1","Logo $3")
COVER_HTML = POSTER_HTML.replace("Poster $1","Cover $1")

SIGNALS_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>VIP Signals Semi-Auto</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:12px;margin:0}nav{background:#1a1a25;padding:12px 20px;display:flex;justify-content:space-between;border-bottom:1px solid #2a2a3a;position:sticky;top:0}nav a{color:#f9c846;text-decoration:none;font-weight:bold}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:14px;border-radius:12px;margin:10px 0}.signal{background:#1e1e2d;border-left:3px solid #00c950;padding:10px;margin:8px 0;border-radius:0 8px 8px 0}.buy{border:2px dashed #f9c846;background:rgba(249,200,70,0.1);text-align:center}button{padding:10px 14px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}</style></head><body>
<nav><a href="/">← Home</a><b>📡 VIP SIGNALS</b><span id="uPhone" style="font-size:11px">-</span></nav>
<div style="max-width:600px;margin:auto;padding:10px">
<div class="card" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black"><b>Bal: $ <span id="uBal">0</span></b> | <span id="vipStatus">Not VIP</span></div>
<div id="notVip" class="card buy"><h3>🔒 Join VIP - $10</h3><button onclick="join()" style="background:#f9c846;color:black;width:100%;padding:12px;font-size:16px">Join VIP $10</button></div>
<div id="vipArea" style="display:none"><div class="card" style="border:1px solid #00c950;background:rgba(0,201,80,0.1);text-align:center"><h3 style="color:#00c950">✅ VIP ACTIVE - Sent by Admin</h3><a href="https://wa.me/254118431854" target="_blank" style="background:#25D366;color:white;padding:10px 20px;border-radius:20px;text-decoration:none;font-weight:bold;display:inline-block">WhatsApp Group</a></div><h3>📈 Live Signals</h3><div id="signals">Loading...</div></div>
</div>
<script>
let userPhone=localStorage.getItem('userPhone_v5')||'';let isVip=localStorage.getItem('isVip_'+userPhone)==='true';
async function load(){if(!userPhone){alert('Login');window.location='/';return;}document.getElementById('uPhone').innerText=userPhone;if(userPhone==='0118431854')isVip=true;let r=await fetch('/api/balance?phone='+userPhone);let d=await r.json();document.getElementById('uBal').innerText=(d.balance||0).toFixed(2);if(isVip){document.getElementById('notVip').style.display='none';document.getElementById('vipArea').style.display='block';document.getElementById('vipStatus').innerText='VIP ACTIVE ✅';let sr=await fetch('/api/signals');let sj=await sr.json();if(sj.length==0)document.getElementById('signals').innerHTML='<p style=color:#666>No signals yet - Admin will post</p>';else document.getElementById('signals').innerHTML=sj.map((s,i)=>`<div class="signal" style="border-left-color:${s.result.includes('✅')?'#00c950':s.result.includes('❌')?'#ef5350':'#f9c846'}"><b>${s.pair} - ${s.type}</b> <span style="background:${s.type==='BUY'?'#00c950':'#ef5350'};color:white;padding:2px 8px;border-radius:10px;font-size:11px">${s.type}</span><br><small>Entry ${s.entry} | TP ${s.tp} | SL ${s.sl}</small><br><small style="color:#aaa">${s.time}</small> <b style="float:right;color:${s.result.includes('✅')?'#00c950':s.result.includes('❌')?'#ef5350':'#f9c846'}">${s.result}</b></div>`).join('');}}
async function join(){if(userPhone==='0118431854'){localStorage.setItem('isVip_'+userPhone,'true');location.reload();return;}let r=await fetch('/api/balance?phone='+userPhone);let dd=await r.json();if(dd.balance<10){alert('Need $10');return;}let res=await fetch('/api/deduct',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:userPhone,amount:10,reason:'vip'})});let d=await res.json();if(!d.ok){alert(d.message);return;}localStorage.setItem('isVip_'+userPhone,'true');location.reload();}load();
</script></body></html>"""

ADMIN_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Admin Semi-Auto</title><style>body{background:#0e0e14;color:white;font-family:Arial;padding:10px}.card{background:#1a1a25;border:1px solid #2a2a3a;padding:12px;border-radius:12px;margin:8px 0}button{padding:7px 12px;border:none;border-radius:6px;font-weight:bold;cursor:pointer}input,select{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px;margin:3px 0;width:100%}.suggest{background:#1e1e2d;border-left:3px solid #f9c846;padding:8px;margin:6px 0;border-radius:0 8px 8px 0}.sig{background:#1e1e2d;padding:8px;margin:6px 0;border-radius:8px;border-left:3px solid #00c950}</style></head><body><a href="/" style="color:#f9c846">← Home</a><h2>ADMIN V10 Semi-Auto + Win/Loss Close</h2>
<div class="card" style="background:linear-gradient(135deg,#f9c846,#ff9800);color:black"><div>Total Fees $<span id="total">0</span> | <span id="userCount">0 users</span></div></div>

<div class="card" style="border:2px solid #f9c846"><h3>🤖 SEMI-AUTO Trend Detector</h3><p style="font-size:11px;color:#aaa">Bot checks trend, YOU approve and send</p><button onclick="checkTrend()" style="background:#f9c846;color:black;width:100%">🔍 Check Trend Now For All Pairs</button><div id="trendBox">Click Check Trend</div></div>

<div class="card" style="border:1px solid #00c950"><h3>📡 Post Manual Signal (You Send)</h3><input id="sPair" placeholder="Pair e.g. XAUUSD"><select id="sType"><option>BUY</option><option>SELL</option></select><input id="sEntry" placeholder="Entry e.g. 2340"><input id="sTp" placeholder="TP e.g. 2360"><input id="sSl" placeholder="SL e.g. 2330"><input id="sResult" placeholder="Result - leave Running..." value="Running..."><button onclick="postSig()" style="background:#00c950;color:white;width:100%;margin-top:6px">📤 Send Signal to VIP</button><p id="sMsg" style="color:#00c950"></p></div>

<div class="card"><h3>📈 Active Signals - Close Win/Loss</h3><div id="activeSigs">Loading...</div></div>

<div class="card"><h3>Pending Deposits</h3><div id="depList">Loading...</div></div>
<div class="card"><h3>Users</h3><div id="usersList">Loading...</div></div>

<script>
async function load(){let res=await fetch('/api/admin-data');let data=await res.json();document.getElementById('total').innerText=(data.total_fees||0).toFixed(2);document.getElementById('userCount').innerText=data.users.length+' users';document.getElementById('usersList').innerHTML=data.users.map(u=>`<div style="border-bottom:1px solid #333;padding:6px;display:flex;justify-content:space-between"><span>${u.phone} $${(u.balance||0).toFixed(2)}</span><button onclick="addBal('${u.phone}')" style="background:#00c950;color:white;padding:4px 6px;font-size:10px">Add</button></div>`).join('');document.getElementById('depList').innerHTML=data.deposits.map((d,i)=>`<div style="background:#2a2a3a;padding:6px;margin:4px 0;border-radius:6px"><b>${d.phone}</b> $${d.amount} ${d.code} ${d.status}<br><button onclick="approveDep(${i})" style="background:#00c950;color:white">Approve</button> <button onclick="rejectDep(${i})" style="background:#ef5350;color:white">Reject</button></div>`).join('')||'No deposits';loadSigs();}
async function loadSigs(){let r=await fetch('/api/signals');let s=await r.json();if(s.length==0){document.getElementById('activeSigs').innerHTML='<small style=color:#666>No active signals - post one above</small>';return;}document.getElementById('activeSigs').innerHTML=s.map((sig,i)=>`<div class="sig"><b>${sig.pair} ${sig.type}</b> Entry ${sig.entry} TP ${sig.tp} SL ${sig.sl}<br><small>${sig.time} - ${sig.result}</small><br><div style="margin-top:6px"><button onclick="closeWin(${i})" style="background:#00c950;color:white;font-size:11px">✅ Close as WIN</button> <button onclick="closeLoss(${i})" style="background:#ef5350;color:white;font-size:11px">❌ Close as LOSS</button> <button onclick="delSig(${i})" style="background:#333;color:white;font-size:11px">🗑 Delete</button></div></div>`).join('');}
async function checkTrend(){document.getElementById('trendBox').innerHTML='Checking...';let r=await fetch('/api/trend-suggest');let d=await r.json();document.getElementById('trendBox').innerHTML=d.map(t=>`<div class="suggest"><b>${t.pair}</b> - Price ${t.price}<br>Bot suggests: <b style="color:${t.trend==='BUY'?'#00c950':'#ef5350'}">${t.trend}</b> ${t.note||''}<br><small>SMA20 ${t.sma20?.toFixed(2)||''} vs SMA50 ${t.sma50?.toFixed(2)||''}</small><br><button onclick="quickPost('${t.pair}','${t.trend}','${t.price}')" style="background:#f9c846;color:black;padding:4px 8px;font-size:11px;margin-top:4px">Use This → Post</button></div>`).join('');}
function quickPost(pair,trend,price){if(trend==='CHECK_CHART'){alert('Open TradingView for '+pair+' to confirm trend like you did for XAUUSD');return;}document.getElementById('sPair').value=pair;document.getElementById('sType').value=trend;document.getElementById('sEntry').value=price;let p=parseFloat(price);if(trend==='BUY'){document.getElementById('sTp').value=(p*1.005).toFixed(2);document.getElementById('sSl').value=(p*0.997).toFixed(2);}else{document.getElementById('sTp').value=(p*0.995).toFixed(2);document.getElementById('sSl').value=(p*1.003).toFixed(2);}window.scrollTo(0,300);}
async function postSig(){let data={pair:document.getElementById('sPair').value,type:document.getElementById('sType').value,entry:document.getElementById('sEntry').value,tp:document.getElementById('sTp').value,sl:document.getElementById('sSl').value,result:document.getElementById('sResult').value||'Running...'};if(!data.pair||!data.entry){alert('Fill pair and entry');return;}let res=await fetch('/api/add-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});let j=await res.json();document.getElementById('sMsg').innerText='✅ Signal sent to all VIP!';loadSigs();}
async function closeWin(i){let p=prompt('Enter win result e.g. +30 pips ✅ or +20$ ✅','+20$ ✅');if(!p)return;let res=await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function closeLoss(i){let p=prompt('Enter loss result e.g. -10$ ❌','-10$ ❌');if(!p)return;let res=await fetch('/api/update-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i,result:p})});loadSigs();}
async function delSig(i){if(!confirm('Delete signal?'))return;await fetch('/api/delete-signal',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});loadSigs();}
async function approveDep(i){let r=await fetch('/api/approve-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function rejectDep(i){let r=await fetch('/api/reject-deposit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({index:i})});alert((await r.json()).message);load();}
async function addBal(ph){let amt=prompt('Amount');if(!amt)return;await fetch('/api/add-balance',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({phone:ph,amount:parseFloat(amt)})});load();}
load();setInterval(loadSigs,5000);
</script></body></html>"""

EBOOKS_HTML = "<html><body style='background:#0e0e14;color:white;padding:20px'><a href='/' style='color:#f9c846'>← Home</a><h2>E-Books</h2><p>Coming - use V9 ebooks if needed</p></body></html>"

TRADING_HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Trading</title><script src="https://s3.tradingview.com/tv.js"></script><style>body{background:#0e0e14;color:white;font-family:Arial;padding:8px}.card{background:#1a1a25;padding:10px;border-radius:8px;margin-top:8px}#tv_chart{height:400px}button{padding:8px 14px;border:none;border-radius:6px;font-weight:bold}</style></head><body><a href="/" style="color:#f9c846">← Home</a> <b>TRADING</b> Bal $<span id="bal">0</span><div id="tv_chart" class="card"></div><script>new TradingView.widget({"autosize":true,"symbol":"OANDA:XAUUSD","interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","container_id":"tv_chart"});async function load(){let ph=localStorage.getItem('userPhone_v5');if(!ph)return;let r=await fetch('/api/balance?phone='+ph);let d=await r.json();document.getElementById('bal').innerText=d.balance.toFixed(2);}load();</script></body></html>"""

GUIDE_HTML = HOME_HTML

@app.route('/')
def home(): return HOME_HTML
@app.route('/service/<k>')
def service(k): return GUIDE_HTML
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
    data=request.get_json(); deps=load_json(DEPOSITS_FILE, []); deps.append({"phone":data['phone'],"code":data['code'],"amount":float(data['amount']),"status":"pending","time":str(datetime.now())}); save_json(DEPOSITS_FILE, deps); return jsonify({"ok":True,"message":"Sent"})

@app.route('/api/add-balance', methods=['POST'])
def api_add_bal():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0}
    users[ph]['balance']=float(users[ph].get('balance',0))+float(data['amount']); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load_json(USERS_FILE, {}); ph=data['phone']; amt=float(data['amount'])
    if ph==ADMIN_PHONE: return jsonify({"ok":True,"balance":999})
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({"ok":False,"message":"Low balance"})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load_json(FEES_FILE, {"total":0}); fees['total']=fees.get('total',0)+amt; save_json(FEES_FILE, fees); save_json(USERS_FILE, users); return jsonify({"ok":True})

@app.route('/api/add-fee', methods=['POST'])
def api_add_fee():
    data=request.get_json(); fees=load_json(FEES_FILE, {"total":0}); fees['total']+=float(data['fee']); save_json(FEES_FILE, fees); return jsonify({"ok":True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load_json(USERS_FILE, {}); deps=load_json(DEPOSITS_FILE, []); fees=load_json(FEES_FILE, {"total":0}); return jsonify({"users":list(users.values()),"deposits":deps,"total_fees":fees.get('total',0)})

@app.route('/api/approve-deposit', methods=['POST'])
def api_approve():
    idx=int(request.get_json()['index']); deps=load_json(DEPOSITS_FILE, []); dep=deps[idx]; users=load_json(USERS_FILE, {})
    if dep['status']!='pending': return jsonify({"message":"Already"})
    ph=dep['phone']
    if ph not in users: users[ph]={"phone":ph,"balance":0,"total_fee":0}
    users[ph]['balance']+=float(dep['amount']); save_json(USERS_FILE, users); deps[idx]['status']='approved'; save_json(DEPOSITS_FILE, deps); return jsonify({"message":"Approved"})

@app.route('/api/reject-deposit', methods=['POST'])
def api_reject():
    idx=int(request.get_json()['index']); deps=load_json(DEPOSITS_FILE, []); deps[idx]['status']='rejected'; save_json(DEPOSITS_FILE, deps); return jsonify({"message":"Rejected"})

# ===== SIGNALS APIS - SEMI-AUTO =====
@app.route('/api/signals')
def api_signals():
    return jsonify(load_json(SIGNALS_FILE, []))

@app.route('/api/trend-suggest')
def api_trend_suggest():
    out=[]
    for pair in ["BTCUSDT","ETHUSDT","EURUSDT","GBPUSDT","XAUUSDT"]:
        t=get_trend(pair)
        out.append({"pair":pair.replace("USDT","USD").replace("EURUSD","EUR/USD").replace("GBPUSD","GBP/USD").replace("XAUUSD","XAUUSD GOLD").replace("BTCUSD","BTC/USD"),"raw":pair,"trend":t.get("trend","BUY"),"price":round(t.get("price",0),2) if t.get("price") else "Check TV","sma20":t.get("sma20",0),"sma50":t.get("sma50",0),"note":t.get("note","")})
    return jsonify(out)

@app.route('/api/add-signal', methods=['POST'])
def api_add_signal():
    data=request.get_json(); sigs=load_json(SIGNALS_FILE, [])
    sigs.insert(0, {"pair":data['pair'],"type":data['type'],"entry":data['entry'],"tp":data['tp'],"sl":data['sl'],"result":data.get('result','Running...'),"time":datetime.now().strftime("%Y-%m-%d %H:%M")})
    save_json(SIGNALS_FILE, sigs[:30]); return jsonify({"ok":True})

@app.route('/api/update-signal', methods=['POST'])
def api_update_signal():
    data=request.get_json(); idx=int(data['index']); sigs=load_json(SIGNALS_FILE, []);
    if 0 <= idx < len(sigs): sigs[idx]['result']=data['result']; save_json(SIGNALS_FILE, sigs)
    return jsonify({"ok":True})

@app.route('/api/delete-signal', methods=['POST'])
def api_delete_signal():
    idx=int(request.get_json()['index']); sigs=load_json(SIGNALS_FILE, [])
    if 0 <= idx < len(sigs): sigs.pop(idx); save_json(SIGNALS_FILE, sigs)
    return jsonify({"ok":True})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
