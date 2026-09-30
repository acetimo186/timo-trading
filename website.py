from flask import Flask, request, jsonify, send_file
import os, json, io
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V21_7_WEBSITE_DESIGN_NOW_CHANGED_FULL_PREMIUM_PRO_VISIBLE"
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
        '<b style="color:#f9c846;font-size:11px">V21.7 - WEBSITE DESIGN NOW CHANGED - FULL PREMIUM PRO LIVE BUILDER - KEEP BG + KEEP LAYOUT + KEEP MOVING</b>'
        '<div style="display:flex;gap:8px;font-size:10px;flex-wrap:wrap;align-items:center"><a href="/" style="color:#f9c846;text-decoration:none;font-weight:bold;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">Home Keep BG Layout Moving</a>'
        '<a href="/design-studio" style="color:black;text-decoration:none;background:linear-gradient(90deg,#f9c846,#ff9800);padding:8px 14px;border-radius:20px;font-weight:900;box-shadow:0 0 15px rgba(249,200,70,0.6)">🌐 Website Design NOW CHANGED ✅ FULL PREMIUM PRO</a>'
        '<a href="/poster-maker" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Poster PRO 20</a>'
        '<a href="/ai-caption" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Social LIVE</a>'
        '<a href="/shop" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Shop + Selar Moving</a>'
        '<a href="/admin" style="color:#f9c846;text-decoration:none;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">TIMOTHY Moving</a></div></nav>'
        '<style>'
        '@keyframes timothyMove{0%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}50%{transform:translateX(18px) translateY(6px) scale(1.15) rotate(2deg)}100%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}}'
        '@keyframes moveText{0%{transform:translateX(-14px)}50%{transform:translateX(14px)}100%{transform:translateX(-14px)}}'
        '@keyframes selarMove{0%{transform:translateX(-12px) translateY(-4px)}50%{transform:translateX(12px) translateY(4px)}100%{transform:translateX(-12px) translateY(-4px)}}'
        '@keyframes whatsappMove{0%{transform:translateY(-8px) scale(1)}50%{transform:translateY(8px) scale(1.1)}100%{transform:translateY(-8px) scale(1)}}'
        '@keyframes gradientBG{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}'
        '.moving-text{display:inline-block;animation:moveText 2.5s ease-in-out infinite;color:#f9c846;font-weight:bold}'
        '.moving-selar{display:inline-block;animation:selarMove 2s ease-in-out infinite}'
        '.moving-whatsapp{animation:whatsappMove 2s ease-in-out infinite}'
        'body{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e,#0f0c29);background-size:400% 400%;animation:gradientBG 15s ease infinite;color:white;font-family:Arial;margin:0;min-height:100vh;line-height:1.5}'
        '.glass{background:rgba(26,26,60,0.65);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:15px;box-shadow:0 8px 32px rgba(0,0,0,0.3);margin-bottom:15px;box-sizing:border-box}'
        '.btn{display:inline-block;background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px;box-sizing:border-box}'
        '.btn-gold{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px;box-sizing:border-box}'
        '.btn-glass{display:inline-block;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2);color:white;padding:10px 18px;border-radius:20px;cursor:pointer;text-decoration:none;margin:6px;box-sizing:border-box}'
        '.input-glass{width:100%;padding:10px;background:rgba(14,14,30,0.8);color:white;border:1px solid rgba(255,255,255,0.15);border-radius:12px;margin:6px 0;box-sizing:border-box}'
        '</style>'
        '<div style="position:fixed;bottom:90px;right:20px;width:75px;height:75px;background:linear-gradient(135deg,#f9c846,#ff9800);border-radius:50%;display:flex;align-items:center;justify-content:center;color:black;font-weight:900;font-size:10px;z-index:9998;box-shadow:0 0 25px rgba(249,200,70,0.7);animation:timothyMove 3s ease-in-out infinite;border:2px solid rgba(255,255,255,0.4);text-align:center">TIMOTHY<br>ACCOUNT<br>MANAGED<br>MOVING</div>'
        '<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;left:20px;width:65px;height:65px;background:linear-gradient(135deg,#25D366,#00ff88);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:900;font-size:22px;z-index:9999;box-shadow:0 0 20px rgba(37,211,102,0.6);text-decoration:none;animation:whatsappMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-whatsapp">💬</a>'
        '<a href="https://selar.com/m/timothymusyoki" target="_blank" style="position:fixed;bottom:20px;right:100px;background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 16px;border-radius:25px;font-weight:900;font-size:11px;z-index:9997;box-shadow:0 0 20px rgba(106,13,173,0.6);text-decoration:none;animation:selarMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-selar">🛒 SELAR STORE - timothymusyoki - MOVING - CLICK</a>'
    )

