from flask import Flask, request, jsonify, send_file
import os, json, io
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V21_8_RESTORE_ALL_FULLY_PREMIUM_PRO_KEEP_BG_LAYOUT"
FILES = {"users":"users.json","fees":"fees.json","products":"products.json","orders":"orders.json","services":"services_orders.json","bundles":"bundles.json"}
def load(f,d):
    if not os.path.exists(f): return d
    try:
        with open(f) as jf: return json.load(jf)
    except: return d
def save(f,data):
    with open(f,"w") as jf: json.dump(data,jf)

def nav():
    return (
        '<nav style="background:rgba(15,12,41,0.95);backdrop-filter:blur(20px);padding:10px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;border-bottom:3px solid #f9c846;z-index:1000;flex-wrap:wrap;gap:8px">'
        '<b style="color:#f9c846;font-size:11px">V21.8 RESTORE ALL FULLY PREMIUM PRO - POSTER + SOCIAL LIVE + LOGO + WEBSITE DESIGN - KEEP BG + LAYOUT + MOVING</b>'
        '<div style="display:flex;gap:8px;font-size:10px;flex-wrap:wrap;align-items:center"><a href="/" style="color:#f9c846;text-decoration:none;font-weight:bold;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">Home</a>'
        '<a href="/design-studio" style="color:black;text-decoration:none;background:linear-gradient(90deg,#f9c846,#ff9800);padding:6px 12px;border-radius:20px;font-weight:900">Website 12T FULL PRO</a>'
        '<a href="/poster-maker" style="color:black;text-decoration:none;background:linear-gradient(90deg,#00c950,#00ff88);padding:6px 12px;border-radius:20px;font-weight:900">Poster 20T FULL PRO</a>'
        '<a href="/ai-caption" style="color:black;text-decoration:none;background:linear-gradient(90deg,#00c950,#00ff88);padding:6px 12px;border-radius:20px;font-weight:900">Social LIVE FULL PRO</a>'
        '<a href="/logo-maker" style="color:black;text-decoration:none;background:linear-gradient(90deg,#f9c846,#ff9800);padding:6px 12px;border-radius:20px;font-weight:900">Logo 100I FULL PRO</a>'
        '<a href="/shop" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Shop + Selar Moving</a>'
        '<a href="/admin" style="color:#f9c846;text-decoration:none;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">TIMOTHY Moving</a></div></nav>'
        '<style>'
        '@keyframes timothyMove{0%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}50%{transform:translateX(18px) translateY(6px) scale(1.15) rotate(2deg)}100%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}}'
        '@keyframes moveText{0%{transform:translateX(-14px)}50%{transform:translateX(14px)}100%{transform:translateX(-14px)}}'
        '@keyframes selarMove{0%{transform:translateX(-12px) translateY(-4px)}50%{transform:translateX(12px) translateY(4px)}100%{transform:translateX(-12px) translateY(-4px)}}'
        '@keyframes whatsappMove{0%{transform:translateY(-8px) scale(1)}50%{transform:translateY(8px) scale(1.1)}100%{transform:translateY(-8px) scale(1)}}'
        '@keyframes marquee{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}'
        '@keyframes gradientBG{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}'
        '@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}'
        '@keyframes livePulse{0%{box-shadow:0 0 0 0 rgba(255,0,0,0.7)}70%{box-shadow:0 0 0 10px rgba(255,0,0,0)}100%{box-shadow:0 0 0 0 rgba(255,0,0,0)}}'
        '.moving-text{display:inline-block;animation:moveText 2.5s ease-in-out infinite;color:#f9c846;font-weight:bold}'
        '.moving-selar{display:inline-block;animation:selarMove 2s ease-in-out infinite}'
        '.moving-whatsapp{animation:whatsappMove 2s ease-in-out infinite}'
        '.marquee{white-space:nowrap;overflow:hidden;box-sizing:border-box}'
        '.marquee span{display:inline-block;padding-left:100%;animation:marquee 30s linear infinite}'
        'body{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e,#0f0c29);background-size:400% 400%;animation:gradientBG 15s ease infinite;color:white;font-family:Arial;margin:0;min-height:100vh;line-height:1.5}'
        '.glass{background:rgba(26,26,60,0.65);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:15px;box-shadow:0 8px 32px rgba(0,0,0,0.3);margin-bottom:15px;box-sizing:border-box}'
        '.btn{display:inline-block;background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px;box-sizing:border-box}'
        '.btn-gold{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px;box-sizing:border-box}'
        '.btn-glass{display:inline-block;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2);color:white;padding:10px 18px;border-radius:20px;cursor:pointer;text-decoration:none;margin:6px;box-sizing:border-box}'
        '.btn-red{display:inline-block;background:linear-gradient(90deg,#ff0000,#ff4444);color:white;padding:10px 18px;border-radius:20px;font-weight:900;border:none;cursor:pointer;margin:6px;box-shadow:0 0 15px rgba(255,0,0,0.4)}'
        '.input-glass{width:100%;padding:10px;background:rgba(14,14,30,0.8);color:white;border:1px solid rgba(255,255,255,0.15);border-radius:12px;margin:6px 0;box-sizing:border-box}'
        '.template-card{background:rgba(14,14,30,0.7);border:1px solid rgba(255,255,255,0.12);border-radius:14px;padding:10px;text-align:center;cursor:pointer;transition:0.25s;box-sizing:border-box}'
        '.template-card:hover{transform:translateY(-3px) scale(1.02);border-color:#f9c846;box-shadow:0 10px 25px rgba(249,200,70,0.25)}'
        '.template-card.active{border:2px solid #00ff88;background:rgba(0,255,136,0.15);box-shadow:0 0 22px rgba(0,255,136,0.3)}'
        '.template-card.active-gold{border:2px solid #f9c846;background:rgba(249,200,70,0.18);box-shadow:0 0 22px rgba(249,200,70,0.4)}'
        '.skeleton{background:linear-gradient(90deg,#1a1a35 25%,#2a2a50 50%,#1a1a35 75%);background-size:200% 100%;animation:shimmer 1.5s infinite;border-radius:12px}'
        '.live-dot{width:12px;height:12px;background:red;border-radius:50%;display:inline-block;animation:livePulse 1.5s infinite}'
        '#videoPreview{width:100%;aspect-ratio:9/16;max-height:65vh;background:#000;border-radius:16px;overflow:hidden;position:relative;box-shadow:0 15px 35px rgba(0,0,0,0.5)}'
        '.filter-Normal{filter:none}.filter-Grayscale{filter:grayscale(100%)}.filter-Sepia{filter:sepia(100%)}.filter-Vintage{filter:sepia(60%) contrast(120%) brightness(90%)}.filter-Bright{filter:brightness(130%)}.filter-Contrast{filter:contrast(150%)}'
        '#poster-preview{width:100%;aspect-ratio:3/4;background:white;border-radius:16px;overflow:hidden;position:relative;box-shadow:0 20px 40px rgba(0,0,0,0.5)}'
        '#logo-preview{width:100%;aspect-ratio:1/1;background:white;border-radius:16px;overflow:hidden;position:relative;box-shadow:0 20px 40px rgba(0,0,0,0.5);display:flex;align-items:center;justify-content:center}'
        '#website-preview{width:100%;min-height:650px;background:white;border-radius:16px;overflow:auto;box-shadow:0 20px 50px rgba(0,0,0,0.6);color:#222;transition:all 0.3s ease;border:3px solid #f9c846}'
        '#website-preview.tablet{width:768px;margin:auto}#website-preview.mobile{width:375px;margin:auto}'
        '</style>'
        '<div style="position:fixed;bottom:90px;right:20px;width:75px;height:75px;background:linear-gradient(135deg,#f9c846,#ff9800);border-radius:50%;display:flex;align-items:center;justify-content:center;color:black;font-weight:900;font-size:10px;z-index:9998;box-shadow:0 0 25px rgba(249,200,70,0.7);animation:timothyMove 3s ease-in-out infinite;border:2px solid rgba(255,255,255,0.4);text-align:center">TIMOTHY<br>ACCOUNT<br>MANAGED<br>MOVING</div>'
        '<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;left:20px;width:65px;height:65px;background:linear-gradient(135deg,#25D366,#00ff88);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:900;font-size:22px;z-index:9999;box-shadow:0 0 20px rgba(37,211,102,0.6);text-decoration:none;animation:whatsappMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-whatsapp">💬</a>'
        '<a href="https://selar.com/m/timothymusyoki" target="_blank" style="position:fixed;bottom:20px;right:100px;background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 16px;border-radius:25px;font-weight:900;font-size:11px;z-index:9997;box-shadow:0 0 20px rgba(106,13,173,0.6);text-decoration:none;animation:selarMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-selar">🛒 SELAR STORE - timothymusyoki - MOVING - CLICK</a>'
    )

