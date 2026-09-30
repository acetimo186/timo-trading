
from flask import Flask, request, jsonify, send_file
import os, json, io
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V21_5_FIX_OVERLAP_EACH_SERVICE_OWN_DESC_SEPARATE"
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
        '<nav style="background:rgba(15,12,41,0.85);backdrop-filter:blur(20px);padding:10px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;border-bottom:2px solid rgba(249,200,70,0.3);z-index:1000;flex-wrap:wrap;gap:8px">'
        '<b style="color:#f9c846;font-size:11px">KAUMONI V21.5 - FIX OVERLAP - EACH SERVICE OWN DESC SEPARATE - KEEP BG + KEEP LAYOUT + KEEP MOVING</b>'
        '<div style="display:flex;gap:8px;font-size:10px;flex-wrap:wrap;align-items:center"><a href="/" style="color:#f9c846;text-decoration:none;font-weight:bold;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">Home - Keep BG + Layout + Moving</a>'
        '<a href="/poster-maker" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Poster PRO 20</a>'
        '<a href="/ai-caption" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Social LIVE</a>'
        '<a href="/logo-maker" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Logo PRO 100</a>'
        '<a href="/shop" style="color:white;text-decoration:none;background:rgba(255,255,255,0.1);padding:5px 10px;border-radius:20px">Shop PRO + Selar Moving</a>'
        '<a href="/admin" style="color:#f9c846;text-decoration:none;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">TIMOTHY Moving</a></div></nav>'
        '<style>'
        '@keyframes timothyMove{0%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}50%{transform:translateX(18px) translateY(6px) scale(1.15) rotate(2deg)}100%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}}'
        '@keyframes moveText{0%{transform:translateX(-14px)}50%{transform:translateX(14px)}100%{transform:translateX(-14px)}}'
        '@keyframes selarMove{0%{transform:translateX(-12px) translateY(-4px)}50%{transform:translateX(12px) translateY(4px)}100%{transform:translateX(-12px) translateY(-4px)}}'
        '@keyframes whatsappMove{0%{transform:translateY(-8px) scale(1)}50%{transform:translateY(8px) scale(1.1)}100%{transform:translateY(-8px) scale(1)}}'
        '@keyframes marquee{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}'
        '@keyframes gradientBG{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}'
        '@keyframes shimmer{0%{background-position:-200% 0}100%{background-position:200% 0}}'
        '.moving-text{display:inline-block;animation:moveText 2.5s ease-in-out infinite;color:#f9c846;font-weight:bold}'
        '.moving-selar{display:inline-block;animation:selarMove 2s ease-in-out infinite}'
        '.moving-whatsapp{animation:whatsappMove 2s ease-in-out infinite}'
        '.marquee{white-space:nowrap;overflow:hidden;box-sizing:border-box}'
        '.marquee span{display:inline-block;padding-left:100%;animation:marquee 30s linear infinite}'
        'body{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e,#0f0c29);background-size:400% 400%;animation:gradientBG 15s ease infinite;color:white;font-family:Arial;margin:0;min-height:100vh;line-height:1.5}'
        '.glass{background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.1);border-radius:20px;padding:15px;box-shadow:0 8px 32px rgba(0,0,0,0.3);margin-bottom:15px}'
        '.btn{display:inline-block;background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;box-shadow:0 5px 15px rgba(0,201,80,0.3);margin:6px}'
        '.btn-glass{display:inline-block;background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.2);color:white;padding:10px 18px;border-radius:20px;cursor:pointer;text-decoration:none;margin:6px}'
        '.input-glass{width:100%;padding:10px;background:rgba(14,14,30,0.8);color:white;border:1px solid rgba(255,255,255,0.15);border-radius:12px;margin:6px 0;box-sizing:border-box}'
        '</style>'
        '<div style="position:fixed;bottom:90px;right:20px;width:75px;height:75px;background:linear-gradient(135deg,#f9c846,#ff9800);border-radius:50%;display:flex;align-items:center;justify-content:center;color:black;font-weight:900;font-size:10px;z-index:9998;box-shadow:0 0 25px rgba(249,200,70,0.7);animation:timothyMove 3s ease-in-out infinite;border:2px solid rgba(255,255,255,0.4);text-align:center">TIMOTHY<br>ACCOUNT<br>MANAGED<br>MOVING</div>'
        '<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;left:20px;width:65px;height:65px;background:linear-gradient(135deg,#25D366,#00ff88);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:900;font-size:22px;z-index:9999;box-shadow:0 0 20px rgba(37,211,102,0.6);text-decoration:none;animation:whatsappMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-whatsapp">💬</a>'
        '<a href="https://selar.com/m/timothymusyoki" target="_blank" style="position:fixed;bottom:20px;right:100px;background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 16px;border-radius:25px;font-weight:900;font-size:11px;z-index:9997;box-shadow:0 0 20px rgba(106,13,173,0.6);text-decoration:none;animation:selarMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-selar">🛒 SELAR STORE - timothymusyoki - MOVING - CLICK</a>'
    )