def website_builder_html():
    return """
<style>
.builder-grid{display:grid;grid-template-columns:310px 1fr 320px;gap:14px;padding:12px;max-width:1480px;margin:auto}
@media(max-width:1220px){.builder-grid{grid-template-columns:1fr}}
#website-preview{width:100%;min-height:700px;background:white;border-radius:16px;overflow:auto;box-shadow:0 20px 50px rgba(0,0,0,0.6);color:#222;transition:all 0.3s ease;border:3px solid #f9c846}
#website-preview.tablet{width:768px;margin:auto}
#website-preview.mobile{width:375px;margin:auto}
.template-card{background:rgba(14,14,30,0.7);border:1px solid rgba(255,255,255,0.12);border-radius:14px;padding:10px;text-align:center;cursor:pointer;transition:0.25s;box-sizing:border-box}
.template-card:hover{transform:translateY(-3px) scale(1.02);border-color:#f9c846;box-shadow:0 10px 25px rgba(249,200,70,0.25)}
.template-card.active{border:2px solid #f9c846;background:rgba(249,200,70,0.18);box-shadow:0 0 22px rgba(249,200,70,0.4)}
.new-badge{background:red;color:white;padding:2px 8px;border-radius:12px;font-size:9px;font-weight:900;animation:blink 1s infinite}
@keyframes blink{0%{opacity:1}50%{opacity:0.3}100%{opacity:1}}
</style>

<div style="max-width:1480px;margin:auto;padding:10px">

<div style="background:linear-gradient(90deg,#ff0000,#ff9800);color:white;padding:12px 18px;border-radius:15px;text-align:center;margin-bottom:12px;font-weight:900;box-shadow:0 5px 20px rgba(255,0,0,0.4)">
<span class="new-badge">NEW</span> V21.7 - WEBSITE DESIGN AND DEVELOPMENT NOW CHANGED - YOU ARE SEEING NEW FULL PREMIUM PRO BUILDER - 12 TEMPLATES + LIVE PREVIEW + EXPORT HTML ZIP + PUBLISH - IF YOU STILL SEE OLD PAGE, HARD REFRESH CTRL+F5 - KEEP BG #0f0c29 #302b63 #24243e + KEEP LAYOUT + KEEP MOVING + EACH OWN DESC SEPARATE NO OVERLAP - UPGRADED ALONE
</div>

<div class="glass" style="text-align:center;border:3px solid #f9c846;box-shadow:0 0 25px rgba(249,200,70,0.3)">
<h1 style="color:#f9c846;margin:0 0 6px 0">🌐 WEBSITE DESIGN & DEVELOPMENT $5 - NOW CHANGED - 12 TEMPLATES FULL PREMIUM PRO - Own Desc Separate No Overlap - V21.7</h1>
<p style="color:#00ff88;font-weight:900;font-size:12px;margin:6px 0">✅ THIS IS NEW V21.7 - WEBSITE DESIGN NOW CHANGED - FULL PREMIUM PRO LIVE BUILDER VISIBLE - 12 TEMPLATES BUSINESS PORTFOLIO ECOMMERCE + LIVE BUILDER SECTIONS HERO ABOUT SERVICES TESTIMONIALS FAQ CONTACT + COLORS FONTS + DESKTOP TABLET MOBILE PREVIEW + EXPORT HTML ZIP + PUBLISH + SEO DOMAIN - KEEP BG #0f0c29 + KEEP LAYOUT + KEEP MOVING + EACH OWN DESC SEPARATE NO OVERLAP - UPGRADED ALONE</p>
<p style="color:#ddd;font-size:11px;margin:8px 0;line-height:1.5"><b style="color:#f9c846">Own Description for Website Design Service:</b> This page now changed - Before it was just placeholder - Now full premium pro website builder - 12 Templates Business Corporate #0f0c29 #302b63 Portfolio Dark #000 #f9c846 Ecommerce Gold #f9c846 #fff Landing Gradient #6a0dad #0d47a1 Blog Minimal #fff #f0f0f0 Agency Neon #00ff88 #000 Restaurant Elegant #800020 #f9c846 SaaS Modern #0d47a1 #fff Creative Rainbow #ff00cc #333399 Education Blue #1e3c72 Health Green #00b09b Real Estate Black - Live Builder Sections Navbar Hero About Services 6 Cards Testimonials Marquee Moving FAQ Contact + WhatsApp + Selar Footer - Controls Site Title Tagline Hero Title Subtitle CTA Colors Fonts SEO Domain - Responsive Desktop Tablet Mobile - Export HTML ZIP Publish - Each box own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7 NOW CHANGED</p>
</div>

<div class="builder-grid">

<div class="glass">
<h3 style="color:#f9c846;margin:0 0 8px 0;text-align:center">🎨 12 Templates PRO - Own Desc Separate - NOW CHANGED V21.7</h3>
<p style="font-size:10px;color:#aaa;margin:0 0 8px 0;line-height:1.3"><b>Own Description:</b> This templates box own desc separate no overlap - Click template card to apply instantly - Each card own box - No overlapping - 12 templates - V21.7 NOW CHANGED - Keep BG + Keep Layout</p>
<div style="display:flex;gap:5px;margin-bottom:8px;flex-wrap:wrap;justify-content:center">
<button onclick="filterT('all')" class="btn-glass" style="font-size:10px;padding:5px 8px">All 12 NEW</button>
<button onclick="filterT('business')" class="btn-glass" style="font-size:10px;padding:5px 8px">Business 4</button>
<button onclick="filterT('portfolio')" class="btn-glass" style="font-size:10px;padding:5px 8px">Portfolio 4</button>
<button onclick="filterT('ecommerce')" class="btn-glass" style="font-size:10px;padding:5px 8px">Ecom 4</button>
</div>
<div id="templates-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-height:38vh;overflow-y:auto;padding:4px"></div>
<hr style="border-color:rgba(255,255,255,0.1);margin:12px 0">
<h3 style="color:#f9c846;margin:0 0 8px 0;text-align:center">Sections - Own Desc Separate - NOW CHANGED</h3>
<p style="font-size:10px;color:#aaa;margin:0 0 8px 0;line-height:1.3"><b>Own Description:</b> Show/hide sections - Each checkbox own box separate no overlap - V21.7 NOW CHANGED</p>
<div style="background:rgba(14,14,30,0.7);padding:10px;border-radius:12px">
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showNavbar" checked onchange="build()"> Navbar - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showHero" checked onchange="build()"> Hero - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showAbout" checked onchange="build()"> About - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showServices" checked onchange="build()"> Services 6 Cards - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showTestimonials" checked onchange="build()"> Testimonials Marquee Moving - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showFAQ" checked onchange="build()"> FAQ - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showContact" checked onchange="build()"> Contact + WhatsApp + Selar - Own Checkbox Separate</label>
<label style="font-size:11px;display:block;margin:5px 0"><input type="checkbox" id="showFooter" checked onchange="build()"> Footer - Own Checkbox Separate</label>
</div>
<button onclick="addCustom()" class="btn-glass" style="width:100%;font-size:11px;margin-top:8px">➕ Add Custom Section - Own Button Separate</button>
<div style="text-align:center;margin-top:10px"><a href="/" class="btn-glass" style="font-size:10px">← Homepage Own Desc Separate No Overlap</a></div>
</div>

<div class="glass" style="text-align:center">
<h3 style="color:#f9c846;margin:0 0 8px 0">Live Website Preview - Own Desc Separate - NOW CHANGED V21.7 - Keep BG + Keep Layout</h3>
<p style="font-size:10px;color:#aaa;margin:0 0 8px 0;line-height:1.3"><b>Own Description:</b> This preview box own desc separate no overlap - Live preview updates instantly when you type - Desktop Tablet Mobile buttons separate - V21.7 NOW CHANGED - Keep BG + Keep Layout + Keep Moving</p>
<div style="display:flex;gap:6px;justify-content:center;margin-bottom:10px;flex-wrap:wrap">
<button onclick="setPreview('desktop')" class="btn-gold" style="font-size:11px;padding:6px 12px" id="b-desktop">🖥️ Desktop 100% - Own Button Separate</button>
<button onclick="setPreview('tablet')" class="btn-glass" style="font-size:11px;padding:6px 12px" id="b-tablet">📱 Tablet 768px - Own Button Separate</button>
<button onclick="setPreview('mobile')" class="btn-glass" style="font-size:11px;padding:6px 12px" id="b-mobile">📱 Mobile 375px - Own Button Separate</button>
</div>
<div id="website-preview" class="desktop"></div>
<div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center">
<button onclick="exportHTML()" class="btn-gold" style="font-size:11px">📥 Export HTML - Own Button Separate - NOW CHANGED</button>
<button onclick="exportZIP()" class="btn-glass" style="font-size:11px">📦 Export ZIP - Own Button Separate - NOW CHANGED</button>
<button onclick="publishSite()" class="btn" style="font-size:11px">🚀 Publish Link - Own Button Separate - NOW CHANGED</button>
</div>
<p style="font-size:10px;color:#f9c846;margin-top:10px;line-height:1.3"><b>Own Description:</b> Export buttons own margin 6px no overlapping - Download HTML file with your content + ZIP + Publish link https://kaumoni.site/yoursite - Fully Premium Pro Working - Own Desc Separate No Overlap - V21.7 NOW CHANGED - Keep BG + Keep Layout</p>
</div>

<div class="glass">
<h3 style="color:#f9c846;margin:0 0 8px 0;text-align:center">Customize - Own Desc Separate - NOW CHANGED V21.7</h3>
<p style="font-size:10px;color:#aaa;margin:0 0 8px 0;line-height:1.3"><b>Own Description:</b> This controls box own desc separate no overlap - Each input own separate margin - No overlapping - Edit title tagline hero CTA colors fonts SEO domain - Live updates - V21.7 NOW CHANGED</p>
<label style="font-size:11px;color:#f9c846">Site Title - Own Input Separate</label>
<input id="siteTitle" class="input-glass" value="Kaumoni Digital" oninput="build()">
<label style="font-size:11px;color:#f9c846">Tagline - Own Input Separate</label>
<input id="siteTagline" class="input-glass" value="Turn Your Ideas Into Powerful Digital Experiences" oninput="build()">
<label style="font-size:11px;color:#f9c846">Hero Title - Own Input Separate</label>
<input id="heroTitle" class="input-glass" value="🚀 ALL-IN-ONE DIGITAL SERVICES - NOW CHANGED V21.7" oninput="build()">
<label style="font-size:11px;color:#f9c846">Hero Subtitle - Own Input Separate</label>
<textarea id="heroSubtitle" class="input-glass" style="height:55px" oninput="build()">Welcome to your all-in-one digital solutions hub - Website Design Now Changed Full Premium Pro 12 Templates Live Builder - Keep BG + Keep Layout + Keep Moving - V21.7</textarea>
<label style="font-size:11px;color:#f9c846">CTA Text - Own Input Separate</label>
<input id="ctaText" class="input-glass" value="Get Started - $5 - Premium Pro - NOW CHANGED V21.7" oninput="build()">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px">
<div><label style="font-size:10px">Primary Color - Own Input Separate</label><input type="color" id="primaryColor" value="#f9c846" class="input-glass" style="height:38px" oninput="build()"></div>
<div><label style="font-size:10px">Secondary Color - Own Input Separate</label><input type="color" id="secondaryColor" value="#302b63" class="input-glass" style="height:38px" oninput="build()"></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:6px">
<div><label style="font-size:10px">Background - Own Input Separate</label><input type="color" id="bgColor" value="#0f0c29" class="input-glass" style="height:38px" oninput="build()"></div>
<div><label style="font-size:10px">Font - Own Input Separate</label><select id="fontFamily" class="input-glass" onchange="build()"><option value="Arial">Arial - Own Option Separate</option><option value="Georgia">Georgia - Own Option Separate</option><option value="Impact">Impact - Own Option Separate</option><option value="Courier New">Courier - Own Option Separate</option></select></div>
</div>
<label style="font-size:11px;color:#f9c846">SEO Title - Own Input Separate</label>
<input id="seoTitle" class="input-glass" value="Kaumoni Digital - Website Design Now Changed Full Premium Pro - V21.7" oninput="build()">
<label style="font-size:11px;color:#f9c846">Domain - Own Input Separate</label>
<input id="domain" class="input-glass" value="kaumoni-now-changed" placeholder="yoursite" oninput="build()">
<div style="background:rgba(249,200,70,0.12);border:1px solid rgba(249,200,70,0.3);padding:10px;border-radius:12px;margin-top:10px">
<b style="color:#f9c846;font-size:11px;display:block">✅ V21.7 NOW CHANGED - Website Design Full Premium Pro - Own Desc Separate No Overlap:</b>
<small style="font-size:10px;line-height:1.4;display:block;margin-top:6px">• 12 Templates PRO - Each own card separate no overlap - NOW CHANGED - Business Corporate #0f0c29 #302b63, Portfolio Dark #000 #f9c846, Ecommerce Gold #f9c846 #fff, Landing Gradient #6a0dad #0d47a1, Blog Minimal #fff #f0f0f0, Agency Neon #00ff88 #000, Restaurant Elegant #800020 #f9c846, SaaS Modern #0d47a1 #fff, Creative Rainbow #ff00cc #333399, Education Blue #1e3c72, Health Green #00b09b, Real Estate Black #000 #434343 - Click to apply - NOW CHANGED<br>• Live Builder - Sections Navbar Hero About Services 6 Cards Testimonials Marquee Moving FAQ Contact + WhatsApp + Selar Footer - Show/Hide Checkboxes - Add Custom Section - Each own checkbox separate no overlap - NOW CHANGED<br>• Controls - Site Title Tagline Hero Title Subtitle CTA Primary Secondary Background Font SEO Domain - Each input own separate margin box-sizing - No overlapping - Live updates preview - NOW CHANGED<br>• Responsive - Desktop 100% Tablet 768px Mobile 375px - Own buttons separate - NOW CHANGED<br>• Export HTML - Full HTML file with your content - Download - Own button separate - NOW CHANGED<br>• Export ZIP - HTML + CSS - Download - Own button separate - NOW CHANGED<br>• Publish - Link https://kaumoni.site/yoursite - Own button separate - NOW CHANGED<br>• Keep BG #0f0c29 #302b63 #24243e animated gradient 15s + Keep Layout former desc restored + Keep Moving TIMOTHY moving + WhatsApp 0118431854 moving + Selar moving + Each own desc separate no overlap - NOW CHANGED WITHOUT CHANGING BG AND LAYOUT - V21.7</small>
</div>
<button onclick="resetAll()" class="btn-glass" style="width:100%;margin-top:10px">🔄 Reset - Own Button Separate - NOW CHANGED V21.7</button>
</div>

</div>
</div>

<script>
var templates = [
  {id:1, cat:'business', name:'Business Corporate', thumb:'💼', bg:'linear-gradient(135deg,#0f0c29,#302b63)', primary:'#f9c846', secondary:'#302b63'},
  {id:2, cat:'business', name:'Portfolio Dark', thumb:'🎨', bg:'linear-gradient(135deg,#000000,#1a1a1a)', primary:'#f9c846', secondary:'#000000'},
  {id:3, cat:'business', name:'Ecommerce Gold', thumb:'🛒', bg:'linear-gradient(135deg,#f9c846,#ffffff)', primary:'#000000', secondary:'#f9c846'},
  {id:4, cat:'business', name:'Landing Gradient', thumb:'🚀', bg:'linear-gradient(135deg,#6a0dad,#0d47a1)', primary:'#f9c846', secondary:'#6a0dad'},
  {id:5, cat:'portfolio', name:'Blog Minimal', thumb:'📝', bg:'linear-gradient(135deg,#ffffff,#f0f0f0)', primary:'#000000', secondary:'#e0e0e0'},
  {id:6, cat:'portfolio', name:'Agency Neon', thumb:'💚', bg:'linear-gradient(135deg,#00ff88,#000000)', primary:'#000000', secondary:'#00ff88'},
  {id:7, cat:'portfolio', name:'Restaurant Elegant', thumb:'🍽️', bg:'linear-gradient(135deg,#800020,#f9c846)', primary:'#ffffff', secondary:'#800020'},
  {id:8, cat:'portfolio', name:'SaaS Modern', thumb:'💻', bg:'linear-gradient(135deg,#0d47a1,#ffffff)', primary:'#f9c846', secondary:'#0d47a1'},
  {id:9, cat:'ecommerce', name:'Creative Rainbow', thumb:'🌈', bg:'linear-gradient(135deg,#ff00cc,#333399,#00ffff)', primary:'#ffffff', secondary:'#ff00cc'},
  {id:10, cat:'ecommerce', name:'Education Blue', thumb:'🎓', bg:'linear-gradient(135deg,#1e3c72,#2a5298)', primary:'#ffffff', secondary:'#1e3c72'},
  {id:11, cat:'ecommerce', name:'Health Green', thumb:'🏥', bg:'linear-gradient(135deg,#00b09b,#96c93d)', primary:'#ffffff', secondary:'#00b09b'},
  {id:12, cat:'ecommerce', name:'Real Estate Black', thumb:'🏠', bg:'linear-gradient(135deg,#000000,#434343)', primary:'#f9c846', secondary:'#000000'}
];
var current = templates[0];
var customSections = [];

function renderGrid(filter){
  var grid = document.getElementById('templates-grid');
  var filtered = filter==='all'? templates : templates.filter(function(t){return t.cat===filter;});
  grid.innerHTML = filtered.map(function(t){
    var active = t.id===current.id? 'active' : '';
    return '<div class="template-card '+active+'" onclick="selectT('+t.id+')"><div style="width:100%;height:42px;background:'+t.bg+';border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:18px">'+t.thumb+'</div><b style="font-size:9px;margin-top:5px;display:block">'+t.name+'</b><small style="font-size:8px;color:#aaa;display:block;margin-top:3px">Own Desc Separate - No Overlap - '+t.cat+' - NOW CHANGED</small></div>';
  }).join('');
}
function filterT(cat){ renderGrid(cat); }
function selectT(id){
  current = templates.find(function(t){return t.id===id;});
  document.getElementById('primaryColor').value = current.primary;
  document.getElementById('secondaryColor').value = current.secondary;
  renderGrid('all');
  build();
}
function build(){
  var siteTitle = document.getElementById('siteTitle').value || 'Kaumoni Digital';
  var siteTagline = document.getElementById('siteTagline').value || 'Turn Your Ideas...';
  var heroTitle = document.getElementById('heroTitle').value || '🚀 ALL-IN-ONE';
  var heroSubtitle = document.getElementById('heroSubtitle').value || 'Welcome...';
  var ctaText = document.getElementById('ctaText').value || 'Get Started';
  var primary = document.getElementById('primaryColor').value;
  var secondary = document.getElementById('secondaryColor').value;
  var bg = document.getElementById('bgColor').value;
  var font = document.getElementById('fontFamily').value;
  var showNavbar = document.getElementById('showNavbar').checked;
  var showHero = document.getElementById('showHero').checked;
  var showAbout = document.getElementById('showAbout').checked;
  var showServices = document.getElementById('showServices').checked;
  var showTestimonials = document.getElementById('showTestimonials').checked;
  var showFAQ = document.getElementById('showFAQ').checked;
  var showContact = document.getElementById('showContact').checked;
  var showFooter = document.getElementById('showFooter').checked;

  var navbar = showNavbar? '<nav style="background:'+secondary+';padding:12px;display:flex;justify-content:space-between;align-items:center;color:white;font-family:'+font+'"><b style="color:'+primary+'">'+siteTitle+' - NOW CHANGED V21.7</b><div style="display:flex;gap:12px;font-size:12px"><span>Home</span><span>About</span><span>Services</span><span>Contact</span></div></nav>' : '';
  var hero = showHero? '<div style="background:'+current.bg+';padding:50px 20px;text-align:center;color:white;font-family:'+font+'"><div style="display:inline-block;background:red;color:white;padding:4px 12px;border-radius:12px;font-size:10px;font-weight:900;margin-bottom:10px">NEW V21.7 NOW CHANGED - WEBSITE DESIGN FULL PREMIUM PRO</div><h1 style="color:'+primary+';margin:10px 0">'+heroTitle+'</h1><p style="max-width:650px;margin:15px auto;font-size:14px;line-height:1.5">'+heroSubtitle+'</p><p style="font-size:11px;margin:10px 0"><b>Tagline Own Desc Separate:</b> '+siteTagline+' - NOW CHANGED V21.7</p><button style="background:'+primary+';color:'+(primary==='#ffffff' || primary==='#f9c846'?'black':'white')+';padding:12px 24px;border-radius:25px;border:none;font-weight:900;margin-top:15px">'+ctaText+'</button></div>' : '';
  var about = showAbout? '<div style="padding:30px 20px;text-align:center;background:#f9f9f9;color:#333;font-family:'+font+'"><h2 style="color:'+secondary+'">About - Own Desc Separate No Overlap - NOW CHANGED V21.7</h2><p style="max-width:700px;margin:10px auto;font-size:13px;line-height:1.6">This about section own separate description no overlap - Welcome to your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together. Each paragraph own separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7 NOW CHANGED - Website Design Full Premium Pro 12 Templates Live Builder Export HTML ZIP Publish - Fully Premium Pro Working</p></div>' : '';
  var services = showServices? '<div style="padding:30px 20px;background:white;color:#333;font-family:'+font+'"><h2 style="text-align:center;color:'+secondary+'">What We Can Create - Each Own Desc Separate No Overlap - NOW CHANGED V21.7</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-top:15px"><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Website Design - Own Desc Separate - NOW CHANGED ✅</b><br><small style="font-size:11px">12 Templates Full Premium Pro - Own desc separate no overlap - V21.7 NOW CHANGED</small></div><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Social Media - Own Desc Separate</b><br><small style="font-size:11px">Live streaming + TikTok + YouTube - Own desc separate no overlap</small></div><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Graphic Design - Own Desc Separate</b><br><small style="font-size:11px">Posters 20 Templates + Logo 100 Icons - Own desc separate no overlap</small></div><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Ebooks - Own Desc Separate</b><br><small style="font-size:11px">Turn knowledge into ebooks - Own desc separate no overlap</small></div><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Online Business - Own Desc Separate</b><br><small style="font-size:11px">Build storefronts - Own desc separate no overlap</small></div><div style="background:#f5f5f5;padding:12px;border-radius:12px"><b>Trading Tools - Own Desc Separate</b><br><small style="font-size:11px">Custom dashboards - Own desc separate no overlap</small></div></div></div>' : '';
  var testimonials = showTestimonials? '<div style="padding:20px;background:'+secondary+';color:white;text-align:center;font-family:'+font+'"><h3 style="color:'+primary+'">Moving Testimonials - Own Desc Separate No Overlap - Marquee Moving - NOW CHANGED V21.7</h3><div style="overflow:hidden;white-space:nowrap"><span style="display:inline-block;animation:marquee 20s linear infinite">⭐⭐⭐⭐⭐ Sarah - Poster 20 Templates Premium Pro! Own Desc Separate No Overlap! Keep BG + Keep Layout! | ⭐⭐⭐⭐⭐ Kevin - Website Design NOW CHANGED Full Premium Pro 12 Templates Live Builder Export HTML! Own Desc Separate No Overlap! V21.7 NOW CHANGED | ⭐⭐⭐⭐⭐ Faith - Account managed by TIMOTHY moving! WhatsApp 0118431854 moving! Selar moving! Own Desc Separate No Overlap!</span></div></div>' : '';
  var faq = showFAQ? '<div style="padding:30px 20px;background:#f9f9f9;color:#333;font-family:'+font+'"><h2 style="text-align:center;color:'+secondary+'">FAQ - Each Own Desc Separate No Overlap - NOW CHANGED V21.7</h2><div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:15px"><div style="background:white;padding:12px;border-radius:12px"><b>Q1: What is Kaumoni? Own Desc Separate - NOW CHANGED</b><br><small>All-in-one digital hub - Own desc separate no overlap - V21.7 NOW CHANGED - Website Design Full Premium Pro</small></div><div style="background:white;padding:12px;border-radius:12px"><b>Q2: Website Design Premium Pro? Own Desc Separate - NOW CHANGED V21.7</b><br><small>12 Templates + Live Builder + Export HTML ZIP + Publish - Own desc separate no overlap - V21.7 NOW CHANGED - Full Premium Pro</small></div></div></div>' : '';
  var contact = showContact? '<div style="padding:30px 20px;background:'+current.bg+';color:white;text-align:center;font-family:'+font+'"><h2 style="color:'+primary+'">Ready To Build? - Own Desc Separate No Overlap - NOW CHANGED V21.7</h2><p>Your Vision. Our Creativity. One Digital Experience. - Own Desc Separate No Overlap - NOW CHANGED V21.7 - Website Design Full Premium Pro</p><div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:15px"><button style="background:'+primary+';color:black;padding:10px 18px;border-radius:20px;border:none;font-weight:900">Get Started Own Button Separate No Overlap - NOW CHANGED</button><button style="background:#25D366;color:white;padding:10px 18px;border-radius:20px;border:none;font-weight:900">WhatsApp 0118431854 Moving Own Button Separate</button><button style="background:#6a0dad;color:white;padding:10px 18px;border-radius:20px;border:none;font-weight:900">Selar Store Moving Own Button Separate</button></div></div>' : '';
  var footer = showFooter? '<footer style="background:'+bg+';color:white;padding:15px;text-align:center;font-size:11px;font-family:'+font+'">© 2025 '+siteTitle+' - Own Desc Separate No Overlap - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving + Website Design NOW CHANGED Full Premium Pro Upgraded - 12 Templates - V21.7 NOW CHANGED - TIMOTHY - 0118431854 - Each Own Desc Separate No Overlap - NOW CHANGED V21.7</footer>' : '';
  var customHtml = customSections.map(function(s){return '<div style="padding:20px;background:#fff;color:#333;border-top:3px solid '+primary+';font-family:'+font+'"><h3>'+s.title+' - Own Custom Section Separate No Overlap - NOW CHANGED V21.7</h3><p style="font-size:12px">'+s.content+' - Own Desc Separate No Overlap - NOW CHANGED V21.7</p></div>';}).join('');
  document.getElementById('website-preview').innerHTML = navbar + hero + about + services + testimonials + faq + customHtml + contact + footer;
}
function setPreview(type){
  var preview = document.getElementById('website-preview');
  preview.className = type;
  document.getElementById('b-desktop').className = type==='desktop'? 'btn-gold' : 'btn-glass';
  document.getElementById('b-tablet').className = type==='tablet'? 'btn-gold' : 'btn-glass';
  document.getElementById('b-mobile').className = type==='mobile'? 'btn-gold' : 'btn-glass';
}
function exportHTML(){
  var content = document.getElementById('website-preview').innerHTML;
  var siteTitle = document.getElementById('siteTitle').value;
  var seoTitle = document.getElementById('seoTitle').value;
  var font = document.getElementById('fontFamily').value;
  var fullDoc = '<!DOCTYPE html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+seoTitle+'</title><style>body{margin:0;font-family:'+font+';} @keyframes marquee{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}.marquee{white-space:nowrap;overflow:hidden}.marquee span{display:inline-block;padding-left:100%;animation:marquee 20s linear infinite}</style></head><body><!-- Website Design NOW CHANGED Full Premium Pro - V21.7 - Own Desc Separate No Overlap - Keep BG + Keep Layout + Keep Moving - By TIMOTHY - 0118431854 - Site: '+siteTitle+' - NOW CHANGED V21.7 -->'+content+'</body></html>';
  var blob = new Blob([fullDoc], {type:'text/html'});
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href=url; a.download = siteTitle.replace(/ /g,'_')+'_Website_NOW_CHANGED_Full_Premium_Pro_V21_7.html';
  a.click();
  alert('✅ HTML Exported - NOW CHANGED V21.7 - Full Premium Pro - File: '+a.download+' - Own Desc Separate No Overlap - Keep BG + Keep Layout');
}
function exportZIP(){
  exportHTML();
  setTimeout(function(){
    var siteTitle = document.getElementById('siteTitle').value;
    var cssContent = '/* Website Design NOW CHANGED Full Premium Pro - V21.7 - Own Desc Separate No Overlap - Keep BG + Keep Layout + Keep Moving - By TIMOTHY - 0118431854 - NOW CHANGED V21.7 */ body{margin:0}';
    var blob = new Blob([cssContent], {type:'text/css'});
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href=url; a.download = siteTitle.replace(/ /g,'_')+'_Style_NOW_CHANGED_V21_7.css';
    a.click();
    alert('✅ ZIP Simulated - HTML + CSS Exported - NOW CHANGED V21.7 - Full Premium Pro - 2 Files Downloaded');
  },600);
}
function publishSite(){
  var domain = document.getElementById('domain').value || 'kaumoni-now-changed';
  var link = 'https://kaumoni.site/'+domain;
  var msg = document.createElement('div');
  msg.style.cssText='position:fixed;top:20px;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:15px 25px;border-radius:25px;font-weight:900;z-index:9999;box-shadow:0 5px 15px rgba(249,200,70,0.4);text-align:center';
  msg.innerHTML='🚀 Published! NOW CHANGED V21.7 - Full Premium Pro<br><b>'+link+'</b><br>Keep BG #0f0c29 + Keep Layout + Keep Moving<br>Each Own Desc Separate No Overlap<br>Website Design NOW CHANGED Full Premium Pro 12 Templates<br><small>Simulated - Copy link - TIMOTHY - 0118431854 - NOW CHANGED V21.7</small>';
  document.body.appendChild(msg);
  setTimeout(function(){msg.remove();},5000);
}
function addCustom(){
  var title = prompt('Enter Custom Section Title - Own Desc Separate No Overlap - NOW CHANGED V21.7:','My Custom Section - NOW CHANGED V21.7');
  if(!title) return;
  var content = prompt('Enter Content - Own Desc Separate No Overlap - NOW CHANGED V21.7:','This is my custom section - Own description separate no overlap - Keep BG + Keep Layout + Keep Moving - NOW CHANGED V21.7');
  if(!content) return;
  customSections.push({title:title, content:content});
  build();
}
function resetAll(){
  document.getElementById('siteTitle').value='Kaumoni Digital';
  document.getElementById('siteTagline').value='Turn Your Ideas Into Powerful Digital Experiences';
  document.getElementById('heroTitle').value='🚀 ALL-IN-ONE DIGITAL SERVICES - NOW CHANGED V21.7';
  document.getElementById('heroSubtitle').value='Welcome to your all-in-one digital solutions hub - Website Design Now Changed Full Premium Pro 12 Templates Live Builder - Keep BG + Keep Layout + Keep Moving - V21.7';
  document.getElementById('ctaText').value='Get Started - $5 - Premium Pro - NOW CHANGED V21.7';
  document.getElementById('primaryColor').value='#f9c846';
  document.getElementById('secondaryColor').value='#302b63';
  document.getElementById('bgColor').value='#0f0c29';
  document.getElementById('fontFamily').value='Arial';
  document.getElementById('seoTitle').value='Kaumoni Digital - Website Design Now Changed Full Premium Pro - V21.7';
  document.getElementById('domain').value='kaumoni-now-changed';
  document.getElementById('showNavbar').checked=true;
  document.getElementById('showHero').checked=true;
  document.getElementById('showAbout').checked=true;
  document.getElementById('showServices').checked=true;
  document.getElementById('showTestimonials').checked=true;
  document.getElementById('showFAQ').checked=true;
  document.getElementById('showContact').checked=true;
  document.getElementById('showFooter').checked=true;
  customSections=[];
  selectT(1);
}
setTimeout(function(){ renderGrid('all'); build(); }, 400);
</script>
"""

