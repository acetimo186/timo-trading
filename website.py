
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO SIMPLE DEPOSIT</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body style="background:#131722;color:#fff;margin:0" class="overflow-hidden">
<div id="lock" class="fixed inset-0 bg-[#131722] z-[100] flex items-center justify-center">
<div class="bg-[#1e222d] p-6 rounded border border-[#2a2e39] w-[300px] text-center">
<h2 class="font-bold">TIMO PRIVATE</h2><p class="text-[11px] text-[#9598a1] mb-4">Mine Alone - Simple Deposit</p>
<input id="user" type="text" value="Timo" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white">
<input id="pwd" type="password" placeholder="Password" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<button onclick="unlock()" class="w-full bg-[#2962ff] py-2 rounded font-bold text-sm">UNLOCK</button>
<p id="err" class="text-[11px] text-red-400 mt-2 hidden">Wrong</p>
</div>
</div>

<div class="flex justify-between items-center px-3 py-2 bg-[#1e222d] border-b border-[#2a2e39]">
<div class="flex items-center gap-2"><span class="font-bold text-sm">TIMO SIMPLE</span><span class="text-[9px] bg-[#26a69a] text-black px-2 py-1 rounded font-bold">PRIVATE BALANCE</span></div>
<div class="flex items-center gap-2"><span class="text-xs text-[#9598a1]">Balance:</span><span id="balance" class="font-bold text-[#26a69a] text-sm">$0.00</span><button onclick="openModal('deposit')" class="bg-[#26a69a] px-4 py-1.5 rounded text-xs font-bold">+ DEPOSIT</button><button onclick="openModal('withdraw')" class="bg-[#ef5350] px-4 py-1.5 rounded text-xs font-bold">- WITHDRAW</button></div>
</div>

<div class="flex h-[calc(100vh-42px)]">
<div class="w-[160px] bg-[#1e222d] border-r border-[#2a2e39] overflow-y-auto text-[11px] p-2">
<div class="text-[10px] text-[#9598a1] font-bold mb-1">FOREX H1</div><div id="forexList"></div>
<div class="text-[10px] text-[#9598a1] font-bold mt-3 mb-1">GOLD OIL</div><div id="commodityList"></div>
<div class="text-[10px] text-[#9598a1] font-bold mt-3 mb-1">US30 NAS100</div><div id="indicesList"></div>
<div class="text-[10px] text-[#9598a1] font-bold mt-3 mb-1">BTC ETH</div><div id="cryptoList"></div>
</div>

<div class="flex-1 flex flex-col bg-[#131722]">
<div class="flex justify-between items-center px-3 py-1.5 bg-[#1e222d] border-b border-[#2a2e39] text-xs"><span id="currentSymbol" class="font-bold bg-[#2a2e39] px-2 py-1 rounded">EURUSD H1</span><span id="currentPrice" class="text-[#26a69a] font-mono">LIVE CHART</span><button onclick="runAIScanner()" class="bg-[#2962ff] px-3 py-1 rounded font-bold text-[11px]">🤖 AI SCANNER</button></div>
<div id="tradingview_widget" class="flex-1"></div>
<div id="aiResult" class="hidden p-2 bg-[#1e222d] border-t border-[#2962ff] text-xs"></div>
</div>

<div class="w-[260px] bg-[#1e222d] border-l border-[#2a2e39] p-3 flex flex-col">
<div class="flex gap-1 mb-3"><button id="modeForex" onclick="setMode('forex')" class="flex-1 py-2 bg-white text-black rounded font-bold text-xs">FOREX</button><button id="modeOption" onclick="setMode('option')" class="flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs">OPTIONS</button></div>
<div id="forexPanel"><label class="text-[10px] text-[#9598a1]">Lot Size</label><input id="lotSize" type="number" value="0.01" step="0.01" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-sm"><div class="flex gap-2"><button onclick="placeTrade('buy')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold text-sm">BUY</button><button onclick="placeTrade('sell')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold text-sm">SELL</button></div></div>
<div id="optionPanel" class="hidden"><label class="text-[10px] text-[#9598a1]">Amount $</label><input id="optAmount" type="number" value="5" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-white text-sm"><select id="optExpiry" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-sm"><option value="1">1 min</option><option value="3" selected>3 min</option><option value="5">5 min</option><option value="15">15 min</option><option value="60">1 hour</option></select><div class="flex gap-2"><button onclick="placeOption('call')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold text-sm">CALL ▲</button><button onclick="placeOption('put')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold text-sm">PUT ▼</button></div></div>
<button onclick="closeAllTrades()" class="mt-4 w-full bg-[#2a2e39] py-2 rounded text-xs">CLOSE ALL TRADES</button>
<div class="mt-4 border-t border-[#2a2e39] pt-3"><p class="text-[11px] text-[#9598a1]">Open Trades (<span id="tradeCount">0</span>)</p><div id="openTrades" class="space-y-2 max-h-[320px] overflow-y-auto text-[11px] mt-2"></div></div>
</div>
</div>

