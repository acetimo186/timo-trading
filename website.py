from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO TRADING - CANDLES</title>
<script src="https://unpkg.com/lightweight-charts@4.1.0/dist/lightweight-charts.standalone.production.js"></script>
<style>
body{background:#0a0a0a;color:white;font-family:Arial;margin:0;padding:10px}
button{padding:9px 14px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
.card{background:#151515;border:1px solid #222;padding:12px;border-radius:10px;margin-top:10px}
select,input{padding:8px;background:#222;color:white;border:1px solid #333;border-radius:5px}
#chart{width:100%;height:350px}
</style>
</head>
<body>
<h2>TIMO TRADING - H1 CANDLES</h2>
<div>Balance: $<span id="bal">0</span> | Price: <span id="price">-</span></div>

<div class="card">
Pair: <select id="pair" onchange="changePair()"></select>
<input id="newPair" placeholder="e.g. SOLUSDT" style="width:110px">
<button onclick="addPair()" style="background:#00aaff">+ Add Pair</button>
</div>

<div class="card">
<input id="amt" type="number" value="10" style="width:70px">
<button onclick="openTrade('BUY')" style="background:#00c950">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ff2c2c;color:white">SELL</button>
</div>

<div id="chart" class="card"></div>

<h3>Open Trades - CLOSE NOW</h3>
<div id="open"></div>

<script>
let currentPrice=0, pair='', chart, candleSeries;
let bal=parseFloat(localStorage.getItem('bal')||'20');
let trades=JSON.parse(localStorage.getItem('trades')||'[]');
let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","SOLUSDT"]');

function initChart(){
 const el=document.getElementById('chart');
 el.innerHTML='';
 chart=LightweightCharts.createChart(el,{layout:{background:{color:'#151515'},textColor:'#fff'},grid:{vertLines:{color:'#222'},horzLines:{color:'#222'}},width:el.clientWidth,height:350});
 candleSeries=chart.addCandlestickSeries({upColor:'#00c950',downColor:'#ff2c2c',borderVisible:false,wickUpColor:'#00c950',wickDownColor:'#ff2c2c'});
}

function loadPairSelect(){
 let sel=document.getElementById('pair'); sel.innerHTML='';
 pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p.replace('USDT','/USD');sel.appendChild(o);});
 pair=pairsList[0]; sel.value=pair; loadPrices();
}
function addPair(){
 let np=document.getElementById('newPair').value.toUpperCase().trim(); if(!np) return;
 if(!np.endsWith('USDT')) np=np+'USDT';
 if(pairsList.includes(np)) return;
 pairsList.push(np); localStorage.setItem('pairsList',JSON.stringify(pairsList)); loadPairSelect(); document.getElementById('newPair').value='';
}
async function loadPrices(){
 try{
  let r=await fetch(`https://api.binance.com/api/v3/klines?symbol=${pair}&interval=1h&limit=100`);
  let d=await r.json();
  let candles=d.map(c=>({time:c[0]/1000, open:parseFloat(c[1]), high:parseFloat(c[2]), low:parseFloat(c[3]), close:parseFloat(c[4])}));
  currentPrice=candles[candles.length-1].close;
  document.getElementById('price').innerText=currentPrice.toFixed(5);
  candleSeries.setData(candles);
  chart.timeScale().fitContent();
 }catch(e){ console.log(e); }
}
function changePair(){ pair=document.getElementById('pair').value; loadPrices(); }
function openTrade(type){
 let amt=parseFloat(document.getElementById('amt').value);
 if(amt>bal){alert('Low bal');return;}
 trades.push({id:Date.now(),pair:pair,type:type,amount:amt,open:currentPrice}); bal-=amt; save();
}
function closeTrade(id){
 let t=trades.find(x=>x.id===id); if(!t) return;
 let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff;
 let profit=(diff/t.open)*t.amount*100;
 bal+=t.amount+profit; trades=trades.filter(x=>x.id!==id); save();
}
function render(){
 document.getElementById('bal').innerText=bal.toFixed(2);
 document.getElementById('open').innerHTML=trades.map(t=>{
  let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff; let fl=(diff/t.open)*t.amount*100;
  return `<div class="card">${t.pair} ${t.type} $${t.amount} Float:<b style="color:${fl>=0?'#00c950':'red'}">${fl.toFixed(2)}</b> <button onclick="closeTrade(${t.id})" style="background:orange">CLOSE NOW</button></div>`;
 }).join('')||'<small>No open trades</small>';
}
function save(){localStorage.setItem('bal',bal); localStorage.setItem('trades',JSON.stringify(trades)); render();}
setInterval(()=>{currentPrice+=(Math.random()-0.5)*0.0002*currentPrice; document.getElementById('price').innerText=currentPrice.toFixed(5); render();},2000);
initChart(); loadPairSelect(); setInterval(render,1000);
window.addEventListener('resize',()=>{chart.applyOptions({width:document.getElementById('chart').clientWidth});});
</script>
</body>
</html>
"""
@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