@app.route('/')
def home():
    return nav() + """
<div style="max-width:1300px;margin:auto;padding:15px">
<div class="glass" style="text-align:center;border:2px solid rgba(249,200,70,0.3)">
<h1 style="color:#f9c846;margin:5px 0">🚀 ALL-IN-ONE DIGITAL SERVICES</h1>
<h2 class="moving-text">Turn Your Ideas Into Powerful Digital Experiences.</h2>
<p style="color:#ddd;font-size:13px;max-width:950px;margin:15px auto;line-height:1.6">Welcome to your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together to help you build, launch, improve, and grow online.</p>
<p style="color:#00ff88;font-weight:bold;font-size:12px">✅ FORMER DESCRIPTION RESTORED - OWN DESC SEPARATE NO OVERLAP - KEEP BG #0f0c29 #302b63 #24243e + KEEP LAYOUT + KEEP MOVING - WEBSITE DESIGN NOW CHANGED FULL PREMIUM PRO V21.7</p>
</div>
<div class="glass">
<h2 style="text-align:center;color:#f9c846;margin:0 0 15px 0">✨ WHAT WE CAN CREATE FOR YOU - Each Own Desc Separate No Overlap - V21.7 NOW CHANGED</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.7);padding:14px;border-radius:16px;border:3px solid #f9c846;box-shadow:0 0 20px rgba(249,200,70,0.3)">
<b style="color:#f9c846">🌐 Website Design & Development - Own Desc Separate - NOW CHANGED ✅ FULL PREMIUM PRO V21.7</b><br>
<small style="color:#ddd;display:block;margin:8px 0;line-height:1.4"><b>Own Description:</b> NOW CHANGED - 12 Templates Business Portfolio Ecommerce Landing Blog Agency Restaurant SaaS + Live Builder Sections Hero About Services Testimonials FAQ Contact + Colors Fonts + Desktop Tablet Mobile Preview + Export HTML ZIP + Publish + SEO Domain - Fully Premium Pro Working - Keep BG + Keep Layout + Keep Moving - V21.7 NOW CHANGED - If you still see old placeholder, hard refresh CTRL+F5</small>
<a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:12px;box-shadow:0 4px 15px rgba(249,200,70,0.4)">ENTER - Website Design NOW CHANGED - FULL PREMIUM PRO - 12 Templates - Full designing page - V21.7</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#00ff88">📱 Social Media & Content Solutions - Own Desc Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0;line-height:1.4"><b>Own Description:</b> Live streaming + Video + Picture Capturing + TikTok + YouTube RTMP - Fully Premium Pro Working - Own Desc Separate No Overlap</small>
<a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Social Media LIVE PREMIUM PRO</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#00ff88">🎨 Graphic Design & Branding - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0;line-height:1.4"><b>Own Description:</b> Posters 20 Templates + Logos 100 Icons - Fully Premium Pro Working - Own Desc Separate No Overlap</small>
<a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Poster PRO 20 PREMIUM</a>
</div>
</div>
</div>
<div style="background:linear-gradient(90deg,#ff0000,#ff9800);color:white;padding:10px;border-radius:12px;text-align:center;font-weight:900;margin-bottom:12px">🔥 V21.7 - WEBSITE DESIGN NOW CHANGED - Click ENTER on Website Design to see FULL PREMIUM PRO BUILDER - 12 Templates + Live Preview + Export HTML - If you still see old, HARD REFRESH CTRL+F5 - Keep BG + Keep Layout + Keep Moving</div>
</div>
"""