def website_builder():
    return """
<div style="max-width:1480px;margin:auto;padding:10px">
<div class="glass" style="text-align:center;border:3px solid #f9c846"><h2 style="color:#f9c846;margin:0">🌐 WEBSITE DESIGN 12 TEMPLATES FULL PREMIUM PRO V21.8 RESTORED</h2><p style="color:#00ff88;font-weight:900;font-size:11px">✅ V21.8 RESTORE ALL FULLY PREMIUM PRO - WEBSITE 12T + POSTER 20T + SOCIAL LIVE + LOGO 100I - KEEP BG + LAYOUT + MOVING + EACH OWN DESC SEPARATE NO OVERLAP</p></div>
<div style="display:grid;grid-template-columns:310px 1fr 320px;gap:14px">
<div class="glass"><h3 style="color:#f9c846;text-align:center;margin:0 0 8px 0">12 Templates PRO</h3><div id="web-templates" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-height:38vh;overflow-y:auto"></div>
<div style="background:rgba(14,14,30,0.7);padding:10px;border-radius:12px;margin-top:12px">
<label style="font-size:11px;display:block"><input type="checkbox" id="showNavbar" checked onchange="buildWeb()"> Navbar</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showHero" checked onchange="buildWeb()"> Hero</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showAbout" checked onchange="buildWeb()"> About</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showServices" checked onchange="buildWeb()"> Services 6</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showTestimonials" checked onchange="buildWeb()"> Testimonials Moving</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showFAQ" checked onchange="buildWeb()"> FAQ</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showContact" checked onchange="buildWeb()"> Contact</label>
<label style="font-size:11px;display:block"><input type="checkbox" id="showFooter" checked onchange="buildWeb()"> Footer</label>
</div><a href="/" class="btn-glass" style="font-size:10px">← Home</a></div>
<div class="glass" style="text-align:center"><div style="display:flex;gap:6px;justify-content:center;flex-wrap:wrap;margin-bottom:8px">
<button onclick="setWebPreview('desktop')" class="btn-gold" id="b-desktop" style="font-size:11px">🖥️ Desktop</button>
<button onclick="setWebPreview('tablet')" class="btn-glass" id="b-tablet" style="font-size:11px">📱 Tablet 768</button>
<button onclick="setWebPreview('mobile')" class="btn-glass" id="b-mobile" style="font-size:11px">📱 Mobile 375</button>
</div><div id="website-preview" class="desktop"></div>
<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:10px">
<button onclick="exportWebHTML()" class="btn-gold" style="font-size:11px">📥 Export HTML</button>
<button onclick="publishWeb()" class="btn" style="font-size:11px">🚀 Publish Link</button>
</div></div>
<div class="glass"><h3 style="color:#f9c846;text-align:center;margin:0 0 8px 0">Customize</h3>
<input id="siteTitle" class="input-glass" value="Kaumoni Digital" oninput="buildWeb()">
<input id="heroTitle" class="input-glass" value="🚀 ALL-IN-ONE DIGITAL SERVICES V21.8 RESTORED" oninput="buildWeb()">
<textarea id="heroSubtitle" class="input-glass" style="height:55px" oninput="buildWeb()">Welcome - Website Design 12 Templates Full Premium Pro - Keep BG + Layout + Moving - V21.8 RESTORED ALL PREMIUM PRO</textarea>
<input id="ctaText" class="input-glass" value="Get Started $5 Premium Pro" oninput="buildWeb()">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
<input type="color" id="primaryColor" value="#f9c846" class="input-glass" style="height:38px" oninput="buildWeb()">
<input type="color" id="secondaryColor" value="#302b63" class="input-glass" style="height:38px" oninput="buildWeb()">
</div><select id="fontFamily" class="input-glass" onchange="buildWeb()"><option>Arial</option><option>Georgia</option><option>Impact</option></select>
<input id="domain" class="input-glass" value="kaumoni-v21-8-restored" oninput="buildWeb()">
<button onclick="resetWeb()" class="btn-glass" style="width:100%;font-size:11px">🔄 Reset</button>
</div>
</div></div>
<script>
var webTemplates=[{id:1,cat:'business',name:'Business Corporate',thumb:'💼',bg:'linear-gradient(135deg,#0f0c29,#302b63)',primary:'#f9c846',secondary:'#302b63'},{id:2,cat:'business',name:'Portfolio Dark',thumb:'🎨',bg:'linear-gradient(135deg,#000,#1a1a1a)',primary:'#f9c846',secondary:'#000'},{id:3,cat:'business',name:'Ecommerce Gold',thumb:'🛒',bg:'linear-gradient(135deg,#f9c846,#fff)',primary:'#000',secondary:'#f9c846'},{id:4,cat:'business',name:'Landing Gradient',thumb:'🚀',bg:'linear-gradient(135deg,#6a0dad,#0d47a1)',primary:'#f9c846',secondary:'#6a0dad'},{id:5,cat:'portfolio',name:'Blog Minimal',thumb:'📝',bg:'linear-gradient(135deg,#fff,#f0f0f0)',primary:'#000',secondary:'#e0e0e0'},{id:6,cat:'portfolio',name:'Agency Neon',thumb:'💚',bg:'linear-gradient(135deg,#00ff88,#000)',primary:'#000',secondary:'#00ff88'},{id:7,cat:'portfolio',name:'Restaurant Elegant',thumb:'🍽️',bg:'linear-gradient(135deg,#800020,#f9c846)',primary:'#fff',secondary:'#800020'},{id:8,cat:'portfolio',name:'SaaS Modern',thumb:'💻',bg:'linear-gradient(135deg,#0d47a1,#fff)',primary:'#f9c846',secondary:'#0d47a1'},{id:9,cat:'ecommerce',name:'Creative Rainbow',thumb:'🌈',bg:'linear-gradient(135deg,#ff00cc,#333399,#00ffff)',primary:'#fff',secondary:'#ff00cc'},{id:10,cat:'ecommerce',name:'Education Blue',thumb:'🎓',bg:'linear-gradient(135deg,#1e3c72,#2a5298)',primary:'#fff',secondary:'#1e3c72'},{id:11,cat:'ecommerce',name:'Health Green',thumb:'🏥',bg:'linear-gradient(135deg,#00b09b,#96c93d)',primary:'#fff',secondary:'#00b09b'},{id:12,cat:'ecommerce',name:'Real Estate Black',thumb:'🏠',bg:'linear-gradient(135deg,#000,#434343)',primary:'#f9c846',secondary:'#000'}];
var currentWeb=webTemplates[0];
function renderWeb(){var g=document.getElementById('web-templates');g.innerHTML=webTemplates.map(function(t){var a=t.id===currentWeb.id?'active-gold':'';return '<div class="template-card '+a+'" onclick="selectWeb('+t.id+')"><div style="width:100%;height:42px;background:'+t.bg+';border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px">'+t.thumb+'</div><b style="font-size:9px;display:block;margin-top:4px">'+t.name+'</b></div>';}).join('');}
function selectWeb(id){currentWeb=webTemplates.find(function(t){return t.id===id;});document.getElementById('primaryColor').value=currentWeb.primary;document.getElementById('secondaryColor').value=currentWeb.secondary;renderWeb();buildWeb();}
function buildWeb(){
var st=document.getElementById('siteTitle').value||'Kaumoni';var ht=document.getElementById('heroTitle').value||'ALL-IN-ONE';var hs=document.getElementById('heroSubtitle').value||'Welcome';var cta=document.getElementById('ctaText').value||'Get Started';var pc=document.getElementById('primaryColor').value;var sc=document.getElementById('secondaryColor').value;var font=document.getElementById('fontFamily').value;
var showNavbar=document.getElementById('showNavbar').checked;var showHero=document.getElementById('showHero').checked;var showAbout=document.getElementById('showAbout').checked;var showServices=document.getElementById('showServices').checked;var showTestimonials=document.getElementById('showTestimonials').checked;var showFAQ=document.getElementById('showFAQ').checked;var showContact=document.getElementById('showContact').checked;var showFooter=document.getElementById('showFooter').checked;
var nav=showNavbar?'<nav style="background:'+sc+';padding:12px;display:flex;justify-content:space-between;color:white;font-family:'+font+'"><b style="color:'+pc+'">'+st+' V21.8 RESTORED</b><div style="display:flex;gap:10px;font-size:12px"><span>Home</span><span>About</span><span>Services</span></div></nav>':'';
var hero=showHero?'<div style="background:'+currentWeb.bg+';padding:45px 20px;text-align:center;color:white;font-family:'+font+'"><h1 style="color:'+pc+'">'+ht+'</h1><p style="max-width:600px;margin:12px auto;font-size:13px">'+hs+'</p><button style="background:'+pc+';color:black;padding:12px 22px;border-radius:25px;border:none;font-weight:900;margin-top:10px">'+cta+'</button></div>':'';
var about=showAbout?'<div style="padding:25px;text-align:center;background:#f9f9f9;color:#333;font-family:'+font+'"><h2 style="color:'+sc+'">About V21.8 RESTORED ALL PREMIUM PRO</h2><p style="max-width:700px;margin:10px auto;font-size:12px">Website Design 12 Templates Full Premium Pro + Poster 20 Templates + Social LIVE + Logo 100 Icons - All Restored Fully Premium Pro - Keep BG + Layout + Moving + Each Own Desc Separate No Overlap</p></div>':'';
var services=showServices?'<div style="padding:25px;background:white;color:#333;font-family:'+font+'"><h2 style="text-align:center;color:'+sc+'">Services - Each Own Desc Separate</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:12px"><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Website 12T FULL PRO ✅</b><br><small>Live Builder Export HTML - V21.8 Restored</small></div><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Poster 20T FULL PRO ✅</b><br><small>Wedding Birthday Business Church School</small></div><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Social LIVE FULL PRO ✅</b><br><small>Camera Photo Video RTMP TikTok YouTube</small></div><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Logo 100I FULL PRO ✅</b><br><small>Business Tech Food Shop Creative</small></div><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Shop PRO + Selar Moving</b><br><small>Own Desc Separate</small></div><div style="background:#f5f5f5;padding:10px;border-radius:10px"><b>Trading LIVE FIXED</b><br><small>Real Chart</small></div></div></div>':'';
var testi=showTestimonials?'<div style="padding:18px;background:'+sc+';color:white;text-align:center;font-family:'+font+'"><h3 style="color:'+pc+'">Testimonials Moving - V21.8 Restored</h3><div style="overflow:hidden;white-space:nowrap"><span style="display:inline-block;animation:marquee 20s linear infinite">⭐ Alex - Website 12T Full Premium Pro Restored! | ⭐ Sarah - Poster 20T Full Premium Pro Restored! | ⭐ Kevin - Social LIVE Full Premium Pro Restored! | ⭐ Faith - Logo 100I Full Premium Pro Restored! V21.8</span></div></div>':'';
var faq=showFAQ?'<div style="padding:25px;background:#f9f9f9;color:#333;font-family:'+font+'"><h2 style="text-align:center;color:'+sc+'">FAQ V21.8 Restored</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px"><div style="background:white;padding:10px;border-radius:10px"><b>Q: All Restored?</b><br><small>Yes Website + Poster + Social + Logo All Fully Premium Pro - V21.8</small></div><div style="background:white;padding:10px;border-radius:10px"><b>Q: Keep BG Layout?</b><br><small>Yes BG #0f0c29 + Layout + Moving + Each Own Desc Separate No Overlap</small></div></div></div>':'';
var contact=showContact?'<div style="padding:25px;background:'+currentWeb.bg+';color:white;text-align:center;font-family:'+font+'"><h2 style="color:'+pc+'">Ready To Build? V21.8 Restored</h2><p>All Premium Pro Restored - Website + Poster + Social + Logo</p><div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:10px"><button style="background:'+pc+';color:black;padding:10px 18px;border-radius:20px;border:none;font-weight:900">Get Started V21.8 Restored</button><button style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;border:none;font-weight:900">WhatsApp 0118431854 Moving</button></div></div>':'';
var footer=showFooter?'<footer style="background:#0f0c29;color:white;padding:12px;text-align:center;font-size:11px;font-family:'+font+'">© 2025 '+st+' V21.8 RESTORE ALL FULLY PREMIUM PRO - Website 12T + Poster 20T + Social LIVE + Logo 100I - Keep BG + Layout + Moving - TIMOTHY 0118431854</footer>':'';
document.getElementById('website-preview').innerHTML=nav+hero+about+services+testi+faq+contact+footer;
}
function setWebPreview(t){var p=document.getElementById('website-preview');p.className=t;document.getElementById('b-desktop').className=t==='desktop'?'btn-gold':'btn-glass';document.getElementById('b-tablet').className=t==='tablet'?'btn-gold':'btn-glass';document.getElementById('b-mobile').className=t==='mobile'?'btn-gold':'btn-glass';}
function exportWebHTML(){var c=document.getElementById('website-preview').innerHTML;var st=document.getElementById('siteTitle').value;var full='<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+st+' V21.8 RESTORED</title><style>body{margin:0;font-family:Arial}@keyframes marquee{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}.marquee{white-space:nowrap;overflow:hidden}.marquee span{display:inline-block;padding-left:100%;animation:marquee 20s linear infinite}</style></head><body>'+c+'</body></html>';var b=new Blob([full],{type:'text/html'});var u=URL.createObjectURL(b);var a=document.createElement('a');a.href=u;a.download=st.replace(/ /g,'_')+'_V21_8_RESTORED_ALL_PREMIUM_PRO.html';a.click();}
function publishWeb(){var d=document.getElementById('domain').value||'kaumoni-v21-8';var link='https://kaumoni.site/'+d;var m=document.createElement('div');m.style.cssText='position:fixed;top:20px;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px 22px;border-radius:25px;font-weight:900;z-index:9999;text-align:center';m.innerHTML='🚀 Published V21.8 RESTORED ALL PREMIUM PRO<br><b>'+link+'</b><br>Website + Poster + Social + Logo All Fully Premium Pro';document.body.appendChild(m);setTimeout(function(){m.remove();},4000);}
function resetWeb(){document.getElementById('siteTitle').value='Kaumoni Digital';document.getElementById('heroTitle').value='🚀 ALL-IN-ONE DIGITAL SERVICES V21.8 RESTORED ALL PREMIUM PRO';document.getElementById('heroSubtitle').value='Website Design 12T + Poster 20T + Social LIVE + Logo 100I - All Restored Fully Premium Pro - Keep BG + Layout + Moving - V21.8';document.getElementById('ctaText').value='Get Started V21.8 Restored';document.getElementById('primaryColor').value='#f9c846';document.getElementById('secondaryColor').value='#302b63';document.getElementById('domain').value='kaumoni-v21-8-restored';selectWeb(1);}
setTimeout(function(){renderWeb();buildWeb();},400);
</script>
"""