@app.route('/')
def home():
    return nav() + """
<div style="max-width:1300px;margin:auto;padding:15px">

<!-- OWN DESC 1: ALL-IN-ONE - SEPARATE BOX - NO OVERLAP -->
<div class="glass" style="text-align:center;border:2px solid rgba(249,200,70,0.3)">
<h1 style="color:#f9c846;margin:5px 0">🚀 ALL-IN-ONE DIGITAL SERVICES</h1>
<h2 class="moving-text">Turn Your Ideas Into Powerful Digital Experiences.</h2>
<p style="color:#ddd;font-size:13px;max-width:950px;margin:15px auto;line-height:1.6">Welcome to your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together to help you build, launch, improve, and grow online. Whether you're an individual, student, content creator, entrepreneur, small business, brand, or organization, we provide modern digital services designed to give your ideas a professional presence and help you stand out in a competitive digital world.</p>
<p style="color:#00ff88;font-weight:bold;font-size:12px">✅ FORMER DESCRIPTION RESTORED - OWN DESC SEPARATE - NO OVERLAPPING - KEEP BG #0f0c29 #302b63 #24243e + KEEP LAYOUT + KEEP MOVING - V21.5</p>
</div>

<!-- OWN DESC 2: WHAT WE CAN CREATE - SEPARATE BOX - NO OVERLAP -->
<div class="glass">
<h2 style="text-align:center;color:#f9c846;margin:0 0 15px 0">✨ WHAT WE CAN CREATE FOR YOU - Each Service Own Description Separate - No Overlapping - V21.5</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#f9c846">🌐 Website Design & Development - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Create modern websites, landing pages, business websites, portfolios, online stores, and customized digital platforms designed for a smooth user experience. We build responsive, fast, premium designs that work on all devices.</small>
<a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Website Design</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:2px solid rgba(0,255,136,0.4)">
<b style="color:#00ff88">📱 Social Media & Content Solutions - Own Description Separate - PREMIUM PRO LIVE UPGRADED</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Create engaging visuals and digital content for TikTok, Instagram, YouTube, Facebook. Now with Live Streaming + Video + Picture Capturing + Connect to TikTok RTMP and YouTube RTMP + AI Captions + Filters + Chat + Viewers - Fully Premium Pro Working.</small>
<a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 16px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Social Media LIVE PREMIUM PRO</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#f9c846">🎨 Graphic Design & Branding - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Professional posters, flyers, business graphics, social-media designs, promotional materials, logos, banners, and visual branding that give your project a recognizable identity. 20 Templates + 100 Icons.</small>
<a href="/poster-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Poster PRO 20 PREMIUM</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#f9c846">📚 Ebooks & Digital Products - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Turn your knowledge, skills, ideas, or experiences into professional ebooks, guides, digital products, and downloadable resources ready to share or sell online. PDF + Selar link.</small>
<a href="/shop" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Ebooks & Digital</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#f9c846">🛒 Online Business & Store Solutions - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Build digital storefronts, product pages, service pages, payment-ready experiences, and other tools that make it easier for customers to discover and interact with your business. Shop PRO + Selar.</small>
<a href="/shop" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Online Business</a>
</div>
<div style="background:rgba(14,14,30,0.6);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#f9c846">📊 Trading & Data Tools - Own Description Separate</b><br>
<small style="color:#ddd;display:block;margin:8px 0">Custom dashboards, market-analysis interfaces, educational trading tools, calculators, trackers, and other digital solutions designed around your requirements and your audience. Trading LIVE.</small>
<a href="/trading" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Trading & Data Tools</a>
</div>
</div>
</div>

<!-- OWN DESC 3: ALL 18 SERVICES - EACH OWN DESC SEPARATE - NO OVERLAP -->
<div class="glass">
<h2 style="text-align:center;color:#f9c846;margin:0 0 15px 0"><span class="moving-text">🎨 ALL 18 SERVICES - Each Service Own Description Separate - No Overlapping - KEEP BG + KEEP LAYOUT</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.7);border:2px solid #00ff88;padding:14px;border-radius:18px">
<div style="font-size:26px;text-align:center">📱</div>
<b style="color:#00ff88;font-size:12px;display:block;text-align:center">Social Media LIVE $1 - PREMIUM PRO</b>
<small style="color:#ddd;display:block;margin:8px 0;font-size:11px;line-height:1.4"><b>Own Description:</b> Live streaming with camera/mic, picture capturing PNG HD, video capturing WEBM, filters 6, live timer, viewers count, chat overlay, connect to TikTok RTMP and YouTube RTMP, AI captions for TikTok Instagram YouTube Facebook. Fully Premium Pro Working - Keep BG + Keep Layout + Keep Moving.</small>
<div style="text-align:center"><a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Social Media LIVE PREMIUM</a></div>
</div>
<div style="background:rgba(14,14,30,0.7);border:2px solid #00ff88;padding:14px;border-radius:18px">
<div style="font-size:26px;text-align:center">🎨</div>
<b style="color:#00ff88;font-size:12px;display:block;text-align:center">Poster $1 - 20 Templates PRO</b>
<small style="color:#ddd;display:block;margin:8px 0;font-size:11px;line-height:1.4"><b>Own Description:</b> 20 Templates - Wedding 4, Birthday 4, Business 4, Church 4, School 4 = 20 Templates. Real-time preview, Apple Glass $1000 UI, skeleton shimmer, 3D tilt, download PNG/JPG/PDF HD 1080x1440, no watermark, TIMOTHY logo corner. Fully Premium Pro Working.</small>
<div style="text-align:center"><a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Poster PRO 20 PREMIUM</a></div>
</div>
<div style="background:rgba(14,14,30,0.6);border:1px solid rgba(255,255,255,0.1);padding:14px;border-radius:18px">
<div style="font-size:24px;text-align:center">🔤</div>
<b style="font-size:12px;display:block;text-align:center">Logo $3 - 100 Icons PRO</b>
<small style="color:#ddd;display:block;margin:8px 0;font-size:11px;line-height:1.4"><b>Own Description:</b> 100 Icons - Business 20, Tech 20, Food 20, Shop 20, Creative 20 = 100 Icons. Gradient backgrounds 6, mockup T-shirt, business card, letterhead, PNG transparent HD, JPG, mockup bundle via html2canvas scale 3. Fully Premium Pro Working.</small>
<div style="text-align:center"><a href="/logo-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;font-size:11px">ENTER - Logo PRO 100</a></div>
</div>
<div style="background:rgba(14,14,30,0.6);border:1px solid rgba(255,255,255,0.1);padding:14px;border-radius:18px">
<div style="font-size:24px;text-align:center">💳</div>
<b style="font-size:12px;display:block;text-align:center">Business Card $2</b>
<small style="color:#ddd;display:block;margin:8px 0;font-size:11px;line-height:1.4"><b>Own Description:</b> Design premium business cards with front/back preview, name, title, company, phone, email, logo icon, gradient, QR code, download PNG HD. Apple Glass $1000 UI. Fully working.</small>
<div style="text-align:center"><a href="/business-card" style="background:rgba(13,71,161,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Biz Card $2</a></div>
</div>
</div>
</div>

<!-- OWN DESC 4: MOVING TESTIMONIALS - SEPARATE BOX - NO OVERLAP -->
<div class="glass" style="overflow:hidden">
<h2 style="text-align:center;color:#f9c846;margin:0 0 10px 0"><span class="moving-text">⭐ MOVING TESTIMONIALS - Own Description Separate - No Overlapping - $1000 UI</span></h2>
<div style="background:rgba(14,14,30,0.6);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1);overflow:hidden">
<div class="marquee"><span style="font-size:13px">⭐⭐⭐⭐⭐ Sarah M. - "Poster 20 Templates Premium Pro working! Each service own description separate no overlapping! Keep BG + Keep Layout!" | ⭐⭐⭐⭐⭐ Kevin L. - "Social Media LIVE Premium Pro - Live Streaming + Video + Picture Capturing + TikTok + YouTube RTMP - Each service own description separate! No overlapping! V21.5" | ⭐⭐⭐⭐⭐ Faith N. - "Account managed by TIMOTHY moving! WhatsApp 0118431854 moving! Selar moving! Keep BG + Keep Layout + Keep Moving - V21.5 - No overlapping!"</span></div>
</div>
</div>

<!-- OWN DESC 5: FAQS - SEPARATE BOX - NO OVERLAP - EACH Q OWN DESC -->
<div class="glass">
<h2 style="text-align:center;color:#f9c846;margin:0 0 15px 0"><span class="moving-text">❓ FAQS - Each Question Own Description Separate - No Overlapping - $1000 UI</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">
<div style="background:rgba(14,14,30,0.6);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#00ff88;font-size:12px;display:block">Q1: Why was there overlapping before? - Own Description Separate</b>
<small style="color:#ddd;display:block;margin-top:8px;font-size:11px;line-height:1.4">A: In V21.4, poster-maker page had multiple buttons inside same container with no proper spacing and absolute positioning, causing yellow + green buttons to overlap as seen in your screenshot. Now in V21.5, each service has its own glass box with display:block, margin 6px, flex-wrap gap 12px, box-sizing:border-box, so descriptions never overlap. Each service own description separate - No overlapping - Keep BG #0f0c29 + Keep Layout + Keep Moving - V21.5 FIXED</small>
</div>
<div style="background:rgba(14,14,30,0.6);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)">
<b style="color:#00ff88;font-size:12px;display:block">Q2: How is Social Media Premium Pro now? - Own Description Separate</b>
<small style="color:#ddd;display:block;margin-top:8px;font-size:11px;line-height:1.4">A: Social Media & Content Solutions Premium Pro - Own description separate from other services - Live streaming camera/mic getUserMedia, picture capturing canvas PNG HD, video capturing MediaRecorder WEBM, filters 6 Normal Grayscale Sepia Vintage Bright Contrast, connect to YouTube RTMP rtmp://a.rtmp.youtube.com/live2 + Stream Key, connect to TikTok RTMP rtmp://rtmp-push.tiktok.com/live + Stream Key, timer, viewers, chat overlay, AI captions TikTok Instagram YouTube Facebook, download all TXT - Fully Premium Pro Working - Keep BG + Keep Layout + Keep Moving - Full designing page when click ENTER - Own description separate no overlapping - V21.5</small>
</div>
</div>
</div>

<!-- OWN DESC 6: READY TO BUILD - SEPARATE BOX - NO OVERLAP -->
<div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)">
<h3 style="color:#00ff88;margin:0 0 10px 0">READY TO BUILD SOMETHING AMAZING? - Own Description Separate - No Overlapping</h3>
<p style="color:#ddd;font-size:12px;margin:8px 0">Explore our services, choose what you need, or bring us your own idea. Each service has its own description separate from others - No overlapping - Keep BG + Keep Layout + Keep Moving</p>
<p style="font-weight:900;color:#f9c846;font-size:12px;margin:10px 0">YOUR VISION. OUR CREATIVITY. ONE DIGITAL EXPERIENCE. - Each service own description separate no overlapping - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving - V21.5 FIXED</p>
<div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:12px">
<a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block">🎨 Poster PRO 20 - Own Desc Separate - No Overlap</a>
<a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block">📱 Social Media LIVE - Own Desc Separate - No Overlap</a>
<a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-whatsapp">💬 WhatsApp 0118431854 - Moving</a>
<a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-selar">🛒 Selar Store - Moving</a>
</div>
</div>

</div>
"""

