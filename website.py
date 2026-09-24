
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
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
</style>
</head>
<body>
<h3 style="color:#f9c846">TIMO TRADING PRO</h3>
<div>Balance: $<span id="bal">0</span> | Fee Pot: $<span id="adminBal">0</span> | <span id="price">-</span></div>

<div class="card">
<button onclick="openModal('dep')" style="background:#00c950;color:white">Deposit M-Pesa</button>
<button onclick="openModal('wd')" style="background:#ff9800">Withdraw</button>
<button onclick="adminLogin()" style="background:#333;color:white;float:right">Admin</button>
</div>

<div class="card">
Pair: <select id="pair" onchange="changePair()"></select>
<input id="newPair" placeholder="SOLUSDT" style="width:80px">
<button onclick="addPair()" style="background:#f9c846;color:black">+ Add</button>
</div>

<div id="tv_chart" class="card"></div>

<div class="card">
<input id="amt" type="number" value="10" style="width:60px"> $
<button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button>
</div>

<div id="open"></div>

<!-- DEPOSIT MODAL -->
<div id="depModal" class="modal"><div class="modalBox">
<h4>Deposit via M-Pesa</h4>
<p>Paybill: <b>522522</b> Acc: <b>YOUR_TILL</b><br>Min $1</p>
<input id="mpesaCode" placeholder="M-Pesa Code e.g. QAB12CD34E">
<input id="depAmt" type="number" placeholder="Amount $">
<button onclick="confirmDeposit()" style="background:#00c950;width:100%;margin-top:8px">Confirm Deposit</button>
<button onclick="closeModal()" style="background:#333;width:100%;margin-top:5px">Cancel</button>
</div></div>

<!-- WITHDRAW MODAL -->
<div id="wdModal" class="modal"><div class="modalBox">
<h4>Withdraw to M-Pesa</h4>
<input id="wdPhone" placeholder="07XXXXXXXX">
<input id="wdAmt" type="number" placeholder="Amount $">
<button onclick="requestWithdraw()" style="background:#ff9800;width:100%;margin-top:8px">Request</button>
<button onclick="closeModal()" style="background:#333;width:100%;margin-top:5px">Cancel</button>
<p id="wdStatus"></p>
</div></div>

<script>
let pair='BTCUSDT', currentPrice=0;
let bal=parseFloat(localStorage.getItem('bal')||'20');
let adminBal=parseFloat(localStorage.getItem('adminBal')||'0');
let trades=JSON.parse(localStorage.getItem('trades')||'[]');
let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"]');

function tvSymbol(s){let m={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT'}; return m[s]||'BINANCE:'+s;}
function loadChart(){document.getElementById('tv_chart').innerHTML=''; new TradingView.widget({"autosize":true,"symbol":tvSymbol(pair),"interval":"60","timezone":"Etc/UTC","theme":"dark","style":"1","locale":"en","toolbar_bg":"#1a1a25","container_id":"tv_chart","backgroundColor":"#1a1a25"});}
function loadPairSelect(){let sel=document.getElementById('pair');sel.innerHTML='';pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p.replace('USDT','/USD');sel.appendChild(o);});pair=pairsList[0];sel.value=pair;loadChart();fetchPrice();}
function addPair(){let np=document.getElementById('newPair').value.toUpperCase().trim();if(!np)return;if(!np.endsWith('USDT'))np=np+'USDT';if(pairsList.includes(np))return;pairsList.push(np);localStorage.setItem('pairsList',JSON.stringify(pairsList));loadPairSelect();}
async function fetchPrice(){try{let r=await fetch(`https://api.binance.com/api/v3/ticker/price?symbol=${pair}`);let d=await r.json();currentPrice=parseFloat(d.price);document.getElementById('price').innerText=currentPrice.toFixed(5);}catch(e){}}
function changePair(){pair=document.getElementById('pair').value;loadChart();fetchPrice();}
function openTrade(t){let amt=parseFloat(document.getElementById('amt').value);if(amt>bal){alert('Low balance');return;}trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice});bal-=amt;save();}
function closeTrade(id){let tr=trades.find(x=>x.id===id);let diff=currentPrice-tr.open;if(tr.type==='SELL')diff=-diff;let profit=(diff/tr.open)*tr.amount*100;let ret=tr.amount+profit;let fee=0;if(profit>0){fee=profit*0.20;ret-=fee;adminBal+=fee;}bal+=ret;trades=trades.filter(x=>x.id!==id);save();}

// DEPOSIT / WITHDRAW
function openModal(type){document.getElementById(type==='dep'?'depModal':'wdModal').style.display='flex';}
function closeModal(){document.getElementById('depModal').style.display='none';document.getElementById('wdModal').style.display='none';}
function confirmDeposit(){let code=document.getElementById('mpesaCode').value;let amt=parseFloat(document.getElementById('depAmt').value);if(!code||!amt){alert('Fill all');return;}bal+=amt;save();alert('Deposit $'+amt+' added! Code:'+code);closeModal();}
function requestWithdraw(){let amt=parseFloat(document.getElementById('wdAmt').value);let phone=document.getElementById('wdPhone').value;if(amt>bal){alert('Low bal');return;}bal-=amt;save();document.getElementById('wdStatus').innerText='Requested $'+amt+' to '+phone+' - Wait admin approval';}
function adminLogin(){let p=prompt('Admin password:');if(p==='Timo2024'){alert('Fee Pot: $'+adminBal.toFixed(2)+'\\nUse Daraja API for real M-Pesa');}}
function render(){document.getElementById('bal').innerText=bal.toFixed(2);document.getElementById('adminBal').innerText=adminBal.toFixed(2);document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open;if(t.type==='SELL')diff=-diff;let fl=(diff/t.open)*t.amount*100;return `<div class="card">${t.pair} ${t.type} $${t.amount} <b style="color:${fl>=0?'#26a69a':'#ef5350'}">${fl.toFixed(2)}</b> <button onclick="closeTrade(${t.id})" style="background:orange">CLOSE NOW</button></div>`;}).join('');}
function save(){localStorage.setItem('bal',bal);localStorage.setItem('adminBal',adminBal);localStorage.setItem('trades',JSON.stringify(trades));render();}
setInterval(fetchPrice,3000);loadPairSelect();setInterval(render,1000);
</script>
</body>
</html>
"""
@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)


Need real M-Pesa Daraja API next?
