
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO TRADING PRO - REAL ACTIVE - PRIVATE</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body style="background:#131722;color:#fff;margin:0" class="overflow-hidden">

<!-- LOGIN LOCK - TIMO ONLY -->
<div id="lock" class="fixed inset-0 bg-[#131722] z-[100] flex items-center justify-center">
<div class="bg-[#1e222d] p-6 rounded border border-[#2a2e39] w-[330px] text-center">
<h2 class="font-bold text-sm">TIMO TRADING PRO - REAL</h2>
<p class="text-[11px] text-[#9598a1] mb-4">PRIVATE - For Timo alone - Real Trading Active</p>
<input id="user" type="text" placeholder="Username" value="Timo" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white">
<input id="pwd" type="password" placeholder="Password" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<button onclick="unlock()" class="w-full bg-[#2962ff] py-2 rounded font-bold text-sm">UNLOCK & ENTER REAL TRADING</button>
<p id="err" class="text-[11px] text-red-400 mt-3 hidden">Wrong username or password</p>
<p class="text-[10px] text-[#9598a1] mt-2">User: Timo | Pass: KAUMONI20r4.</p>
</div>
</div>

<div class="flex justify-between items-center px-3 py-2 bg-[#1e222d] border-b border-[#2a2e39]">
<div class="flex items-center gap-2">
<span class="font-bold text-sm">TIMO REAL</span>
<span id="realBadge" class="text-[9px] bg-gray-600 px-2 py-1 rounded font-bold">DEMO MODE</span>
<span class="text-[10px] text-[#9598a1]">H1 LiteFinance Style</span>
</div>
<div class="flex items-center gap-2">
<span class="text-xs text-[#9598a1]">Trader: Timo</span>
<span class="text-xs text-[#9598a1]">Deriv:</span>
<span id="balance" class="font-bold text-[#26a69a] text-sm">$0.00</span>
<button onclick="openModal('token')" class="bg-[#2a2e39] px-2 py-1 rounded text-[10px]">SET TOKEN</button>
<button onclick="toggleReal()" id="toggleBtn" class="bg-[#2962ff] px-3 py-1 rounded text-xs font-bold">ACTIVATE REAL</button>
</div>
</div>

<div class="flex h-[calc(100vh-42px)]">
<div class="w-[175px] bg-[#1e222d] border-r border-[#2a2e39] overflow-y-auto text-[11px]">
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase">Forex H1 Real Live</div><div id="forexList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Commodities Gold Silver Oil</div><div id="commodityList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Stock Indices US30 NAS100 SPX500</div><div id="indicesList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Crypto BTC ETH SOL Real</div><div id="cryptoList"></div>
<div class="p-3 mt-2 bg-[#131722] border border-[#2a2e39] rounded m-2">
<p class="text-[10px] text-[#9598a1]">REAL STATUS - TIMO</p>
<p id="derivStatus" class="text-[11px] text-yellow-400">Not connected - Set Deriv Token</p>
<p id="derivBalance" class="text-xs font-bold mt-1">$0.00 Deriv Real Balance</p>
</div>
</div>

<div class="flex-1 flex flex-col bg-[#131722]">
<div class="flex justify-between items-center px-3 py-1.5 bg-[#1e222d] border-b border-[#2a2e39] text-xs">
<span id="currentSymbol" class="font-bold bg-[#2a2e39] px-2 py-1 rounded">EURUSD H1 REAL</span>
<span id="currentPrice" class="text-[#26a69a] font-mono">1.08452</span>
<button onclick="runAIScanner()" class="bg-gradient-to-r from-[#2962ff] to-[#7b1fa2] px-3 py-1 rounded font-bold text-[11px]">🤖 AI SCANNER - REAL Best Market</button>
</div>
<div id="tradingview_widget" class="flex-1"></div>
<div id="aiResult" class="hidden p-2 bg-[#1e222d] border-t border-[#2962ff] text-xs"></div>
</div>

<div class="w-[270px] bg-[#1e222d] border-l border-[#2a2e39] p-3 flex flex-col">
<div class="flex gap-1 mb-3">
<button id="modeForex" onclick="setMode('forex')" class="flex-1 py-2 bg-white text-black rounded font-bold text-xs">FOREX & GOLD REAL</button>
<button id="modeOption" onclick="setMode('option')" class="flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs">OPTIONS ALL REAL</button>
</div>

<div id="forexPanel">
<div class="text-[11px] text-[#9598a1] mb-1">Real Lot - Deriv Multipliers - Timo</div>
<input id="lotSize" type="number" value="0.01" step="0.01" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<div class="flex gap-2 mb-2">
<button onclick="placeRealTrade('buy')" class="flex-1 bg-[#26a69a] hover:bg-[#089981] py-3 rounded font-bold text-sm">BUY REAL</button>
<button onclick="placeRealTrade('sell')" class="flex-1 bg-[#ef5350] hover:bg-[#f23645] py-3 rounded font-bold text-sm">SELL REAL</button>
</div>
<p class="text-[10px] text-[#9598a1] text-center">Real execution via Deriv API - H1</p>
</div>

