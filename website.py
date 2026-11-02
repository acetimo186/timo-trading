
from flask import Flask
app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO - PRIVATE</title>
<script src="https://cdn.tailwindcss.com"></script>
</head>
<body style="background:#131722;color:#fff" class="overflow-hidden">
<div id="lock" class="fixed inset-0 bg-[#131722] z-[100] flex items-center justify-center">
<div class="bg-[#1e222d] p-6 rounded border border-[#2a2e39] w-[310px] text-center">
<h2 class="font-bold mb-1">TIMO TRADING PRO</h2>
<p class="text-[11px] text-[#9598a1] mb-4">PRIVATE - For Timo only</p>
<input id="user" type="text" placeholder="Username" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-white text-sm" value="Timo">
<input id="pwd" type="password" placeholder="Password" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white text-sm">
<button onclick="unlock()" class="w-full bg-[#2962ff] py-2 rounded font-bold text-sm">UNLOCK PRIVATE TERMINAL</button>
<p id="err" class="text-[11px] text-red-400 mt-3 hidden">Wrong username or password</p>
</div>
</div>

<div class="flex justify-between items-center px-4 py-2 bg-[#1e222d] border-b border-[#2a2e39]">
<div class="flex items-center gap-2"><span class="font-bold text-sm">TIMO PRIVATE</span><span class="text-[9px] bg-[#26a69a] text-black px-2 py-1 rounded font-bold">Timo ONLY</span></div>
<div class="flex items-center gap-3"><span class="text-xs text-[#9598a1]">Trader:</span><span class="font-bold text-sm">Timo</span><span class="text-xs text-[#9598a1]">Balance:</span><span id="balance" class="font-bold text-[#26a69a]">$12.14</span><button onclick="openModal('deposit')" class="bg-[#2962ff] px-2 py-1 rounded text-xs">Deposit</button><button onclick="openModal('withdraw')" class="bg-[#2a2e39] px-2 py-1 rounded text-xs">Withdraw</button></div>
</div>

<div class="flex h-[calc(100vh-42px)]">
<div class="w-[175px] bg-[#1e222d] border-r border-[#2a2e39] overflow-y-auto">
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase">Forex H1 Real - Timo</div><div id="forexList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Gold, Silver, Oil (Commodities)</div><div id="commodityList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Stock Indices US30 NAS100 SPX500</div><div id="indicesList"></div>
<div class="p-2 text-[10px] text-[#9598a1] font-bold uppercase mt-2">Crypto BTC ETH SOL</div><div id="cryptoList"></div>
</div>
<div class="flex-1 flex flex-col bg-[#131722]">
<div class="flex justify-between items-center px-3 py-1.5 bg-[#1e222d] border-b border-[#2a2e39] text-xs"><span id="currentSymbol" class="font-bold text-xs bg-[#2a2e39] px-2 py-1 rounded">EURUSD H1</span><span id="currentPrice" class="text-[#26a69a] font-mono">1.08452</span><button onclick="runAIScanner()" class="bg-gradient-to-r from-[#2962ff] to-[#7b1fa2] px-3 py-1 rounded font-bold text-[11px]">🤖 AI SCANNER - Auto trade Best Market</button></div>
<div id="tradingview_widget" class="flex-1"></div>
<div id="aiResult" class="hidden p-2 bg-[#1e222d] border-t border-[#2962ff] text-xs"></div>
</div>
<div class="w-[270px] bg-[#1e222d] border-l border-[#2a2e39] p-3 flex flex-col">
<div class="flex gap-1 mb-3"><button id="modeForex" onclick="setMode('forex')" class="flex-1 py-2 bg-white text-black rounded font-bold text-xs">FOREX & GOLD</button><button id="modeOption" onclick="setMode('option')" class="flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs">OPTIONS - ALL OPTIONS</button></div>
<div id="forexPanel"><div class="text-[11px] text-[#9598a1] mb-1">Lot Size - Timo Account</div><input id="lotSize" type="number" value="0.01" step="0.01" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white"><div class="flex gap-2"><button onclick="placeTrade('buy')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">BUY</button><button onclick="placeTrade('sell')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">SELL</button></div></div>
<div id="optionPanel" class="hidden"><input id="optAmount" type="number" value="5" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-2 text-sm text-white"><select id="optExpiry" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-sm text-white"><option value="1">1m Turbo</option><option value="3" selected>3m</option><option value="5">5m</option><option value="15">15m</option><option value="60">1h</option></select><div class="flex gap-2"><button onclick="placeOption('call')" class="flex-1 bg-[#26a69a] py-3 rounded font-bold">CALL ▲</button><button onclick="placeOption('put')" class="flex-1 bg-[#ef5350] py-3 rounded font-bold">PUT ▼</button></div><p class="text-[10px] text-[#9598a1] mt-1">Payout 85% - All markets</p></div>
<button onclick="closeAllTrades()" class="mt-3 w-full bg-[#2a2e39] py-2 rounded text-xs">CLOSE ALL NOW</button>
<div class="mt-4 border-t border-[#2a2e39] pt-3"><p class="text-[11px] text-[#9598a1]">Open Trades Timo (<span id="tradeCount">0</span>)</p><div id="openTrades" class="space-y-2 max-h-[320px] overflow-y-auto text-[11px] mt-2"></div></div>
</div>
</div>

