<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO TRADING</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns"></script>
<style>
body{background:#0a0a0a;color:white;font-family:Arial;margin:0;padding:10px}
button{padding:10px 20px;border:none;border-radius:5px;cursor:pointer;font-weight:bold}
.card{background:#151515;border:1px solid #222;padding:15px;border-radius:10px;margin-top:10px}
#chart{height:350px}
</style>
</head>
<body>

<h2>TIMO TRADING - LIVE H1</h2>
<div>Balance: $<span id="balance">0.00</span> <small id="mode"></small></div>
<div>EUR/USD: <span id="price">loading...</span></div>

<div class="card">
<input id="amount" type="number" value="10" style="width:100px;padding:8px"> 
<button onclick="openTrade('BUY')" style="background:#00c950;color:black">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ff2c2c;color:white">SELL</button>
</div>

<canvas id="chart"></canvas>

<h3>Open Trades (close anytime)</h3>
<div id="open-trades"></div>

<h3>History</h3>
<div id="history"></div>

<script>
// ===== CONFIG - CHANGE FEE AT 18 =====
const FEE_PERCENT = 0; // At 18 change to 0.20 = 20% of profit goes to you
const ADMIN_EMAIL = "your email here"; // Your admin login email
// =====================================

let liveBalance = parseFloat(localStorage.getItem('liveBal') || '0');
let demoBalance = parseFloat(localStorage.getItem('demoBal') || '1000');
let isLive = localStorage.getItem('isLive') === 'true';
let currentPrice = 1.08500;
let openTrades = JSON.parse(localStorage.getItem('openTrades') || '[]');
let adminBalance = parseFloat(localStorage.getItem('adminBal') || '0');

document.getElementById('balance').innerText = (isLive?liveBalance:demoBalance).toFixed(2);
document.getElementById('mode').innerText = isLive?'LIVE':'DEMO';

// REAL H1 CHART FROM BINANCE
let chart;
async function loadChart(){
  const res = await fetch('https://api.binance.com/api/v3/klines?symbol=EURUSDT&interval=1h&limit=100');
  const data = await res.json();
  const prices = data.map(c=>({x:new Date(c[0]), y:parseFloat(c[4])}));
  currentPrice = prices[prices.length-1].y;
  document.getElementById('price').innerText = currentPrice.toFixed(5);
  
  const ctx = document.getElementById('chart').getContext('2d');
  chart = new Chart(ctx, {
    type:'line',
    data:{datasets:[{data:prices, borderColor:'#00c950', backgroundColor:'rgba(0,201,80,0.1)', pointRadius:0, tension:0.2}]},
    options:{scales:{x:{type:'time'}, y:{beginAtZero:false}}, plugins:{legend:{display:false}}}
  });
  
  // Update price live every 5 sec
  setInterval(async()=>{
    const r = await fetch('https://api.binance.com/api/v3/ticker/price?symbol=EURUSDT');
    const j = await r.json();
    currentPrice = parseFloat(j.price);
    document.getElementById('price').innerText = currentPrice.toFixed(5);
    renderTrades();
  },5000);
}
loadChart();

function openTrade(type){
  const amount = parseFloat(document.getElementById('amount').value);
  let bal = isLive?liveBalance:demoBalance;
  if(amount>bal){ alert('No balance'); return; }
  
  const trade = {
    id: Date.now(),
    type: type,
    amount: amount,
    openPrice: currentPrice,
    openTime: new Date().toLocaleTimeString()
  };
  openTrades.push(trade);
  
  if(isLive) liveBalance -= amount; else demoBalance -= amount;
  save();
  renderTrades();
}

function closeTrade(id){
  const trade = openTrades.find(t=>t.id===id);
  if(!trade) return;
  
  let diff = currentPrice - trade.openPrice;
  if(trade.type==='SELL') diff = -diff;
  let profit = (diff / trade.openPrice) * trade.amount * 100; // leverage 100
  
  let returnAmount = trade.amount + profit;
  let fee = 0;
  
  if(profit>0 && FEE_PERCENT>0){
    fee = profit * FEE_PERCENT;
    returnAmount -= fee;
    adminBalance += fee; // AUTO TO YOU
    localStorage.setItem('adminBal', adminBalance);
  }
  
  if(isLive) liveBalance += returnAmount; else demoBalance += returnAmount;
  
  // history
  const h = document.getElementById('history');
  h.innerHTML = `<div style="color:${profit>=0?'#00c950':'#ff2c2c'}">${trade.type} $${trade.amount} -> ${profit.toFixed(2)}$ fee:${fee.toFixed(2)}$ CLOSED</div>` + h.innerHTML;
  
  openTrades = openTrades.filter(t=>t.id!==id);
  save();
  renderTrades();
}

function renderTrades(){
  document.getElementById('balance').innerText = (isLive?liveBalance:demoBalance).toFixed(2);
  const div = document.getElementById('open-trades');
  div.innerHTML = openTrades.map(t=>{
    let diff = currentPrice - t.openPrice;
    if(t.type==='SELL') diff = -diff;
    let floating = (diff / t.openPrice) * t.amount * 100;
    return `<div class="card"> ${t.type} $${t.amount} | Open:${t.openPrice.toFixed(5)} | Floating:<span style="color:${floating>=0?'#00c950':'#ff2c2c'}">${floating.toFixed(2)}$</span>
      <button onclick="closeTrade(${t.id})" style="background:orange;margin-left:10px">CLOSE NOW</button></div>`;
  }).join('');
  if(openTrades.length===0) div.innerHTML='<small>No open trades - open stays until you close</small>';
}

function save(){
  localStorage.setItem('liveBal', liveBalance);
  localStorage.setItem('demoBal', demoBalance);
  localStorage.setItem('openTrades', JSON.stringify(openTrades));
  document.getElementById('balance').innerText = (isLive?liveBalance:demoBalance).toFixed(2);
}
renderTrades();

// Simple /admin simulation - give yourself live balance
if(window.location.pathname.includes('admin')){
  let add = prompt('Add LIVE balance:');
  if(add){ liveBalance+=parseFloat(add); save(); alert('Added'); }
}
</script>
</body>
</html>