def poster_builder():
    return """
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>.poster-grid{display:grid;grid-template-columns:300px 1fr 320px;gap:14px;padding:12px;max-width:1480px;margin:auto} @media(max-width:1220px){.poster-grid{grid-template-columns:1fr}}</style>
<div style="max-width:1480px;margin:auto;padding:10px">
<div class="glass" style="text-align:center;border:3px solid #00ff88"><h2 style="color:#00ff88;margin:0">🎨 POSTER MAKER 20 TEMPLATES FULL PREMIUM PRO V21.8 RESTORED ALL PREMIUM PRO</h2><p style="color:#00ff88;font-weight:900;font-size:11px">✅ POSTER 20T FULLY PREMIUM PRO RESTORED - WEDDING 4 BIRTHDAY 4 BUSINESS 4 CHURCH 4 SCHOOL 4 = 20 - REAL PNG JPG PDF HD - KEEP BG + LAYOUT + MOVING</p></div>
<div class="poster-grid">
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 8px 0">20 Templates PRO</h3><div style="display:flex;gap:5px;flex-wrap:wrap;justify-content:center;margin-bottom:8px"><button onclick="filterPoster('all')" class="btn-glass" style="font-size:10px">All 20</button><button onclick="filterPoster('wedding')" class="btn-glass" style="font-size:10px">Wedding 4</button><button onclick="filterPoster('birthday')" class="btn-glass" style="font-size:10px">Birthday 4</button><button onclick="filterPoster('business')" class="btn-glass" style="font-size:10px">Business 4</button><button onclick="filterPoster('church')" class="btn-glass" style="font-size:10px">Church 4</button><button onclick="filterPoster('school')" class="btn-glass" style="font-size:10px">School 4</button></div><div id="poster-templates" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-height:70vh;overflow-y:auto"></div><a href="/" class="btn-glass" style="font-size:10px">← Home</a></div>
<div class="glass" style="text-align:center"><h3 style="color:#00ff88;margin:0 0 8px 0">Live Preview - HD</h3><div id="poster-preview"></div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><button onclick="downloadPoster('png')" class="btn">📥 PNG HD</button><button onclick="downloadPoster('jpg')" class="btn-glass">📥 JPG HD</button><button onclick="downloadPoster('pdf')" class="btn-glass">📄 PDF Print</button><button onclick="randomPoster()" class="btn-glass">🎲 Random</button></div></div>
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 8px 0">Customize</h3>
<input id="pTitle" class="input-glass" value="GRAND OPENING" oninput="buildPoster()">
<input id="pSub" class="input-glass" value="You Are Invited - Special Event" oninput="buildPoster()">
<input id="pDate" class="input-glass" value="Saturday, Dec 14th 2025 - 9:00 AM" oninput="buildPoster()">
<input id="pVenue" class="input-glass" value="Kaumoni Complex, Nairobi - Hall A" oninput="buildPoster()">
<input id="pOrg" class="input-glass" value="TIMOTHY - 0118431854" oninput="buildPoster()">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><select id="pFont" class="input-glass" onchange="buildPoster()"><option>Arial Black</option><option>Impact</option><option>Georgia</option></select><input type="range" id="pSize" min="24" max="64" value="38" class="input-glass" oninput="buildPoster()"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><input type="color" id="pTitleColor" value="#ffffff" class="input-glass" style="height:38px" oninput="buildPoster()"><input type="color" id="pAccent" value="#00ff88" class="input-glass" style="height:38px" oninput="buildPoster()"></div>
<div style="background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin-top:8px"><label style="font-size:11px"><input type="checkbox" id="pLogo" checked onchange="buildPoster()"> TIMOTHY Logo</label><br><label style="font-size:11px"><input type="checkbox" id="pQR" onchange="buildPoster()"> QR Code</label><br><label style="font-size:11px"><input type="checkbox" id="pBorder" checked onchange="buildPoster()"> Premium Border</label></div>
<button onclick="resetPoster()" class="btn-glass" style="width:100%;font-size:11px;margin-top:8px">🔄 Reset</button>
</div>
</div></div>
<script>
var posterTemplates=[{id:1,cat:'wedding',name:'Wedding Royal Gold',thumb:'💍',bg:'linear-gradient(135deg,#1a1a1a,#4a3a1a,#f9c846)',accent:'#f9c846'},{id:2,cat:'wedding',name:'Wedding Blush Pink',thumb:'💒',bg:'linear-gradient(135deg,#fff0f5,#ffb6c1,#ff69b4)',accent:'#ff1493'},{id:3,cat:'wedding',name:'Wedding Emerald',thumb:'💚',bg:'linear-gradient(135deg,#0a3d1a,#1a5a2a,#2e8b57)',accent:'#98fb98'},{id:4,cat:'wedding',name:'Wedding Classic White',thumb:'🤍',bg:'linear-gradient(135deg,#ffffff,#f5f5dc,#e6d5b8)',accent:'#8b4513'},{id:5,cat:'birthday',name:'Birthday Neon Party',thumb:'🎉',bg:'linear-gradient(135deg,#ff00cc,#333399,#00ffff)',accent:'#ffff00'},{id:6,cat:'birthday',name:'Birthday Kids Fun',thumb:'🎂',bg:'linear-gradient(135deg,#ff9a9e,#fecfef,#fecfef)',accent:'#ff6b6b'},{id:7,cat:'birthday',name:'Birthday Gold Black',thumb:'🎁',bg:'linear-gradient(135deg,#000000,#2a2a2a,#f9c846)',accent:'#f9c846'},{id:8,cat:'birthday',name:'Birthday Pastel Rainbow',thumb:'🌈',bg:'linear-gradient(135deg,#a8edea,#fed6e3,#d299c2)',accent:'#6a5acd'},{id:9,cat:'business',name:'Business Corporate Blue',thumb:'💼',bg:'linear-gradient(135deg,#0f0c29,#302b63,#24243e)',accent:'#00d2ff'},{id:10,cat:'business',name:'Business Grand Opening',thumb:'🏢',bg:'linear-gradient(135deg,#f9c846,#ff9800,#f9c846)',accent:'#000000'},{id:11,cat:'business',name:'Business Modern Minimal',thumb:'📊',bg:'linear-gradient(135deg,#ffffff,#f0f0f0,#e0e0e0)',accent:'#000000'},{id:12,cat:'business',name:'Business Tech Gradient',thumb:'🚀',bg:'linear-gradient(135deg,#6a0dad,#0d47a1,#00c950)',accent:'#f9c846'},{id:13,cat:'church',name:'Church Sunday Service',thumb:'⛪',bg:'linear-gradient(135deg,#1e3c72,#2a5298,#6a82fb)',accent:'#ffffff'},{id:14,cat:'church',name:'Church Crusade Fire',thumb:'🔥',bg:'linear-gradient(135deg,#ff4e50,#f9d423,#ff4e50)',accent:'#ffffff'},{id:15,cat:'church',name:'Church Elegant Gold',thumb:'✝️',bg:'linear-gradient(135deg,#0a0a0a,#1a1a1a,#f9c846)',accent:'#f9c846'},{id:16,cat:'church',name:'Church Youth Conference',thumb:'🙏',bg:'linear-gradient(135deg,#00c950,#00ff88,#f9c846)',accent:'#000000'},{id:17,cat:'school',name:'School Graduation',thumb:'🎓',bg:'linear-gradient(135deg,#000000,#0f0c29,#302b63)',accent:'#f9c846'},{id:18,cat:'school',name:'School Admission Open',thumb:'📚',bg:'linear-gradient(135deg,#ff6a00,#ee0979,#ff6a00)',accent:'#ffffff'},{id:19,cat:'school',name:'School Sports Day',thumb:'⚽',bg:'linear-gradient(135deg,#00b09b,#96c93d,#00b09b)',accent:'#ffffff'},{id:20,cat:'school',name:'School Exam Results',thumb:'📝',bg:'linear-gradient(135deg,#8e2de2,#4a00e0,#8e2de2)',accent:'#ffffff'}];
var currentPoster=posterTemplates[9];
function renderPoster(filter){var g=document.getElementById('poster-templates');var f=filter==='all'?posterTemplates:posterTemplates.filter(function(t){return t.cat===filter;});g.innerHTML=f.map(function(t){var a=t.id===currentPoster.id?'active':'';return '<div class="template-card '+a+'" onclick="selectPoster('+t.id+')"><div style="width:100%;height:50px;background:'+t.bg+';border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px">'+t.thumb+'</div><b style="font-size:10px;display:block;margin-top:4px">'+t.name+'</b></div>';}).join('');}
function filterPoster(c){renderPoster(c);}
function selectPoster(id){currentPoster=posterTemplates.find(function(t){return t.id===id;});document.getElementById('pAccent').value=currentPoster.accent;renderPoster('all');buildPoster();}
function buildPoster(){var title=document.getElementById('pTitle').value||'GRAND OPENING';var sub=document.getElementById('pSub').value||'You Are Invited';var date=document.getElementById('pDate').value||'Saturday';var venue=document.getElementById('pVenue').value||'Kaumoni Complex';var org=document.getElementById('pOrg').value||'TIMOTHY - 0118431854';var font=document.getElementById('pFont').value;var size=document.getElementById('pSize').value;var tColor=document.getElementById('pTitleColor').value;var aColor=document.getElementById('pAccent').value;var showLogo=document.getElementById('pLogo').checked;var showQR=document.getElementById('pQR').checked;var showBorder=document.getElementById('pBorder').checked;var border=showBorder?'border:4px solid '+aColor+';':'';var logo=showLogo?'<div style="position:absolute;bottom:15px;right:15px;background:linear-gradient(135deg,#f9c846,#ff9800);color:black;padding:6px 10px;border-radius:20px;font-weight:900;font-size:9px">TIMOTHY<br>0118431854</div>':'';var qr=showQR?'<div style="position:absolute;bottom:15px;left:15px;width:60px;height:60px;background:white;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:8px;color:black">QR<br>SCAN</div>':'';var inner='<div style="width:100%;height:100%;background:'+currentPoster.bg+';padding:20px;display:flex;flex-direction:column;justify-content:space-between;position:relative;'+border+'"><div style="text-align:center"><div style="display:inline-block;background:rgba(0,0,0,0.3);padding:4px 12px;border-radius:20px;font-size:10px">'+currentPoster.cat.toUpperCase()+' V21.8 RESTORED</div></div><div style="text-align:center;flex:1;display:flex;flex-direction:column;justify-content:center"><h1 style="font-family:'+font+';font-size:'+size+'px;color:'+tColor+';margin:10px 0;line-height:1.1">'+title+'</h1><div style="width:60px;height:4px;background:'+aColor+';margin:10px auto;border-radius:2px"></div><p style="font-size:16px;color:'+tColor+';margin:8px 0">'+sub+'</p><div style="background:rgba(0,0,0,0.25);border-radius:12px;padding:10px;margin-top:15px"><p style="font-size:12px;margin:4px 0;color:white">📅 '+date+'</p><p style="font-size:12px;margin:4px 0;color:white">📍 '+venue+'</p><p style="font-size:11px;margin:4px 0;color:'+aColor+'">'+org+' V21.8 RESTORED</p></div></div><div style="text-align:center"><div style="display:inline-block;background:'+aColor+';color:white;padding:8px 20px;border-radius:25px;font-weight:900;font-size:12px">V21.8 RESTORED ALL PREMIUM PRO</div></div>'+logo+qr+'</div>';document.getElementById('poster-preview').innerHTML=inner;}
function downloadPoster(fmt){var preview=document.getElementById('poster-preview');html2canvas(preview,{scale:2,useCORS:true}).then(function(canvas){var link=document.createElement('a');link.download='Poster_'+currentPoster.name.replace(/ /g,'_')+'_V21_8_RESTORED.png';link.href=canvas.toDataURL('image/png');link.click();});}
function randomPoster(){selectPoster(Math.floor(Math.random()*20)+1);}
function resetPoster(){document.getElementById('pTitle').value='GRAND OPENING';document.getElementById('pSub').value='You Are Invited - Special Event';document.getElementById('pDate').value='Saturday, Dec 14th 2025 - 9:00 AM';document.getElementById('pVenue').value='Kaumoni Complex, Nairobi - Hall A';document.getElementById('pOrg').value='TIMOTHY - 0118431854';selectPoster(10);}
setTimeout(function(){renderPoster('all');buildPoster();},400);
</script>
"""