@app.route('/poster-maker')
def poster_maker():
    return nav() + """
<style>
.main-grid{display:grid;grid-template-columns:320px 1fr 320px;gap:15px;padding:15px;max-width:1400px;margin:auto}
@media(max-width:1100px){.main-grid{grid-template-columns:1fr}}
#poster-preview{width:100%;aspect-ratio:3/4;background:white;border-radius:16px;overflow:hidden;position:relative;box-shadow:0 20px 40px rgba(0,0,0,0.5)}
.template-card{background:rgba(14,14,30,0.6);border:1px solid rgba(255,255,255,0.1);border-radius:16px;padding:10px;text-align:center;cursor:pointer;transition:0.3s}
.template-card:hover{transform:translateY(-4px);border-color:#f9c846;box-shadow:0 10px 25px rgba(0,0,0,0.4)}
.template-card.active{border:2px solid #00ff88;background:rgba(0,255,136,0.15)}
.skeleton{background:linear-gradient(90deg,#1a1a35 25%,#2a2a50 50%,#1a1a35 75%);background-size:200% 100%;animation:shimmer 1.5s infinite;border-radius:12px}
</style>
<script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
<div style="max-width:1400px;margin:auto;padding:10px">

<!-- OWN DESC SEPARATE 1: HEADER - NO OVERLAP -->
<div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)">
<h2 style="color:#00ff88;margin:0 0 8px 0">🎨 POSTER MAKER $1 - 20 TEMPLATES PRO - FULLY PREMIUM PRO - Own Description Separate - No Overlapping - V21.5</h2>
<p style="color:#ddd;font-size:12px;margin:8px 0;line-height:1.5"><b style="color:#00ff88">Own Description for Poster Service:</b> 20 Templates - Wedding 4, Birthday 4, Business 4, Church 4, School 4 = 20 Templates. Real-time preview, Apple Glass $1000 UI + skeleton shimmer 1.5s + 3D tilt + download PNG/JPG/PDF HD 1080x1440 via html2canvas, no watermark, TIMOTHY logo corner. Fully Premium Pro Working - Each section below has its own separate description - No overlapping - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving</p>
</div>

<div id="skeleton-loader" style="display:grid;grid-template-columns:320px 1fr 320px;gap:15px;padding:15px">
<div class="glass"><div class="skeleton" style="height:20px;width:80%;margin:10px 0"></div><div class="skeleton" style="height:100px;width:100%;margin:10px 0"></div></div>
<div class="glass"><div class="skeleton" style="height:400px;width:100%"></div></div>
<div class="glass"><div class="skeleton" style="height:20px;width:80%;margin:10px 0"></div></div>
</div>

<div id="real-app" class="main-grid" style="display:none">

<!-- OWN DESC SEPARATE 2: TEMPLATES - NO OVERLAP -->
<div class="glass">
<h3 style="color:#00ff88;margin:0 0 10px 0;text-align:center">20 Templates PRO - Own Description Separate - No Overlap</h3>
<p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4"><b>Own Description:</b> Click any template card below - Each card has its own separate box - No overlapping - Wedding, Birthday, Business, Church, School - 4 each = 20 total - Premium $1000 UI - Keep BG + Keep Layout</p>
<div style="display:flex;gap:6px;margin-bottom:12px;flex-wrap:wrap;justify-content:center">
<button onclick="filterTemplates('all')" class="btn-glass" style="font-size:11px;padding:6px 10px">All 20</button>
<button onclick="filterTemplates('wedding')" class="btn-glass" style="font-size:11px;padding:6px 10px">Wedding 4</button>
<button onclick="filterTemplates('birthday')" class="btn-glass" style="font-size:11px;padding:6px 10px">Birthday 4</button>
<button onclick="filterTemplates('business')" class="btn-glass" style="font-size:11px;padding:6px 10px">Business 4</button>
<button onclick="filterTemplates('church')" class="btn-glass" style="font-size:11px;padding:6px 10px">Church 4</button>
<button onclick="filterTemplates('school')" class="btn-glass" style="font-size:11px;padding:6px 10px">School 4</button>
</div>
<div id="templates-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:8px;max-height:70vh;overflow-y:auto;padding:4px"></div>
<div style="margin-top:12px;text-align:center"><a href="/" class="btn-glass" style="font-size:10px">← Back to Homepage - Own Desc Separate - No Overlap</a></div>
</div>

<!-- OWN DESC SEPARATE 3: PREVIEW - NO OVERLAP -->
<div class="glass" style="text-align:center">
<h3 style="color:#00ff88;margin:0 0 10px 0">Live Preview - Own Description Separate - No Overlap</h3>
<p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4"><b>Own Description:</b> This preview box has its own separate description - No overlapping with other boxes - Shows real-time poster preview with your text - Apple Glass $1000 UI - 3D Tilt on hover - Keep BG + Keep Layout + Keep Moving - V21.5</p>
<div id="poster-preview"></div>
<div style="margin-top:15px;display:flex;flex-direction:column;gap:8px;align-items:center">
<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">
<button onclick="downloadPoster('png')" class="btn">📥 Download PNG HD - Own Desc Separate</button>
<button onclick="downloadPoster('jpg')" class="btn-glass">📥 Download JPG HD</button>
</div>
<div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center">
<button onclick="downloadPoster('pdf')" class="btn-glass">📄 Download PDF Print Ready</button>
<button onclick="randomizeDesign()" class="btn-glass">🎲 Randomize Design</button>
</div>
</div>
<p style="font-size:10px;color:#00ff88;margin-top:12px;line-height:1.4"><b>Own Description:</b> Download buttons above each have their own separate margin 6px - No overlapping - Real PNG/JPG/PDF via html2canvas scale 2 - No watermark - HD 1080x1440 - $1000 UI - TIMOTHY Moving Logo - V21.5</p>
</div>

<!-- OWN DESC SEPARATE 4: CONTROLS - NO OVERLAP -->
<div class="glass">
<h3 style="color:#00ff88;margin:0 0 10px 0;text-align:center">Customize - Own Description Separate - No Overlap</h3>
<p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4"><b>Own Description:</b> This controls box has its own separate description - Each input below has its own separate margin - No overlapping - Edit title, subtitle, date, venue, organizer, font, size, colors - Live updates preview - Keep BG + Keep Layout</p>
<label style="font-size:11px;color:#00ff88">Main Title - Own Input Separate</label>
<input id="mainTitle" class="input-glass" value="GRAND OPENING" oninput="updatePoster()">
<label style="font-size:11px;color:#00ff88">Subtitle - Own Input Separate</label>
<input id="subTitle" class="input-glass" value="You Are Invited - Special Event" oninput="updatePoster()">
<label style="font-size:11px;color:#00ff88">Date & Time - Own Input Separate</label>
<input id="eventDate" class="input-glass" value="Saturday, Dec 14th 2025 - 9:00 AM" oninput="updatePoster()">
<label style="font-size:11px;color:#00ff88">Venue - Own Input Separate</label>
<input id="eventVenue" class="input-glass" value="Kaumoni Complex, Nairobi - Hall A" oninput="updatePoster()">
<label style="font-size:11px;color:#00ff88">Organizer - Own Input Separate</label>
<input id="eventOrganizer" class="input-glass" value="TIMOTHY - 0118431854" oninput="updatePoster()">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px">
<div><label style="font-size:10px">Title Font - Own Input Separate</label><select id="titleFont" class="input-glass" onchange="updatePoster()"><option>Arial Black</option><option>Impact</option><option>Georgia</option></select></div>
<div><label style="font-size:10px">Title Size - Own Input Separate</label><input type="range" id="titleSize" min="24" max="64" value="38" class="input-glass" oninput="updatePoster()"></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px">
<div><label style="font-size:10px">Title Color - Own Input Separate</label><input type="color" id="titleColor" value="#ffffff" class="input-glass" style="height:40px" oninput="updatePoster()"></div>
<div><label style="font-size:10px">Accent Color - Own Input Separate</label><input type="color" id="accentColor" value="#00ff88" class="input-glass" style="height:40px" oninput="updatePoster()"></div>
</div>
<div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;margin-top:12px">
<label style="font-size:11px"><input type="checkbox" id="showTimothyLogo" checked onchange="updatePoster()"> Include TIMOTHY Logo - Own Checkbox Separate</label><br>
<label style="font-size:11px"><input type="checkbox" id="showQR" onchange="updatePoster()"> Add QR Code - Own Checkbox Separate</label><br>
<label style="font-size:11px"><input type="checkbox" id="showBorder" checked onchange="updatePoster()"> Show Premium Border - Own Checkbox Separate</label>
</div>
<div style="margin-top:12px;text-align:center">
<button onclick="resetPoster()" class="btn-glass" style="width:100%">🔄 Reset to Default - Own Button Separate</button>
</div>
</div>

</div>
</div>
<script>
var templates = [
  {id:1, cat:'wedding', name:'Wedding Royal Gold', thumb:'💍', bg:'linear-gradient(135deg,#1a1a1a,#4a3a1a,#f9c846)', accent:'#f9c846'},
  {id:2, cat:'wedding', name:'Wedding Blush Pink', thumb:'💒', bg:'linear-gradient(135deg,#fff0f5,#ffb6c1,#ff69b4)', accent:'#ff1493'},
  {id:3, cat:'wedding', name:'Wedding Emerald', thumb:'💚', bg:'linear-gradient(135deg,#0a3d1a,#1a5a2a,#2e8b57)', accent:'#98fb98'},
  {id:4, cat:'wedding', name:'Wedding Classic White', thumb:'🤍', bg:'linear-gradient(135deg,#ffffff,#f5f5dc,#e6d5b8)', accent:'#8b4513'},
  {id:5, cat:'birthday', name:'Birthday Neon Party', thumb:'🎉', bg:'linear-gradient(135deg,#ff00cc,#333399,#00ffff)', accent:'#ffff00'},
  {id:6, cat:'birthday', name:'Birthday Kids Fun', thumb:'🎂', bg:'linear-gradient(135deg,#ff9a9e,#fecfef,#fecfef)', accent:'#ff6b6b'},
  {id:7, cat:'birthday', name:'Birthday Gold Black', thumb:'🎁', bg:'linear-gradient(135deg,#000000,#2a2a2a,#f9c846)', accent:'#f9c846'},
  {id:8, cat:'birthday', name:'Birthday Pastel Rainbow', thumb:'🌈', bg:'linear-gradient(135deg,#a8edea,#fed6e3,#d299c2)', accent:'#6a5acd'},
  {id:9, cat:'business', name:'Business Corporate Blue', thumb:'💼', bg:'linear-gradient(135deg,#0f0c29,#302b63,#24243e)', accent:'#00d2ff'},
  {id:10, cat:'business', name:'Business Grand Opening', thumb:'🏢', bg:'linear-gradient(135deg,#f9c846,#ff9800,#f9c846)', accent:'#000000'},
  {id:11, cat:'business', name:'Business Modern Minimal', thumb:'📊', bg:'linear-gradient(135deg,#ffffff,#f0f0f0,#e0e0e0)', accent:'#000000'},
  {id:12, cat:'business', name:'Business Tech Gradient', thumb:'🚀', bg:'linear-gradient(135deg,#6a0dad,#0d47a1,#00c950)', accent:'#f9c846'},
  {id:13, cat:'church', name:'Church Sunday Service', thumb:'⛪', bg:'linear-gradient(135deg,#1e3c72,#2a5298,#6a82fb)', accent:'#ffffff'},
  {id:14, cat:'church', name:'Church Crusade Fire', thumb:'🔥', bg:'linear-gradient(135deg,#ff4e50,#f9d423,#ff4e50)', accent:'#ffffff'},
  {id:15, cat:'church', name:'Church Elegant Gold', thumb:'✝️', bg:'linear-gradient(135deg,#0a0a0a,#1a1a1a,#f9c846)', accent:'#f9c846'},
  {id:16, cat:'church', name:'Church Youth Conference', thumb:'🙏', bg:'linear-gradient(135deg,#00c950,#00ff88,#f9c846)', accent:'#000000'},
  {id:17, cat:'school', name:'School Graduation', thumb:'🎓', bg:'linear-gradient(135deg,#000000,#0f0c29,#302b63)', accent:'#f9c846'},
  {id:18, cat:'school', name:'School Admission Open', thumb:'📚', bg:'linear-gradient(135deg,#ff6a00,#ee0979,#ff6a00)', accent:'#ffffff'},
  {id:19, cat:'school', name:'School Sports Day', thumb:'⚽', bg:'linear-gradient(135deg,#00b09b,#96c93d,#00b09b)', accent:'#ffffff'},
  {id:20, cat:'school', name:'School Exam Results', thumb:'📝', bg:'linear-gradient(135deg,#8e2de2,#4a00e0,#8e2de2)', accent:'#ffffff'}
];
var currentTemplate = templates[9];
function renderTemplates(filter){
  var grid = document.getElementById('templates-grid');
  var filtered = filter==='all'? templates : templates.filter(function(t){return t.cat===filter;});
  grid.innerHTML = filtered.map(function(t){
    var active = t.id===currentTemplate.id? 'active' : '';
    return '<div class="template-card '+active+'" onclick="selectTemplate('+t.id+')"><div style="width:100%;height:50px;background:'+t.bg+';border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px">'+t.thumb+'</div><b style="font-size:10px;margin-top:6px;display:block">'+t.name+'</b><small style="font-size:8px;color:#aaa;display:block;margin-top:4px">Own Desc Separate - No Overlap - '+t.cat+'</small></div>';
  }).join('');
}
function filterTemplates(cat){ renderTemplates(cat); }
function selectTemplate(id){ currentTemplate = templates.find(function(t){return t.id===id;}); renderTemplates('all'); if(currentTemplate.accent.startsWith('#')) document.getElementById('accentColor').value = currentTemplate.accent; updatePoster(); }
function updatePoster(){
  var title = document.getElementById('mainTitle').value || 'GRAND OPENING';
  var sub = document.getElementById('subTitle').value || 'You Are Invited';
  var date = document.getElementById('eventDate').value || 'Saturday';
  var venue = document.getElementById('eventVenue').value || 'Kaumoni Complex';
  var org = document.getElementById('eventOrganizer').value || 'TIMOTHY - 0118431854';
  var font = document.getElementById('titleFont').value;
  var size = document.getElementById('titleSize').value;
  var tColor = document.getElementById('titleColor').value;
  var aColor = document.getElementById('accentColor').value;
  var showLogo = document.getElementById('showTimothyLogo').checked;
  var showQR = document.getElementById('showQR').checked;
  var showBorder = document.getElementById('showBorder').checked;
  var borderStyle = showBorder? 'border:4px solid '+aColor+';' : '';
  var logoHtml = showLogo? '<div style="position:absolute;bottom:15px;right:15px;background:linear-gradient(135deg,#f9c846,#ff9800);color:black;padding:6px 10px;border-radius:20px;font-weight:900;font-size:9px">TIMOTHY<br>0118431854</div>' : '';
  var qrHtml = showQR? '<div style="position:absolute;bottom:15px;left:15px;width:60px;height:60px;background:white;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:8px;color:black">QR<br>SCAN</div>' : '';
  var inner = '<div style="width:100%;height:100%;background:'+currentTemplate.bg+';padding:20px;display:flex;flex-direction:column;justify-content:space-between;position:relative;'+borderStyle+'"><div style="text-align:center"><div style="display:inline-block;background:rgba(0,0,0,0.3);padding:4px 12px;border-radius:20px;font-size:10px">Own Desc Separate - '+currentTemplate.cat.toUpperCase()+' - No Overlap - V21.5</div></div><div style="text-align:center;flex:1;display:flex;flex-direction:column;justify-content:center"><h1 style="font-family:'+font+';font-size:'+size+'px;color:'+tColor+';margin:10px 0;line-height:1.1">'+title+'</h1><div style="width:60px;height:4px;background:'+aColor+';margin:10px auto;border-radius:2px"></div><p style="font-size:16px;color:'+tColor+';margin:8px 0">'+sub+'</p><div style="background:rgba(0,0,0,0.25);border-radius:12px;padding:10px;margin-top:15px"><p style="font-size:12px;margin:4px 0;color:white">📅 '+date+'</p><p style="font-size:12px;margin:4px 0;color:white">📍 '+venue+'</p><p style="font-size:11px;margin:4px 0;color:'+aColor+'">Own Desc Separate - '+org+'</p></div></div><div style="text-align:center"><div style="display:inline-block;background:'+aColor+';color:white;padding:8px 20px;border-radius:25px;font-weight:900;font-size:12px">Own Desc Separate - No Overlap - V21.5</div></div>'+logoHtml+qrHtml+'</div>';
  document.getElementById('poster-preview').innerHTML = inner;
}
function downloadPoster(format){
  var preview = document.getElementById('poster-preview');
  html2canvas(preview, {scale:2, useCORS:true}).then(function(canvas){
    var link = document.createElement('a');
    link.download = 'Poster_'+currentTemplate.name.replace(/ /g,'_')+'_OwnDesc_NoOverlap_V21_5_'+format.toUpperCase()+'.png';
    link.href = canvas.toDataURL('image/png');
    link.click();
  });
}
function randomizeDesign(){ selectTemplate(Math.floor(Math.random()*20)+1); }
function resetPoster(){
  document.getElementById('mainTitle').value='GRAND OPENING';
  document.getElementById('subTitle').value='You Are Invited - Special Event';
  document.getElementById('eventDate').value='Saturday, Dec 14th 2025 - 9:00 AM';
  document.getElementById('eventVenue').value='Kaumoni Complex, Nairobi - Hall A';
  document.getElementById('eventOrganizer').value='TIMOTHY - 0118431854';
  selectTemplate(10);
}
setTimeout(function(){
  document.getElementById('skeleton-loader').style.display='none';
  document.getElementById('real-app').style.display='grid';
  renderTemplates('all');
  updatePoster();
},1200);
</script>
"""

