from flask import Flask
app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO TRADING</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<style>
body{background:#0a0a0a;color:white;font-family:Arial;margin:0;padding:12px}
button{padding:10px 18px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
.card{background:#151515;border:1px solid #222;padding:12px;border-radius:10px;margin-top:10px}
</style>
</head>
<body>
<h2>TIMO TRADING - H1 LIVE</h2>
<div>Balance: $<span id="balance">0.00</span></div>
<div>EUR/USD: <span id="price">1.08500</span></div>
<div class="card">
Amount: <input id="amount" type="number" value="10" style="width:80px;padding:8px">
<button onclick="openTrade('BUY')" style="background:#00c950">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ff2c2c;color:white">SELL</button>
</div>
<canvas id="chart" height="300"></canvas>
<h3>Open Trades - Close Anytime</h3>
<div id="open-trades"></div>
<h3>History</h3>
<div id="history"></div>
<script>
const FEE_PERCENT = 0;
let liveBalance = parseFloat(localStorage.getItem('liveBal')||'20');
let currentPrice = 1.08500;
let openTrades = JSON.parse(localStorage.getItem('openTrades')||'[]');
let prices = []; let chart;
document.getElementById('balance').innerText = liveBalance.toFixed(2);
async function loadPrices(){
 try{
  let res = await fetch('https://api.binance.com/api/v3/klines?symbol=EURUSDT&interval=1h&limit=80');
  let data = await res.json();
  prices = data.map(c=>parseFloat(c[4]));
  currentPrice = prices[prices.length-1];
 }catch(e){
  prices = Array.from({length:80},(_,i)=>1.08+Math.sin(i/10)*0.01+Math.random()*0.005);
  currentPrice = prices[79];
 }
 const ctx = document.getElementById('chart').getContext('2d');
 if(chart) chart.destroy();
 chart = new Chart(ctx, {type:'line', data:{labels:prices.map((_,i)=>i), datasets:[{data:prices, borderColor:'#00c950', pointRadius:0, tension:0.3}]}, options:{plugins:{legend:{display:false}}, scales:{x:{display:false}}}});
 renderTrades();
}
function openTrade(type){
 let amt = parseFloat(document.getElementById('amount').value);
 if(amt>liveBalance){alert('Low balance');return;}
 openTrades.push({id:Date.now(), type:type, amount:amt, openPrice:currentPrice});
 liveBalance-=amt; save();
}
function closeTrade(id){
 let t = openTrades.find(x=>x.id===id); if(!t) return;
 let diff = currentPrice - t.openPrice; if(t.type==='SELL') diff=-diff;
 let profit = (diff/t.openPrice)*t.amount*100;
 let ret = t.amount+profit; let fee=0;
 if(profit>0 && FEE_PERCENT>0){fee=profit*FEE_PERCENT; ret-=fee;}
 liveBalance+=ret;
 openTrades=openTrades.filter(x=>x.id!==id);
 document.getElementById('history').innerHTML = `<div style="color:${profit>=0?'#00c950':'red'}">${t.type} $${t.amount} PnL:${profit.toFixed(2)}$ Fee:${fee.toFixed(2)}$</div>`+document.getElementById('history').innerHTML;
 save();
}
function renderTrades(){
 document.getElementById('balance').innerText=liveBalance.toFixed(2);
 document.getElementById('price').innerText=currentPrice.toFixed(5);
 let div=document.getElementById('open-trades');
 div.innerHTML=openTrades.map(t=>{
  let diff=currentPrice-t.openPrice; if(t.type==='SELL') diff=-diff;
  let floating=(diff/t.openPrice)*t.amount*100;
  return `<div class="card">${t.type} $${t.amount} Float:<b style="color:${floating>=0?'#00c950':'red'}">${floating.toFixed(2)}$</b> <button onclick="closeTrade(${t.id})" style="background:orange">CLOSE NOW</button></div>`;
 }).join('')||'<small>No open trades - stays open till you close</small>';
}
function save(){localStorage.setItem('liveBal',liveBalance); localStorage.setItem('openTrades',JSON.stringify(openTrades)); renderTrades();}
setInterval(()=>{currentPrice+=(Math.random()-0.5)*0.0004; renderTrades();},2000);
loadPrices(); setInterval(renderTrades,1000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