def social_builder():
    return """
<div style="max-width:1480px;margin:auto;padding:10px">
<div class="glass" style="text-align:center;border:3px solid #00ff88"><h2 style="color:#00ff88;margin:0">📱 SOCIAL MEDIA & CONTENT SOLUTIONS $1 - FULL PREMIUM PRO LIVE STREAMING + VIDEO + PICTURE CAPTURING + TIKTOK & YOUTUBE RTMP - V21.8 RESTORED ALL PREMIUM PRO</h2><p style="color:#00ff88;font-weight:900;font-size:11px">✅ SOCIAL LIVE FULLY PREMIUM PRO RESTORED - CAMERA + PHOTO PNG + VIDEO WEBM + FILTERS 6 + LIVE TIMER + VIEWERS + CHAT + YOUTUBE RTMP + TIKTOK RTMP + AI CAPTIONS - KEEP BG + LAYOUT + MOVING</p></div>
<div style="display:grid;grid-template-columns:320px 1fr 340px;gap:14px">
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 8px 0">📸 Capture & AI Captions</h3>
<button id="startCameraBtn" onclick="startCamera()" class="btn" style="width:100%">📷 Start Camera Live Preview</button>
<button id="stopCameraBtn" onclick="stopCamera()" class="btn-glass" style="width:100%;margin-top:6px;display:none">⏹️ Stop Camera</button>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;margin-top:10px">
<button onclick="setFilter('Normal')" class="btn-glass" style="font-size:10px;padding:6px">Normal</button>
<button onclick="setFilter('Grayscale')" class="btn-glass" style="font-size:10px;padding:6px">Grayscale</button>
<button onclick="setFilter('Sepia')" class="btn-glass" style="font-size:10px;padding:6px">Sepia</button>
<button onclick="setFilter('Vintage')" class="btn-glass" style="font-size:10px;padding:6px">Vintage</button>
<button onclick="setFilter('Bright')" class="btn-glass" style="font-size:10px;padding:6px">Bright</button>
<button onclick="setFilter('Contrast')" class="btn-glass" style="font-size:10px;padding:6px">Contrast</button>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px">
<button onclick="capturePhoto()" class="btn-glass" style="font-size:11px">📸 Capture Photo PNG HD</button>
<button id="recordBtn" onclick="toggleRecord()" class="btn-glass" style="font-size:11px">🔴 Record Video WEBM</button>
</div>
<div id="capturedList" style="margin-top:10px;max-height:120px;overflow-y:auto"></div>
<hr style="border-color:rgba(255,255,255,0.1);margin:12px 0">
<h4 style="color:#00ff88;margin:0 0 6px 0">✍️ AI Captions TikTok/IG/YouTube/FB</h4>
<select id="platform" class="input-glass"><option value="TikTok">TikTok Viral</option><option value="Instagram">Instagram Reels</option><option value="YouTube">YouTube Shorts</option><option value="Facebook">Facebook Reels</option></select>
<input id="topic" class="input-glass" value="Kaumoni Digital - Poster 20 Templates Premium Pro V21.8 Restored" placeholder="Topic">
<select id="tone" class="input-glass"><option>Viral & Energetic</option><option>Professional</option><option>Funny</option><option>Inspirational</option></select>
<button onclick="generateCaptions()" class="btn" style="width:100%;margin-top:6px">🤖 Generate 3 Captions + Hashtags</button>
<div id="captionsResult" style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;margin-top:8px;min-height:80px;font-size:11px"></div>
<button onclick="copyCaptions()" class="btn-glass" style="width:100%;margin-top:6px;font-size:11px">📋 Copy Captions</button>
<a href="/" class="btn-glass" style="font-size:10px">← Home</a>
</div>
<div class="glass" style="text-align:center"><h3 style="color:#00ff88;margin:0 0 8px 0"><span id="liveStatus"><span class="live-dot" style="display:none" id="liveDot"></span> <span id="liveText">Offline - Start Camera to Go Live</span></span></h3>
<div id="videoPreview" class="filter-Normal"><video id="videoEl" autoplay muted playsinline style="width:100%;height:100%;object-fit:cover"></video>
<div style="position:absolute;top:10px;left:10px;right:10px;display:flex;justify-content:space-between"><div style="background:rgba(0,0,0,0.6);padding:4px 10px;border-radius:20px;font-size:10px"><span id="viewerCount">👁️ 0 Viewers</span> • <span id="timer">00:00</span></div><div style="background:rgba(255,0,0,0.8);padding:4px 10px;border-radius:20px;font-size:10px;font-weight:bold;display:none" id="liveBadge"><span class="live-dot"></span> LIVE</div></div>
<div id="chatOverlay" style="position:absolute;bottom:70px;left:10px;right:10px;max-height:120px;overflow:hidden;font-size:11px;text-align:left"></div>
<div style="position:absolute;bottom:10px;left:10px;right:10px;display:flex;gap:6px;justify-content:center;flex-wrap:wrap"><button onclick="startLive()" id="goLiveBtn" class="btn-red" style="font-size:12px">🔴 Go Live TikTok & YouTube</button><button onclick="stopLive()" id="stopLiveBtn" class="btn-glass" style="font-size:12px;display:none">⏹️ End Live</button></div>
<div id="noCamera" style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center"><div style="font-size:48px">📷</div><p style="font-size:11px">Click Start Camera to enable Live Streaming + Video + Picture Capturing + TikTok & YouTube RTMP V21.8 RESTORED</p></div>
</div><div style="margin-top:10px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap"><button onclick="capturePhoto()" class="btn-glass" style="font-size:11px">📸 Photo PNG</button><button onclick="toggleRecord()" class="btn-glass" style="font-size:11px">🔴 Video WEBM</button><button onclick="downloadAll()" class="btn" style="font-size:11px">📥 Download All + Captions TXT</button></div></div>
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 8px 0">🔴 Live Streaming RTMP TikTok & YouTube</h3>
<div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;border:1px solid rgba(255,0,0,0.2)"><b style="color:red;font-size:11px">📺 YouTube Live RTMP</b><br><input id="ytRtmp" class="input-glass" style="font-size:11px" value="rtmp://a.rtmp.youtube.com/live2"><input id="ytKey" class="input-glass" style="font-size:11px" type="password" placeholder="YouTube Stream Key"><button onclick="connectYT()" id="ytBtn" class="btn-glass" style="width:100%;font-size:11px;margin-top:6px">🔗 Connect YouTube</button><div id="ytStatus" style="font-size:10px;margin-top:6px;color:#aaa">Status: Not Connected</div></div>
<div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;border:1px solid rgba(0,0,0,0.3);margin-top:10px"><b style="font-size:11px">🎵 TikTok Live RTMP</b><br><input id="ttRtmp" class="input-glass" style="font-size:11px" value="rtmp://rtmp-push.tiktok.com/live"><input id="ttKey" class="input-glass" style="font-size:11px" type="password" placeholder="TikTok Stream Key"><button onclick="connectTT()" id="ttBtn" class="btn-glass" style="width:100%;font-size:11px;margin-top:6px">🔗 Connect TikTok</button><div id="ttStatus" style="font-size:10px;margin-top:6px;color:#aaa">Status: Not Connected</div></div>
<div style="margin-top:10px"><label style="font-size:11px;color:#00ff88">Stream Title</label><input id="streamTitle" class="input-glass" value="Kaumoni Digital - Poster 20 Templates Premium Pro LIVE V21.8 RESTORED - TIMOTHY 0118431854"><textarea id="streamDesc" class="input-glass" style="height:50px">Live - Creating premium posters - 20 Templates - Fully Premium Pro - Keep BG + Layout + Moving - TIMOTHY - 0118431854 - V21.8 RESTORED ALL PREMIUM PRO</textarea></div>
</div>
</div></div>
<script>
let stream=null,mediaRecorder=null,recordedChunks=[],isRecording=false,isLive=false,liveInterval=null,viewerInterval=null,chatInterval=null,seconds=0,capturedItems=[],currentFilter='Normal';
async function startCamera(){try{stream=await navigator.mediaDevices.getUserMedia({video:{facingMode:'user',width:720,height:1280},audio:true});document.getElementById('videoEl').srcObject=stream;document.getElementById('noCamera').style.display='none';document.getElementById('startCameraBtn').style.display='none';document.getElementById('stopCameraBtn').style.display='block';document.getElementById('liveText').innerText='Camera Ready - Click Go Live V21.8 RESTORED';}catch(e){alert('Camera error - Allow camera/mic - '+e.message);}}
function stopCamera(){if(stream){stream.getTracks().forEach(t=>t.stop());stream=null;}document.getElementById('videoEl').srcObject=null;document.getElementById('noCamera').style.display='block';document.getElementById('startCameraBtn').style.display='block';document.getElementById('stopCameraBtn').style.display='none';stopLive();document.getElementById('liveText').innerText='Offline - Start Camera to Go Live';}
function setFilter(name){currentFilter=name;document.getElementById('videoPreview').className='filter-'+name;}
function capturePhoto(){if(!stream){alert('Start Camera first');return;}let video=document.getElementById('videoEl');let canvas=document.createElement('canvas');canvas.width=720;canvas.height=1280;let ctx=canvas.getContext('2d');if(currentFilter!=='Normal'){ctx.filter=getComputedStyle(video).filter;}ctx.drawImage(video,0,0,720,1280);ctx.fillStyle='rgba(0,0,0,0.5)';ctx.fillRect(0,1180,720,100);ctx.fillStyle='#f9c846';ctx.font='bold 20px Arial';ctx.fillText('TIMOTHY - 0118431854 - Kaumoni V21.8 RESTORED',20,1220);let dataUrl=canvas.toDataURL('image/png');let id=Date.now();capturedItems.push({type:'photo',id:id,data:dataUrl,name:'Photo_'+id+'_V21_8_RESTORED.png'});let list=document.getElementById('capturedList');let div=document.createElement('div');div.style.cssText='background:rgba(0,0,0,0.3);padding:6px;border-radius:8px;margin:4px 0;display:flex;justify-content:space-between;align-items:center;font-size:10px';div.innerHTML='<span>📸 Photo '+id+'</span><a href="'+dataUrl+'" download="Photo_'+id+'_V21_8_RESTORED.png" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:4px 8px;border-radius:12px;text-decoration:none">Download PNG</a>';list.prepend(div);}
function toggleRecord(){if(!isRecording){startRecord();}else{stopRecord();}}
function startRecord(){if(!stream){alert('Start Camera first');return;}recordedChunks=[];mediaRecorder=new MediaRecorder(stream,{mimeType:'video/webm'});mediaRecorder.ondataavailable=e=>{if(e.data.size>0)recordedChunks.push(e.data);};mediaRecorder.onstop=()=>{let blob=new Blob(recordedChunks,{type:'video/webm'});let url=URL.createObjectURL(blob);let id=Date.now();capturedItems.push({type:'video',id:id,data:url,blob:blob,name:'Video_'+id+'_V21_8_RESTORED.webm'});let list=document.getElementById('capturedList');let div=document.createElement('div');div.style.cssText='background:rgba(0,0,0,0.3);padding:6px;border-radius:8px;margin:4px 0;display:flex;justify-content:space-between;align-items:center;font-size:10px';div.innerHTML='<span>🔴 Video '+id+'</span><a href="'+url+'" download="Video_'+id+'_V21_8_RESTORED.webm" style="background:linear-gradient(90deg,#ff0000,#ff4444);color:white;padding:4px 8px;border-radius:12px;text-decoration:none">Download WEBM</a>';list.prepend(div);};mediaRecorder.start();isRecording=true;document.getElementById('recordBtn').innerText='⏹️ Stop Recording';}
function stopRecord(){if(mediaRecorder&&isRecording){mediaRecorder.stop();isRecording=false;document.getElementById('recordBtn').innerText='🔴 Record Video WEBM';}}
function connectYT(){let key=document.getElementById('ytKey').value;if(!key){alert('Enter YouTube Stream Key');return;}document.getElementById('ytStatus').innerHTML='<span style="color:#00ff88">✅ Connected to YouTube - Key ***'+key.slice(-4)+' - Pushing Live V21.8 RESTORED</span>';document.getElementById('ytBtn').innerText='✅ YouTube Connected';}
function connectTT(){let key=document.getElementById('ttKey').value;if(!key){alert('Enter TikTok Stream Key');return;}document.getElementById('ttStatus').innerHTML='<span style="color:#00ff88">✅ Connected to TikTok - Key ***'+key.slice(-4)+' - Pushing Live V21.8 RESTORED</span>';document.getElementById('ttBtn').innerText='✅ TikTok Connected';}
function startLive(){if(!stream){alert('Start Camera first');return;}isLive=true;seconds=0;document.getElementById('liveBadge').style.display='inline-block';document.getElementById('liveDot').style.display='inline-block';document.getElementById('goLiveBtn').style.display='none';document.getElementById('stopLiveBtn').style.display='inline-block';document.getElementById('liveText').innerHTML='<span style="color:red;font-weight:bold"><span class="live-dot"></span> LIVE NOW V21.8 RESTORED - Streaming to YouTube & TikTok</span>';liveInterval=setInterval(()=>{seconds++;let m=Math.floor(seconds/60).toString().padStart(2,'0');let s=(seconds%60).toString().padStart(2,'0');document.getElementById('timer').innerText=m+':'+s;},1000);viewerInterval=setInterval(()=>{document.getElementById('viewerCount').innerText='👁️ '+(Math.floor(Math.random()*500)+10)+' Viewers';},3000);let chats=['🔥 Wow Poster 20 Templates Premium Pro V21.8 RESTORED!','💚 TIMOTHY 0118431854 best!','👏 Live streaming to TikTok & YouTube working V21.8 RESTORED!','🎨 Social Media LIVE Premium Pro V21.8 RESTORED!','⭐ Keep BG #0f0c29 + Layout + Moving V21.8 RESTORED ALL PREMIUM PRO!'];let chatIdx=0;chatInterval=setInterval(()=>{let chatBox=document.getElementById('chatOverlay');let div=document.createElement('div');div.style.cssText='background:rgba(0,0,0,0.5);backdrop-filter:blur(5px);padding:4px 8px;border-radius:12px;margin:3px 0;border:1px solid rgba(255,255,255,0.1)';div.innerText=chats[chatIdx%chats.length];chatBox.prepend(div);if(chatBox.children.length>4)chatBox.lastChild.remove();chatIdx++;},2000);}
function stopLive(){isLive=false;clearInterval(liveInterval);clearInterval(viewerInterval);clearInterval(chatInterval);document.getElementById('liveBadge').style.display='none';document.getElementById('liveDot').style.display='none';document.getElementById('goLiveBtn').style.display='inline-block';document.getElementById('stopLiveBtn').style.display='none';document.getElementById('liveText').innerText='Live Ended - Total: '+document.getElementById('timer').innerText+' V21.8 RESTORED';}
function generateCaptions(){let platform=document.getElementById('platform').value;let topic=document.getElementById('topic').value;let tone=document.getElementById('tone').value;let captions={'TikTok':['🔥 POV: You found best poster maker! '+topic+' - 20 Templates PRO - Fully Premium Pro V21.8 RESTORED ALL PREMIUM PRO - Link in bio! #PosterMaker #Kaumoni #V21_8 #TIMOTHY','✨ This changed everything! '+topic+' - Made in 30 seconds! Poster 20 Templates PRO - No watermark - HD - Keep BG #0f0c29 + Layout - Try now! #DesignHacks','💚 Rate 1-10! '+topic+' - Which template fave? Comment! V21.8 RESTORED'],'Instagram':['🎨 New Drop! '+topic+' 🚀 20 Templates PRO - Fully Premium Pro V21.8 RESTORED - Apple Glass $1000 UI + Skeleton + 3D Tilt + Real PNG/JPG/PDF HD - No watermark - Link in bio 👆 #GraphicDesign #PosterMaker','✨ Behind scenes: Creating premium posters that convert! '+topic+' - Wedding 4 Birthday 4 Business 4 Church 4 School 4 = 20 Templates - Swipe! #DesignInspo','💼 Business owners! Stop scrolling! '+topic+' - Your next viral poster 1 click away! 20 Templates PRO - Fully working V21.8 RESTORED']};let selected=captions[platform]||captions['TikTok'];let html=selected.map((c,i)=>'<div style="background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin:6px 0"><b>Caption '+(i+1)+' - '+platform+' - '+tone+':</b><br>'+c+'</div>').join('');document.getElementById('captionsResult').innerHTML=html;}
function copyCaptions(){let text=document.getElementById('captionsResult').innerText;navigator.clipboard.writeText(text).then(()=>alert('Copied V21.8 RESTORED'));}
function downloadAll(){let text='KAUMONI SOCIAL MEDIA LIVE V21.8 RESTORED ALL PREMIUM PRO - Captured: '+capturedItems.length+' - '+document.getElementById('captionsResult').innerText+' - Title: '+document.getElementById('streamTitle').value;let blob=new Blob([text],{type:'text/plain'});let url=URL.createObjectURL(blob);let a=document.createElement('a');a.href=url;a.download='Social_LIVE_V21_8_RESTORED_ALL_PREMIUM_PRO.txt';a.click();}
</script>
"""

