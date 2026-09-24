from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TIMO - LiteFinance Style</title>
<script src="https://s3.tradingview.com/tv.js"></script>
<style>
body{background:#0e0e14;color:white;font-family:Arial;margin:0;padding:8px}
.card{background:#1a1a25;border:1px solid #2a2a3a;padding:10px;border-radius:8px;margin-top:8px}
button{padding:8px 14px;border:none;border-radius:6px;cursor:pointer;font-weight:bold}
select,input{padding:8px;background:#1e1e2d;color:white;border:1px solid #333;border-radius:5px}
#tv_chart{height:420px}
</style>
</head>
<body>
<h3 style="color:#f9c846">TIMO TRADING - LiteFinance Chart</h3>
<div>Balance: $<span id="bal">20</span> | Live: <span id="price">-</span></div>

<div class="card">
Pair: <select id="pair" onchange="changePair()"></select>
<input id="newPair" placeholder="SOLUSDT" style="width:90px">
<button onclick="addPair()" style="background:#f9c846;color:black">+ Add</button>
</div>

<div id="tv_chart" class="card"></div>

<div class="card">
<input id="amt" type="number" value="10" style="width:70px">
<button onclick="openTrade('BUY')" style="background:#26a69a;color:white">BUY</button>
<button onclick="openTrade('SELL')" style="background:#ef5350;color:white">SELL</button>
</div>

<div id="open"></div>

<script>
let pair='BTCUSDT', currentPrice=0;
let bal=parseFloat(localStorage.getItem('bal')||'20');
let trades=JSON.parse(localStorage.getItem('trades')||'[]');
let pairsList=JSON.parse(localStorage.getItem('pairsList')||'["EURUSDT","GBPUSDT","BTCUSDT","ETHUSDT","XAUUSDT"]');
let tvWidget=null;

function tvSymbol(binanceSym){
 // LiteFinance mapping
 let map={'EURUSDT':'FX:EURUSD','GBPUSDT':'FX:GBPUSD','XAUUSDT':'OANDA:XAUUSD','BTCUSDT':'BINANCE:BTCUSDT','ETHUSDT':'BINANCE:ETHUSDT','SOLUSDT':'BINANCE:SOLUSDT'};
 if(map[binanceSym]) return map[binanceSym];
 return 'BINANCE:'+binanceSym;
}

function loadChart(){
 document.getElementById('tv_chart').innerHTML='';
 tvWidget=new TradingView.widget({
  "autosize": true,
  "symbol": tvSymbol(pair),
  "interval": "60",
  "timezone": "Etc/UTC",
  "theme": "dark",
  "style": "1",
  "locale": "en",
  "toolbar_bg": "#1a1a25",
  "enable_publishing": false,
  "hide_top_toolbar": false,
  "save_image": false,
  "container_id": "tv_chart",
  "backgroundColor": "#1a1a25",
  "gridColor": "rgba(42,42,58,0.5)",
  "overrides": {"paneProperties.background": "#1a1a25", "paneProperties.vertGridProperties.color": "#2a2a3a", "paneProperties.horzGridProperties.color": "#2a2a3a"}
 });
}

function loadPairSelect(){
 let sel=document.getElementById('pair'); sel.innerHTML='';
 pairsList.forEach(p=>{let o=document.createElement('option');o.value=p;o.innerText=p.replace('USDT','/USD');sel.appendChild(o);});
 pair=pairsList[0]; sel.value=pair; loadChart(); fetchPrice();
}
function addPair(){
 let np=document.getElementById('newPair').value.toUpperCase().trim(); if(!np) return;
 if(!np.endsWith('USDT')) np=np+'USDT';
 if(pairsList.includes(np)) return;
 pairsList.push(np); localStorage.setItem('pairsList',JSON.stringify(pairsList)); loadPairSelect();
}
async function fetchPrice(){
 try{let r=await fetch(`https://api.binance.com/api/v3/ticker/price?symbol=${pair}`); let d=await r.json(); currentPrice=parseFloat(d.price); document.getElementById('price').innerText=currentPrice.toFixed(5);}catch(e){}
}
function changePair(){ pair=document.getElementById('pair').value; loadChart(); fetchPrice(); }
function openTrade(t){let amt=parseFloat(document.getElementById('amt').value); if(amt>bal){alert('Low');return;} trades.push({id:Date.now(),pair:pair,type:t,amount:amt,open:currentPrice}); bal-=amt; save();}
function closeTrade(id){let t=trades.find(x=>x.id===id); let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff; let profit=(diff/t.open)*t.amount*100; bal+=t.amount+profit; trades=trades.filter(x=>x.id!==id); save();}
function render(){document.getElementById('bal').innerText=bal.toFixed(2); document.getElementById('open').innerHTML=trades.map(t=>{let diff=currentPrice-t.open; if(t.type==='SELL') diff=-diff; let fl=(diff/t.open)*t.amount*100; return `<div class="card">${t.pair} ${t.type} $${t.amount} <b style="color:${fl>=0?'#26a69a':'#ef5350'}">${fl.toFixed(2)}</b> <button onclick="closeTrade(${t.id})" style="background:orange">CLOSE NOW</button></div>`;}).join('');}
function save(){localStorage.setItem('bal',bal); localStorage.setItem('trades',JSON.stringify(trades)); render();}
setInterval(fetchPrice,3000); loadPairSelect(); setInterval(render,1000);
</script>
</body>
</html>
"""
@app.route('/')
def home(): return HTML
if __name__=='__main__': app.run(host='0.0.0.0',port=10000)