<!-- SIMPLE DEPOSIT -->
<div id="depositModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-6 rounded w-[340px] border border-[#2a2e39] text-center">
<h3 class="font-bold mb-1">DEPOSIT - Timo Private</h3><p class="text-[11px] text-[#9598a1] mb-4">Add to your private balance - yours alone</p>
<input id="depositAmount" type="number" placeholder="Amount USD e.g 10" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-3 mb-2 text-white text-center text-lg font-bold">
<div class="flex gap-2 mb-3"><button onclick="quickAmt(5)" class="flex-1 bg-[#2a2e39] py-1 rounded text-xs">$5</button><button onclick="quickAmt(10)" class="flex-1 bg-[#2a2e39] py-1 rounded text-xs">$10</button><button onclick="quickAmt(50)" class="flex-1 bg-[#2a2e39] py-1 rounded text-xs">$50</button><button onclick="quickAmt(100)" class="flex-1 bg-[#2a2e39] py-1 rounded text-xs">$100</button></div>
<button onclick="doDeposit()" class="w-full bg-[#26a69a] py-3 rounded font-bold text-sm mb-2">DEPOSIT NOW - ADD TO BALANCE</button>
<button onclick="closeModal('deposit')" class="w-full bg-[#2a2e39] py-2 rounded text-sm">Cancel</button>
<p class="text-[10px] text-[#9598a1] mt-3">Balance saved on your device only. No M-Pesa code needed. Private.</p>
</div>
</div>

<!-- SIMPLE WITHDRAW -->
<div id="withdrawModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50">
<div class="bg-[#1e222d] p-6 rounded w-[340px] border border-[#2a2e39] text-center">
<h3 class="font-bold mb-1">WITHDRAW - Timo Private</h3><p class="text-[11px] text-[#9598a1] mb-4">Remove from private balance</p>
<input id="withdrawAmount" type="number" placeholder="Amount USD e.g 10" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-3 mb-3 text-white text-center text-lg font-bold">
<button onclick="doWithdraw()" class="w-full bg-[#ef5350] py-3 rounded font-bold text-sm mb-2">WITHDRAW NOW</button>
<button onclick="closeModal('withdraw')" class="w-full bg-[#2a2e39] py-2 rounded text-sm">Cancel</button>
<p class="text-[10px] text-[#9598a1] mt-3">Current: <span id="withdrawBalance">$0.00</span></p>
</div>
</div>