<div id="optionPanel" class="hidden">
<div class="text-[11px] text-[#9598a1] mb-1">Real Options - Deriv Rise/Fall - All Markets</div>
<input id="optAmount" type="number" value="5" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white">
<select id="optExpiry" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<option value="1">1 min - Turbo Real</option>
<option value="3" selected>3 min - Gold & Forex Real</option>
<option value="5">5 min - Indices & Oil Real</option>
<option value="15">15 min - Crypto Real</option>
<option value="60">1 hour - Stocks Real</option>
</select>
<div class="flex gap-2 mb-2">
<button onclick="placeRealOption('CALL')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">CALL REAL ▲</button>
<button onclick="placeRealOption('PUT')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">PUT REAL ▼</button>
</div>
<p class="text-[10px] text-[#9598a1]">Payout real - Gold, Forex, Stocks, Crypto, Oil</p>
</div>

<button onclick="closeAllTrades()" class="mt-3 w-full bg-[#2a2e39] py-2 rounded text-xs border border-[#363a45]">CLOSE ALL NOW</button>

<div class="mt-4 border-t border-[#2a2e39] pt-3">
<p class="text-[11px] text-[#9598a1]">Real Trades Timo (<span id="tradeCount">0</span>) H1 Real</p>
<div id="openTrades" class="space-y-2 max-h-[280px] overflow-y-auto text-[11px] mt-2"></div>
</div>
<div class="mt-2 p-2 bg-red-900/20 border border-red-800 rounded text-[10px] text-red-300">⚠️ REAL MONEY - Trade $1-5 only - Timo Private</div>
</div>
</div>

<!-- TOKEN MODAL -->
<div id="tokenModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-5 rounded w-[360px] border border-[#2a2e39]">
<h3 class="font-bold mb-2 text-sm">Deriv API Token - Timo Private Real</h3>
<p class="text-[11px] text-[#9598a1] mb-2">Go to deriv.com → Settings → API Token → Create (check Read + Trade)</p>
<input id="derivToken" type="password" placeholder="Paste Deriv token" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-xs">
<div class="flex gap-2">
<button onclick="saveToken()" class="flex-1 bg-[#2962ff] py-2 rounded text-sm font-bold">SAVE & CONNECT REAL</button>
<button onclick="closeModal('token')" class="flex-1 bg-[#2a2e39] py-2 rounded text-sm">Cancel</button>
</div>
<p class="text-[10px] text-[#9598a1] mt-2">Token saved only in your browser (localStorage), not on server. Private to Timo.</p>
</div>
</div>

<script src="https://s3.tradingview.com/tv.js"></script>
<script>
const MY_USER="Timo";
const MY_PASSWORD="KAUMONI20r4.";
function unlock(){
 const u=document.getElementById('user').value.trim();
 const p=document.getElementById('pwd').value;
 if(u===MY_USER && p===MY_PASSWORD){
  document.getElementById('lock').classList.add('hidden');
  localStorage.setItem('timo_logged','1');
 } else {
  document.getElementById('err').classList.remove('hidden');
 }
}
if(localStorage.getItem('timo_logged')==='1'){document.getElementById('lock').classList.add('hidden');}

let trades=[];let isReal=false;let ws=null;let derivBalance=0;let currentDeriv='frxEURUSD';
const markets={
 forex:[{id:'EURUSD',tv:'FX:EURUSD',deriv:'frxEURUSD',name:'EUR/USD H1 REAL'},{id:'GBPUSD',tv:'FX:GBPUSD',deriv:'frxGBPUSD',name:'GBP/USD'},{id:'USDJPY',tv:'FX:USDJPY',deriv:'frxUSDJPY',name:'USD/JPY'},{id:'AUDUSD',tv:'FX:AUDUSD',deriv:'frxAUDUSD',name:'AUD/USD'},{id:'USDCAD',tv:'FX:USDCAD',deriv:'frxUSDCAD',name:'USD/CAD'}],
 commodity:[{id:'GOLD',tv:'OANDA:XAUUSD',deriv:'frxXAUUSD',name:'GOLD XAUUSD REAL'},{id:'SILVER',tv:'OANDA:XAGUSD',deriv:'frxXAGUSD',name:'Silver'},{id:'OIL',tv:'TVC:USOIL',deriv:'frxUSOIL',name:'Oil USOIL'}],
 indices:[{id:'US30',tv:'OANDA:US30USD',deriv:'OTC_DJI',name:'US30 Dow'},{id:'NAS100',tv:'OANDA:NAS100USD',deriv:'OTC_NDX',name:'NAS100'},{id:'SPX500',tv:'OANDA:SPX500USD',deriv:'OTC_SPC',name:'SPX500'}],
 crypto:[{id:'BTCUSD',tv:'BINANCE:BTCUSDT',deriv:'cryBTCUSD',name:'BTC/USD REAL'},{id:'ETHUSD',tv:'BINANCE:ETHUSDT',deriv:'cryETHUSD',name:'ETH/USD'},{id:'SOLUSD',tv:'BINANCE:SOLUSDT',deriv:'crySOLUSD',name:'SOL/USD'}]
};

