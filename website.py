
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO PRIVATE - DEPOSIT ON SITE</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body style="background:#131722;color:#fff;margin:0" class="overflow-hidden">
<div id="lock" class="fixed inset-0 bg-[#131722] z-[100] flex items-center justify-center">
<div class="bg-[#1e222d] p-6 rounded border border-[#2a2e39] w-[320px] text-center">
<h2 class="font-bold">TIMO PRIVATE TERMINAL</h2><p class="text-[11px] text-[#9598a1] mb-4">Mine Alone - Deposit on My Site</p>
<input id="user" type="text" value="Timo" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white">
<input id="pwd" type="password" placeholder="Password" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white">
<button onclick="unlock()" class="w-full bg-[#2962ff] py-2 rounded font-bold text-sm">UNLOCK PRIVATE</button>
<p id="err" class="text-[11px] text-red-400 mt-2 hidden">Wrong</p>
</div>
</div>

<div class="flex justify-between items-center px-3 py-2 bg-[#1e222d] border-b border-[#2a2e39]">
<div class="flex items-center gap-2"><span class="font-bold text-sm">TIMO PRIVATE</span><span class="text-[9px] bg-[#26a69a] text-black px-2 py-1 rounded font-bold">MINE ALONE</span></div>
<div class="flex items-center gap-2"><span class="text-xs text-[#9598a1]">Balance:</span><span id="balance" class="font-bold text-[#26a69a]">$12.14</span><button onclick="openModal('deposit')" class="bg-[#26a69a] px-3 py-1 rounded text-xs font-bold">DEPOSIT ON SITE</button><button onclick="openModal('withdraw')" class="bg-[#2a2e39] px-3 py-1 rounded text-xs border">WITHDRAW ON SITE</button></div>
</div>