<script src="https://s3.tradingview.com/tv.js"></script>
<script>
const MY_USER="Timo";const MY_PASSWORD="KAUMONI20r4.";
function unlock(){const u=document.getElementById('user').value.trim();const p=document.getElementById('pwd').value;if(u===MY_USER&&p===MY_PASSWORD){document.getElementById('lock').classList.add('hidden');localStorage.setItem('timo_logged','1');}else{document.getElementById('err').classList.remove('hidden');}}
if(localStorage.getItem('timo_logged')==='1'){document.getElementById('lock').classList.add('hidden');}
let balance=parseFloat(localStorage.getItem('timo_simple_balance')||'0');let trades=JSON.parse(localStorage.getItem('timo_simple_trades')||'[]');
function updateBal(){document.getElementById('balance').innerText='$'+balance.toFixed(2);document.getElementById('withdrawBalance').innerText='$'+balance.toFixed(2);localStorage.setItem('timo_simple_balance',balance);}
function quickAmt(a){document.getElementById('depositAmount').value=a;}
function doDeposit(){const amt=parseFloat(document.getElementById('depositAmount').value);if(!amt||amt<=0){alert('Enter amount');return;}balance+=amt;updateBal();closeModal('deposit');alert('✅ Deposited $'+amt.toFixed(2)+'! New balance $'+balance.toFixed(2));document.getElementById('depositAmount').value='';}
function doWithdraw(){const amt=parseFloat(document.getElementById('withdrawAmount').value);if(!amt||amt<=0){alert('Enter amount');return;}if(amt>balance){alert('Insufficient - Balance $'+balance.toFixed(2));return;}balance-=amt;updateBal();closeModal('withdraw');alert('✅ Withdrew $'+amt.toFixed(2)+'! New balance $'+balance.toFixed(2)+'. (For private use, money stays with you)');document.getElementById('withdrawAmount').value='';}
const markets={forex:[{id:'EURUSD',tv:'FX:EURUSD',name:'EUR/USD H1'},{id:'GBPUSD',tv:'FX:GBPUSD',name:'GBP/USD'},{id:'USDJPY',tv:'FX:USDJPY',name:'USD/JPY'}],commodity:[{id:'GOLD',tv:'OANDA:XAUUSD',name:'GOLD H1'},{id:'OIL',tv:'TVC:USOIL',name:'Oil'}],indices:[{id:'US30',tv:'OANDA:US30USD',name:'US30'},{id:'NAS100',tv:'OANDA:NAS100USD',name:'NAS100'}],crypto:[{id:'BTCUSD',tv:'BINANCE:BTCUSDT',name:'BTC'},{id:'ETHUSD',tv:'BINANCE:ETHUSDT',name:'ETH'}]};
function renderLists(){const make=(arr,c)=>{document.getElementById(c).innerHTML=arr.map(m=>`<div onclick="selectSymbol('${m.tv}','${m.id}')" class="px-2 py-2 hover:bg-[#2a2e39] cursor-pointer flex justify-between border-b border-[#1f222d]"><span>${m.name}</span><span class="text-[#26a69a]">●</span></div>`).join('');};make(markets.forex,'forexList');make(markets.commodity,'commodityList');make(markets.indices,'indicesList');make(markets.crypto,'cryptoList');}
function selectSymbol(tv,id){document.getElementById('currentSymbol').innerText=id+' H1';loadTV(tv);}
function loadTV(s){document.getElementById('tradingview_widget').innerHTML='';new TradingView.widget({autosize:true,symbol:s,interval:"60",theme:"dark",style:"1",container_id:"tradingview_widget",backgroundColor:"#131722"});}
function setMode(m){document.getElementById('modeForex').className=m==='forex'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('modeOption').className=m==='option'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('forexPanel').classList.toggle('hidden',m!=='forex');document.getElementById('optionPanel').classList.toggle('hidden',m!=='option');}
function placeTrade(dir){trades.push({id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:dir.toUpperCase(),amount:parseFloat(document.getElementById('lotSize').value||0.01),profit:(Math.random()*4-1).toFixed(2),time:new Date().toLocaleTimeString()});saveTrades();renderTrades();}
function placeOption(dir){const amt=parseFloat(document.getElementById('optAmount').value||5);if(balance<amt){alert('Low balance - Click + DEPOSIT');return;}balance-=amt;updateBal();const t={id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:'OPTION '+dir.toUpperCase(),amount:amt,profit:'RUNNING',time:new Date().toLocaleTimeString()};trades.push(t);saveTrades();renderTrades();const mins=parseInt(document.getElementById('optExpiry').value);setTimeout(()=>{const win=Math.random()>0.45;const tr=trades.find(x=>x.id===t.id);if(tr){if(win){const prof=amt*0.85;tr.profit='+'+prof.toFixed(2);balance+=amt+prof;}else{tr.profit=(-amt).toFixed(2);}updateBal();saveTrades();renderTrades();}},mins*60000);}
function renderTrades(){document.getElementById('tradeCount').innerText=trades.length;document.getElementById('openTrades').innerHTML=trades.slice().reverse().map(tr=>{const col=String(tr.profit).includes('+')||parseFloat(tr.profit)>0?'text-[#26a69a]':tr.profit==='RUNNING'?'text-yellow-400':'text-[#ef5350]';return `<div class="bg-[#131722] border border-[#2a2e39] p-2 rounded flex justify-between"><div><div class="font-bold">${tr.symbol} ${tr.type}</div><div class="text-[#9598a1] text-[10px]">${tr.time} $${tr.amount}</div></div><div class="${col} font-bold">${tr.profit}</div></div>`;}).join('');}
function saveTrades(){localStorage.setItem('timo_simple_trades',JSON.stringify(trades));}
function runAIScanner(){const box=document.getElementById('aiResult');box.classList.remove('hidden');box.innerHTML='🤖 AI scanning H1...';setTimeout(()=>{box.innerHTML='✅ AI: STRONG BUY - Auto placing...';placeTrade('buy');},1500);}
function openModal(m){document.getElementById(m+'Modal').classList.remove('hidden');}
function closeModal(m){document.getElementById(m+'Modal').classList.add('hidden');}
function closeAllTrades(){trades=[];saveTrades();renderTrades();}
renderLists();loadTV('FX:EURUSD');updateBal();renderTrades();
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