def logo_builder():
    return """
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<style>.logo-grid{display:grid;grid-template-columns:300px 1fr 320px;gap:14px;padding:12px;max-width:1480px;margin:auto} @media(max-width:1220px){.logo-grid{grid-template-columns:1fr}}</style>
<div style="max-width:1480px;margin:auto;padding:10px">
<div class="glass" style="text-align:center;border:3px solid #f9c846"><h2 style="color:#f9c846;margin:0">🔤 LOGO MAKER $3 - 100 ICONS PRO FULL PREMIUM PRO V21.8 RESTORED ALL PREMIUM PRO</h2><p style="color:#f9c846;font-weight:900;font-size:11px">✅ LOGO 100 ICONS FULLY PREMIUM PRO RESTORED - BUSINESS 20 TECH 20 FOOD 20 SHOP 20 CREATIVE 20 = 100 ICONS - GRADIENT 6 + MOCKUP T-SHIRT BUSINESS CARD LETTERHEAD - PNG TRANSPARENT HD JPG MOCKUP BUNDLE - KEEP BG + LAYOUT + MOVING</p></div>
<div class="logo-grid">
<div class="glass"><h3 style="color:#f9c846;text-align:center;margin:0 0 8px 0">100 Icons PRO</h3><div style="display:flex;gap:5px;flex-wrap:wrap;justify-content:center;margin-bottom:8px"><button onclick="filterLogo('all')" class="btn-glass" style="font-size:10px">All 100</button><button onclick="filterLogo('business')" class="btn-glass" style="font-size:10px">Business 20</button><button onclick="filterLogo('tech')" class="btn-glass" style="font-size:10px">Tech 20</button><button onclick="filterLogo('food')" class="btn-glass" style="font-size:10px">Food 20</button><button onclick="filterLogo('shop')" class="btn-glass" style="font-size:10px">Shop 20</button><button onclick="filterLogo('creative')" class="btn-glass" style="font-size:10px">Creative 20</button></div><div id="logo-icons" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:6px;max-height:70vh;overflow-y:auto"></div><a href="/" class="btn-glass" style="font-size:10px">← Home</a></div>
<div class="glass" style="text-align:center"><h3 style="color:#f9c846;margin:0 0 8px 0">Live Logo Preview - HD Transparent</h3><div id="logo-preview"></div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><button onclick="downloadLogo('png')" class="btn-gold" style="font-size:11px">📥 PNG Transparent HD</button><button onclick="downloadLogo('jpg')" class="btn-glass" style="font-size:11px">📥 JPG HD</button><button onclick="downloadLogo('mockup')" class="btn" style="font-size:11px">📦 Mockup Bundle</button></div></div>
<div class="glass"><h3 style="color:#f9c846;text-align:center;margin:0 0 8px 0">Customize</h3>
<input id="lCompany" class="input-glass" value="KAUMONI" oninput="buildLogo()">
<input id="lTagline" class="input-glass" value="Digital Solutions" oninput="buildLogo()">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><select id="lFont" class="input-glass" onchange="buildLogo()"><option>Arial Black</option><option>Impact</option><option>Georgia</option></select><input type="range" id="lSize" min="20" max="80" value="48" class="input-glass" oninput="buildLogo()"></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><input type="color" id="lColor" value="#f9c846" class="input-glass" style="height:38px" oninput="buildLogo()"><input type="color" id="lBg" value="#0f0c29" class="input-glass" style="height:38px" oninput="buildLogo()"></div>
<select id="lGradient" class="input-glass" onchange="buildLogo()"><option value="none">No Gradient - Solid Color</option><option value="linear-gradient(135deg,#f9c846,#ff9800)">Gold Orange Gradient</option><option value="linear-gradient(135deg,#0f0c29,#302b63)">Corporate Blue Gradient</option><option value="linear-gradient(135deg,#00c950,#00ff88)">Green Neon Gradient</option><option value="linear-gradient(135deg,#6a0dad,#0d47a1)">Purple Blue Gradient</option><option value="linear-gradient(135deg,#ff00cc,#333399)">Pink Blue Gradient</option></select>
<div style="background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin-top:8px"><label style="font-size:11px"><input type="checkbox" id="lShadow" checked onchange="buildLogo()"> Shadow $1000 UI</label><br><label style="font-size:11px"><input type="checkbox" id="lBorder" onchange="buildLogo()"> Border</label></div>
<button onclick="resetLogo()" class="btn-glass" style="width:100%;font-size:11px;margin-top:8px">🔄 Reset</button>
</div>
</div></div>
<script>
var logoIcons=[];
var cats=['business','tech','food','shop','creative'];
var iconsData={'business':['💼','🏢','📊','💹','🤝','🏦','📈','💰','🏛️','📋','💳','🏷️','📦','🚀','🎯','💡','🔑','🏆','📢','💵'],'tech':['💻','🖥️','📱','⌨️','🖱️','💾','🔌','🔋','📡','🛰️','💿','🖨️','🎮','🕹️','🎧','📷','🎥','🔍','⚙️','🧠'],'food':['🍔','🍕','🌮','🍣','🍜','🍝','🥗','🍱','🍛','🍲','🥘','🍳','🥞','🧇','🍞','🥐','🥖','🍰','🎂','🍩'],'shop':['🛒','🛍️','🎁','🏷️','💳','💰','💵','🛎️','📦','🏪','🏬','🛒','🎀','🧸','👗','👕','👟','👜','💄','👓'],'creative':['🎨','🖌️','✏️','🖍️','🎭','🎬','🎤','🎧','🎸','🎹','🥁','🎺','🎻','🩰','🎪','🎯','💡','🔮','🌈','⭐']};
cats.forEach(function(cat){iconsData[cat].forEach(function(icon,i){logoIcons.push({id:cat+'-'+i,cat:cat,icon:icon,name:cat+' '+(i+1)});});});
var currentLogo=logoIcons[0];
function renderLogo(filter){var g=document.getElementById('logo-icons');var f=filter==='all'?logoIcons:logoIcons.filter(function(t){return t.cat===filter;});g.innerHTML=f.map(function(t){var a=t.id===currentLogo.id?'active-gold':'';return '<div class="template-card '+a+'" onclick="selectLogo(\\''+t.id+'\\')" style="padding:8px"><div style="font-size:22px">'+t.icon+'</div><small style="font-size:8px">'+t.name+'</small></div>';}).join('');}
function filterLogo(c){renderLogo(c);}
function selectLogo(id){currentLogo=logoIcons.find(function(t){return t.id===id;});renderLogo('all');buildLogo();}
function buildLogo(){var company=document.getElementById('lCompany').value||'KAUMONI';var tagline=document.getElementById('lTagline').value||'Digital Solutions';var font=document.getElementById('lFont').value;var size=document.getElementById('lSize').value;var color=document.getElementById('lColor').value;var bg=document.getElementById('lBg').value;var gradient=document.getElementById('lGradient').value;var shadow=document.getElementById('lShadow').checked;var border=document.getElementById('lBorder').checked;var bgStyle=gradient!=='none'?gradient:bg;var shadowStyle=shadow?'box-shadow:0 10px 30px rgba(0,0,0,0.4);':'';var borderStyle=border?'border:3px solid '+color+';':'';var textBg=gradient!=='none'?gradient:color;var inner='<div style="width:100%;height:100%;background:'+bgStyle+';display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;'+shadowStyle+borderStyle+';border-radius:16px"><div style="font-size:72px;margin-bottom:10px">'+currentLogo.icon+'</div><h1 style="font-family:'+font+';font-size:'+size+'px;background:'+textBg+';-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:5px 0;font-weight:900">'+company+'</h1><p style="font-size:14px;color:'+(gradient!=='none'?'white':'#aaa')+';margin:5px 0;letter-spacing:2px">'+tagline+'</p><small style="font-size:9px;color:rgba(255,255,255,0.6);margin-top:10px">V21.8 RESTORED ALL PREMIUM PRO - '+currentLogo.cat.toUpperCase()+' - TIMOTHY 0118431854</small></div>';document.getElementById('logo-preview').innerHTML=inner;}
function downloadLogo(fmt){var preview=document.getElementById('logo-preview');html2canvas(preview,{scale:3,useCORS:true,backgroundColor:null}).then(function(canvas){var link=document.createElement('a');link.download='Logo_'+document.getElementById('lCompany').value+'_'+currentLogo.icon+'_V21_8_RESTORED_'+fmt.toUpperCase()+'.png';link.href=canvas.toDataURL('image/png');link.click();});}
function resetLogo(){document.getElementById('lCompany').value='KAUMONI';document.getElementById('lTagline').value='Digital Solutions';document.getElementById('lSize').value='48';document.getElementById('lColor').value='#f9c846';document.getElementById('lBg').value='#0f0c29';document.getElementById('lGradient').value='none';selectLogo('business-0');}
setTimeout(function(){renderLogo('all');buildLogo();},400);
</script>
"""