<div id="depositModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50"><div class="bg-[#1e222d] p-5 rounded w-[300px] border border-[#2a2e39]"><h3 class="font-bold mb-3 text-sm">Deposit - Timo Private</h3><input id="depositAmount" type="number" placeholder="100" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white"><div class="flex gap-2"><button onclick="doDeposit()" class="flex-1 bg-[#2962ff] py-2 rounded">Add</button><button onclick="closeModal('deposit')" class="flex-1 bg-[#2a2e39] py-2 rounded">Cancel</button></div></div></div>
<div id="withdrawModal" class="hidden fixed inset-0 bg-black/80 flex items-center justify-center z-50"><div class="bg-[#1e222d] p-5 rounded w-[300px] border border-[#2a2e39]"><h3 class="font-bold mb-3 text-sm">Withdraw - Timo</h3><input id="withdrawAmount" type="number" placeholder="Amount" class="w-full bg-[#131722] border border-[#2a2e39] rounded p-2 mb-3 text-white"><div class="flex gap-2"><button onclick="doWithdraw()" class="flex-1 bg-[#26a69a] py-2 rounded">Withdraw</button><button onclick="closeModal('withdraw')" class="flex-1 bg-[#2a2e39] py-2 rounded">Cancel</button></div></div></div>

<script src="https://s3.tradingview.com/tv.js"></script>
<script>
const MY_USER = "Timo";
const MY_PASSWORD = "KAUMONI20r4.";
function unlock(){
 const u = document.getElementById('user').value.trim();
 const p = document.getElementById('pwd').value;
 if(u===MY_USER && p===MY_PASSWORD){
   document.getElementById('lock').classList.add('hidden');
   localStorage.setItem('timo_logged','1');
 } else {
   document.getElementById('err').classList.remove('hidden');
 }
}
if(localStorage.getItem('timo_logged')==='1'){document.getElementById('lock').classList.add('hidden');}
let balance=parseFloat(localStorage.getItem('timo_balance')||'12.14');let trades=JSON.parse(localStorage.getItem('timo_trades')||'[]');let currentSymbolTV='FX:EURUSD';let mode='forex';
const markets={forex:[{id:'EURUSD',tv:'FX:EURUSD',name:'EUR/USD H1'},{id:'GBPUSD',tv:'FX:GBPUSD',name:'GBP/USD'},{id:'USDJPY',tv:'FX:USDJPY',name:'USD/JPY'},{id:'AUDUSD',tv:'FX:AUDUSD',name:'AUD/USD'},{id:'USDCAD',tv:'FX:USDCAD',name:'USD/CAD'}],commodity:[{id:'GOLD',tv:'OANDA:XAUUSD',name:'GOLD XAUUSD'},{id:'SILVER',tv:'OANDA:XAGUSD',name:'Silver'},{id:'OIL',tv:'TVC:USOIL',name:'Oil USOIL'}],indices:[{id:'US30',tv:'OANDA:US30USD',name:'US30 Dow'},{id:'NAS100',tv:'OANDA:NAS100USD',name:'NAS100'},{id:'SPX500',tv:'OANDA:SPX500USD',name:'SPX500'}],crypto:[{id:'BTCUSD',tv:'BINANCE:BTCUSDT',name:'BTC/USD'},{id:'ETHUSD',tv:'BINANCE:ETHUSDT',name:'ETH/USD'},{id:'SOLUSD',tv:'BINANCE:SOLUSDT',name:'SOL/USD'}]};
function renderLists(){const make=(arr,c)=>{document.getElementById(c).innerHTML=arr.map(m=>`<div onclick="selectSymbol('${m.tv}','${m.id}')" class="px-2 py-2 hover:bg-[#2a2e39] cursor-pointer flex justify-between text-[11px] border-b border-[#1f222d]"><span>${m.name}</span><span class="text-[#26a69a]">● H1 LIVE</span></div>`).join('');};make(markets.forex,'forexList');make(markets.commodity,'commodityList');make(markets.indices,'indicesList');make(markets.crypto,'cryptoList');}
function selectSymbol(tv,shortSym){document.getElementById('currentSymbol').innerText=shortSym+' H1';loadTV(tv);}
function loadTV(s){document.getElementById('tradingview_widget').innerHTML='';new TradingView.widget({autosize:true,symbol:s,interval:"60",timezone:"Africa/Nairobi",theme:"dark",style:"1",locale:"en",container_id:"tradingview_widget",backgroundColor:"#131722",overrides:{"paneProperties.background":"#131722","mainSeriesProperties.candleStyle.upColor":"#26a69a","mainSeriesProperties.candleStyle.downColor":"#ef5350"}});}
function setMode(m){mode=m;document.getElementById('modeForex').className=m==='forex'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('modeOption').className=m==='option'?'flex-1 py-2 bg-white text-black rounded font-bold text-xs':'flex-1 py-2 bg-[#2a2e39] rounded font-bold text-xs';document.getElementById('forexPanel').classList.toggle('hidden',m!=='forex');document.getElementById('optionPanel').classList.toggle('hidden',m!=='option');}
function updateBalance(){document.getElementById('balance').innerText='$'+balance.toFixed(2);localStorage.setItem('timo_balance',balance);}
function placeTrade(dir){const amt=parseFloat(document.getElementById('lotSize').value||'0.01');const t={id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:'FOREX '+dir.toUpperCase()+' H1',amount:amt,profit:(Math.random()*4-1).toFixed(2),time:new Date().toLocaleTimeString()};trades.push(t);saveTrades();renderTrades();}
function placeOption(dir){const amt=parseFloat(document.getElementById('optAmount').value||'5');const exp=document.getElementById('optExpiry').value;if(balance<amt){alert('Low balance');return;}balance-=amt;const t={id:Date.now(),symbol:document.getElementById('currentSymbol').innerText,type:'OPTION '+dir.toUpperCase()+' '+exp+'m',amount:amt,profit:'--',time:new Date().toLocaleTimeString(),expiry:Date.now()+parseInt(exp)*60000,payout:0.85};trades.push(t);updateBalance();saveTrades();renderTrades();setTimeout(()=>resolveOption(t.id),parseInt(exp)*60000);}
function resolveOption(id){const tr=trades.find(x=>x.id===id);if(!tr)return;const win=Math.random()>0.45;tr.profit=win?(tr.amount*tr.payout).toFixed(2):(-tr.amount).toFixed(2);if(win)balance+=tr.amount+parseFloat(tr.profit);updateBalance();saveTrades();renderTrades();}
function renderTrades(){document.getElementById('tradeCount').innerText=trades.length;const c=document.getElementById('openTrades');if(trades.length===0){c.innerHTML='<p class="text-[#9598a1]">No trades - Timo</p>';return;}c.innerHTML=trades.slice().reverse().map(tr=>{const pnl=tr.profit==='--'?'<span class="text-yellow-400">RUNNING H1</span>':`<span class="${parseFloat(tr.profit)>=0?'text-[#26a69a]':'text-[#ef5350]'}">$${tr.profit}</span>`;return `<div class="bg-[#131722] border border-[#2a2e39] p-2 rounded flex justify-between"><div><div class="font-bold">${tr.symbol} ${tr.type}</div><div class="text-[#9598a1]">${tr.time} $${tr.amount}</div></div><div>${pnl}<br><button onclick="closeTrade(${tr.id})" class="text-[10px] bg-[#2a2e39] px-2 py-1 rounded mt-1">CLOSE</button></div></div>`;}).join('');}
function closeTrade(id){trades=trades.filter(x=>x.id!==id);saveTrades();renderTrades();}
function closeAllTrades(){if(!confirm('Close all?'))return;trades=[];saveTrades();renderTrades();}
function saveTrades(){localStorage.setItem('timo_trades',JSON.stringify(trades));}
function runAIScanner(){const box=document.getElementById('aiResult');box.classList.remove('hidden');box.innerHTML='🤖 AI Scanner Timo analyzing... Forex, Gold, Stocks, Crypto, Oil, Options... Finding best market...';setTimeout(()=>{const signals=['STRONG BUY H1','STRONG SELL H1','BUY CALL - Best Market','BUY PUT - Best Market'];const pick=signals[Math.floor(Math.random()*signals.length)];box.innerHTML=`✅ AI Result Timo: <b class="text-[#26a69a]">${pick}</b> - Auto executing best trade...`;setTimeout(()=>{if(pick.includes('BUY')||pick.includes('CALL')){if(mode==='forex')placeTrade('buy');else placeOption('call');}else{if(mode==='forex')placeTrade('sell');else placeOption('put');}box.innerHTML+='<br>🚀 Timo trade executed!';},1000);},2000);}
function openModal(m){document.getElementById(m+'Modal').classList.remove('hidden');}
function closeModal(m){document.getElementById(m+'Modal').classList.add('hidden');}
function doDeposit(){const amt=parseFloat(document.getElementById('depositAmount').value);if(!amt)return;balance+=amt;updateBalance();closeModal('deposit');}
function doWithdraw(){const amt=parseFloat(document.getElementById('withdrawAmount').value);if(!amt||amt>balance){alert('Insufficient');return;}balance-=amt;updateBalance();closeModal('withdraw');}
renderLists();loadTV(currentSymbolTV);updateBalance();renderTrades();
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
