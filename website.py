from flask import Flask, request, redirect
import json, os

app = Flask(__name__)

# ===== CONFIG - CHANGE AT 18 =====
FEE_PERCENT = 0.0  # At 18 change to 0.20 (20% profit share to you)
REAL_MONEY = False  # Keep False now. At 18 set True and add Daraja keys
MY_PHONE = "2547XXXXXXXX"  # Your M-Pesa number for fees
# =================================

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO TRADING PRO</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body{background:#0a0a0a;color:white;font-family:Arial;margin:0;padding:10px}
button{padding:9px 14px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
.card{background:#151515;border:1px solid #222;padding:12px;border-radius:10px;margin-top:10px}
select,input{padding:8px;background:#222;color:white;border:1px solid #333;border-radius:5px}
.top{display:flex;justify-content:space-between;align-items:center}
</style>
</head>
<body>
<div class="top">
<h2>TIMO TRADING PRO</h2>
<button onclick="location.href='/admin'" style="background:#222">Admin</button>
</div>

<div>Balance: $<span id="bal">0</span> | Admin Fee Pot: $<span id="adminBal">0</span></div>

<div class="card">
Pair: 
<select id="pair" onchange="changePair()">
<option>EURUSDT</option><option>GBPUSDT</option><option>BTCUSDT</option><option>XAUUSDT</option><option>USDJPY</option>
</select>
<span id="price">-</span>
</div>

<div class="card">
<input id="amt" type="number" value="10" style="width:70px"> 
<button onclick="openTrade('BUY')" style="background:#00c950">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ff2c2c;color:white">SELL</button>
</div>

<canvas id="chart" height="280"></canvas>

<div class="card">
<h3>Deposit / Withdraw (M-Pesa)</h3>
<input id="mpesaAmt" placeholder="Amount KES" type="number" style="width:100px">
<button onclick="deposit()" style="background:#00aaff">Deposit (STK)</button>
<button onclick="withdraw()" style="background:#ffaa00;color:black">Withdraw</button>
<div id="mpesaStatus" style="margin-top:8px;color:#00c950"></div>
<small>Now: DEMO mode. At 18 connect real Daraja API.</small>
</div>

<h3>Open Trades - Close Anytime</h3>
<div id="open"></div>
<h3>History (Fee auto to you)</h3>
<div id="hist"></div>

<script>
let currentPrice=0, pair='EURUSDT', prices=[], chart;
let bal = parseFloat(localStorage.getItem('bal')||'20');
let adminBal = parseFloat(localStorage.getItem('adminBal')||'0');
let trades = JSON.parse(localStorage.getItem('trades')||'[]');
const FEE = 0.0; // JS mirror, real calc is server-side at 18

document.getElementById('bal').innerText=bal.toFixed(2);
document.getElementById('adminBal').innerText=adminBal.toFixed(2);

async function loadPrices(){
 try{
  let r = await fetch(`https://api.binance.com/api/v3/klines?symbol=${pair}&interval=1h&limit=80`);
  let d = await r.json();
  prices = d.map(c=>parseFloat(c[4]));
  currentPrice = prices[prices.length-1];
  document.getElementById('price').innerText=currentPrice.toFixed(5);
  draw();
 }catch(e){ prices=Array.from({length:80},(_,i)=>1+Math.sin(i/10)*0.01); currentPrice=prices[79]; draw(); }
}
function draw(){
 let ctx=document.getElementById('chart').getContext('2d');
 if(chart) chart.destroy();
 chart=new Chart(ctx,{type:'line',data:{labels:prices.map((_,i)=>i),datasets:[{data:prices,borderColor:'#00c950',pointRadius:0,tension:0.3}]},options:{plugins:{legend:{display:false}},scales:{x:{display:false}}}});
}
function changePair(){ pair=document.getElementById('pair').value; loadPrices(); }

function openTrade(type){
 let amt=parseFloat(document.getElementById('amt').value);
 if(amt>bal){alert('Low bal');return;}
 trades.push({id:Date.now(),pair:pair,type:type,amount:amt,open:currentPrice});
 bal-=amt; save();
}
function closeTrade(id){
 let t=trades.find(x=>x.id===id); if(!t) return;
 let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff;
 let profit=(diff/t.open)*t.amount*100;
 let ret=t.amount+profit; let fee=0;
 if(profit>0 && FEE>0){fee=profit*FEE; ret-=fee; adminBal+=fee;}
 bal+=ret; trades=trades.filter(x=>x.id!==id);
 document.getElementById('hist').innerHTML=`<div style="color:${profit>=0?'#00c950':'red'}">${t.pair} ${t.type} $${t.amount} PnL:${profit.toFixed(2)} Fee:${fee.toFixed(2)} -> Bal $${bal.toFixed(2)}</div>`+document.getElementById('hist').innerHTML;
 save();
}
function render(){
 document.getElementById('bal').innerText=bal.toFixed(2);
 document.getElementById('adminBal').innerText=adminBal.toFixed(2);
 document.getElementById('price').innerText=currentPrice.toFixed(5);
 document.getElementById('open').innerHTML=trades.map(t=>{
  let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff;
  let fl=(diff/t.open)*t.amount*100;
  return `<div class="card">${t.pair} ${t.type} $${t.amount} Float:<b style="color:${fl>=0?'#00c950':'red'}">${fl.toFixed(2)}</b> <button onclick="closeTrade(${t.id})" style="background:orange">CLOSE NOW</button></div>`;
 }).join('')||'<small>No open trades</small>';
}
function save(){localStorage.setItem('bal',bal); localStorage.setItem('adminBal',adminBal); localStorage.setItem('trades',JSON.stringify(trades)); render();}
function deposit(){
 let a=document.getElementById('mpesaAmt').value;
 if(!a) return;
 // DEMO MODE NOW - At 18 replace with fetch('/stk_push')
 bal+=parseFloat(a)/130; // KES to USD approx
 document.getElementById('mpesaStatus').innerText=`DEMO Deposit +$${(a/130).toFixed(2)} added! (Real M-Pesa at 18)`;
 save();
}
function withdraw(){
 let a=document.getElementById('mpesaAmt').value;
 if(!a) return;
 let usd=a/130;
 if(usd>bal){alert('Low bal');return;}
 bal-=usd;
 document.getElementById('mpesaStatus').innerText=`DEMO Withdraw KES ${a} requested. At 18 will send real M-Pesa to you.`;
 save();
}
setInterval(()=>{currentPrice+=(Math.random()-0.5)*0.0002*currentPrice; render();},2000);
loadPrices(); setInterval(render,1000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/admin')
def admin():
    return """
    <body style="background:black;color:white;font-family:Arial;padding:20px">
    <h2>Admin Panel</h2>
    <p>Your Fee Pot is stored in user's browser now. At 18, use database.</p>
    <p>To add balance to a user: Give them code: localStorage.setItem('bal','100')</p>
    <p>To go live at 18: <br>
    1. Set REAL_MONEY=True<br>
    2. Set FEE_PERCENT=0.20<br>
    3. Add Daraja API keys<br>
    4. Add KYC check (ID upload)</p>
    <a href="/" style="color:lime">Back</a>
    </body>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