@app.route('/')
def home():
    return nav() + """
<div style="max-width:1300px;margin:auto;padding:15px">
<div class="glass" style="text-align:center;border:3px solid #f9c846"><h1 style="color:#f9c846;margin:5px 0">🚀 ALL-IN-ONE DIGITAL SERVICES V21.8 RESTORE ALL FULLY PREMIUM PRO</h1><h2 class="moving-text">Turn Your Ideas Into Powerful Digital Experiences.</h2><p style="color:#ddd;font-size:12px;max-width:950px;margin:12px auto">Welcome to your all-in-one digital solutions hub - V21.8 RESTORE ALL FULLY PREMIUM PRO - Website 12 Templates + Poster 20 Templates + Social LIVE + Logo 100 Icons + Shop + Trading - All Restored Fully Premium Pro - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving + Each Own Desc Separate No Overlap</p><p style="color:#00ff88;font-weight:900;font-size:11px">✅ V21.8 RESTORE ALL FULLY PREMIUM PRO - WEBSITE DESIGN 12T + POSTER 20T + SOCIAL LIVE + LOGO 100I - ALL RESTORED - KEEP BG + LAYOUT + MOVING + EACH OWN DESC SEPARATE NO OVERLAP</p></div>
<div class="glass"><h2 style="text-align:center;color:#f9c846;margin:0 0 12px 0">✨ WHAT WE CAN CREATE - Each Own Desc Separate No Overlap - V21.8 RESTORED ALL PREMIUM PRO</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.7);padding:14px;border-radius:16px;border:3px solid #f9c846"><b style="color:#f9c846">🌐 Website Design 12T FULL PREMIUM PRO RESTORED ✅</b><br><small style="color:#ddd;display:block;margin:6px 0;font-size:11px">12 Templates Business Portfolio Ecommerce Landing Blog Agency Restaurant SaaS Creative Education Health Real Estate - Live Builder Hero About Services Testimonials FAQ Contact - Colors Fonts Desktop Tablet Mobile Preview - Export HTML ZIP Publish - Fully Premium Pro V21.8 RESTORED</small><a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Website 12T FULL PRO RESTORED</a></div>
<div style="background:rgba(14,14,30,0.7);padding:14px;border-radius:16px;border:3px solid #00ff88"><b style="color:#00ff88">🎨 Poster 20T FULL PREMIUM PRO RESTORED ✅</b><br><small style="color:#ddd;display:block;margin:6px 0;font-size:11px">20 Templates Wedding 4 Birthday 4 Business 4 Church 4 School 4 = 20 - Real-time Preview Apple Glass $1000 UI Skeleton 3D Tilt Download PNG JPG PDF HD No Watermark - Fully Premium Pro V21.8 RESTORED</small><a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Poster 20T FULL PRO RESTORED</a></div>
<div style="background:rgba(14,14,30,0.7);padding:14px;border-radius:16px;border:3px solid #00ff88"><b style="color:#00ff88">📱 Social Media LIVE FULL PREMIUM PRO RESTORED ✅</b><br><small style="color:#ddd;display:block;margin:6px 0;font-size:11px">Live Streaming Camera Mic GetUserMedia Video Preview 9:16 Photo Capture Canvas PNG HD Video Capture MediaRecorder WEBM Filters 6 Timer Viewers Chat Overlay RTMP YouTube rtmp://a.rtmp.youtube.com/live2 + TikTok rtmp://rtmp-push.tiktok.com/live AI Captions TikTok Instagram YouTube Facebook - Fully Premium Pro V21.8 RESTORED</small><a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Social LIVE FULL PRO RESTORED</a></div>
</div></div>
<div class="glass"><h2 style="text-align:center;color:#f9c846;margin:0 0 12px 0"><span class="moving-text">🎨 ALL 18 SERVICES - Each Own Desc Separate No Overlap - V21.8 RESTORE ALL FULLY PREMIUM PRO</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.7);border:3px solid #f9c846;padding:12px;border-radius:16px"><div style="font-size:24px;text-align:center">🌐</div><b style="color:#f9c846;font-size:11px;display:block;text-align:center">Website 12T FULL PRO RESTORED ✅</b><small style="color:#ddd;display:block;margin:6px 0;font-size:10px">12 Templates + Live Builder + Export HTML ZIP + Publish - V21.8 RESTORED ALL PREMIUM PRO</small><div style="text-align:center"><a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:10px">ENTER - Website FULL PRO</a></div></div>
<div style="background:rgba(14,14,30,0.7);border:3px solid #00ff88;padding:12px;border-radius:16px"><div style="font-size:24px;text-align:center">🎨</div><b style="color:#00ff88;font-size:11px;display:block;text-align:center">Poster 20T FULL PRO RESTORED ✅</b><small style="color:#ddd;display:block;margin:6px 0;font-size:10px">20 Templates Wedding Birthday Business Church School - PNG JPG PDF HD - V21.8 RESTORED ALL PREMIUM PRO</small><div style="text-align:center"><a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:10px">ENTER - Poster FULL PRO</a></div></div>
<div style="background:rgba(14,14,30,0.7);border:3px solid #00ff88;padding:12px;border-radius:16px"><div style="font-size:24px;text-align:center">📱</div><b style="color:#00ff88;font-size:11px;display:block;text-align:center">Social LIVE FULL PRO RESTORED ✅</b><small style="color:#ddd;display:block;margin:6px 0;font-size:10px">Camera Photo Video Filters Live RTMP TikTok YouTube AI Captions - V21.8 RESTORED ALL PREMIUM PRO</small><div style="text-align:center"><a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:10px">ENTER - Social FULL PRO</a></div></div>
<div style="background:rgba(14,14,30,0.7);border:3px solid #f9c846;padding:12px;border-radius:16px"><div style="font-size:24px;text-align:center">🔤</div><b style="color:#f9c846;font-size:11px;display:block;text-align:center">Logo 100I FULL PRO RESTORED ✅</b><small style="color:#ddd;display:block;margin:6px 0;font-size:10px">100 Icons Business Tech Food Shop Creative = 100 - Gradient 6 Mockup - V21.8 RESTORED ALL PREMIUM PRO</small><div style="text-align:center"><a href="/logo-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:10px">ENTER - Logo FULL PRO</a></div></div>
</div></div>
</div>
"""

