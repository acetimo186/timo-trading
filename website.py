import os, json
from flask import Flask, jsonify, request
import websocket

app = Flask(__name__)

# Token comes ONLY from Render Env Vars - never paste it in code
DERIV_TOKEN = os.environ.get("DERIV_TOKEN", "")
DERIV_APP_ID = os.environ.get("DERIV_APP_ID", "1089")

HTML_CODE = r"""
<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO TRADING — Intelligence. Precision. Execution.</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"></script>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#070A0F;color:#E8EEF6;font-family:Inter,sans-serif}nav{display:flex;justify-content:space-between;align-items:center;padding:14px 22px;border-bottom:1px solid #1A2E4A;position:sticky;top:0;background:#070A0F;z-index:99}.logo{font-weight:900}.logo small{display:block;color:#D4AF37;font-size:11px;letter-spacing:3px}.btn{border:0;border-radius:10px;padding:11px 18px;font-weight:800;cursor:pointer}.btn-blue{background:#0EA5E9;color:#fff}.btn-gold{background:#D4AF37;color:#111}.hero{padding:40px 22px;text-align:center;background:linear-gradient(180deg,rgba(7,10,15,.55),#070A0F),url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2000&auto=format&fit=crop') center/cover}h1{font-size:clamp(32px,6vw,58px);line-height:1}h1 span{color:#D4AF37}.wrap{max-width:1280px;margin:0 auto;padding:18px 16px 40px}.card{background:#0A1628;border:1px solid #1A2E4A;border-radius:14px;overflow:hidden}.card-h{padding:12px 14px;border-bottom:1px solid #1A2E4A;display:flex;justify-content:space-between;font-weight:800;font-size:13px}.card-h span{color:#D4AF37}.terminal{display:grid;grid-template-columns:260px 1fr 320px;gap:12px}.watch-row{display:flex;justify-content:space-between;padding:11px 14px;border-bottom:1px solid #12233A;cursor:pointer}.watch-row.active{background:#0E2A3D}#chart{height:340px}.order{padding:14px}.order input,.order select{width:100%;background:#05070A;border:1px solid #1A2E4A;color:#fff;padding:11px;border-radius:10px;margin:6px 0}.buy{background:#26A69A;color:#fff;border:0;padding:13px;border-radius:10px;font-weight:900}.sell{background:#EF5350;color:#fff;border:0;padding:13px;border-radius:10px;font-weight:900}.order-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}.pillars{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.pillar{background:#0E1E33;border:1px solid #1A2E4A;border-radius:14px;padding:16px}.pillar h3{color:#D4AF37}.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.kpi div{background:#0A1628;border:1px solid #1A2E4A;border-radius:14px;padding:14px}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}table{width:100%;border-collapse:collapse;font-size:13px}th{text-align:left;color:#8AA0B8;padding:10px;border-bottom:1px solid #1A2E4A}td{padding:11px;border-bottom:1px solid #12233A}.badge2{padding:4px 8px;border-radius:100px;font-size:11px;font-weight:800}.b-bull{background:rgba(38,166,154,.15);color:#2DD4BF}.b-neutral{background:rgba(212,175,55,.15);color:#F5D67A}@media(max-width:1020px){.terminal{grid-template-columns:1fr 1fr}.pillars{grid-template-columns:repeat(2,1fr)}}@media(max-width:640px){.terminal{grid-template-columns:1fr}.pillars{grid-template-columns:1fr}.grid2,.kpi{grid-template-columns:1fr 1fr}}
</style></head><body>
<nav><div class="logo"><small>TIMO</small>TRADING</div><div><span id="derivStatus" style="font-size:12px;color:#F87171">● DERIV DEMO: NOT CONNECTED</span> &nbsp; <button class="btn btn-gold" onclick="connectDeriv()">Connect Deriv Demo</button></div></nav>
<header class="hero"><div style="display:inline-block;background:#0E1E33;border:1px solid #1A2E4A;padding:7px 12px;border-radius:100px;font-size:12px;color:#38BDF8">● LIVE • DERIV DEMO API READY</div><h1>TIMO TRADING<br><span>INTELLIGENCE. PRECISION.<br>EXECUTION.</span></h1><p style="max-width:700px;margin:12px auto;color:#C3D0DE">Trade only on your website. Connected to Deriv Demo — real live prices, real execution, virtual money.</p><div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:18px"><div class="card" style="padding:14px;min-width:160px;text-align:left"><small style="color:#8AA0B8">Deriv Demo Balance</small><b id="derivBalance" style="display:block;font-size:20px">$10,000.00</b></div><div class="card" style="padding:14px;min-width:160px;text-align:left"><small style="color:#8AA0B8">Account</small><b id="derivLogin" style="display:block">VRTC - Demo</b></div><div class="card" style="padding:14px;min-width:160px;text-align:left"><small style="color:#8AA0B8">Mode</small><b style="display:block;color:#D4AF37">DEMO • SAFE</b></div></div></header>
<div class="wrap"><div id="ticker" style="display:flex;gap:10px;overflow:auto"></div>
<div style="display:flex;justify-content:space-between;margin:20px 0 10px"><h2 id="terminal">◈ TIMO TERMINAL — DERIV DEMO</h2><span id="clock">--:--:-- EAT</span></div>
<div class="terminal"><div class="card"><div class="card-h">WATCHLIST <span>DERIV</span></div><div id="watchlist"></div></div>
<div class="card"><div class="card-h"><span id="chartSymbol">EUR/USD • 1H</span><span id="chartPrice">1.16482</span></div><div id="chart"></div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:12px"><div><small style="color:#8AA0B8">BIAS</small><b style="color:#2DD4BF;display:block">Bullish</b></div><div><small style="color:#8AA0B8">STRUCTURE</small><b style="display:block">HH / HL</b></div><div><small style="color:#8AA0B8">LIQUIDITY</small><b style="display:block">BSL</b></div><div><small style="color:#8AA0B8">RSI</small><b id="rsiVal" style="display:block">52.4</b></div></div></div>
<div class="card"><div class="card-h">ORDER TICKET — DERIV DEMO <span>API</span></div><div class="order"><select id="ordSymbol"><option value="frxEURUSD">EUR/USD</option><option value="frxXAUUSD">XAUUSD GOLD</option><option value="frxGBPUSD">GBP/USD</option><option value="cryBTCUSD">BTCUSD</option><option value="frxUSDJPY">USD/JPY</option></select><div class="order-row"><input id="lot" value="0.10" type="number" step="0.01"><input id="stake" value="10" type="number" placeholder="Stake $"></div><select id="tradeType"><option value="CALL">CALL / BUY ↑ (Rise)</option><option value="PUT">PUT / SELL ↓ (Fall)</option></select><select id="duration"><option value="60">1 Minute</option><option value="300">5 Minutes</option></select><div class="order-row" style="margin-top:10px"><button class="buy" onclick="placeDerivTrade('CALL')">BUY CALL ↑</button><button class="sell" onclick="placeDerivTrade('PUT')">SELL PUT ↓</button></div><p id="orderMsg" style="font-size:12px;color:#F5D67A;margin-top:10px"></p><div style="background:#05070A;border:1px solid #1A2E4A;border-radius:10px;padding:10px;font-size:12px">Balance: <b id="equity2">$10,000.00</b><br>P&L Today: <b id="pnl" style="color:#2DD4BF">+$0.00</b><br>Your 10% Fee: <b id="fee" style="color:#D4AF37">$0.00</b></div></div></div></div>
<div style="margin:18px 0 10px"><h2>THE TIMO PLATFORM • FIVE PILLARS</h2></div><div class="pillars"><div class="pillar"><h3>TERMINAL</h3><p>Trade on Deriv Demo from here.</p></div><div class="pillar"><h3>INTELLIGENCE</h3><p>AI bias + RSI + structure.</p></div><div class="pillar"><h3>SCANNER</h3><p>SMC BOS / CHoCH / FVG.</p></div><div class="pillar"><h3>RISK</h3><p>1% risk, 10% fee tracker.</p></div><div class="pillar"><h3>RESEARCH</h3><p>Daily brief + calendar.</p></div></div>
<div class="grid2" style="margin-top:16px"><div class="card"><div class="card-h">RISK CALCULATOR</div><div style="padding:14px">Balance: <input id="bal" value="1000" type="number" oninput="calcRisk()" style="width:100%;background:#05070A;border:1px solid #1A2E4A;color:#fff;padding:10px;border-radius:8px"> Risk %: <input id="risk" value="1" type="number" oninput="calcRisk()" style="width:100%;background:#05070A;border:1px solid #1A2E4A;color:#fff;padding:10px;border-radius:8px;margin-top:6px"> SL Pips: <input id="slPips" value="30" type="number" oninput="calcRisk()" style="width:100%;background:#05070A;border:1px solid #1A2E4A;color:#fff;padding:10px;border-radius:8px;margin-top:6px"><div style="background:#05070A;border:1px solid #1A2E4A;border-radius:10px;padding:12px;margin-top:10px">Risk: <b id="riskAmt">$10</b> | Lot: <b id="lotCalc" style="color:#D4AF37">0.03</b> | Profit 1:2: <b id="profitCalc" style="color:#2DD4BF">$20</b> | 10% Fee: <b id="feeCalc" style="color:#D4AF37">$2</b></div></div></div>
<div class="card"><div class="card-h">CLIENTS — 10% TRACKER</div><table><thead><tr><th>CLIENT</th><th>PROFIT</th><th>10%</th><th>STATUS</th></tr></thead><tbody><tr><td>Sarah M.</td><td style="color:#2DD4BF">+$150</td><td>$15.00</td><td><span class="badge2 b-neutral">UNPAID</span></td></tr><tr><td>David K.</td><td style="color:#2DD4BF">+$85</td><td>$8.50</td><td><span class="badge2 b-bull">PAID ✓</span></td></tr></tbody></table><div style="padding:12px"><button class="btn btn-gold" style="width:100%">Collect 10% via M-Pesa Till</button></div></div></div>
<footer style="text-align:center;color:#8AA0B8;font-size:12px;margin-top:20px">TIMO TRADING • DEMO MODE — Virtual money. Trading is risky. Start demo, go real only when ready.<br>© 2026 TIMO TRADING</footer></div>
<script>
let prices={'EUR/USD':1.16482,'XAUUSD':2642.10,'GBP/USD':1.3120,'BTCUSD':97842,'USD/JPY':154.20};
function renderAll(){document.getElementById('ticker').innerHTML=Object.keys(prices).map(k=>`<div class="card" style="min-width:170px;padding:12px"><small style="color:#8AA0B8">${k}</small><br><b>${prices[k].toLocaleString()}</b></div>`).join('');document.getElementById('watchlist').innerHTML=Object.keys(prices).map(k=>`<div class="watch-row" onclick="selectSym('${k}',this)"><b>${k}</b><b>${prices[k].toLocaleString()}</b></div>`).join('');}
renderAll();
function selectSym(s,el){document.querySelectorAll('.watch-row').forEach(r=>r.classList.remove('active'));el.classList.add('active');document.getElementById('chartSymbol').textContent=s+' • 1H';}
let chart=LightweightCharts.createChart(document.getElementById('chart'),{layout:{background:{color:'#0A1628'},textColor:'#8AA0B8'},grid:{vertLines:{color:'#12233A'},horzLines:{color:'#12233A'}},width:document.getElementById('chart').clientWidth,height:340});
let cs=chart.addCandlestickSeries({upColor:'#26A69A',downColor:'#EF5350',wickUpColor:'#26A69A',wickDownColor:'#EF5350'});let data=[];let base=1.1648;let t=Math.floor(Date.now()/1000)-100*3600;for(let i=0;i<100;i++){let o=base;let c=base+(Math.random()-0.46)*0.0018;base=c;data.push({time:t+i*3600,open:o,high:Math.max(o,c)+0.0004,low:Math.min(o,c)-0.0004,close:c});}cs.setData(data);
let ws=new WebSocket('wss://ws.binaryws.com/websockets/v3?app_id=1089');
ws.onopen=()=>{['frxEURUSD','frxXAUUSD','frxGBPUSD','cryBTCUSD','frxUSDJPY'].forEach(s=>ws.send(JSON.stringify({ticks:s})));};
ws.onmessage=(m)=>{let d=JSON.parse(m.data);if(d.tick){let map={'frxEURUSD':'EUR/USD','frxXAUUSD':'XAUUSD','frxGBPUSD':'GBP/USD','cryBTCUSD':'BTCUSD','frxUSDJPY':'USD/JPY'};let k=map[d.tick.symbol];if(k){prices[k]=d.tick.quote;renderAll();document.getElementById('chartPrice').textContent=d.tick.quote;}}};
async function connectDeriv(){let r=await fetch('/api/deriv/status');let j=await r.json();if(j.connected){document.getElementById('derivStatus').textContent='● DERIV DEMO: CONNECTED • '+j.loginid;document.getElementById('derivStatus').style.color='#2DD4BF';document.getElementById('derivBalance').textContent='$'+j.balance.toLocaleString();document.getElementById('derivLogin').textContent=j.loginid;document.getElementById('equity2').textContent='$'+j.balance.toLocaleString();}else{document.getElementById('derivStatus').textContent='● DERIV DEMO: '+j.error;alert('Add DERIV_TOKEN in Render Env Vars, then redeploy. Error: '+j.error);}}
async function placeDerivTrade(type){let sym=document.getElementById('ordSymbol').value;let stake=document.getElementById('stake').value;document.getElementById('orderMsg').textContent='Placing '+type+' '+sym+' $'+stake+' on Deriv Demo...';let r=await fetch('/api/deriv/buy',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({symbol:sym,amount:parseFloat(stake),contract_type:type,duration:60})});let j=await r.json();document.getElementById('orderMsg').textContent=j.message||JSON.stringify(j);}
function calcRisk(){let bal=parseFloat(document.getElementById('bal').value)||1000;let rr=parseFloat(document.getElementById('risk').value)||1;let sl=parseFloat(document.getElementById('slPips').value)||30;let amt=bal*rr/100;document.getElementById('riskAmt').textContent='$'+amt.toFixed(2);document.getElementById('lotCalc').textContent=(amt/(sl*10)).toFixed(2);document.getElementById('profitCalc').textContent='$'+(amt*2).toFixed(2);document.getElementById('feeCalc').textContent='$'+(amt*2*0.10).toFixed(2);document.getElementById('fee').textContent='$'+(amt*2*0.10).toFixed(2);}calcRisk();
setInterval(()=>{document.getElementById('clock').textContent=new Date().toLocaleTimeString('en-GB',{timeZone:'Africa/Nairobi'})+' EAT';document.getElementById('rsiVal').textContent=(50+Math.random()*10).toFixed(1);},1000);
</script></body></html>
"""

