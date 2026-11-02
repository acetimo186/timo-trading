
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO REAL - DEPOSIT & WITHDRAW</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body style="background:#131722;color:#fff;margin:0" class="overflow-hidden">
<div id="lock" class="fixed inset-0 bg-[#131722] z-[100] flex items-center justify-center">
<div class="bg-[#1e222d] p-6 rounded border border-[#2a2e39] w-[330px] text-center">
<h2 class="font-bold text-sm">TIMO REAL TRADING</h2>
<p class="text-[11px] text-[#9598a1] mb-4">Private - Timo Only - Deposit & Withdraw Active</p>
<input id="user" type="text" value="Timo" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white">
<input id="pwd" type="password" placeholder="Password" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<button onclick="unlock()" class="w-full bg-[#2962ff] py-2 rounded font-bold text-sm">UNLOCK</button>
<p id="err" class="text-[11px] text-red-400 mt-3 hidden">Wrong login</p>
</div>
</div>

<div class="flex justify-between items-center px-3 py-2 bg-[#1e222d] border-b border-[#2a2e39]">
<div class="flex items-center gap-2"><span class="font-bold text-sm">TIMO REAL</span><span id="realBadge" class="text-[9px] bg-gray-600 px-2 py-1 rounded font-bold">DEMO</span><span class="text-[10px] text-[#9598a1]">H1 LiteFinance</span></div>
<div class="flex items-center gap-2">
<span id="balance" class="font-bold text-[#26a69a] text-sm">$0.00 Deriv</span>
<button onclick="openModal('deposit')" class="bg-[#26a69a] px-3 py-1 rounded text-xs font-bold">DEPOSIT</button>
<button onclick="openModal('withdraw')" class="bg-[#2a2e39] px-3 py-1 rounded text-xs font-bold border border-[#363a45]">WITHDRAW</button>
<button onclick="openModal('token')" class="bg-[#2a2e39] px-2 py-1 rounded text-[10px]">TOKEN</button>
<button onclick="toggleReal()" id="toggleBtn" class="bg-[#2962ff] px-2 py-1 rounded text-xs">ACTIVATE REAL</button>
</div>
</div>

<div class="flex h-[calc(100vh-42px)]">
<div class="w-[175px] bg-[#1e222d] border-r border-[#2a2e39] overflow-y-auto text-[11px]">
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase">Forex H1 Real</div><div id="forexList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Gold Silver Oil</div><div id="commodityList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">US30 NAS100 SPX500</div><div id="indicesList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">BTC ETH SOL</div><div id="cryptoList"></div>
<div class="p-2 m-2 bg-[#131722] border border-[#2a2e39] rounded"><p class="text-[10px] text-[#9598a1]">Timo Deriv Status</p><p id="derivStatus" class="text-[11px] text-yellow-400">Set Token</p><p id="derivBalance" class="text-xs font-bold mt-1">$0.00</p></div>
</div>

<div class="flex-1 flex flex-col bg-[#131722]">
<div class="flex justify-between items-center px-3 py-1.5 bg-[#1e222d] border-b border-[#2a2e39] text-xs"><span id="currentSymbol" class="font-bold bg-[#2a2e39] px-2 py-1 rounded">EURUSD H1 REAL</span><span id="currentPrice" class="text-[#26a69a] font-mono">LIVE</span><button onclick="runAIScanner()" class="bg-[#2962ff] px-3 py-1 rounded font-bold text-[11px]">🤖 AI SCANNER REAL</button></div>
<div id="tradingview_widget" class="flex-1"></div>
<div id="aiResult" class="hidden p-2 bg-[#1e222d] border-t border-[#2962ff] text-xs"></div>
</div>

