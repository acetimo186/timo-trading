
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="TIMO TRADING - Intelligence. Precision. Execution.", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
#MainMenu, footer, header {visibility:hidden;}
.block-container {padding:0 !important; max-width:100% !important;}
.stApp {background:#070A0F;}
</style>
""", unsafe_allow_html=True)

HTML_CODE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIMO TRADING — Intelligence. Precision. Execution.</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lightweight-charts@4.1.3/dist/lightweight-charts.standalone.production.js"></script>
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{--bg:#070A0F;--card:#0A1628;--card2:#0E1E33;--line:#1A2E4A;--blue:#0EA5E9;--blue2:#38BDF8;--gold:#D4AF37;--gold2:#F5D67A;--green:#26A69A;--red:#EF5350;--text:#E8EEF6;--muted:#8AA0B8}
body{background:var(--bg);color:var(--text);font-family:Inter,system-ui,sans-serif;line-height:1.5;overflow-x:hidden}
a{color:inherit;text-decoration:none}
button{cursor:pointer;font-family:inherit}
.mono{font-family:'JetBrains Mono',monospace}
.topbar{background:#05070A;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;padding:8px 22px;font-size:12px;color:var(--muted);position:sticky;top:0;z-index:100}
.topbar b{color:var(--green)}
nav{display:flex;justify-content:space-between;align-items:center;padding:14px 22px;background:rgba(7,10,15,.92);backdrop-filter:blur(12px);position:sticky;top:31px;z-index:99;border-bottom:1px solid var(--line)}
.logo{display:flex;align-items:center;gap:10px;font-weight:900;letter-spacing:.5px}
.logo-mark{width:38px;height:38px;border:1.5px solid var(--gold);display:grid;place-items:center;color:var(--gold);font-size:20px;transform:rotate(45deg);border-radius:4px}
.logo-mark span{transform:rotate(-45deg)}
.logo small{display:block;color:var(--gold);font-size:11px;letter-spacing:3px;font-weight:700}
.logo b{font-size:19px;line-height:1}
.nav-links{display:flex;gap:22px;font-size:13.5px;font-weight:600;color:#C7D3E0}
.nav-links a:hover{color:var(--blue2)}
.btn{border:0;border-radius:10px;padding:11px 18px;font-weight:800;font-size:14px}
.btn-blue{background:var(--blue);color:#fff}
.btn-gold{background:var(--gold);color:#111}
.btn-outline{background:transparent;color:#fff;border:1px solid #2A3F5A}
.hero{position:relative;padding:52px 22px 36px;overflow:hidden;background:linear-gradient(180deg,rgba(7,10,15,.55),rgba(7,10,15,.92) 65%,#070A0F 100%),url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=2000&auto=format&fit=crop') center/cover,url('https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=2000&auto=format&fit=crop') center/cover;}
.hero:before{content:'';position:absolute;inset:0;background:radial-gradient(800px 300px at 50% 0%,rgba(14,165,233,.28),transparent 70%);pointer-events:none}
.hero-inner{max-width:1180px;margin:0 auto;position:relative;text-align:center}
.badge{display:inline-flex;gap:8px;align-items:center;background:#0E1E33;border:1px solid var(--line);padding:7px 12px;border-radius:100px;font-size:12px;color:var(--blue2);font-weight:700}
.badge i{width:7px;height:7px;background:#22C55E;border-radius:50%;display:inline-block;box-shadow:0 0 0 4px rgba(34,197,94,.18)}
h1{font-size:clamp(32px,6vw,62px);line-height:.98;font-weight:900;letter-spacing:-1px;margin:18px 0 14px}
h1 span{color:var(--gold)}
.hero p{max-width:760px;margin:0 auto;color:#C3D0DE;font-size:clamp(15px,2vw,18px)}
.hero-cta{display:flex;gap:12px;justify-content:center;margin:22px 0;flex-wrap:wrap}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;max-width:900px;margin:0 auto}
.stat{background:rgba(10,22,40,.85);border:1px solid var(--line);border-radius:14px;padding:16px;text-align:left;display:flex;gap:12px;align-items:flex-start}
.stat b{font-size:20px} .stat small{color:var(--muted);display:block;font-size:13px}
.wrap{max-width:1280px;margin:0 auto;padding:18px 16px 40px}
.section-title{display:flex;justify-content:space-between;align-items:end;margin:26px 0 12px}
.section-title h2{font-size:22px} .section-title p{color:var(--muted);font-size:13px}
.ticker{display:flex;gap:10px;overflow:auto;padding-bottom:6px;scrollbar-width:none}
.ticker::-webkit-scrollbar{display:none}
.tick{min-width:180px;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px}
.tick small{color:var(--muted)} .tick b{font-size:17px} .up{color:var(--green)} .down{color:var(--red)}
.terminal{display:grid;grid-template-columns:260px 1fr 320px;gap:12px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.card-h{padding:12px 14px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;font-weight:800;font-size:13px;letter-spacing:.4px}
.card-h span{color:var(--gold)}
.watch-row{display:flex;justify-content:space-between;padding:11px 14px;border-bottom:1px solid #12233A;cursor:pointer}
.watch-row.active{background:#0E2A3D}
.watch-row:hover{background:#0E1E33}
.watch-row small{color:var(--muted);display:block}
#chart{height:340px;width:100%}
.chart-tools{display:flex;gap:6px;padding:10px 14px;flex-wrap:wrap}
.chip{padding:7px 11px;border-radius:100px;border:1px solid var(--line);background:#0E1E33;font-size:12px;font-weight:700;color:#fff}
.chip.active{background:var(--blue);color:#fff;border-color:var(--blue)}
.order{padding:14px}
.order input,.order select{width:100%;background:#05070A;border:1px solid var(--line);color:#fff;padding:11px;border-radius:10px;margin:6px 0}
.order-row{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.buy{background:var(--green)} .sell{background:var(--red)} .buy,.sell{color:#fff;border:0;padding:13px;border-radius:10px;font-weight:900}
.pillars{display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
.pillar{background:linear-gradient(180deg,#0E1E33,#0A1628);border:1px solid var(--line);border-radius:14px;padding:16px}
.pillar i{font-size:26px} .pillar h3{color:var(--gold);font-size:15px;margin:10px 0 6px} .pillar p{color:var(--muted);font-size:13px}
.pillar button{margin-top:12px;width:100%;background:#122A44;border:1px solid var(--line);color:#fff;padding:9px;border-radius:8px;font-weight:700}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
table{width:100%;border-collapse:collapse;font-size:13px}
th{text-align:left;color:var(--muted);font-size:11px;letter-spacing:.6px;padding:10px 12px;border-bottom:1px solid var(--line)}
td{padding:11px 12px;border-bottom:1px solid #12233A}
.badge2{padding:4px 8px;border-radius:100px;font-size:11px;font-weight:800}
.b-bull{background:rgba(38,166,154,.15);color:#2DD4BF} .b-bear{background:rgba(239,83,80,.15);color:#F87171} .b-neutral{background:rgba(212,175,55,.15);color:var(--gold2)}
.ai-box{padding:14px} .ai-box p{color:#C3D0DE;font-size:14px}
.kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.kpi div{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px}
.kpi small{color:var(--muted)} .kpi b{font-size:22px;display:block}
input,select{font-family:inherit}
.field{margin:8px 0} .field label{font-size:12px;color:var(--muted)} .field input,.field select{width:100%;background:#05070A;border:1px solid var(--line);color:#fff;padding:11px;border-radius:10px}
.news{padding:12px 14px;border-bottom:1px solid #12233A} .news small{color:var(--blue2)} .news b{display:block;margin:3px 0}
footer{border-top:1px solid var(--line);padding:22px;text-align:center;color:var(--muted);font-size:13px}
.disclaimer{max-width:900px;margin:12px auto 0;color:#5A6E86;font-size:12px;line-height:1.6}
@media(max-width:1020px){.terminal{grid-template-columns:1fr 1fr}.terminal .ai-col{grid-column:1/-1}.pillars{grid-template-columns:repeat(2,1fr)}.grid3{grid-template-columns:1fr 1fr}.kpi{grid-template-columns:repeat(2,1fr)}}
@media(max-width:640px){
.topbar{display:none} nav{top:0} .nav-links{display:none} .stats{grid-template-columns:1fr} .terminal{grid-template-columns:1fr} .pillars{grid-template-columns:1fr} .grid2,.grid3{grid-template-columns:1fr} .kpi{grid-template-columns:1fr 1fr}
.mobile-nav{position:fixed;bottom:0;left:0;right:0;background:#0A1628;border-top:1px solid var(--line);display:flex;justify-content:space-around;padding:10px 6px 14px;z-index:100;font-size:11px}
.mobile-nav a{text-align:center;color:var(--muted)} .mobile-nav a.active{color:var(--blue2)} body{padding-bottom:62px}
}
@media(min-width:641px){.mobile-nav{display:none}}
</style>
</head>
<body>
<div class="topbar"><div>● LIVE &nbsp; XAUUSD <b id="topGold">2,642.10</b> &nbsp; EURUSD <b id="topEur">1.1648</b> &nbsp; BTCUSD <b id="topBtc">97,842</b></div><div>DERIV • BINANCE • TRADINGVIEW &nbsp; | &nbsp; <span style="color:#22C55E">● SYSTEM OPERATIONAL</span></div></div>
<nav><a href="#" class="logo"><div class="logo-mark"><span>◬</span></div><div><small>TIMO</small><b>TRADING</b></div></a><div class="nav-links"><a href="#terminal">Terminal</a><a href="#intelligence">Intelligence</a><a href="#scanner">Scanner</a><a href="#risk">Risk</a><a href="#research">Research</a></div><div style="display:flex;gap:8px"><button class="btn btn-outline" onclick="showAuth()">Login</button><button class="btn btn-gold" onclick="showAuth()">Sign Up</button></div></nav>
<header class="hero"><div class="hero-inner"><div class="badge"><i></i> MARKET INTELLIGENCE • LIVE</div><h1>TIMO TRADING<br><span>INTELLIGENCE. PRECISION.<br>EXECUTION.</span></h1><p>The next generation of trading intelligence. Advanced market analytics, institutional-style charting, intelligent market research and professional trading tools in one platform.</p><div class="hero-cta"><button class="btn btn-blue" onclick="document.getElementById('terminal').scrollIntoView({behavior:'smooth'})">Explore Platform →</button><button class="btn btn-outline" onclick="document.getElementById('scanner').scrollIntoView({behavior:'smooth'})">Explore Markets</button></div><div class="stats"><div class="stat"><span style="font-size:22px">◉</span><div><b>24/5</b><small>Market monitoring</small></div></div><div class="stat"><span style="font-size:22px">▦</span><div><b>MTF</b><small>Market analysis</small></div></div><div class="stat"><span style="font-size:22px">🤖</span><div><b>AI</b><small>Research assistant</small></div></div></div></div></header>
<div class="wrap">
<div class="ticker" id="ticker"></div>
<div class="section-title" id="terminal"><div><h2>◈ TIMO TERMINAL</h2><p>Professional charting and trading workspace — Desktop workstation / Mobile app</p></div><div><span class="badge2 b-bull">● CONNECTED</span> <span class="mono" id="clock">--:--:-- EAT</span></div></div>
<div class="terminal">
<div class="card"><div class="card-h">WATCHLIST <span>▼</span></div><div id="watchlist"></div><div style="padding:12px"><button class="btn btn-blue" style="width:100%" onclick="alert('Connect Deriv API in Settings to enable real execution. Demo mode now.')">+ Add Symbol</button></div></div>
<div class="card"><div class="card-h"><span id="chartSymbol">EUR/USD • 1H</span><span id="chartPrice" class="mono">1.16482 • +0.24%</span></div><div class="chart-tools"><button class="chip" onclick="setTF('1m',this)">1m</button><button class="chip" onclick="setTF('15m',this)">15m</button><button class="chip active" onclick="setTF('1H',this)">1H</button><button class="chip" onclick="setTF('4H',this)">4H</button><span style="margin-left:auto;color:var(--muted);font-size:12px">PRICE ACTION • Connect Deriv for live candles</span></div><div id="chart"></div><div style="display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:12px 14px"><div><small style="color:var(--muted)">MARKET BIAS</small><b style="color:#2DD4BF;display:block">Bullish</b></div><div><small style="color:var(--muted)">TIMEFRAME</small><b style="display:block">H4</b></div><div><small style="color:var(--muted)">STRUCTURE</small><b style="display:block">HH / HL</b></div><div><small style="color:var(--muted)">LIQUIDITY</small><b style="display:block">BSL</b></div></div></div>
<div class="card ai-col"><div class="card-h">AI MARKET COMMENTARY <span>AI</span></div><div class="ai-box"><p id="aiText">Illustrative scenario: Price is showing bullish structure. Monitor nearby liquidity and wait for confirmation before considering a setup.</p><p style="margin-top:10px;font-size:12px;color:var(--muted)">RSI <b id="rsiVal" style="color:#fff">52.4</b> • MACD <b style="color:#fff">Bullish Cross</b> • ATR <b style="color:#fff">0.0018</b></p></div><div class="card-h">ORDER TICKET</div><div class="order"><select id="ordSymbol"><option>EUR/USD</option><option>XAUUSD</option><option>GBP/USD</option><option>BTCUSD</option><option>USD/JPY</option></select><div class="order-row"><div><label style="font-size:12px;color:var(--muted)">Lot Size</label><input id="lot" value="0.10" type="number" step="0.01"></div><div><label style="font-size:12px;color:var(--muted)">Risk %</label><input id="riskPct" value="1" type="number"></div></div><div class="order-row"><input id="sl" placeholder="Stop Loss"><input id="tp" placeholder="Take Profit"></div><div class="order-row" style="margin-top:10px"><button class="buy" onclick="placeOrder('BUY')">BUY ↑</button><button class="sell" onclick="placeOrder('SELL')">SELL ↓</button></div><p id="orderMsg" style="font-size:12px;color:var(--gold2);margin-top:10px"></p><div style="background:#05070A;border:1px solid var(--line);border-radius:10px;padding:10px;margin-top:10px;font-size:12px">Balance (Demo): <b>$10,000.00</b><br>Equity: <b id="equity">$10,000.00</b> • Open P&L: <b id="pnl" style="color:#2DD4BF">+$0.00</b></div></div></div>
</div>
<div class="section-title"><div><h2>THE TIMO PLATFORM • FIVE PILLARS</h2><p>One platform, five professional systems</p></div></div>
<div class="pillars">
<div class="pillar"><i>⌨️</i><h3>TIMO TERMINAL</h3><p>Institutional-grade trading terminal with advanced charting, order execution, and risk controls.</p><button onclick="document.getElementById('terminal').scrollIntoView({behavior:'smooth'})">Open Terminal →</button></div>
<div class="pillar"><i>🧠</i><h3>TIMO INTELLIGENCE</h3><p>AI-powered market research, sentiment analysis, and predictive insights.</p><button onclick="document.getElementById('intelligence').scrollIntoView({behavior:'smooth'})">View AI →</button></div>
<div class="pillar"><i>◎</i><h3>TIMO SCANNER</h3><p>Real-time market scanner for opportunities across equities, crypto, FX & commodities.</p><button onclick="document.getElementById('scanner').scrollIntoView({behavior:'smooth'})">Open Scanner →</button></div>
<div class="pillar"><i>🛡️</i><h3>TIMO RISK</h3><p>Advanced portfolio risk management and scenario modelling for institutions.</p><button onclick="document.getElementById('risk').scrollIntoView({behavior:'smooth'})">Manage Risk →</button></div>
<div class="pillar"><i>📰</i><h3>TIMO RESEARCH</h3><p>In-depth macro research, earnings analysis, and strategy reports from experts.</p><button onclick="document.getElementById('research').scrollIntoView({behavior:'smooth'})">Read Research →</button></div>
</div>
<div class="grid2" style="margin-top:18px">
<div class="card" id="intelligence"><div class="card-h">TIMO INTELLIGENCE — AI ANALYSIS <span>LIVE</span></div><div class="ai-box"><div style="display:flex;gap:10px;flex-wrap:wrap"><span class="badge2 b-bull">XAUUSD • BULLISH 72%</span><span class="badge2 b-bear">EURUSD • BEARISH 58%</span><span class="badge2 b-neutral">BTCUSD • NEUTRAL 51%</span></div><h3 style="margin:14px 0 6px">XAUUSD — Gold Outlook</h3><p>Gold is holding above 2,642 support. Structure is HH/HL on H4. If price sweeps 2,638 liquidity and reclaims, AI favours long to 2,685. Invalidation below 2,630. RSI 58 — room to run. News risk: US CPI this week.</p><div style="margin-top:12px;background:#05070A;border:1px solid var(--line);border-radius:10px;padding:10px;font-size:13px">Key Levels: Support <b>2,642 / 2,630</b> • Resistance <b>2,685 / 2,710</b> • AI Confidence: <b style="color:#2DD4BF">High</b></div><button class="btn btn-blue" style="width:100%;margin-top:12px" onclick="generateAI()">Generate Fresh AI Report</button><p id="aiReport" style="font-size:12px;color:var(--muted);margin-top:8px"></p></div></div>
<div class="card" id="scanner"><div class="card-h">TIMO SCANNER — SMC DETECTION <span id="scanTime">Scanning...</span></div><div style="overflow:auto"><table><thead><tr><th>PAIR</th><th>SIGNAL</th><th>STRUCTURE</th><th>CONF.</th></tr></thead><tbody id="scannerBody"></tbody></table></div><div style="padding:12px"><small style="color:var(--muted)">Scanner updates every 30s. SMC: BOS / CHoCH / FVG / Order Block. This is analysis, not financial advice.</small></div></div>
</div>
<div class="section-title" id="risk"><div><h2>🛡️ TIMO RISK — Portfolio & Risk Management</h2><p>Risk first. Profit second.</p></div></div>
<div class="kpi"><div><small>Total Equity</small><b id="kpiEquity">$10,000.00</b><small style="color:#2DD4BF">▲ +2.4% today</small></div><div><small>Max Drawdown</small><b>-3.1%</b><small>Healthy • Limit -10%</small></div><div><small>Exposure</small><b id="kpiExposure">18%</b><small>Low risk</small></div><div><small>Your 10% Fee Due</small><b id="kpiFee" style="color:var(--gold)">$0.00</b><small>Auto-calc on profit</small></div></div>
<div class="grid2" style="margin-top:12px">
<div class="card"><div class="card-h">RISK CALCULATOR — LOT SIZE</div><div style="padding:14px"><div class="field"><label>Account Balance ($)</label><input id="bal" value="1000" type="number" oninput="calcRisk()"></div><div class="field"><label>Risk Per Trade (%)</label><input id="risk" value="1" type="number" oninput="calcRisk()"></div><div class="field"><label>Stop Loss (pips)</label><input id="slPips" value="30" type="number" oninput="calcRisk()"></div><div style="background:#05070A;border:1px solid var(--line);border-radius:10px;padding:12px;margin-top:10px">Risk Amount: <b id="riskAmt">$10.00</b><br>Recommended Lot: <b id="lotCalc" style="color:var(--gold)">0.03</b><br>Profit if TP hits (1:2): <b style="color:#2DD4BF" id="profitCalc">$20.00</b><br>Your 10% Fee on Profit: <b id="feeCalc" style="color:var(--gold)">$2.00</b></div></div></div>
<div class="card"><div class="card-h">MANAGED CLIENTS — 10% AUTO TRACKER</div><div style="overflow:auto"><table><thead><tr><th>CLIENT</th><th>START</th><th>NOW</th><th>PROFIT</th><th>10%</th><th>STATUS</th></tr></thead><tbody><tr><td>Sarah M.</td><td>$1,000</td><td>$1,150</td><td style="color:#2DD4BF">+$150</td><td>$15.00</td><td><span class="badge2 b-neutral">UNPAID</span></td></tr><tr><td>David K.</td><td>$500</td><td>$585</td><td style="color:#2DD4BF">+$85</td><td>$8.50</td><td><span class="badge2 b-bull">PAID ✓</span></td></tr><tr><td>Amina A.</td><td>$2,000</td><td>$2,180</td><td style="color:#2DD4BF">+$180</td><td>$18.00</td><td><span class="badge2 b-neutral">UNPAID</span></td></tr></tbody></table></div><div style="padding:12px"><button class="btn btn-gold" style="width:100%" onclick="alert('M-Pesa Till payment link will be generated here. Add your real Till number in Settings.')">Collect 10% via M-Pesa Till</button></div></div>
</div>
<div class="section-title" id="research"><div><h2>📰 TIMO RESEARCH — Financial News & Economic Intelligence</h2><p>Daily brief, calendar, research</p></div></div>
<div class="grid3">
<div class="card"><div class="card-h">DAILY BRIEF — TODAY</div><div class="news"><small>NOV 9 • MARKETS</small><b>Gold holds above $2,640 as traders await US CPI</b><p style="color:var(--muted);font-size:13px">Risk-on tone in Asia, USD slightly weaker. Watch 2,685 resistance.</p></div><div class="news"><small>FOREX</small><b>EURUSD tests 1.1650 — Bullish structure intact</b><p style="color:var(--muted);font-size:13px">HH/HL on H4, liquidity above 1.1680.</p></div></div>
<div class="card"><div class="card-h">ECONOMIC CALENDAR</div><table><thead><tr><th>TIME (EAT)</th><th>EVENT</th><th>IMPACT</th></tr></thead><tbody><tr><td>15:30</td><td>US CPI MoM</td><td><span class="badge2 b-bear">HIGH</span></td></tr><tr><td>17:00</td><td>ECB Speech</td><td><span class="badge2 b-neutral">MEDIUM</span></td></tr><tr><td>21:00</td><td>FOMC Minutes</td><td><span class="badge2 b-bear">HIGH</span></td></tr><tr><td>Thu 15:30</td><td>US NFP</td><td><span class="badge2 b-bear">HIGH</span></td></tr></tbody></table></div>
<div class="card"><div class="card-h">ACCOUNT / ADMIN</div><div style="padding:14px"><div class="field"><label>Full Name</label><input id="uName" placeholder="Your name"></div><div class="field"><label>Email</label><input placeholder="you@email.com"></div><div class="field"><label>Deriv API Token (for real data)</label><input id="derivToken" placeholder="Paste Deriv API token — keep private"></div><div class="field"><label>M-Pesa Till for 10% Fee</label><input id="till" placeholder="e.g. Till 5878421"></div><button class="btn btn-blue" style="width:100%" onclick="saveSettings()">Save Settings • Create Account</button><p id="saveMsg" style="font-size:12px;color:#2DD4BF;margin-top:8px"></p><small style="color:var(--muted)">Demo accounts are stored in this browser only. For real accounts, connect backend + database in Drop 3.</small></div></div>
</div>
<footer><b style="color:#fff">TIMO TRADING</b> • Ultimate Professional Edition • Intelligence. Precision. Execution.<br><div class="disclaimer">Risk Warning: Trading forex, gold, indices and crypto carries substantial risk of loss. Past performance is not a guarantee of future results. TIMO TRADING provides market analysis and technology, not guaranteed profits. Never trade with money you cannot afford to lose. Demo data shown — connect Deriv API for live execution.</div>© 2026 TIMO TRADING • Privacy • Terms • Contact</footer>
</div>
<div class="mobile-nav"><a href="#terminal" class="active">◈<br>Terminal</a><a href="#scanner">◎<br>Scanner</a><a href="#intelligence">🧠<br>AI</a><a href="#risk">🛡️<br>Risk</a><a href="#research">📰<br>Research</a></div>
<script>
let prices={ 'EUR/USD':1.16482,'XAUUSD':2642.10,'GBP/USD':1.3120,'BTCUSD':97842,'USD/JPY':154.20,'NASDAQ':19784,'Crude Oil':76.22,'US30':44210 };
let changes={ 'EUR/USD':0.24,'XAUUSD':0.42,'GBP/USD':-0.12,'BTCUSD':2.18,'USD/JPY':-0.08,'NASDAQ':1.12,'Crude Oil':-0.81,'US30':0.34 };
function renderTicker(){
  document.getElementById('ticker').innerHTML=Object.keys(prices).map(k=>`<div class="tick"><small>${k}</small><br><b class="mono">${prices[k].toLocaleString()}</b> <span class="${changes[k]>=0?'up':'down'}">${changes[k]>=0?'+':''}${changes[k].toFixed(2)}%</span></div>`).join('');
  document.getElementById('watchlist').innerHTML=Object.keys(prices).map((k,i)=>`<div class="watch-row ${i===0?'active':''}" onclick="selectSymbol('${k}',this)"><div><b>${k}</b><small>${k.includes('BTC')?'Crypto':k.includes('XAU')?'Gold':k.includes('NASDAQ')||k.includes('US30')?'Indices':k.includes('Oil')?'Energy':'Forex'}</small></div><div style="text-align:right"><b class="mono">${prices[k].toLocaleString()}</b><br><small class="${changes[k]>=0?'up':'down'}">${changes[k]>=0?'+':''}${changes[k].toFixed(2)}%</small></div></div>`).join('');
}
function selectSymbol(sym,el){document.querySelectorAll('.watch-row').forEach(r=>r.classList.remove('active'));el.classList.add('active');document.getElementById('chartSymbol').textContent=sym+' • 1H';document.getElementById('chartPrice').textContent=prices[sym].toLocaleString()+' • '+(changes[sym]>=0?'+':'')+changes[sym].toFixed(2)+'%';document.getElementById('ordSymbol').value=sym;}
renderTicker();
setInterval(()=>{Object.keys(prices).forEach(k=>{let v=(Math.random()-0.48)*0.002;prices[k]=prices[k]*(1+v);changes[k]=Math.max(-3,Math.min(3,changes[k]+v*10));});renderTicker();document.getElementById('topGold').textContent=prices['XAUUSD'].toLocaleString();document.getElementById('topEur').textContent=prices['EUR/USD'].toFixed(4);document.getElementById('topBtc').textContent=Math.round(prices['BTCUSD']).toLocaleString();},4000);
let chart=LightweightCharts.createChart(document.getElementById('chart'),{layout:{background:{color:'#0A1628'},textColor:'#8AA0B8'},grid:{vertLines:{color:'#12233A'},horzLines:{color:'#12233A'}},width:document.getElementById('chart').clientWidth,height:340});
let candleSeries=chart.addCandlestickSeries({upColor:'#26A69A',downColor:'#EF5350',wickUpColor:'#26A69A',wickDownColor:'#EF5350'});
let data=[];let base=1.1648;let t=Date.now()/1000-100*3600;
for(let i=0;i<100;i++){let open=base;let close=base+(Math.random()-0.46)*0.0018;base=close;let high=Math.max(open,close)+Math.random()*0.0006;let low=Math.min(open,close)-Math.random()*0.0006;data.push({time:Math.floor(t+i*3600),open,high,low,close});}
candleSeries.setData(data);
let lineSeries=chart.addLineSeries({color:'#0EA5E9',lineWidth:1});
lineSeries.setData(data.map(d=>({time:d.time,value:d.close})));
function setTF(tf,btn){document.querySelectorAll('.chip').forEach(c=>c.classList.remove('active'));btn.classList.add('active');document.getElementById('chartSymbol').textContent='EUR/USD • '+tf;}
let scannerData=[['EUR/USD','BULLISH','BOS ↑','78%','b-bull'],['XAUUSD','BULLISH','FVG + OB','72%','b-bull'],['GBP/USD','BEARISH','CHoCH ↓','64%','b-bear'],['BTCUSD','NEUTRAL','Range','51%','b-neutral'],['USD/JPY','BULLISH','BOS ↑','69%','b-bull'],['NASDAQ','BULLISH','HH/HL','74%','b-bull']];
function renderScanner(){document.getElementById('scannerBody').innerHTML=scannerData.map(r=>`<tr><td><b>${r[0]}</b></td><td><span class="badge2 ${r[4]}">${r[1]}</span></td><td>${r[2]}</td><td><b>${r[3]}</b></td></tr>`).join('');document.getElementById('scanTime').textContent='Updated '+new Date().toLocaleTimeString();}
renderScanner(); setInterval(renderScanner,30000);
let equity=10000;
function placeOrder(side){let lot=parseFloat(document.getElementById('lot').value)||0.1;let sym=document.getElementById('ordSymbol').value;document.getElementById('orderMsg').textContent='✓ '+side+' '+lot+' '+sym+' placed (DEMO). Connect Deriv API for real execution.';let pnl=(Math.random()*40-10);equity+=pnl;document.getElementById('equity').textContent='$'+equity.toFixed(2);document.getElementById('kpiEquity').textContent='$'+equity.toFixed(2);document.getElementById('pnl').textContent=(pnl>=0?'+$':'-$')+Math.abs(pnl).toFixed(2);}
function calcRisk(){let bal=parseFloat(document.getElementById('bal').value)||1000;let r=parseFloat(document.getElementById('risk').value)||1;let sl=parseFloat(document.getElementById('slPips').value)||30;let amt=bal*r/100;let lot=(amt/(sl*10)).toFixed(2);document.getElementById('riskAmt').textContent='$'+amt.toFixed(2);document.getElementById('lotCalc').textContent=lot;document.getElementById('profitCalc').textContent='$'+(amt*2).toFixed(2);document.getElementById('feeCalc').textContent='$'+(amt*2*0.10).toFixed(2);document.getElementById('kpiFee').textContent='$'+(amt*2*0.10).toFixed(2);}
calcRisk();
function generateAI(){document.getElementById('aiReport').textContent='AI Report generated: '+new Date().toLocaleString()+' — XAUUSD bias Bullish, EURUSD pullback expected, BTCUSD consolidation. Full PDF export in Drop 2.';document.getElementById('aiText').textContent='Fresh AI scan: Gold holding support, EURUSD showing HH/HL, BTC consolidating near resistance. Wait for BOS confirmation on 15m before entry. Risk 1% max.';}
function showAuth(){document.getElementById('research').scrollIntoView({behavior:'smooth'});alert('Create account below in Account / Admin — enter name, email, Deriv token and Till.');}
function saveSettings(){let n=document.getElementById('uName').value||'Trader';let till=document.getElementById('till').value||'Not set';localStorage.setItem('timo_user',n);localStorage.setItem('timo_till',till);localStorage.setItem('timo_deriv',document.getElementById('derivToken').value);document.getElementById('saveMsg').textContent='✓ Saved for '+n+' • Till: '+till+' • Settings stored in this browser.';}
setInterval(()=>{document.getElementById('clock').textContent=new Date().toLocaleTimeString('en-GB',{timeZone:'Africa/Nairobi'})+' EAT';document.getElementById('rsiVal').textContent=(50+Math.random()*10).toFixed(1);},1000);
window.addEventListener('resize',()=>{chart.applyOptions({width:document.getElementById('chart').clientWidth})});
</script>
</body>
</html>
"""

components.html(HTML_CODE, height=3200, scrolling=True)