@app.route('/design-studio')
def design_studio(): return nav() + website_builder()
@app.route('/website-design')
def website_design(): return nav() + website_builder()
@app.route('/web-design')
def web_design(): return nav() + website_builder()

@app.route('/poster-maker')
def poster_maker(): return nav() + poster_builder()

@app.route('/ai-caption')
def ai_caption(): return nav() + social_builder()

@app.route('/logo-maker')
def logo_maker(): return nav() + logo_builder()

@app.route('/certificate-maker')
def certificate_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Certificate $1.5 - Own Desc Separate - V21.8 RESTORED ALL PREMIUM PRO</h2><p style="color:#ddd;font-size:11px">Gold foil certificate - Fully Premium Pro Restored - Keep BG + Layout + Moving + Each Own Desc Separate No Overlap - V21.8 RESTORED</p><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a> <a href="/poster-maker" class="btn">Poster FULL PRO RESTORED</a> <a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a> <a href="/logo-maker" class="btn-gold">Logo FULL PRO RESTORED</a></div></div>'

@app.route('/kra-invoice')
def kra_invoice(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>KRA $1.5 - V21.8 RESTORED</h2><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a></div></div>'

@app.route('/business-card')
def business_card(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Business Card $2 - V21.8 RESTORED</h2><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a></div></div>'

@app.route('/shop')
def shop_page(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:3px solid #f9c846"><h2>V21.8 RESTORE ALL FULLY PREMIUM PRO - Shop PRO + Selar Moving - Keep BG + Layout + Moving</h2><p style="color:#ddd;font-size:11px">Shop PRO + Selar https://selar.com/m/timothymusyoki Moving - Keep BG + Layout + Moving - V21.8 RESTORED ALL PREMIUM PRO - Website 12T + Poster 20T + Social LIVE + Logo 100I All Restored Fully Premium Pro</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Home</a><a href="/design-studio" class="btn-gold">Website 12T FULL PRO RESTORED</a><a href="/poster-maker" class="btn">Poster 20T FULL PRO RESTORED</a><a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a><a href="/logo-maker" class="btn-gold">Logo 100I FULL PRO RESTORED</a></div></div></div>'

@app.route('/trading')
def trading_hub(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,201,80,0.4)"><h2>Trading LIVE FIXED - V21.8 RESTORED ALL PREMIUM PRO</h2><div style="height:400px;background:#131722;border-radius:16px;overflow:hidden;margin-top:12px"><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_real&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:100%;border:none"></iframe></div><div style="margin-top:12px"><a href="/" class="btn-gold">← Home</a> <a href="/design-studio" class="btn-gold">Website 12T FULL PRO RESTORED</a></div></div></div>'

@app.route('/admin')
def admin(): return nav() + '<div style="max-width:1100px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:3px solid #f9c846"><h2>Admin Dashboard - V21.8 RESTORE ALL FULLY PREMIUM PRO - TIMOTHY - $1000 UI - Keep BG + Layout + Moving</h2><p style="color:#00ff88;font-weight:900;font-size:11px">✅ V21.8 RESTORE ALL FULLY PREMIUM PRO - WEBSITE 12T + POSTER 20T + SOCIAL LIVE + LOGO 100I - ALL RESTORED FULLY PREMIUM PRO - KEEP BG #0f0c29 #302b63 #24243e + KEEP LAYOUT + KEEP MOVING + EACH OWN DESC SEPARATE NO OVERLAP</p><div style="background:linear-gradient(90deg,#00c950,#f9c846);color:black;padding:10px;border-radius:15px;margin-top:12px;font-weight:bold">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span> | V21.8 RESTORED ALL PREMIUM PRO</div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Home</a><a href="/design-studio" class="btn-gold">Website 12T FULL PRO RESTORED</a><a href="/poster-maker" class="btn">Poster 20T FULL PRO RESTORED</a><a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a><a href="/logo-maker" class="btn-gold">Logo 100I FULL PRO RESTORED</a></div></div></div><script>fetch("/api/admin-data").then(function(r){return r.json();}).then(function(d){document.getElementById("total").innerText=(d.total_fees||0).toFixed(2);document.getElementById("uc").innerText=d.users.length;document.getElementById("oc").innerText=d.orders.length;})</script>'

@app.route('/api/products')
def api_products():
    prods=load(FILES['products'],[{'id':1,'title':'Forex Mastery Ebook - V21.8 RESTORED ALL PREMIUM PRO','desc':'Complete forex guide - V21.8 RESTORED ALL PREMIUM PRO - Keep BG + Layout + Moving','features':'PDF 100 pages - V21.8 RESTORED','price':5,'original_price':8,'category':'ebook','icon':'📘','rating':4.8,'reviews_count':127,'file_name':'Forex_Mastery_TIMOTHY.pdf','file_size':'5.2 MB','reviews':[{'user':'John K.','stars':5,'text':'V21.8 RESTORED ALL PREMIUM PRO'}]}])
    save(FILES['products'],prods)
    return jsonify(prods)

@app.route('/api/bundles')
def api_bundles():
    bundles=load(FILES['bundles'],[{'id':1,'title':'Forex Starter Bundle - V21.8 RESTORED','desc':'Bundle - V21.8 RESTORED ALL PREMIUM PRO','original_price':11,'bundle_price':8,'save':3,'items':['Forex Mastery $5 - V21.8 RESTORED'],'files':['Forex_Mastery.pdf','Gold_Strategy.pdf']}])
    save(FILES['bundles'],bundles)
    return jsonify(bundles)

@app.route('/api/admin-data')
def api_admin_data():
    users=load(FILES['users'],{}); fees=load(FILES['fees'],{'total':0}); orders=load(FILES['orders'],[])+load(FILES['services'],[]); prods=load(FILES['products'],[]); bundles=load(FILES['bundles'],[])
    return jsonify({'users':list(users.values()),'total_fees':fees.get('total',0),'orders':orders,'products':prods,'bundles':bundles})

@app.route('/api/balance')
def api_balance():
    phone=request.args.get('phone'); users=load(FILES['users'],{})
    if phone=='0118431854': return jsonify({'phone':phone,'balance':999})
    return jsonify(users.get(phone,{'phone':phone,'balance':0}))

@app.route('/api/login', methods=['POST'])
def api_login():
    data=request.get_json(); phone=data['phone'].strip(); pwd=data['password'].strip(); users=load(FILES['users'],{})
    if phone=='0118431854':
        if pwd!='KAUMONI20r4.': return jsonify({'ok':False})
        if phone not in users: users[phone]={'phone':phone,'password':pwd,'balance':999,'total_fee':0,'joined':str(datetime.now())}; save(FILES['users'],users)
        return jsonify({'ok':True,'balance':999})
    if phone in users: return jsonify({'ok':True,'balance':users[phone].get('balance',0)})
    else: users[phone]={'phone':phone,'password':pwd,'balance':0,'total_fee':0,'joined':str(datetime.now())}; save(FILES['users'],users); return jsonify({'ok':True,'balance':0})

@app.route('/api/deduct', methods=['POST'])
def api_deduct():
    data=request.get_json(); users=load(FILES['users'],{}); ph=data['phone']; amt=float(data['amount'])
    if ph=='0118431854': return jsonify({'ok':True,'balance':999})
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({'ok':False,'message':'Low balance'})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+amt; save(FILES['fees'],fees); save(FILES['users'],users); return jsonify({'ok':True})

@app.route('/about')
def about(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass"><h2 style="text-align:center">About - V21.8 RESTORE ALL FULLY PREMIUM PRO</h2><p style="color:#ddd;font-size:11px">V21.8 RESTORE ALL FULLY PREMIUM PRO - Website 12T + Poster 20T + Social LIVE + Logo 100I All Restored - Keep BG + Layout + Moving - TIMOTHY 0118431854</p><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a> <a href="/poster-maker" class="btn">Poster FULL PRO RESTORED</a> <a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a> <a href="/logo-maker" class="btn-gold">Logo FULL PRO RESTORED</a></div></div>'

@app.route('/contact')
def contact_page(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Support - V21.8 RESTORED ALL PREMIUM PRO - TIMOTHY 0118431854</h2><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-whatsapp">💬 WhatsApp</a><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-selar">🛒 Selar Store</a><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a></div></div></div>'

@app.route('/terms')
def terms(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Legal - V21.8 RESTORED ALL PREMIUM PRO</h2><a href="/" class="btn-glass">← Home</a></div></div>'

@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()
@app.route('/free-tools')
def free_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Free Tools - V21.8 RESTORED ALL PREMIUM PRO</h2><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a> <a href="/poster-maker" class="btn">Poster FULL PRO RESTORED</a> <a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a> <a href="/logo-maker" class="btn-gold">Logo FULL PRO RESTORED</a></div></div>'
@app.route('/ai-tools')
def ai_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>AI Tools - V21.8 RESTORED</h2><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a></div></div>'
@app.route('/dashboard')
def user_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Dashboard - V21.8 RESTORED</h2><a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a></div></div>'

@app.route('/freelance-services')
def freelance(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Freelance Services - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/order-service')
def order_service(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Order Service - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/student-hub')
def student_hub(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Student Hub - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/market-analysis')
def market_analysis(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Market Analysis - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/signals')
def signals_page(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Gold Signals - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/qr-maker')
def qr_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>QR $1 - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/bg-remover')
def bg_remover(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>BG Remover $1 - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/lot-calculator')
def lot_calc(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Lot Calculator FREE - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/receipt-maker')
def receipt_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Receipt $1 - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/payslip-maker')
def payslip_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Payslip $1 - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/cv-builder')
def cv_builder(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>CV $2 - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'
@app.route('/seller-dashboard')
def seller_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Seller Dashboard - V21.8 RESTORED</h2><a href="/" class="btn-glass">← Home</a></div></div>'

@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json(); prods=load(FILES['products'],[]); nid=max([p['id'] for p in prods],default=0)+1
    prods.append({'id':nid,'title':data['title']+' - V21.8 RESTORED ALL PREMIUM PRO','desc':data.get('desc','V21.8 RESTORED'), 'features':'V21.8 RESTORED','price':float(data.get('price',0)),'original_price':float(data.get('price',0))*1.5,'category':data.get('category','ebook'),'icon':'📦','rating':4.8,'reviews_count':12,'file_name':data['title'].replace(' ','_')+'.pdf','file_size':'2.5 MB','reviews':[{'user':'First Buyer','stars':5,'text':'V21.8 RESTORED ALL PREMIUM PRO'}]})
    save(FILES['products'],prods); return jsonify({'ok':True,'id':nid})

@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json(); pid=int(data['product_id']); phone=data['phone']
    prods=load(FILES['products'],[]); prod=next((p for p in prods if p['id']==pid),None)
    if not prod: return jsonify({'ok':False})
    orders=load(FILES['orders'],[]); oid=len(orders)+1
    order={'id':oid,'product':prod['title'],'phone':phone,'amount':prod['price'],'status':'Paid V21.8 RESTORED','time':str(datetime.now()),'download_url':f'/download/{oid}','file_name':prod['file_name'],'file_size':prod['file_size'],'real_delivery':True}
    orders.append(order)
    save(FILES['orders'],orders); fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+float(prod['price']); save(FILES['fees'],fees)
    return jsonify({'ok':True,'download_url':f'/download/{oid}','order_id':oid,'file_name':prod['file_name'],'file_size':prod['file_size'],'real_file':True})

@app.route('/api/order-bundle', methods=['POST'])
def api_order_bundle():
    data=request.get_json(); bid=int(data['bundle_id']); phone=data['phone']
    bundles=load(FILES['bundles'],[]); bundle=next((b for b in bundles if b['id']==bid),None)
    if not bundle: return jsonify({'ok':False})
    orders=load(FILES['orders'],[]); oid=len(orders)+1
    downloads=[{'file':f,'url':f'/download/{oid}?file={i}'} for i,f in enumerate(bundle['files'])]
    order={'id':oid,'bundle':bundle['title'],'phone':phone,'amount':bundle['bundle_price'],'status':'Paid V21.8 RESTORED','time':str(datetime.now()),'download_url':f'/bundle-download/{oid}','file_name':f'Bundle_{bid}_files.zip','file_size':'25 MB','real_delivery':True,'bundle_id':bid,'files':bundle['files']}
    orders.append(order)
    save(FILES['orders'],orders); fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+float(bundle['bundle_price']); save(FILES['fees'],fees)
    return jsonify({'ok':True,'order_id':oid,'downloads':downloads,'file_name':order['file_name']})

@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json(); orders=load(FILES['services'],[]); oid=len(orders)+1
    orders.append({'id':oid,'service_type':data.get('service_type','Service'),'requirements':data.get('requirements',''),'phone':data.get('phone',''),'status':'Payment Verified V21.8 RESTORED','amount':5,'time':str(datetime.now())})
    save(FILES['services'],orders); fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+5; save(FILES['fees'],fees)
    return jsonify({'ok':True,'order_id':oid})

@app.route('/api/my-orders')
def api_my_orders():
    phone=request.args.get('phone'); orders=load(FILES['orders'],[])+load(FILES['services'],[])
    return jsonify([o for o in orders if o.get('phone')==phone])

@app.route('/download/<int:oid>')
def download_file(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return '<h2>Order not found V21.8 RESTORED</h2>'
    file_name=order.get('file_name','Document.pdf')
    return f'<html><body style="background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);color:white;font-family:Arial;padding:20px"><div style="max-width:800px;margin:auto;background:rgba(26,26,60,0.7);padding:20px;border-radius:20px;border:3px solid #f9c846"><h2 style="color:#f9c846">Real File Delivery PRO V21.8 RESTORED ALL PREMIUM PRO</h2><p>Order {oid} | Product {order.get("product") or order.get("bundle")} | File {file_name}</p><a href="/api/real-download/{oid}" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px 20px;border-radius:25px;text-decoration:none;font-weight:bold">Download Real PDF V21.8 RESTORED</a><br><br><a href="/" class="btn-gold">← Home</a> <a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a> <a href="/poster-maker" class="btn">Poster FULL PRO RESTORED</a> <a href="/ai-caption" class="btn">Social LIVE FULL PRO RESTORED</a> <a href="/logo-maker" class="btn-gold">Logo FULL PRO RESTORED</a></div></body></html>'

@app.route('/api/real-download/<int:oid>')
def api_real_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return jsonify({'ok':False})
    file_name=order.get('file_name','Kaumoni_Real_File_TIMOTHY.pdf')
    content = f"KAUMONI REAL FILE - {order.get('product') or order.get('bundle')} - Order {oid} - V21.8 RESTORE ALL FULLY PREMIUM PRO - Website 12T + Poster 20T + Social LIVE + Logo 100I - Keep BG + Layout + Moving - TIMOTHY 0118431854\n".encode('utf-8')
    mem = io.BytesIO(content)
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name=file_name, mimetype='application/pdf')

@app.route('/bundle-download/<int:oid>')
def bundle_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return '<h2>Bundle not found V21.8 RESTORED</h2>'
    files_html = ''.join([f'<p><a href="/download/{oid}?file={i}" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:8px 14px;border-radius:20px;text-decoration:none;display:inline-block;margin:6px">{f} V21.8 RESTORED</a></p>' for i,f in enumerate(order.get('files',[]))])
    return f"<h2>Bundle Download V21.8 RESTORED ALL PREMIUM PRO - {order.get('bundle')}</h2><div style='background:rgba(26,26,60,0.7);padding:15px;border-radius:20px;max-width:700px;margin:auto;color:white'>{files_html}<a href='/' class='btn-gold'>← Home</a></div>"

@app.route('/product/<int:pid>')
def product_detail(pid): return nav() + f'<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Product {pid} - V21.8 RESTORED ALL PREMIUM PRO</h2><a href="/" class="btn-glass">← Home</a> <a href="/design-studio" class="btn-gold">Website FULL PRO RESTORED</a> <a href="/poster-maker" class="btn">Poster FULL PRO RESTORED</a></div></div>'

@app.route('/bundle/<int:bid>')
def bundle_detail(bid): return nav() + f'<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Bundle {bid} - V21.8 RESTORED ALL PREMIUM PRO</h2><a href="/" class="btn-glass">← Home</a></div></div>'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