<div class="flex h-[calc(100vh-42px)]">
<div class="w-[175px] bg-[#1e222d] border-r border-[#2a2e39] overflow-y-auto text-[11px]"><div id="forexList"></div><div id="commodityList"></div><div id="indicesList"></div><div id="cryptoList"></div></div>
<div class="flex-1 flex flex-col bg-[#131722]"><div class="flex justify-between items-center px-3 py-1.5 bg-[#1e222d] border-b border-[#2a2e39] text-xs"><span id="currentSymbol" class="font-bold bg-[#2a2e39] px-2 py-1 rounded">EURUSD H1</span><button onclick="runAIScanner()" class="bg-[#2962ff] px-3 py-1 rounded font-bold text-[11px]">🤖 AI SCANNER</button></div><div id="tradingview_widget" class="flex-1"></div><div id="aiResult" class="hidden p-2 bg-[#1e222d] border-t border-[#2962ff] text-xs"></div></div>
<div class="w-[270px] bg-[#1e222d] border-l border-[#2a2e39] p-3 flex flex-col"><div class="flex gap-1 mb-3"><button id="modeForex" onclick="setMode('forex')" class="flex-1 py-2 bg-white text-black rounded font-bold text-xs">FOREX</button><button id="modeOption" onclick="setMode('option')" class="flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs">OPTIONS</button></div><div id="forexPanel"><input id="lotSize" type="number" value="0.01" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white"><div class="flex gap-2"><button onclick="placeTrade('buy')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">BUY</button><button onclick="placeTrade('sell')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">SELL</button></div></div><div id="optionPanel" class="hidden"><input id="optAmount" type="number" value="5" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-white"><select id="optExpiry" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white"><option value="1">1m</option><option value="3" selected>3m</option><option value="5">5m</option><option value="15">15m</option><option value="60">1h</option></select><div class="flex gap-2"><button onclick="placeOption('call')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">CALL</button><button onclick="placeOption('put')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">PUT</button></div></div><button onclick="closeAllTrades()" class="mt-3 w-full bg-[#2a2e39] py-2 rounded text-xs">CLOSE ALL</button><div class="mt-4 border-t border-[#2a2e39] pt-3"><p class="text-[11px] text-[#9598a1]">Trades (<span id="tradeCount">0</span>)</p><div id="openTrades" class="space-y-2 max-h-[300px] overflow-y-auto text-[11px] mt-2"></div></div></div>
</div>

<div id="depositModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50"><div class="bg-[#1e222d] p-5 rounded w-[340px] border border-[#2a2e39]"><h3 class="font-bold mb-3">DEPOSIT - On My Site Alone</h3><input id="depositAmount" type="number" placeholder="Amount $ e.g 10" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-white"><input id="mpesaCode" type="text" placeholder="M-Pesa Code (optional) for your record" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-sm"><div class="flex gap-2"><button onclick="doDeposit()" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">DEPOSIT NOW ON SITE</button><button onclick="closeModal('deposit')" class="flex-1 bg-[#2a2e39] py-2 rounded">Cancel</button></div><p class="text-[10px] text-[#9598a1] mt-2">This adds to your private balance on this device only. No redirect to Deriv.</p></div></div>

<div id="withdrawModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50"><div class="bg-[#1e222d] p-5 rounded w-[340px] border border-[#2a2e39]"><h3 class="font-bold mb-3">WITHDRAW - From My Site</h3><input id="withdrawAmount" type="number" placeholder="Amount $" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-white"><input id="mpesaPhone" type="text" placeholder="Your M-Pesa phone 07..." class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-sm"><div class="flex gap-2"><button onclick="doWithdraw()" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">WITHDRAW ON SITE</button><button onclick="closeModal('withdraw')" class="flex-1 bg-[#2a2e39] py-2 rounded">Cancel</button></div></div></div>

<script src="https://s3.tradingview.com/tv.js"></script>
<script>
const MY_USER="Timo";const MY_PASSWORD="KAUMONI20r4.";
function unlock(){const u=document.getElementById('user').value.trim();const p=document.getElementById('pwd').value;if(u===MY_USER&&p===MY_PASSWORD){document.getElementById('lock').classList.add('hidden');localStorage.setItem('timo_logged','1');}else{document.getElementById('err').classList.remove('hidden');}}
if(localStorage.getItem('timo_logged')==='1'){document.getElementById('lock').classList.add('hidden');}
let balance=parseFloat(localStorage.getItem('timo_private_balance')||'12.14');let trades=JSON.parse(localStorage.getItem('timo_trades')||'[]');
function updateBal(){document.getElementById('balance').innerText='$'+balance.toFixed(2);localStorage.setItem('timo_private_balance',balance);}
const markets={forex:[{id:'EURUSD',tv:'FX:EURUSD',name:'EUR/USD H1'},{id:'GBPUSD',tv:'FX:GBPUSD',name:'GBP/USD'}],commodity:[{id:'GOLD',tv:'OANDA:XAUUSD',name:'GOLD'},{id:'OIL',tv:'TVC:USOIL',name:'Oil'}],indices:[{id:'US30',tv:'OANDA:US30USD',name:'US30'},{id:'NAS100',tv:'OANDA:NAS100USD',name:'NAS100'}],crypto:[{id:'BTCUSD',tv:'BINANCE:BTCUSDT',name:'BTC'},{id:'ETHUSD',tv:'BINANCE:ETHUSDT',name:'ETH'}]};
function renderLists(){const make=(arr,c)=>{document.getElementById(c).innerHTML=arr.map(m=>`<div onclick="selectSymbol('${m.tv}','${m.id}')" class="px-2 py-2 hover:bg-[#2a2e39] cursor-pointer flex justify-between border-b border-[#1f222d]"><span>${m.name}</span><span class="text-[#26a69a]">●</span></div>`).join('');};make(markets.forex,'forexList');make(markets.commodity,'commodityList');make(markets.indices,'indicesList');make(markets.crypto,'cryptoList');}
function selectSymbol(tv,id){document.getElementById('currentSymbol').innerText=id+' H1';loadTV(tv);}
function loadTV(s){document.getElementById('tradingview_widget').innerHTML='';new TradingView.widget({autosize:true,symbol:s,interval:"60",theme:"dark",style:"1",container_id:"tradingview_widget",backgroundColor:"#131722"});}
function setMode(m){document.getElementById('modeForex').className=m==='forex'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('modeOption').className=m==='option'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('forexPanel').classList.toggle('hidden',m!=='forex');document.getElementById('optionPanel').classList.toggle('hidden',m!=='option');}
function doDeposit(){const amt=parseFloat(document.getElementById('depositAmount').value);if(!amt||amt<=0){alert('Enter amount');return;}balance+=amt;updateBal();closeModal('deposit');alert('Deposited $'+amt+' on your private site! New balance $'+balance.toFixed(2));document.getElementById('depositAmount').value='';}
function doWithdraw(){const amt=parseFloat(document.getElementById('withdrawAmount').value);if(!amt||amt>balance){alert('Insufficient balance');return;}balance-=amt;updateBal();closeModal('withdraw');alert('Withdrew $'+amt+' - Send to M-Pesa '+document.getElementById('mpesaPhone').value+' - Balance $'+balance.toFixed(2));}
function placeTrade(dir){const amt=parseFloat(document.getElementById('lotSize').value||'0.01');trades.push({id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:dir.toUpperCase(),amount:amt,profit:(Math.random()*4-1).toFixed(2),time:new Date().toLocaleTimeString()});saveTrades();renderTrades();}
function placeOption(dir){const amt=parseFloat(document.getElementById('optAmount').value||'5');if(balance<amt){alert('Low balance - Deposit');return;}balance-=amt;const t={id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:'OPTION '+dir.toUpperCase(),amount:amt,profit:'--',time:new Date().toLocaleTimeString()};trades.push(t);updateBal();saveTrades();renderTrades();setTimeout(()=>{const win=Math.random()>0.45;const tr=trades.find(x=>x.id===t.id);if(tr){tr.profit=win?(amt*0.85).toFixed(2):(-amt).toFixed(2);if(win)balance+=amt+parseFloat(tr.profit);updateBal();saveTrades();renderTrades();}},parseInt(document.getElementById('optExpiry').value)*60000);}
function renderTrades(){document.getElementById('tradeCount').innerText=trades.length;document.getElementById('openTrades').innerHTML=trades.slice().reverse().map(tr=>{const pnl=tr.profit==='--'?'<span class="text-yellow-400">RUNNING</span>':`<span class="${parseFloat(tr.profit)>=0?'text-[#26a69a]':'text-[#ef5350]'}">$${tr.profit}</span>`;return `<div class="bg-[#131722] border border-[#2a2e39] p-2 rounded flex justify-between"><div><div class="font-bold">${tr.symbol} ${tr.type}</div><div class="text-[#9598a1]">${tr.time}</div></div><div>${pnl}</div></div>`;}).join('');}
function saveTrades(){localStorage.setItem('timo_trades',JSON.stringify(trades));}
function runAIScanner(){const box=document.getElementById('aiResult');box.classList.remove('hidden');box.innerHTML='🤖 AI scanning best market...';setTimeout(()=>{box.innerHTML='✅ AI: STRONG BUY - Auto buying...';placeTrade('buy');},1500);}
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
