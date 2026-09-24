from flask import Flask
app = Flask(__name__)

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
</style>
</head>
<body>
<h2>TIMO TRADING PRO</h2>
<div>Balance: $<span id="bal">0</span> | Fee Pot: $<span id="adminBal">0</span></div>

<div class="card">
Pair: <select id="pair" onchange="changePair()"></select>
<span id="price">-</span>
<br><br>
<input id="newPair" placeholder="e.g. ETHUSDT or SOLUSDT" style="width:150px">
<button onclick="addPair()" style="background:#00aaff">+ Add Pair</button>
<button onclick="resetPairs()" style="background:#333;color:white">Reset</button>
<small> Type Binance symbol - must end with USDT</small>
</div>

<div class="card">
<input id="amt" type="number" value="10" style="width:70px">
<button onclick="openTrade('BUY')" style="background:#00c950">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ff2c2c;color:white">SELL</button>
</div>

<canvas id="chart" height="280"></canvas>

<h3>Open Trades - CLOSE NOW</h3>
<div id="open"></div>

<script>
let currentPrice=0, pair='', prices=[], chart;
let bal=parseFloat(localStorage.getItem('bal')||'20');
let adminBal=parseFloat(localStorage.getItem('adminBal')||'0');
let trades=JSON.parse(localStorage.getItem('trades')||'[]');
let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","XAUUSDT","ETHUSDT"]');

function loadPairSelect(){
 let sel=document.getElementById('pair'); sel.innerHTML='';
 pairsList.forEach(p=>{
  let o=document.createElement('option'); o.value=p; o.innerText=p.replace('USDT','/USD'); sel.appendChild(o);
 });
 pair=pairsList[0]; sel.value=pair; loadPrices();
}
function addPair(){
 let np=document.getElementById('newPair').value.toUpperCase().trim();
 if(!np){alert('Type symbol');return;}
 if(!np.endsWith('USDT')) np=np+'USDT';
 if(pairsList.includes(np)){alert('Already exists');return;}
 pairsList.push(np);
 localStorage.setItem('pairsList',JSON.stringify(pairsList));
 loadPairSelect();
 document.getElementById('newPair').value='';
}
function resetPairs(){
 localStorage.removeItem('pairsList');
 pairsList=["EURUSDT","GBPUSDT","BTCUSDT","XAUUSDT","ETHUSDT"];
 localStorage.setItem('pairsList',JSON.stringify(pairsList));
 loadPairSelect();
}
async function loadPrices(){
 try{
  let r=await fetch(`https://api.binance.com/api/v3/klines?symbol=${pair}&interval=1h&limit=80`);
  let d=await r.json();
  prices=d.map(c=>parseFloat(c[4]));
  currentPrice=prices[prices.length-1];
  document.getElementById('price').innerText=currentPrice.toFixed(5);
  draw();
 }catch(e){ prices=Array.from({length:80},(_,i)=>1+Math.sin(i/10)*0.01); currentPrice=prices[79]; draw(); document.getElementById('price').innerText=currentPrice.toFixed(5)+' (demo)'; }
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
 if(profit>0){fee=profit*0; ret-=fee; adminBal+=fee;}
 bal+=ret; trades=trades.filter(x=>x.id!==id); save();
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
setInterval(()=>{currentPrice+=(Math.random()-0.5)*0.0002*currentPrice; render();},2000);
loadPairSelect(); setInterval(render,1000);
</script>
</body>
</html>
"""
@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