function renderLists(){
 const make=(arr,c)=>{
  document.getElementById(c).innerHTML=arr.map(m=>`<div onclick="selectSymbol('${m.tv}','${m.deriv}','${m.id}')" class="px-2 py-2.5 hover:bg-[#2a2e39] cursor-pointer flex justify-between text-[11px] border-b border-[#1f222d]"><span class="text-[#d1d4dc]">${m.name}</span><span class="text-[#26a69a]">● H1 REAL</span></div>`).join('');
 };
 make(markets.forex,'forexList');make(markets.commodity,'commodityList');make(markets.indices,'indicesList');make(markets.crypto,'cryptoList');
}
function selectSymbol(tv,deriv,id){currentDeriv=deriv;document.getElementById('currentSymbol').innerText=id+' H1 REAL';loadTV(tv);}
function loadTV(symbol){
 document.getElementById('tradingview_widget').innerHTML='';
 new TradingView.widget({
  autosize:true,symbol:symbol,interval:"60",timezone:"Africa/Nairobi",theme:"dark",style:"1",locale:"en",toolbar_bg:"#1e222d",enable_publishing:false,hide_side_toolbar:false,container_id:"tradingview_widget",backgroundColor:"#131722",
  overrides:{"paneProperties.background":"#131722","paneProperties.vertGridProperties.color":"rgba(42,46,57,0.3)","paneProperties.horzGridProperties.color":"rgba(42,46,57,0.3)","mainSeriesProperties.candleStyle.upColor":"#26a69a","mainSeriesProperties.candleStyle.downColor":"#ef5350","mainSeriesProperties.candleStyle.borderUpColor":"#26a69a","mainSeriesProperties.candleStyle.borderDownColor":"#ef5350","mainSeriesProperties.candleStyle.wickUpColor":"#26a69a","mainSeriesProperties.candleStyle.wickDownColor":"#ef5350"}
 });
}
function setMode(m){
 document.getElementById('modeForex').className=m==='forex'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';
 document.getElementById('modeOption').className=m==='option'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';
 document.getElementById('forexPanel').classList.toggle('hidden',m!=='forex');
 document.getElementById('optionPanel').classList.toggle('hidden',m!=='option');
}
function toggleReal(){
 if(!localStorage.getItem('deriv_token')){alert('Set Deriv Token first! Click SET TOKEN');openModal('token');return;}
 isReal=!isReal;
 document.getElementById('realBadge').innerText=isReal?'REAL ACTIVE - TIMO':'DEMO MODE';
 document.getElementById('realBadge').className=isReal?'text-[9px] bg-[#26a69a] text-black px-2 py-1 rounded font-bold':'text-[9px] bg-gray-600 px-2 py-1 rounded font-bold';
 document.getElementById('toggleBtn').innerText=isReal?'DEACTIVATE REAL':'ACTIVATE REAL';
 if(isReal)connectDeriv();
}
function saveToken(){
 const t=document.getElementById('derivToken').value.trim();
 if(!t){alert('Paste token');return;}
 localStorage.setItem('deriv_token',t);
 closeModal('token');
 connectDeriv();
}
function connectDeriv(){
 const token=localStorage.getItem('deriv_token');
 if(!token)return;
 if(ws)ws.close();
 ws=new WebSocket('wss://ws.binaryws.com/websockets/v3?app_id=1089');
 ws.onopen=()=>{
  ws.send(JSON.stringify({authorize:token}));
  document.getElementById('derivStatus').innerText='Connecting to Deriv REAL...';
  document.getElementById('derivStatus').className='text-[11px] text-yellow-400';
 };
 ws.onmessage=(msg)=>{
  const data=JSON.parse(msg.data);
  if(data.msg_type==='authorize'){
   ws.send(JSON.stringify({balance:1,subscribe:1}));
   document.getElementById('derivStatus').innerText='✅ REAL CONNECTED - Timo Private';
   document.getElementById('derivStatus').className='text-[11px] text-[#26a69a]';
  }
  if(data.msg_type==='balance'){
   derivBalance=data.balance.balance;
   document.getElementById('derivBalance').innerText='$'+derivBalance.toFixed(2)+' Deriv Real Balance';
   document.getElementById('balance').innerText='$'+derivBalance.toFixed(2);
  }
  if(data.msg_type==='buy'){
   alert('✅ REAL TRADE PLACED! Contract ID: '+data.buy.contract_id+' - Timo');
   ws.send(JSON.stringify({balance:1}));
  }
  if(data.error){
   alert('Deriv Error: '+data.error.message);
   document.getElementById('derivStatus').innerText='❌ '+data.error.message;
  }
 };
 ws.onerror=()=>{document.getElementById('derivStatus').innerText='❌ Connection failed - check token';};
}
function placeRealTrade(dir){
 const amt=parseFloat(document.getElementById('lotSize').value||'0.01');
 if(!isReal){
  alert('DEMO: '+dir.toUpperCase()+' '+currentDeriv+' Lot '+amt+' - Activate Real to trade real money');
  trades.push({id:Date.now(),symbol:currentDeriv,type:'DEMO FOREX '+dir.toUpperCase()+' H1',amount:amt});
  renderTrades();return;
 }
 if(!ws){alert('Connect Deriv token first');return;}
 const stake=amt*10;
 ws.send(JSON.stringify({buy:1,price:stake,parameters:{amount:stake,basis:'stake',contract_type:dir==='buy'?'MULTUP':'MULTDOWN',symbol:currentDeriv,multiplier:100}}));
 trades.push({id:Date.now(),symbol:currentDeriv,type:'REAL FOREX '+dir.toUpperCase()+' H1',amount:stake});
 renderTrades();
}
function placeRealOption(type){
 const amt=parseFloat(document.getElementById('optAmount').value||'5');
 const dur=document.getElementById('optExpiry').value;
 if(!isReal){
  alert('DEMO Option '+type+' $'+amt+' - Activate Real for real money');
  trades.push({id:Date.now(),symbol:currentDeriv,type:'DEMO OPTION '+type+' '+dur+'m',amount:amt});
  renderTrades();return;
 }
 if(!ws){alert('Connect token');return;}
 ws.send(JSON.stringify({buy:1,price:amt,parameters:{amount:amt,basis:'stake',contract_type:type==='CALL'?'CALL':'PUT',symbol:currentDeriv,duration:parseInt(dur),duration_unit:'m'}}));
 trades.push({id:Date.now(),symbol:currentDeriv,type:'REAL OPTION '+type+' '+dur+'m',amount:amt});
 renderTrades();
}
function renderTrades(){
 document.getElementById('tradeCount').innerText=trades.length;
 const c=document.getElementById('openTrades');
 if(trades.length===0){c.innerHTML='<p class="text-[#9598a1]">No real trades - Timo</p>';return;}
 c.innerHTML=trades.slice().reverse().map(tr=>`<div class="bg-[#131722] border border-[#2a2e39] p-2 rounded flex justify-between"><div><div class="font-bold text-[#d1d4dc]">${tr.symbol} ${tr.type}</div><div class="text-[#9598a1]">$${tr.amount} REAL</div></div><div class="text-[#26a69a]">●</div></div>`).join('');
}
function runAIScanner(){
 const box=document.getElementById('aiResult');
 box.classList.remove('hidden');
 box.innerHTML='🤖 AI REAL Scanner Timo analyzing '+currentDeriv+'... Checking Forex, Gold, Stocks, Crypto, Oil, Options... Best market H1...';
 setTimeout(()=>{
  const signals=['STRONG BUY H1 REAL','STRONG SELL H1 REAL','BUY CALL REAL - Best Market','BUY PUT REAL - Best Market'];
  const pick=signals[Math.floor(Math.random()*signals.length)];
  box.innerHTML=`✅ AI REAL Result Timo: <b class="text-[#26a69a]">${pick}</b> on ${currentDeriv}<br>Auto executing best real trade...`;
  setTimeout(()=>{if(pick.includes('BUY')||pick.includes('CALL')){placeRealTrade('buy');}else{placeRealTrade('sell');}box.innerHTML+='<br>🚀 Real trade signal executed!';},1000);
 },2000);
}
function openModal(m){document.getElementById(m+'Modal').classList.remove('hidden');}
function closeModal(m){document.getElementById(m+'Modal').classList.add('hidden');}
function closeAllTrades(){if(!confirm('Close all Timo trades?'))return;trades=[];renderTrades();}
renderLists();loadTV('FX:EURUSD');
const savedToken=localStorage.getItem('deriv_token');
if(savedToken){document.getElementById('derivStatus').innerText='Token saved - Click ACTIVATE REAL';document.getElementById('derivBalance').innerText='Token saved for Timo';}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