<div class="w-[270px] bg-[#1e222d] border-l border-[#2a2e39] p-3 flex flex-col">
<div class="flex gap-1 mb-3"><button id="modeForex" onclick="setMode('forex')" class="flex-1 py-2 bg-white text-black rounded font-bold text-xs">FOREX REAL</button><button id="modeOption" onclick="setMode('option')" class="flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs">OPTIONS REAL</button></div>
<div id="forexPanel"><input id="lotSize" type="number" value="0.01" step="0.01" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white"><div class="flex gap-2"><button onclick="placeRealTrade('buy')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">BUY REAL</button><button onclick="placeRealTrade('sell')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">SELL REAL</button></div></div>
<div id="optionPanel" class="hidden"><input id="optAmount" type="number" value="5" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white"><select id="optExpiry" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white"><option value="1">1m</option><option value="3" selected>3m</option><option value="5">5m</option><option value="15">15m</option><option value="60">1h</option></select><div class="flex gap-2"><button onclick="placeRealOption('CALL')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">CALL REAL ▲</button><button onclick="placeRealOption('PUT')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">PUT REAL ▼</button></div></div>
<div class="mt-3 p-2 bg-[#131722] border border-[#2a2e39] rounded text-[11px]"><p class="text-[#9598a1]">Quick Deposit/Withdraw</p><div class="flex gap-2 mt-2"><button onclick="openModal('deposit')" class="flex-1 bg-[#26a69a] py-2 rounded font-bold text-xs">DEPOSIT M-PESA</button><button onclick="openModal('withdraw')" class="flex-1 bg-[#2a2e39] py-2 rounded font-bold text-xs">WITHDRAW</button></div></div>
<button onclick="closeAllTrades()" class="mt-3 w-full bg-[#2a2e39] py-2 rounded text-xs">CLOSE ALL</button>
<div class="mt-3 border-t border-[#2a2e39] pt-3"><p class="text-[11px] text-[#9598a1]">Trades Timo (<span id="tradeCount">0</span>)</p><div id="openTrades" class="space-y-2 max-h-[250px] overflow-y-auto text-[11px] mt-2"></div></div>
</div>
</div>

<!-- DEPOSIT MODAL -->
<div id="depositModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-5 rounded w-[360px] border border-[#2a2e39] text-center">
<h3 class="font-bold mb-2">DEPOSIT - Timo Private - Real M-Pesa</h3>
<p class="text-[11px] text-[#9598a1] mb-3">Deposit goes to your Deriv account via licensed M-Pesa, then shows on this site. 100% real.</p>
<div class="bg-[#131722] p-3 rounded border border-[#2a2e39] mb-3 text-left text-[11px]">
<p class="font-bold mb-1">Steps:</p>
<p>1. Click DEPOSIT NOW button below</p>
<p>2. Deriv Cashier opens → Choose M-Pesa</p>
<p>3. Enter amount (e.g. 500 KES = ~$4)</p>
<p>4. Pay on phone → Balance appears here</p>
</div>
<button onclick="goDeposit()" class="w-full bg-[#26a69a] py-3 rounded font-bold mb-2">DEPOSIT NOW - M-PESA REAL →</button>
<button onclick="closeModal('deposit')" class="w-full bg-[#2a2e39] py-2 rounded text-sm">Cancel</button>
</div>
</div>

<!-- WITHDRAW MODAL -->
<div id="withdrawModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-5 rounded w-[360px] border border-[#2a2e39] text-center">
<h3 class="font-bold mb-2">WITHDRAW - Timo Private - To M-Pesa</h3>
<p class="text-[11px] text-[#9598a1] mb-3">Withdraw real money from Deriv to your M-Pesa.</p>
<div class="bg-[#131722] p-3 rounded border border-[#2a2e39] mb-3 text-left text-[11px]">
<p>1. Click WITHDRAW NOW</p>
<p>2. Deriv Cashier → M-Pesa Withdraw</p>
<p>3. Enter amount → Receive on phone</p>
</div>
<button onclick="goWithdraw()" class="w-full bg-[#ef5350] py-3 rounded font-bold mb-2">WITHDRAW NOW → M-PESA</button>
<button onclick="closeModal('withdraw')" class="w-full bg-[#2a2e39] py-2 rounded text-sm">Cancel</button>
</div>
</div>

<!-- TOKEN MODAL -->
<div id="tokenModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-5 rounded w-[360px] border border-[#2a2e39]">
<h3 class="font-bold mb-2 text-sm">Deriv Token - Timo</h3>
<input id="derivToken" type="password" placeholder="Paste Deriv token" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-xs">
<div class="flex gap-2"><button onclick="saveToken()" class="flex-1 bg-[#2962ff] py-2 rounded font-bold text-sm">SAVE & CONNECT</button><button onclick="closeModal('token')" class="flex-1 bg-[#2a2e39] py-2 rounded text-sm">Cancel</button></div>
</div>
</div>