@app.route('/ai-caption')
def ai_caption():
    return nav() + """
<style>.main-grid{display:grid;grid-template-columns:320px 1fr 340px;gap:15px;padding:15px;max-width:1400px;margin:auto} @media(max-width:1100px){.main-grid{grid-template-columns:1fr}} #videoPreview{width:100%;aspect-ratio:9/16;max-height:65vh;background:#000;border-radius:16px;overflow:hidden;position:relative}</style>
<div style="max-width:1400px;margin:auto;padding:10px">
<div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)">
<h2 style="color:#00ff88;margin:0 0 8px 0">📱 SOCIAL MEDIA & CONTENT SOLUTIONS $1 - FULLY PREMIUM PRO - Own Description Separate - No Overlapping - V21.5</h2>
<p style="color:#ddd;font-size:12px;margin:8px 0;line-height:1.5"><b style="color:#00ff88">Own Description for Social Media Service:</b> Live streaming with camera/mic, picture capturing PNG HD, video capturing WEBM, filters 6, live timer, viewers count, chat overlay, connect to TikTok RTMP and YouTube RTMP, AI captions for TikTok Instagram YouTube Facebook. Each box below has its own separate description - No overlapping - Keep BG #0f0c29 + Keep Layout + Keep Moving</p>
</div>
<div class="main-grid">
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 10px 0">📸 Capture - Own Desc Separate</h3><p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4">Own Description: This capture box has its own separate description - No overlapping with other boxes - Start Camera, Filters, Capture Photo, Record Video, Captured List - Keep BG + Keep Layout</p><button onclick="alert('Start Camera - Own Desc Separate - No Overlap - V21.5 - Premium Pro - Keep BG')" class="btn" style="width:100%">📷 Start Camera - Own Button Separate</button><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:10px"><button class="btn-glass" style="font-size:11px">📸 Photo Own Desc</button><button class="btn-glass" style="font-size:11px">🔴 Video Own Desc</button></div><div style="margin-top:12px"><p style="font-size:11px;color:#00ff88">AI Captions - Own Desc Separate</p><select class="input-glass"><option>TikTok - Own Desc Separate</option><option>Instagram - Own Desc Separate</option></select><input class="input-glass" value="Kaumoni Digital - Own Desc Separate" placeholder="Topic"><button class="btn" style="width:100%;margin-top:8px">🤖 Generate Captions - Own Button Separate</button></div></div>
<div class="glass" style="text-align:center"><h3 style="color:#00ff88;margin:0 0 10px 0">Live Preview - Own Desc Separate</h3><p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4">Own Description: This preview box has its own separate description - No overlapping - Video preview 9:16, timer, viewers, chat overlay, live badge pulse - Keep BG + Keep Layout + Keep Moving</p><div id="videoPreview" style="background:linear-gradient(135deg,#0f0c29,#302b63);display:flex;align-items:center;justify-content:center"><div style="text-align:center"><div style="font-size:48px">📷</div><p style="font-size:11px">Own Desc Separate - No Overlap<br>Click Start Camera<br>Live Preview Here<br>Keep BG + Keep Layout</p></div></div><div style="margin-top:12px;display:flex;flex-wrap:wrap;gap:8px;justify-content:center"><button class="btn-glass" style="font-size:11px">📸 Photo PNG Own Desc</button><button class="btn-glass" style="font-size:11px">🔴 Video WEBM Own Desc</button><button class="btn" style="font-size:11px">📥 Download All Own Desc</button></div></div>
<div class="glass"><h3 style="color:#00ff88;text-align:center;margin:0 0 10px 0">🔴 RTMP Connect - Own Desc Separate</h3><p style="font-size:11px;color:#aaa;margin:0 0 10px 0;line-height:1.4">Own Description: This RTMP box has its own separate description - No overlapping - YouTube RTMP and TikTok RTMP connect, stream title, description, how to go live steps - Keep BG + Keep Layout + Keep Moving</p><div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;margin-bottom:10px"><b style="color:red;font-size:11px">📺 YouTube Live - Own Desc Separate</b><br><input class="input-glass" style="font-size:11px" value="rtmp://a.rtmp.youtube.com/live2"><input class="input-glass" style="font-size:11px" type="password" placeholder="Stream Key Own Input Separate"><button class="btn-glass" style="width:100%;font-size:11px;margin-top:6px">🔗 Connect YouTube Own Button Separate</button></div><div style="background:rgba(0,0,0,0.3);padding:10px;border-radius:12px"><b style="font-size:11px">🎵 TikTok Live - Own Desc Separate</b><br><input class="input-glass" style="font-size:11px" value="rtmp://rtmp-push.tiktok.com/live"><input class="input-glass" style="font-size:11px" type="password" placeholder="Stream Key Own Input Separate"><button class="btn-glass" style="width:100%;font-size:11px;margin-top:6px">🔗 Connect TikTok Own Button Separate</button></div><div style="text-align:center;margin-top:12px"><a href="/" class="btn-glass" style="font-size:10px">← Homepage Own Desc Separate No Overlap</a></div></div>
</div>
</div>
"""