def deriv_call(payload):
    if not DERIV_TOKEN:
        return {"error": "No DERIV_TOKEN in Render Env Vars"}
    try:
        ws = websocket.create_connection(f"wss://ws.binaryws.com/websockets/v3?app_id={DERIV_APP_ID}", timeout=10)
        ws.send(json.dumps({"authorize": DERIV_TOKEN}))
        auth = json.loads(ws.recv())
        if "error" in auth:
            ws.close()
            return {"error": auth["error"]["message"]}
        ws.send(json.dumps(payload))
        res = json.loads(ws.recv())
        ws.close()
        return res
    except Exception as e:
        return {"error": str(e)}

@app.route("/")
def index():
    return HTML_CODE

@app.route("/health")
def health():
    return "OK"

@app.route("/api/deriv/status")
def deriv_status():
    if not DERIV_TOKEN:
        return jsonify({"connected": False, "error": "DERIV_TOKEN not set in Render"})
    res = deriv_call({"balance": 1})
    if "error" in res:
        return jsonify({"connected": False, "error": res["error"]})
    bal = res.get("balance", {}).get("balance", 0)
    loginid = res.get("balance", {}).get("loginid", "VRTC")
    return jsonify({"connected": True, "balance": bal, "loginid": loginid})

@app.route("/api/deriv/buy", methods=["POST"])
def deriv_buy():
    data = request.get_json() or {}
    symbol = data.get("symbol", "frxEURUSD")
    amount = data.get("amount", 10)
    ctype = data.get("contract_type", "CALL")
    duration = data.get("duration", 60)
    prop = deriv_call({"proposal": 1, "amount": amount, "basis": "stake", "contract_type": ctype, "currency": "USD", "duration": duration, "duration_unit": "s", "symbol": symbol})
    if "error" in prop:
        return jsonify({"success": False, "message": "Proposal error: " + str(prop["error"])})
    proposal_id = prop.get("proposal", {}).get("id")
    if not proposal_id:
        return jsonify({"success": False, "message": "No proposal: " + str(prop)})
    buy = deriv_call({"buy": proposal_id, "price": amount})
    if "error" in buy:
        return jsonify({"success": False, "message": "Buy error: " + str(buy["error"])})
    contract_id = buy.get("buy", {}).get("contract_id")
    return jsonify({"success": True, "message": f"✓ {ctype} {symbol} ${amount} placed on Deriv Demo! Contract: {contract_id}", "contract_id": contract_id})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