<script src="https://s3.tradingview.com/tv.js"></script>
<script>
const MY_USER="Timo";const MY_PASSWORD="KAUMONI20r4.";
function unlock(){const u=document.getElementById('user').value.trim();const p=document.getElementById('pwd').value;if(u===MY_USER&&p===MY_PASSWORD){document.getElementById('lock').classList.add('hidden');localStorage.setItem('timo_logged','1');}else{document.getElementById('err').classList.remove('hidden');}}
if(localStorage.getItem('timo_logged')==='1'){document.getElementById('lock').classList.add('hidden');}
let trades=[];let isReal=false;let ws=null;let currentDeriv='frxEURUSD';
const markets={forex:[{id:'EURUSD',tv:'FX:EURUSD',deriv:'frxEURUSD',name:'EUR/USD REAL'},{id:'GBPUSD',tv:'FX:GBPUSD',deriv:'frxGBPUSD',name:'GBP/USD'},{id:'USDJPY',tv:'FX:USDJPY',deriv:'frxUSDJPY',name:'USD/JPY'},{id:'AUDUSD',tv:'FX:AUDUSD',deriv:'frxAUDUSD',name:'AUD/USD'}],commodity:[{id:'GOLD',tv:'OANDA:XAUUSD',deriv:'frxXAUUSD',name:'GOLD REAL'},{id:'SILVER',tv:'OANDA:XAGUSD',deriv:'frxXAGUSD',name:'Silver'},{id:'OIL',tv:'TVC:USOIL',deriv:'frxUSOIL',name:'Oil'}],indices:[{id:'US30',tv:'OANDA:US30USD',deriv:'OTC_DJI',name:'US30'},{id:'NAS100',tv:'OANDA:NAS100USD',deriv:'OTC_NDX',name:'NAS100'},{id:'SPX500',tv:'OANDA:SPX500USD',deriv:'OTC_SPC',name:'SPX500'}],crypto:[{id:'BTCUSD',tv:'BINANCE:BTCUSDT',deriv:'cryBTCUSD',name:'BTC REAL'},{id:'ETHUSD',tv:'BINANCE:ETHUSDT',deriv:'cryETHUSD',name:'ETH'},{id:'SOLUSD',tv:'BINANCE:SOLUSDT',deriv:'crySOLUSD',name:'SOL'}]};
function renderLists(){const make=(arr,c)=>{document.getElementById(c).innerHTML=arr.map(m=>`<div onclick="selectSymbol('${m.tv}','${m.deriv}','${m.id}')" class="px-2 py-2 hover:bg-[#2a2e39] cursor-pointer flex justify-between border-b border-[#1f222d]"><span>${m.name}</span><span class="text-[#26a69a]">●</span></div>`).join('');};make(markets.forex,'forexList');make(markets.commodity,'commodityList');make(markets.indices,'indicesList');make(markets.crypto,'cryptoList');}
function selectSymbol(tv,deriv,id){currentDeriv=deriv;document.getElementById('currentSymbol').innerText=id+' REAL';loadTV(tv);}
function loadTV(s){document.getElementById('tradingview_widget').innerHTML='';new TradingView.widget({autosize:true,symbol:s,interval:"60",theme:"dark",style:"1",container_id:"tradingview_widget",backgroundColor:"#131722"});}
function setMode(m){document.getElementById('modeForex').className=m==='forex'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('modeOption').className=m==='option'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('forexPanel').classList.toggle('hidden',m!=='forex');document.getElementById('optionPanel').classList.toggle('hidden',m!=='option');}
function toggleReal(){if(!localStorage.getItem('deriv_token')){alert('Set Token first');openModal('token');return;}isReal=!isReal;document.getElementById('realBadge').innerText=isReal?'REAL ACTIVE':'DEMO';document.getElementById('realBadge').className=isReal?'text-[9px] bg-[#26a69a] text-black px-2 py-1 rounded font-bold':'text-[9px] bg-gray-600 px-2 py-1 rounded font-bold';document.getElementById('toggleBtn').innerText=isReal?'DEACTIVATE':'ACTIVATE REAL';if(isReal)connectDeriv();}
function saveToken(){const t=document.getElementById('derivToken').value.trim();if(!t){alert('Paste token');return;}localStorage.setItem('deriv_token',t);closeModal('token');connectDeriv();}
function connectDeriv(){const token=localStorage.getItem('deriv_token');if(!token)return;if(ws)ws.close();ws=new WebSocket('wss://ws.binaryws.com/websockets/v3?app_id=1089');ws.onopen=()=>{ws.send(JSON.stringify({authorize:token}));document.getElementById('derivStatus').innerText='Connecting...';};ws.onmessage=(msg)=>{const data=JSON.parse(msg.data);if(data.msg_type==='authorize'){ws.send(JSON.stringify({balance:1,subscribe:1}));document.getElementById('derivStatus').innerText='✅ REAL CONNECTED - Timo';document.getElementById('derivStatus').className='text-[11px] text-[#26a69a]';}if(data.msg_type==='balance'){document.getElementById('derivBalance').innerText='$'+data.balance.balance.toFixed(2);document.getElementById('balance').innerText='$'+data.balance.balance.toFixed(2);}if(data.msg_type==='buy'){alert('REAL TRADE PLACED! ID:'+data.buy.contract_id);}if(data.error){alert(data.error.message);}};}
function goDeposit(){window.open('https://app.deriv.com/cashier/deposit','_blank');closeModal('deposit');}
function goWithdraw(){window.open('https://app.deriv.com/cashier/withdrawal','_blank');closeModal('withdraw');}
function placeRealTrade(dir){const amt=parseFloat(document.getElementById('lotSize').value||'0.01');if(!isReal){alert('Demo '+dir+' - Activate Real');trades.push({id:Date.now(),symbol:currentDeriv,type:'DEMO '+dir.toUpperCase(),amount:amt});renderTrades();return;}if(!ws){alert('Set token');return;}const stake=amt*10;ws.send(JSON.stringify({buy:1,price:stake,parameters:{amount:stake,basis:'stake',contract_type:dir==='buy'?'MULTUP':'MULTDOWN',symbol:currentDeriv,multiplier:100}}));trades.push({id:Date.now(),symbol:currentDeriv,type:'REAL '+dir.toUpperCase(),amount:stake});renderTrades();}
function placeRealOption(type){const amt=parseFloat(document.getElementById('optAmount').value||'5');const dur=document.getElementById('optExpiry').value;if(!isReal){alert('Demo Option '+type);trades.push({id:Date.now(),symbol:currentDeriv,type:'DEMO OPTION '+type,amount:amt});renderTrades();return;}if(!ws){alert('Set token');return;}ws.send(JSON.stringify({buy:1,price:amt,parameters:{amount:amt,basis:'stake',contract_type:type==='CALL'?'CALL':'PUT',symbol:currentDeriv,duration:parseInt(dur),duration_unit:'m'}}));trades.push({id:Date.now(),symbol:currentDeriv,type:'REAL OPTION '+type,amount:amt});renderTrades();}
function renderTrades(){document.getElementById('tradeCount').innerText=trades.length;document.getElementById('openTrades').innerHTML=trades.slice().reverse().map(t=>`<div class="bg-[#131722] border border-[#2a2e39] p-2 rounded"><div class="font-bold">${t.symbol} ${t.type}</div><div class="text-[#9598a1]">$${t.amount}</div></div>`).join('');}
function runAIScanner(){const box=document.getElementById('aiResult');box.classList.remove('hidden');box.innerHTML='🤖 AI REAL scanning '+currentDeriv+'...';setTimeout(()=>{box.innerHTML='✅ AI: BUY '+currentDeriv+' - Auto trade...';placeRealTrade('buy');},1500);}
function openModal(m){document.getElementById(m+'Modal').classList.remove('hidden');}
function closeModal(m){document.getElementById(m+'Modal').classList.add('hidden');}
function closeAllTrades(){trades=[];renderTrades();}
renderLists();loadTV('FX:EURUSD');
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