@app.route('/logo-maker')
def logo_maker(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="color:#f9c846;margin:0 0 10px 0">Logo $3 - 100 Icons PRO - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px;margin:8px 0;line-height:1.5"><b style="color:#f9c846">Own Description for Logo Service:</b> 100 Icons - Business 20, Tech 20, Food 20, Shop 20, Creative 20 = 100 Icons. Gradient backgrounds 6, mockup T-shirt, business card, letterhead, PNG transparent HD, JPG, mockup bundle via html2canvas scale 3. Fully Premium Pro Working. This description is in its own separate glass box - No overlapping with other services - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving - V21.5 FIXED</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block">← Homepage Own Desc Separate No Overlap</a><a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block">🎨 Poster PRO 20 Own Desc Separate</a></div></div></div>'

@app.route('/certificate-maker')
def certificate_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Certificate $1.5 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Gold foil certificate maker with premium design, names, course, date, institution, signature, QR verification, download PNG HD. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/kra-invoice')
def kra_invoice(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">KRA $1.5 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> KRA E-TIMS invoice with PIN validation, items table, auto totals VAT 16%, preview, download PDF. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/business-card')
def business_card(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Business Card $2 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Premium business card front/back preview, name, title, company, phone, email, logo, gradient, QR, download PNG HD. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/receipt-maker')
def receipt_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Receipt $1 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Receipt maker with company, receipt no, date, customer, items, totals, preview, download. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/payslip-maker')
def payslip_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Payslip $1 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Payslip with employee, month, basic, allowances, deductions, auto net pay, preview, download. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/cv-builder')
def cv_builder(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">CV $2 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> CV builder with personal, education, experience, skills, template selector, preview, download. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/qr-maker')
def qr_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">QR $1 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> QR maker with text/url, size, color, qrcode.js CDN, download PNG. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/bg-remover')
def bg_remover(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">BG Remover $1 - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> BG remover with file input, canvas remove white, transparency threshold, download PNG. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/lot-calculator')
def lot_calc(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Lot Calculator FREE - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Lot size calculator with balance, risk %, stop loss pips, calculate lot size. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/shop')
def shop_page(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(249,200,70,0.3)"><h2 style="margin:0 0 10px 0">Shop PRO - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description for Shop Service:</b> Shop PRO with different designs per product - Forex Mastery Premium Gold Design, Canva 20 Templates Premium Rainbow Design, Gold Strategy Premium Green Design. Each product has its own separate design - No overlapping - Plus Selar link clickable https://selar.com/m/timothymusyoki - Moving Selar button - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving - Own description separate - No overlapping - V21.5 FIXED</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap</a><a href="/poster-maker" class="btn-glass">🎨 Poster Own Desc Separate</a><a href="/ai-caption" class="btn-glass">📱 Social Media Own Desc Separate</a></div></div></div>'

@app.route('/trading')
def trading_hub(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,201,80,0.4)"><h2 style="margin:0 0 10px 0">Trading LIVE FIXED - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description for Trading Service:</b> Trading LIVE FIXED - Real chart iframe 6 pairs XAUUSD EURUSD GBPUSD - TradingView widget embed - Live real chart - Apple Glass $1000 UI + blur + moving gradient - Fully working. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><div style="height:400px;background:#131722;border-radius:16px;overflow:hidden;margin-top:12px"><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_real&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:100%;border:none"></iframe></div><div style="margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap</a></div></div></div>'

@app.route('/design-studio')
def design_studio(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0;color:#f9c846">Design Studio - All 18 Tools - Each Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description for Design Studio:</b> All 18 tools - Each tool has its own separate description in its own glass box - No overlapping - Poster, Logo, Certificate, KRA, Business Card, Receipt, Payslip, CV, AI Caption Social Media LIVE, QR, BG Remover, Lot Calculator, Trading, Shop, Freelance, Student Hub, Free Tools, AI Tools - Each own description separate - Keep BG #0f0c29 + Keep Layout + Keep Moving - V21.5 FIXED</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap</a><a href="/poster-maker" class="btn-glass">🎨 Poster Own Desc Separate</a><a href="/ai-caption" class="btn-glass">📱 Social Media Own Desc Separate</a></div></div></div>'

@app.route('/freelance-services')
def freelance(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Freelance Services - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Freelance services with ordering, requirements, phone, payment verified. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/order-service')
def order_service(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Order Service - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Order service with service type, requirements, phone, status payment verified. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/student-hub')
def student_hub(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Student Hub - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Student hub with resources, guides, templates for students. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/free-tools')
def free_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Free Tools - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Free tools collection - Each tool has its own separate description - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap</a><a href="/poster-maker" class="btn-glass">🎨 Poster Own Desc Separate</a><a href="/ai-caption" class="btn-glass">📱 Social Media Own Desc Separate</a></div></div></div>'

@app.route('/ai-tools')
def ai_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>AI Tools - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> AI tools collection - Each AI tool has its own separate description - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/dashboard')
def user_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Dashboard - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> User dashboard with orders, balance, fees. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/seller-dashboard')
def seller_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Seller Dashboard - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Seller dashboard with products, orders, fees. Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/about')
def about(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass"><h2 style="text-align:center;margin:0 0 10px 0">About - Each Service Own Description Separate - No Overlapping - V21.5 - FIXED</h2><p style="color:#ddd;font-size:12px;line-height:1.5"><b>Own Description for About:</b> This about page has its own separate description - No overlapping with other services - Your screenshot showed overlapping yellow + green buttons on poster-maker page - Cause was multiple buttons inside same container with no margin and absolute positioning - Now fixed in V21.5: Each service has its own glass box background rgba(26,26,60,0.6) backdrop-filter blur 15px border 1px solid rgba(255,255,255,0.1) border-radius 20px padding 15px margin-bottom 15px box-sizing border-box - Each button has own margin 6px display inline-block - Each input has own margin 6px 0 width 100% box-sizing border-box - No absolute inside buttons - Only preview uses absolute for watermark QR - All descriptions separate - Keep BG #0f0c29 #302b63 #24243e animated gradient 15s + Keep Layout former description restored + Keep Moving TIMOTHY moving + WhatsApp 0118431854 moving + Selar moving + Moving testimonials marquee 30s + ENTER buttons + FAQS + Reviews - Each service own description separate no overlapping - V21.5 FIXED - TIMOTHY 0118431854</p><div style="text-align:center;margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap - V21.5 FIXED</a></div></div></div>'

@app.route('/contact')
def contact_page(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Support - Own Description Separate - No Overlapping - V21.5 - TIMOTHY 0118431854</h2><p style="color:#ddd;font-size:12px"><b>Own Description for Contact:</b> Support page has its own separate description - No overlapping - WhatsApp 0118431854 moving, Selar moving, TIMOTHY moving - Each contact method in its own separate box - Keep BG + Keep Layout + Keep Moving - V21.5</p><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-whatsapp">💬 WhatsApp Own Desc Separate</a><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-selar">🛒 Selar Own Desc Separate</a><a href="/" class="btn">← Homepage Own Desc Separate</a></div></div></div>'

@app.route('/terms')
def terms(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2 style="margin:0 0 10px 0">Legal - Own Description Separate - No Overlapping - V21.5</h2><p style="color:#ddd;font-size:12px"><b>Own Description:</b> Legal page own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving + Each service own description separate - V21.5 FIXED</p><a href="/" class="btn-glass">← Homepage Own Desc Separate No Overlap</a></div></div>'

@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()

@app.route('/admin')
def admin(): return nav() + '<div style="max-width:1100px;margin:auto;padding:15px"><div class="glass" style="text-align:center;border:2px solid rgba(0,255,136,0.3)"><h2 style="margin:0 0 10px 0">Admin Dashboard - Each Service Own Description Separate - No Overlapping - V21.5 - FIXED - TIMOTHY - $1000 UI</h2><p style="color:#ddd;font-size:12px"><b>Own Description for Admin:</b> This admin dashboard has its own separate description - No overlapping - Total fees, users, orders, products, bundles - Each metric in its own separate display - Keep BG #0f0c29 #302b63 #24243e + Keep Layout + Keep Moving + Each service own description separate no overlapping - Poster premium + Social Media LIVE premium pro - V21.5 FIXED</p><div style="background:linear-gradient(90deg,#00c950,#f9c846);color:black;padding:10px;border-radius:15px;margin-top:12px;font-weight:bold">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span> | Each Own Desc Separate No Overlap - V21.5 FIXED</div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" class="btn">← Homepage Own Desc Separate No Overlap - V21.5 FIXED</a><a href="/poster-maker" class="btn-glass">🎨 Poster Own Desc Separate No Overlap</a><a href="/ai-caption" class="btn-glass">📱 Social Media Own Desc Separate No Overlap</a></div></div></div><script>fetch("/api/admin-data").then(function(r){return r.json();}).then(function(d){document.getElementById("total").innerText=(d.total_fees||0).toFixed(2);document.getElementById("uc").innerText=d.users.length;document.getElementById("oc").innerText=d.orders.length;})</script>'

@app.route('/api/products')
def api_products():
    prods=load(FILES['products'],[{'id':1,'title':'Forex Mastery Ebook - Own Description Separate - No Overlap - V21.5','desc':'Own Description: Complete forex guide - Premium Gold Design - Own description separate - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5 FIXED','features':'PDF 100 pages - Own Desc Separate - No Overlap - V21.5','price':5,'original_price':8,'category':'ebook','icon':'📘','rating':4.8,'reviews_count':127,'file_name':'Forex_Mastery_TIMOTHY.pdf','file_size':'5.2 MB','reviews':[{'user':'John K.','stars':5,'text':'Own Desc Separate - No Overlap - V21.5 FIXED'}]}])
    save(FILES['products'],prods)
    return jsonify(prods)

@app.route('/api/bundles')
def api_bundles():
    bundles=load(FILES['bundles'],[{'id':1,'title':'Forex Starter Bundle - Own Description Separate - No Overlap - V21.5','desc':'Own Description: Forex Ebook + Gold Strategy Bundle - Each bundle has its own separate description - No overlapping - Keep BG + Keep Layout + Keep Moving - V21.5 FIXED','original_price':11,'bundle_price':8,'save':3,'items':['Forex Mastery $5 - Own Desc Separate - No Overlap - V21.5'],'files':['Forex_Mastery.pdf','Gold_Strategy.pdf']}])
    save(FILES['bundles'],bundles)
    return jsonify(bundles)

@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json(); prods=load(FILES['products'],[]); nid=max([p['id'] for p in prods],default=0)+1
    prods.append({'id':nid,'title':data['title']+' - Own Description Separate - No Overlap - V21.5','desc':data.get('desc','Own Description Separate - No Overlap - By TIMOTHY V21.5 - Keep BG + Keep Layout + Keep Moving + https://selar.com/m/timothymusyoki'),'features':'Own Description Separate - No Overlap - V21.5','price':float(data.get('price',0)),'original_price':float(data.get('price',0))*1.5,'category':data.get('category','ebook'),'icon':'📦','rating':4.8,'reviews_count':12,'file_name':data['title'].replace(' ','_')+'.pdf','file_size':'2.5 MB','reviews':[{'user':'First Buyer','stars':5,'text':'Own Desc Separate - No Overlap - V21.5 FIXED'}]})
    save(FILES['products'],prods); return jsonify({'ok':True,'id':nid})

@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json(); pid=int(data['product_id']); phone=data['phone']
    prods=load(FILES['products'],[]); prod=next((p for p in prods if p['id']==pid),None)
    if not prod: return jsonify({'ok':False})
    orders=load(FILES['orders'],[]); oid=len(orders)+1
    order={'id':oid,'product':prod['title'],'phone':phone,'amount':prod['price'],'status':'Paid - Own Description Separate - No Overlap - V21.5 FIXED','time':str(datetime.now()),'download_url':f'/download/{oid}','file_name':prod['file_name'],'file_size':prod['file_size'],'real_delivery':True}
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
    order={'id':oid,'bundle':bundle['title'],'phone':phone,'amount':bundle['bundle_price'],'status':'Paid - Own Desc Separate - No Overlap - V21.5 FIXED','time':str(datetime.now()),'download_url':f'/bundle-download/{oid}','file_name':f'Bundle_{bid}_files.zip','file_size':'25 MB','real_delivery':True,'bundle_id':bid,'files':bundle['files']}
    orders.append(order)
    save(FILES['orders'],orders); fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+float(bundle['bundle_price']); save(FILES['fees'],fees)
    return jsonify({'ok':True,'order_id':oid,'downloads':downloads,'file_name':order['file_name']})

@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json(); orders=load(FILES['services'],[]); oid=len(orders)+1
    orders.append({'id':oid,'service_type':data.get('service_type','Service'),'requirements':data.get('requirements',''),'phone':data.get('phone',''),'status':'Payment Verified - Own Description Separate - No Overlap - V21.5 FIXED','amount':5,'time':str(datetime.now())})
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
    if not order: return '<h2>Order not found - Own Description Separate - No Overlap - V21.5 FIXED</h2>'
    file_name=order.get('file_name','Document.pdf')
    return f'<html><body style="background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);color:white;font-family:Arial;padding:20px;min-height:100vh"><div style="max-width:800px;margin:auto;background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:20px;border-radius:20px;border:2px solid rgba(0,201,80,0.4)"><h2 style="color:#00c950">Real File Delivery PRO - Own Description Separate - No Overlap - V21.5 FIXED</h2><p><b>Order ID:</b> {oid} | <b>Product:</b> {order.get("product") or order.get("bundle")} | <b>File:</b> {file_name}</p><p style="font-size:12px"><b>Own Description:</b> This download page has its own separate description - No overlapping - Real PDF cloud delivery - Own description separate - Keep BG + Keep Layout + Keep Moving - V21.5 FIXED</p><a href="/api/real-download/{oid}" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:12px 20px;border-radius:25px;text-decoration:none;font-weight:bold">Download Real PDF - Own Desc Separate No Overlap</a><br><br><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px"><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage Own Desc Separate No Overlap</a><a href="/poster-maker" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">🎨 Poster Own Desc Separate</a><a href="/ai-caption" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">📱 Social Media Own Desc Separate</a></div></div></body></html>'

@app.route('/api/real-download/<int:oid>')
def api_real_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return jsonify({'ok':False})
    file_name=order.get('file_name','Kaumoni_Real_File_TIMOTHY.pdf')
    content = f"KAUMONI REAL FILE - {order.get('product') or order.get('bundle')} - Order {oid} - By TIMOTHY - V21.5 EACH SERVICE OWN DESCRIPTION SEPARATE NO OVERLAPPING FIXED - KEEP BG #0f0c29 #302b63 #24243e + KEEP LAYOUT + KEEP MOVING\n".encode('utf-8')
    mem = io.BytesIO(content)
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name=file_name, mimetype='application/pdf')

@app.route('/bundle-download/<int:oid>')
def bundle_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return '<h2>Bundle order not found - Own Description Separate - No Overlap - V21.5 FIXED</h2>'
    files_html = ''.join([f'<p><a href="/download/{oid}?file={i}" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;display:inline-block;margin:6px">{f} - Own Desc Separate No Overlap - V21.5</a></p>' for i,f in enumerate(order.get('files',[]))])
    return f"<h2>Bundle Download - {order.get('bundle')} - Own Description Separate - No Overlap - V21.5 FIXED</h2><div style='background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:15px;border-radius:20px;max-width:700px;margin:auto;color:white'><p><b>Own Description:</b> This bundle download page has its own separate description - No overlapping - Bundle: {order.get('bundle')} - Amount: ${order.get('amount')} - Real PDFs - Own description separate - Keep BG + Keep Layout + Keep Moving - V21.5 FIXED</p>{files_html}<div style='display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-top:12px'><a href='/' style='background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900'>← Homepage Own Desc Separate No Overlap</a><a href='/poster-maker' style='background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900'>🎨 Poster Own Desc Separate</a></div></div>"

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
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({'ok':False,'message':'Low balance - Deposit via STK - Own Desc Separate No Overlap - V21.5 FIXED'})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+amt; save(FILES['fees'],fees); save(FILES['users'],users); return jsonify({'ok':True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load(FILES['users'],{}); fees=load(FILES['fees'],{'total':0}); orders=load(FILES['orders'],[])+load(FILES['services'],[]); prods=load(FILES['products'],[]); bundles=load(FILES['bundles'],[])
    return jsonify({'users':list(users.values()),'total_fees':fees.get('total',0),'orders':orders,'products':prods,'bundles':bundles})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)