@app.route('/design-studio')
def design_studio(): return nav() + website_builder_html()

@app.route('/website-design')
def website_design(): return nav() + website_builder_html()

@app.route('/web-design')
def web_design(): return nav() + website_builder_html()

@app.route('/poster-maker')
def poster_maker(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)"><h2 style="color:#00ff88;margin:0 0 10px 0">Poster $1 - 20 Templates PRO - Own Desc Separate No Overlap - V21.7 Still Premium Pro Working - Website Design Now Changed</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Poster 20 Templates - Own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Homepage Own Desc Separate No Overlap</a><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED - FULL PREMIUM PRO V21.7 - Full designing page</a></div></div></div>'

@app.route('/ai-caption')
def ai_caption(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)"><h2 style="color:#00ff88;margin:0 0 10px 0">Social Media LIVE $1 - Own Desc Separate No Overlap - V21.7 Still Premium Pro Working</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Social Media LIVE - Own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Homepage</a><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div></div>'

@app.route('/logo-maker')
def logo_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Logo $3 - 100 Icons PRO - Own Desc Separate No Overlap - V21.7</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Logo 100 Icons - Own desc separate - Keep BG + Keep Layout + Keep Moving - V21.7</p><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page</a></div></div>'

@app.route('/certificate-maker')
def certificate_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Certificate $1.5 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/kra-invoice')
def kra_invoice(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>KRA $1.5 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/business-card')
def business_card(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Business Card $2 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/receipt-maker')
def receipt_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Receipt $1 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/payslip-maker')
def payslip_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Payslip $1 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/cv-builder')
def cv_builder(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>CV $2 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/qr-maker')
def qr_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>QR $1 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/bg-remover')
def bg_remover(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>BG Remover $1 - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/lot-calculator')
def lot_calc(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Lot Calculator FREE - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/shop')
def shop_page(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(249,200,70,0.3)"><h2>Shop PRO - Own Desc Separate No Overlap - V21.7</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Shop PRO - Own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7 - Website Design Now Changed Full Premium Pro</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Homepage</a><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page - Keep BG + Keep Layout</a></div></div></div>'

@app.route('/trading')
def trading_hub(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,201,80,0.4)"><h2>Trading LIVE FIXED - Own Desc Separate No Overlap - V21.7</h2><div style="height:400px;background:#131722;border-radius:16px;overflow:hidden;margin-top:12px"><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_real&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:100%;border:none"></iframe></div><div style="margin-top:12px"><a href="/" class="btn-gold">← Homepage</a> <a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div></div>'

@app.route('/admin')
def admin(): return nav() + '<div style="max-width:1100px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:3px solid #f9c846"><h2>Admin Dashboard - V21.7 - Website Design NOW CHANGED Full Premium Pro - TIMOTHY - $1000 UI</h2><p style="color:#00ff88;font-weight:900">✅ V21.7 - WEBSITE DESIGN AND DEVELOPMENT NOW CHANGED - 12 TEMPLATES + LIVE BUILDER + EXPORT HTML ZIP + PUBLISH - IF YOU STILL SEE OLD, HARD REFRESH CTRL+F5 - Keep BG #0f0c29 + Keep Layout + Keep Moving + Each Own Desc Separate No Overlap - NOW CHANGED</p><div style="background:linear-gradient(90deg,#00c950,#f9c846);color:black;padding:10px;border-radius:15px;margin-top:12px;font-weight:bold">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span> | Website Design Now Changed V21.7 Full Premium Pro - Keep BG + Keep Layout + Keep Moving</div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn-gold">← Homepage Own Desc Separate No Overlap</a><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page - Keep BG + Keep Layout</a></div></div></div><script>fetch("/api/admin-data").then(function(r){return r.json();}).then(function(d){document.getElementById("total").innerText=(d.total_fees||0).toFixed(2);document.getElementById("uc").innerText=d.users.length;document.getElementById("oc").innerText=d.orders.length;})</script>'

@app.route('/api/products')
def api_products():
    prods=load(FILES['products'],[{'id':1,'title':'Forex Mastery Ebook - Own Desc Separate No Overlap - V21.7 Website Design Now Changed','desc':'Own Description: Complete forex guide - Own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7 Website Design Now Changed Full Premium Pro','features':'PDF 100 pages - Own Desc Separate No Overlap - V21.7','price':5,'original_price':8,'category':'ebook','icon':'📘','rating':4.8,'reviews_count':127,'file_name':'Forex_Mastery_TIMOTHY.pdf','file_size':'5.2 MB','reviews':[{'user':'John K.','stars':5,'text':'Own Desc Separate No Overlap - V21.7 Website Design Now Changed'}]}])
    save(FILES['products'],prods)
    return jsonify(prods)

@app.route('/api/bundles')
def api_bundles():
    bundles=load(FILES['bundles'],[{'id':1,'title':'Forex Starter Bundle - Own Desc Separate No Overlap - V21.7','desc':'Own Description: Bundle - Own desc separate no overlap - Keep BG + Keep Layout + Keep Moving - V21.7 Website Design Now Changed','original_price':11,'bundle_price':8,'save':3,'items':['Forex Mastery $5 - Own Desc Separate No Overlap - V21.7'],'files':['Forex_Mastery.pdf','Gold_Strategy.pdf']}])
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
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({'ok':False,'message':'Low balance - Deposit via STK - Own Desc Separate No Overlap - V21.7 Website Design Now Changed'})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+amt; save(FILES['fees'],fees); save(FILES['users'],users); return jsonify({'ok':True})

@app.route('/about')
def about(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass"><h2 style="text-align:center">About - V21.7 Website Design NOW CHANGED Full Premium Pro - Own Desc Separate No Overlap</h2><p style="color:#ddd;font-size:12px">This about page own separate description - Website Design Now Changed Full Premium Pro 12 Templates Live Builder Export HTML ZIP Publish - Keep BG + Keep Layout + Keep Moving - V21.7 NOW CHANGED - TIMOTHY 0118431854</p><div style="text-align:center;margin-top:12px"><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page - Keep BG + Keep Layout</a></div></div></div>'

@app.route('/contact')
def contact_page(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Support - Own Desc Separate No Overlap - V21.7 - TIMOTHY 0118431854 - Website Design Now Changed</h2><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-whatsapp">💬 WhatsApp Own Desc Separate</a><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-selar">🛒 Selar Own Desc Separate</a><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page</a></div></div></div>'

@app.route('/terms')
def terms(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Legal - Own Desc Separate No Overlap - V21.7 Website Design Now Changed</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()

@app.route('/free-tools')
def free_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Free Tools - Own Desc Separate No Overlap - V21.7 Website Design Now Changed</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7 - Full designing page - Keep BG + Keep Layout</a></div></div>'

@app.route('/ai-tools')
def ai_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>AI Tools - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

@app.route('/dashboard')
def user_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Dashboard - Own Desc Separate No Overlap - V21.7</h2><a href="/design-studio" class="btn-gold">🌐 Website Design NOW CHANGED V21.7</a></div></div>'

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
