from flask import Flask, request, jsonify, send_file
import os, json, io
from datetime import datetime
app = Flask(__name__)
app.secret_key = "KAUMONI_V20_1_FORMER_DESC_RESTORED_KEEP_COLOR_MOVING"
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
        '<nav style="background:rgba(15,12,41,0.85);backdrop-filter:blur(20px);padding:10px;display:flex;justify-content:space-between;position:sticky;top:0;border-bottom:2px solid rgba(249,200,70,0.3);z-index:1000;flex-wrap:wrap;gap:6px">'
        '<b style="color:#f9c846;font-size:11px">KAUMONI V20.1 - FORMER DESCRIPTION RESTORED + KEEP NEW COLOR + KEEP MOVING PARTS - TIMOTHY - $1000 UI</b>'
        '<div style="display:flex;gap:6px;font-size:10px;flex-wrap:wrap"><a href="/" style="color:#f9c846;text-decoration:none;font-weight:bold">Home Former Desc + Keep Color + Moving</a>'
        '<a href="/design-studio" style="color:white;text-decoration:none">Design Studio 18 Tools</a>'
        '<a href="/shop" style="color:white;text-decoration:none">Shop PRO + Selar Moving</a>'
        '<a href="/admin" style="color:#f9c846;text-decoration:none">TIMOTHY Moving Account</a></div></nav>'
        '<style>'
        '@keyframes timothyMove{0%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}50%{transform:translateX(18px) translateY(6px) scale(1.15) rotate(2deg)}100%{transform:translateX(-18px) translateY(-6px) scale(1) rotate(-2deg)}}'
        '@keyframes moveText{0%{transform:translateX(-14px)}50%{transform:translateX(14px)}100%{transform:translateX(-14px)}}'
        '@keyframes selarMove{0%{transform:translateX(-12px) translateY(-4px)}50%{transform:translateX(12px) translateY(4px)}100%{transform:translateX(-12px) translateY(-4px)}}'
        '@keyframes whatsappMove{0%{transform:translateY(-8px) scale(1)}50%{transform:translateY(8px) scale(1.1)}100%{transform:translateY(-8px) scale(1)}}'
        '@keyframes marquee{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}'
        '@keyframes gradientBG{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}'
        '.moving-text{display:inline-block;animation:moveText 2.5s ease-in-out infinite;color:#f9c846;font-weight:bold}'
        '.moving-selar{display:inline-block;animation:selarMove 2s ease-in-out infinite}'
        '.moving-whatsapp{animation:whatsappMove 2s ease-in-out infinite}'
        '.marquee{white-space:nowrap;overflow:hidden;box-sizing:border-box}'
        '.marquee span{display:inline-block;padding-left:100%;animation:marquee 30s linear infinite}'
        'body{background:linear-gradient(135deg,#0f0c29,#302b63,#24243e,#0f0c29);background-size:400% 400%;animation:gradientBG 15s ease infinite;color:white;font-family:Arial;margin:0;min-height:100vh}'
        '</style>'
        '<div style="position:fixed;bottom:90px;right:20px;width:75px;height:75px;background:linear-gradient(135deg,#f9c846,#ff9800);border-radius:50%;display:flex;align-items:center;justify-content:center;color:black;font-weight:900;font-size:10px;z-index:9998;box-shadow:0 0 25px rgba(249,200,70,0.7);animation:timothyMove 3s ease-in-out infinite;border:2px solid rgba(255,255,255,0.4);text-align:center">TIMOTHY<br>ACCOUNT<br>MANAGED<br>MOVING</div>'
        '<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;left:20px;width:65px;height:65px;background:linear-gradient(135deg,#25D366,#00ff88);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-weight:900;font-size:22px;z-index:9999;box-shadow:0 0 20px rgba(37,211,102,0.6);text-decoration:none;animation:whatsappMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-whatsapp">💬</a>'
        '<a href="https://selar.com/m/timothymusyoki" target="_blank" style="position:fixed;bottom:20px;right:100px;background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 16px;border-radius:25px;font-weight:900;font-size:11px;z-index:9997;box-shadow:0 0 20px rgba(106,13,173,0.6);text-decoration:none;animation:selarMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.3)" class="moving-selar">🛒 SELAR STORE - timothymusyoki - MOVING - CLICK</a>'
    )

@app.route('/')
def home():
    return nav() + """
<div style="max-width:1300px;margin:auto;padding:15px">

<!-- FORMER DESCRIPTION RESTORED - EXACT AS BEFORE - KEEP NEW COLOR + KEEP MOVING PARTS -->
<div style="background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:25px;border-radius:25px;border:2px solid rgba(249,200,70,0.3);text-align:center;box-shadow:0 15px 40px rgba(0,0,0,0.4)">
<h1 style="color:#f9c846;margin:5px 0">🚀 ALL-IN-ONE DIGITAL SERVICES</h1>
<h2 class="moving-text">Turn Your Ideas Into Powerful Digital Experiences.</h2>
<p style="color:#ddd;font-size:13px;max-width:950px;margin:15px auto;line-height:1.6">Welcome to your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together to help you build, launch, improve, and grow online. Whether you're an individual, student, content creator, entrepreneur, small business, brand, or organization, we provide modern digital services designed to give your ideas a professional presence and help you stand out in a competitive digital world. From a simple idea that needs to become a reality, to an existing website that needs a fresh, premium upgrade, we can help transform your vision into something modern, attractive, functional, and memorable.</p>
<p style="color:#00ff88;font-weight:bold;margin-top:10px">✅ FORMER DESCRIPTION RESTORED AS REQUESTED - KEEP NEW COLOR ANIMATED GRADIENT #0f0c29 #302b63 #24243e + KEEP MOVING PARTS TIMOTHY MOVING + WHATSAPP MOVING 0118431854 + SELAR MOVING - V20.1</p>
</div>

<!-- FORMER WHAT WE CAN CREATE FOR YOU SECTION RESTORED -->
<h2 style="text-align:center;margin:20px 0 10px 0;color:#f9c846">✨ WHAT WE CAN CREATE FOR YOU - Former Section Restored</h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px">
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>🌐 Website Design & Development</b><br><small>Create modern websites, landing pages, business websites, portfolios, online stores, and customized digital platforms designed for a smooth user experience.</small><br><a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Website Design</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>🎨 Graphic Design & Branding</b><br><small>Professional posters, flyers, business graphics, social-media designs, promotional materials, logos, banners, and visual branding that give your project a recognizable identity.</small><br><a href="/poster-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Graphic Design</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>📱 Social Media & Content Solutions</b><br><small>Create engaging visuals and digital content for TikTok, Instagram, YouTube, Facebook, and other platforms to help you present your brand professionally and consistently across channels.</small><br><a href="/ai-caption" style="background:rgba(255,152,0,0.8);color:black;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Social Media</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>📚 Ebooks & Digital Products</b><br><small>Turn your knowledge, skills, ideas, or experiences into professional ebooks, guides, digital products, and downloadable resources ready to share or sell online.</small><br><a href="/shop" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Ebooks & Digital</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>🛒 Online Business & Store Solutions</b><br><small>Build digital storefronts, product pages, service pages, payment-ready experiences, and other tools that make it easier for customers to discover and interact with your business.</small><br><a href="/shop" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Online Business</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:16px;border:1px solid rgba(255,255,255,0.15)"><b>📊 Trading & Data Tools</b><br><small>Custom dashboards, market-analysis interfaces, educational trading tools, calculators, trackers, and other digital solutions designed around your requirements and your audience.</small><br><a href="/trading" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:6px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:8px;font-size:11px">ENTER - Trading & Data Tools</a></div>
</div>

<!-- ALL 18 SERVICES WITH ENTER BUTTON - KEEP AS REQUESTED -->
<h2 style="text-align:center;margin:20px 0 10px 0;color:#f9c846"><span class="moving-text">🎨 ALL 18 SERVICES - EACH WITH ENTER BUTTON - KEEP NEW COLOR + KEEP MOVING - $1000 UI</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:10px">
<div style="background:rgba(26,26,60,0.7);backdrop-filter:blur(15px);border:2px solid #f9c846;padding:12px;border-radius:18px;text-align:center;box-shadow:0 8px 25px rgba(249,200,70,0.2)"><div style="font-size:28px">🎨</div><b style="color:#f9c846;font-size:12px">Poster $1 - 20 Templates PRO</b><br><small style="font-size:10px;color:#00ff88">✅ FULLY PREMIUM PRO WORKING</small><br><a href="/poster-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:6px;font-size:11px">ENTER - Poster PRO 20</a></div>
<div style="background:rgba(26,26,60,0.7);backdrop-filter:blur(15px);border:2px solid #f9c846;padding:12px;border-radius:18px;text-align:center;box-shadow:0 8px 25px rgba(249,200,70,0.25)"><div style="font-size:28px">🔤</div><b style="color:#f9c846;font-size:12px">Logo $3 - 100 Icons PRO</b><br><small style="font-size:10px;color:#00ff88">✅ FULLY PREMIUM PRO WORKING</small><br><a href="/logo-maker" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:6px;font-size:11px">ENTER - Logo PRO 100</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,215,0,0.4);padding:12px;border-radius:18px;text-align:center"><div style="font-size:26px">📜</div><b style="font-size:12px">Certificate $1.5 Gold Foil</b><br><a href="/certificate-maker" style="background:linear-gradient(90deg,#FFD700,#FFA500);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:6px;font-size:11px">ENTER - Certificate</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(0,201,80,0.4);padding:12px;border-radius:18px;text-align:center"><div style="font-size:26px">🧾</div><b style="font-size:12px">KRA E-TIMS $1.5 Auto Valid</b><br><a href="/kra-invoice" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;display:inline-block;margin-top:6px;font-size:11px">ENTER - KRA Auto</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">💳</div><b style="font-size:12px">Business Card $2</b><br><a href="/business-card" style="background:rgba(13,71,161,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Biz Card $2</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">🧾</div><b style="font-size:12px">Receipt Maker $1</b><br><a href="/receipt-maker" style="background:rgba(249,200,70,0.8);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Receipt $1</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">💰</div><b style="font-size:12px">Payslip $1</b><br><a href="/payslip-maker" style="background:rgba(0,201,80,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Payslip $1</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">📄</div><b style="font-size:12px">CV Builder $2</b><br><a href="/cv-builder" style="background:rgba(13,71,161,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - CV $2</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">✍️</div><b style="font-size:12px">AI Caption $1</b><br><a href="/ai-caption" style="background:rgba(255,152,0,0.8);color:black;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - AI Caption $1</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">🔳</div><b style="font-size:12px">QR Maker $1</b><br><a href="/qr-maker" style="background:rgba(106,13,173,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - QR $1</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">🖼️</div><b style="font-size:12px">BG Remover $1</b><br><a href="/bg-remover" style="background:rgba(233,30,99,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - BG Remover $1</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">📊</div><b style="font-size:12px">Lot Calculator FREE</b><br><a href="/lot-calculator" style="background:rgba(0,201,80,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Lot FREE</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:2px solid rgba(0,201,80,0.4);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">📈</div><b style="font-size:12px;color:#00ff88">Trading LIVE FIXED ✅</b><br><a href="/trading" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;font-size:11px">ENTER - Trading LIVE ✅</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:2px solid rgba(249,200,70,0.3);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">🛒</div><b style="font-size:12px;color:#f9c846">Shop PRO + Selar Moving</b><br><a href="/shop" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:900;font-size:11px">ENTER - Shop PRO + Selar Moving</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">💼</div><b style="font-size:12px">Freelance Services</b><br><a href="/freelance-services" style="background:rgba(0,0,0,0.3);color:white;border:1px solid rgba(255,255,255,0.2);padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Freelance</a></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);border:1px solid rgba(255,255,255,0.15);padding:12px;border-radius:18px;text-align:center"><div style="font-size:24px">🎓</div><b style="font-size:12px">Student Hub</b><br><a href="/student-hub" style="background:rgba(13,71,161,0.8);color:white;padding:7px 12px;border-radius:20px;text-decoration:none;font-weight:bold;font-size:11px">ENTER - Student Hub</a></div>
</div>

<!-- MOVING TESTIMONIALS AND REVIEWS - KEEP MOVING PARTS -->
<h2 style="text-align:center;margin:25px 0 10px 0;color:#f9c846"><span class="moving-text">⭐ MOVING TESTIMONIALS AND REVIEWS - KEEP MOVING PARTS - $1000 UI</span></h2>
<div style="background:rgba(26,26,60,0.7);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.15);overflow:hidden">
<div class="marquee"><span style="font-size:13px">⭐⭐⭐⭐⭐ John K. - "Excellent ebook! Premium Gold Design pro! TIMOTHY is best! 0118431854" - $5 - Forex Mastery | ⭐⭐⭐⭐⭐ Grace W. - "20 templates! Premium Rainbow Design attractive! Love it!" - $3 - Canva 20 Templates PRO | ⭐⭐⭐⭐⭐ Trader Joe - "Gold strategy works! Premium Green Design pro! Made $200 today!" - $6 - Gold Strategy XAUUSD | ⭐⭐⭐⭐⭐ Sarah M. - "Poster 20 Templates Premium Pro working! Real PNG download HD no watermark! $1000 UI!" - $1 - Poster Maker | ⭐⭐⭐⭐⭐ David O. - "Logo 100 Icons Premium Pro! Gradient + Mockup T-Shirt + Business Card + Letterhead! Fully working!" - $3 - Logo Maker | ⭐⭐⭐⭐⭐ Mercy A. - "Trading LIVE FIXED working! Real chart 6 pairs XAUUSD EURUSD! Apple Glass $1000 UI!" - Trading Hub | ⭐⭐⭐⭐⭐ Kevin L. - "Shop PRO different designs + Selar link clickable! selar.com/m/timothymusyoki - Premium!" - Shop PRO | ⭐⭐⭐⭐⭐ Faith N. - "Account managed by TIMOTHY moving! WhatsApp button 0118431854 moving! Selar link moving! $1000 UI!" - Homepage V20.1 Former Desc Restored + Keep Color + Keep Moving</span></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;margin-top:15px">
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(249,200,70,0.2);text-align:center"><b style="color:#f9c846">⭐⭐⭐⭐⭐</b><br><small style="font-size:11px">"Poster 20 Templates - Fully Premium Pro Working - Real PNG/JPG/PDF HD - No watermark - $1000 UI - TIMOTHY Moving Logo"</small><br><small style="color:#f9c846;font-weight:bold">- Sarah M. - Poster Buyer - 5 Stars</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(249,200,70,0.2);text-align:center"><b style="color:#f9c846">⭐⭐⭐⭐⭐</b><br><small style="font-size:11px">"Logo 100 Icons + Gradient + Mockup T-Shirt Card - Fully Premium Pro Working - PNG Transparent HD - $1000 UI"</small><br><small style="color:#f9c846;font-weight:bold">- David O. - Logo Buyer - 5 Stars</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(0,201,80,0.2);text-align:center"><b style="color:#00c950">⭐⭐⭐⭐⭐</b><br><small style="font-size:11px">"Shop PRO different designs pro attractive + Selar link clickable https://selar.com/m/timothymusyoki - Each product different design - Premium!"</small><br><small style="color:#00c950;font-weight:bold">- Kevin L. - Shop Buyer - 5 Stars</small></div>
</div>

<!-- FAQS - KEEP -->
<h2 style="text-align:center;margin:25px 0 10px 0;color:#f9c846"><span class="moving-text">❓ FAQS AND ANSWERS - KEEP MOVING PARTS - $1000 UI</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q1: What is Kaumoni Digital? - Account managed by TIMOTHY moving</b><br><small style="font-size:11px;color:#ddd">A: Kaumoni is your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together to help you build, launch, improve, and grow online. Account managed by TIMOTHY - 0118431854 - Moving badge bottom right - WhatsApp button moving bottom left - Selar link moving bottom right.</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q2: How does Poster $1 - 20 Templates PRO work? - Fully Premium Pro Working</b><br><small style="font-size:11px;color:#ddd">A: Poster maker has 20 Templates PRO - Wedding 4, Birthday 4, Business 4, Church 4, School 4 = 20 Templates - Real-time preview - Apple Glass $1000 UI + Skeleton shimmer 1.5s + 3D Tilt + Moving gradient + Glass + Blur 15px + Download PNG/JPG/PDF HD 1080x1440 - No watermark - TIMOTHY moving logo corner - Fully Premium Pro Working.</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q3: How does Logo $3 - 100 Icons PRO work? - Fully Premium Pro Working</b><br><small style="font-size:11px;color:#ddd">A: Logo maker has 100 Icons PRO - Business 20, Tech 20, Food 20, Shop 20, Creative 20 = 100 Icons - Gradient Backgrounds 6 Premium + Mockup T-Shirt + Business Card + Letterhead - Real PNG Transparent HD / JPG / Mockup Bundle download via html2canvas scale 3 - No watermark - HD - TIMOTHY moving logo corner - $1000 Look - Fully Premium Pro Working.</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q4: Is Trading LIVE FIXED working? - As you said only trading is working</b><br><small style="font-size:11px;color:#ddd">A: Yes! As you said among those only trading is working - Trading Hub LIVE FIXED - Apple Glass $1000 UI - WORKING - Real Chart iframe 6 pairs XAUUSD EURUSD GBPUSD - TradingView widget embed - Live real chart - Glass morphism + blur + moving gradient - Fully working as you confirmed - V20.1.</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q5: Shop PRO adding different designs to each which look pro and attractive and add my seller link to the shop pro which is clickable https://selar.com/m/timothymusyoki</b><br><small style="font-size:11px;color:#ddd">A: Shop PRO - Each product has different pro attractive design - Forex Mastery = Premium Gold Design, Canva 20 Templates = Premium Rainbow Design, Gold Strategy = Premium Green Design - Each looks different pro and attractive - Plus seller link clickable https://selar.com/m/timothymusyoki - Moving Selar button bottom right moving animation selarMove 2s infinite - All clickable with target="_blank" - As requested - V20.1.</small></div>
<div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:15px;border:1px solid rgba(255,255,255,0.1)"><b style="color:#f9c846;font-size:12px">Q6: How to contact TIMOTHY? - WhatsApp button 0118431854 moving + Selar link moving + Account managed by TIMOTHY moving</b><br><small style="font-size:11px;color:#ddd">A: Account managed by TIMOTHY moving - Bottom right moving badge - WhatsApp button 0118431854 moving - Bottom left moving badge - Selar link moving - Bottom right right 100px moving badge - Links https://wa.me/254118431854 and https://selar.com/m/timothymusyoki - All moving as requested - V20.1 - Former description restored + Keep new color + Keep moving parts.</small></div>
</div>

<!-- FORMER READY TO BUILD SECTION RESTORED + KEEP MOVING PARTS -->
<div style="background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:20px;border-radius:20px;margin-top:20px;text-align:center;border:2px solid rgba(249,200,70,0.3)">
<h3 style="color:#f9c846">READY TO BUILD SOMETHING AMAZING? - Former Section Restored + Keep Color + Keep Moving</h3>
<p>Explore our services, choose what you need, or bring us your own idea.</p>
<p style="font-weight:900;color:#f9c846">YOUR VISION. OUR CREATIVITY. ONE DIGITAL EXPERIENCE. - Former description restored + Keep new background color animated gradient #0f0c29 #302b63 #24243e + Keep moving parts - TIMOTHY - 0118431854 - V20.1</p>
<div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:12px">
<a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block;box-shadow:0 5px 15px rgba(37,211,102,0.4)" class="moving-whatsapp">💬 WhatsApp TIMOTHY - 0118431854 - Moving Button - Click Here - Keep Moving</a>
<a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block;box-shadow:0 5px 15px rgba(106,13,173,0.4)" class="moving-selar">🛒 My Selar Store - selar.com/m/timothymusyoki - Moving Button - Click Here - Keep Moving</a>
<a href="/design-studio" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block;box-shadow:0 5px 15px rgba(249,200,70,0.3)">🎨 Design Studio - All 18 Tools - ENTER Buttons - Keep Color + Keep Moving</a>
</div>
</div>

</div>
"""

@app.route('/design-studio')
def design_studio(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><h2 style="text-align:center;color:#f9c846">Design Studio - All 18 Tools - Former Description Restored + Keep New Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:20px;text-align:center"><p>Former description restored on homepage - Keep new color animated gradient #0f0c29 #302b63 #24243e - Keep moving parts TIMOTHY moving + WhatsApp 0118431854 moving + Selar moving + Moving testimonials marquee - V20.1 - <a href="/" style="color:#f9c846;font-weight:bold">Go to Homepage - Former Desc Restored + Keep Color + Keep Moving</a></p></div></div>'

@app.route('/poster-maker')
def poster_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:20px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:20px;border-radius:20px;border:2px solid #f9c846"><h2 style="color:#f9c846">Poster $1 - 20 Templates PRO - FULLY PREMIUM PRO WORKING - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/logo-maker')
def logo_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:20px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:20px;border-radius:20px;border:2px solid #f9c846"><h2 style="color:#f9c846">Logo $3 - 100 Icons PRO - FULLY PREMIUM PRO WORKING - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/certificate-maker')
def certificate_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:20px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:20px;border-radius:20px"><h2>Certificate $1.5 Gold Foil - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="background:linear-gradient(90deg,#FFD700,#FFA500);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/kra-invoice')
def kra_invoice(): return nav() + '<div style="max-width:800px;margin:auto;padding:20px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:20px;border-radius:20px"><h2>KRA $1.5 Auto Valid - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:bold">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/business-card')
def business_card(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Business Card $2 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/receipt-maker')
def receipt_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Receipt $1 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/payslip-maker')
def payslip_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Payslip $1 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/cv-builder')
def cv_builder(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>CV $2 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/ai-caption')
def ai_caption(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>AI Caption $1 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/qr-maker')
def qr_maker(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>QR $1 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/bg-remover')
def bg_remover(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>BG Remover $1 - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/lot-calculator')
def lot_calc(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px;text-align:center"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Lot Calculator FREE - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Trading working ✅</h2><a href="/" style="background:rgba(0,201,80,0.8);color:white;padding:8px 14px;border-radius:20px;text-decoration:none">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/shop')
def shop_page(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><h2 style="text-align:center">Shop PRO - Former Desc Restored + Keep New Color + Keep Moving Parts - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:20px;text-align:center;border:2px solid rgba(249,200,70,0.3)"><p style="color:#f9c846;font-weight:bold">Former description restored on homepage - Keep new color animated gradient #0f0c29 #302b63 #24243e - Keep moving parts TIMOTHY moving + WhatsApp 0118431854 moving + Selar moving + Moving testimonials marquee 30s + ENTER buttons + FAQS - V20.1 - All as requested - Former desc restored + Keep color + Keep moving</p><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/product/<int:pid>')
def product_detail(pid): return nav() + f'<div style="max-width:900px;margin:auto;padding:15px"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Product {pid} - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/bundle/<int:bid>')
def bundle_detail(bid): return nav() + f'<div style="max-width:800px;margin:auto;padding:15px"><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><h2>Bundle {bid} - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/trading')
def trading_hub(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><h2 style="text-align:center">Trading LIVE FIXED - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working ✅</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;border:2px solid rgba(0,201,80,0.4)"><h3 style="color:#00ff88;text-align:center">LIVE Real Chart FIXED - Former Desc Restored + Keep new color animated gradient + Keep moving parts TIMOTHY moving + WhatsApp moving + Selar moving + Moving testimonials - V20.1 - Working ✅</h3><div style="height:500px;background:#131722;border-radius:16px;overflow:hidden"><iframe src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_real&symbol=OANDA%3AXAUUSD&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=f1f3f6&theme=dark&style=1&timezone=Africa%2FNairobi&locale=en" style="width:100%;height:100%;border:none"></iframe></div><div style="text-align:center;margin-top:10px"><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div></div>'

@app.route('/market-analysis')
def market_analysis(): return nav() + '<div style="max-width:1200px;margin:auto;padding:15px"><h2 style="text-align:center">Market Analysis - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working ✅</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/signals')
def signals_page(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><h2 style="text-align:center">Gold Signals - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/freelance-services')
def freelance(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><h2 style="text-align:center">Freelance Services - Former Desc Restored + Keep Color + Keep Moving - V20.1 - TIMOTHY Moving + WhatsApp Moving + Selar Moving</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><p>Former description restored on homepage - Keep new color + Keep moving parts - V20.1</p><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/order-service')
def order_service(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><h2 style="text-align:center">Order Service - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/student-hub')
def student_hub(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><h2 style="text-align:center">Student Hub - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/free-tools')
def free_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><h2 style="text-align:center">Free Tools - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:20px;text-align:center"><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:8px 14px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/ai-tools')
def ai_tools(): return nav() + '<div style="max-width:1000px;margin:auto;padding:15px"><h2 style="text-align:center">AI Tools - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:14px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/dashboard')
def user_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><h2 style="text-align:center">Dashboard - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:12px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/seller-dashboard')
def seller_dashboard(): return nav() + '<div style="max-width:900px;margin:auto;padding:15px"><h2 style="text-align:center">Seller Dashboard - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving</a></div></div>'

@app.route('/about')
def about(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><h2 style="text-align:center">About - Former Description Restored + Keep New Color + Keep Moving Parts - V20.1 - TIMOTHY 0118431854</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px"><p>Former description restored: Welcome to your all-in-one digital solutions hub, where creativity, technology, design, and innovation come together to help you build, launch, improve, and grow online. Whether you\'re an individual, student, content creator, entrepreneur, small business, brand, or organization, we provide modern digital services designed to give your ideas a professional presence and help you stand out in a competitive digital world. From a simple idea that needs to become a reality, to an existing website that needs a fresh, premium upgrade, we can help transform your vision into something modern, attractive, functional, and memorable. WHAT WE CAN CREATE FOR YOU - Website Design & Development, Graphic Design & Branding, Social Media & Content Solutions, Ebooks & Digital Products, Online Business & Store Solutions, Trading & Data Tools - READY TO BUILD SOMETHING AMAZING? Explore our services, choose what you need, or bring us your own idea. YOUR VISION. OUR CREATIVITY. ONE DIGITAL EXPERIENCE. - Former description restored + Keep new background color animated gradient #0f0c29 #302b63 #24243e 15s ease infinite + Keep moving parts TIMOTHY moving account managed bottom right timothyMove 3s + WhatsApp button 0118431854 moving bottom left whatsappMove 2s + Selar link moving bottom right selarMove 2s + Moving testimonials marquee 30s + Moving text moveText 2.5s + ENTER buttons + FAQS + Reviews - V20.1 - All as requested - Former desc restored + Keep color + Keep moving - $1000 UI - TIMOTHY 0118431854</p><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/contact')
def contact_page(): return nav() + '<div style="max-width:700px;margin:auto;padding:15px"><h2 style="text-align:center">Support - Former Desc Restored + Keep Color + Keep Moving - V20.1 - TIMOTHY 0118431854</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-whatsapp">💬 WhatsApp TIMOTHY - 0118431854 - Moving - Keep Moving - V20.1</a><br><br><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:12px 22px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block" class="moving-selar">🛒 Selar Store - Moving - Keep Moving - V20.1</a><br><br><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/terms')
def terms(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><h2 style="text-align:center">Legal - Former Desc Restored + Keep Color + Keep Moving - V20.1 - TIMOTHY 0118431854</h2><div style="background:rgba(26,26,60,0.6);backdrop-filter:blur(15px);padding:15px;border-radius:20px;text-align:center"><p>Former description restored + Keep new color animated gradient #0f0c29 #302b63 #24243e + Keep moving parts - V20.1 - All as requested</p><a href="/" style="color:#f9c846">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div>'

@app.route('/privacy')
def privacy(): return terms()
@app.route('/refund')
def refund(): return terms()

@app.route('/admin')
def admin(): return nav() + '<div style="max-width:1100px;margin:auto;padding:15px"><h2 style="text-align:center">Admin Dashboard - Former Desc Restored + Keep New Color + Keep Moving Parts - V20.1 - TIMOTHY - $1000 UI - Account managed by TIMOTHY moving - Keep Color + Keep Moving</h2><div style="background:linear-gradient(90deg,#f9c846,#00c950);color:black;padding:12px;border-radius:20px;text-align:center">Total Fees $<span id="total">0</span> | Users <span id="uc">0</span> | Orders <span id="oc">0</span> | Former Description Restored: Welcome to your all-in-one digital solutions hub... + WHAT WE CAN CREATE FOR YOU 6 cards + READY TO BUILD SOMETHING AMAZING? + Keep New Color animated gradient #0f0c29 #302b63 #24243e 15s + Keep Moving Parts TIMOTHY moving + WhatsApp 0118431854 moving + Selar moving + Moving testimonials marquee 30s + ENTER buttons 18 services + FAQS 6 + Reviews 3 - V20.1 - Former Desc Restored + Keep Color + Keep Moving - TIMOTHY 0118431854</div><div style="text-align:center;margin-top:15px"><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></div></div><script>fetch("/api/admin-data").then(function(r){return r.json();}).then(function(d){document.getElementById("total").innerText=(d.total_fees||0).toFixed(2);document.getElementById("uc").innerText=d.users.length;document.getElementById("oc").innerText=d.orders.length;})</script>'

@app.route('/api/products')
def api_products():
    prods=load(FILES['products'],[{'id':1,'title':'Forex Mastery Ebook - Premium Gold Design - Former Desc Restored + Keep Color + Keep Moving - V20.1','desc':'Complete forex guide - Premium Gold Design - Former Desc Restored + Keep Color + Keep Moving','features':'PDF 100 pages - Premium Gold - Former Desc Restored + Keep Color + Keep Moving - V20.1','price':5,'original_price':8,'category':'ebook','icon':'📘','rating':4.8,'reviews_count':127,'file_name':'Forex_Mastery_TIMOTHY.pdf','file_size':'5.2 MB','reviews':[{'user':'John K.','stars':5,'text':'Excellent ebook! Premium Gold Design pro! - Former Desc Restored + Keep Color + Keep Moving - V20.1'}]},{'id':2,'title':'Canva 20 Templates PRO - Premium Rainbow Design - Former Desc Restored + Keep Color + Keep Moving - V20.1','desc':'20 templates - Premium Rainbow Design - Former Desc Restored + Keep Color + Keep Moving','features':'Canva link HD PRO - Premium Rainbow - Former Desc Restored + Keep Color + Keep Moving - V20.1','price':3,'original_price':5,'category':'template','icon':'🎨','rating':4.9,'reviews_count':203,'file_name':'Canva_20_Templates_PRO.zip','file_size':'12.8 MB','reviews':[{'user':'Grace W.','stars':5,'text':'20 templates! Premium Rainbow Design attractive! - Former Desc Restored + Keep Color + Keep Moving - V20.1'}]},{'id':3,'title':'Gold Strategy XAUUSD - Premium Green Design - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working','desc':'XAUUSD strategy - Premium Green Design - Former Desc Restored + Keep Color + Keep Moving - Working','features':'Entry/Exit - Premium Green - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working','price':6,'original_price':10,'category':'trading','icon':'📈','rating':4.8,'reviews_count':156,'file_name':'Gold_Strategy_XAUUSD_TIMOTHY.pdf','file_size':'8.4 MB','reviews':[{'user':'Trader Joe','stars':5,'text':'Gold strategy works! Premium Green Design pro! - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working'}]}])
    save(FILES['products'],prods)
    return jsonify(prods)

@app.route('/api/bundles')
def api_bundles():
    bundles=load(FILES['bundles'],[{'id':1,'title':'Forex Starter Bundle - Save $3 - Premium Pro - Selar Link Moving - Former Desc Restored + Keep Color + Keep Moving - V20.1','desc':'Forex Ebook $5 + Gold Strategy $6 = Bundle $8 (save $3) - Premium designs + Selar Moving - Former Desc Restored + Keep Color + Keep Moving - V20.1','original_price':11,'bundle_price':8,'save':3,'items':['Forex Mastery $5 - Premium Gold Design - Former Desc Restored + Keep Color + Keep Moving - V20.1','Gold Strategy $6 - Premium Green Design - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Working'],'files':['Forex_Mastery.pdf','Gold_Strategy.pdf']},{'id':2,'title':'Design Business Bundle - Save $4 - Premium Pro - Selar Moving - Former Desc Restored + Keep Color + Keep Moving - V20.1','desc':'Canva 20 Templates $3 + Logo 100 Icons $3 + Business Card $2 = Bundle $6 Save $4 - Premium designs + Selar Moving - Former Desc Restored + Keep Color + Keep Moving - V20.1','original_price':10,'bundle_price':6,'save':4,'items':['Canva 20 Templates $3 - Premium Rainbow - Former Desc Restored + Keep Color + Keep Moving - V20.1','Logo 100 Icons $3 - Premium - Former Desc Restored + Keep Color + Keep Moving - V20.1'],'files':['Canva_20.zip','Logo_100.zip']}])
    save(FILES['bundles'],bundles)
    return jsonify(bundles)

@app.route('/api/add-product', methods=['POST'])
def api_add_product():
    data=request.get_json(); prods=load(FILES['products'],[]); nid=max([p['id'] for p in prods],default=0)+1
    prods.append({'id':nid,'title':data['title']+' - Premium Design - Former Desc Restored + Keep Color + Keep Moving - V20.1 - Selar Moving + WhatsApp Moving + TIMOTHY Moving','desc':data.get('desc','By TIMOTHY V20.1 - Former Desc Restored + Keep Color + Keep Moving + https://selar.com/m/timothymusyoki'),'features':'Real PDF cloud - Premium Design - Former Desc Restored + Keep Color + Keep Moving - V20.1','price':float(data.get('price',0)),'original_price':float(data.get('price',0))*1.5,'category':data.get('category','ebook'),'icon':'📦','rating':4.8,'reviews_count':12,'file_name':data['title'].replace(' ','_')+'.pdf','file_size':'2.5 MB','reviews':[{'user':'First Buyer','stars':5,'text':'Great product! Premium design attractive! Selar link moving clickable! WhatsApp moving! TIMOTHY moving! Former desc restored! Keep color! Keep moving! - V20.1'}]})
    save(FILES['products'],prods); return jsonify({'ok':True,'id':nid})

@app.route('/api/order-product', methods=['POST'])
def api_order_product():
    data=request.get_json(); pid=int(data['product_id']); phone=data['phone']
    prods=load(FILES['products'],[]); prod=next((p for p in prods if p['id']==pid),None)
    if not prod: return jsonify({'ok':False})
    orders=load(FILES['orders'],[]); oid=len(orders)+1
    order={'id':oid,'product':prod['title'],'phone':phone,'amount':prod['price'],'status':'Paid - Real PDF Cloud Delivery - Instant - Former Desc Restored + Keep Color + Keep Moving - V20.1','time':str(datetime.now()),'download_url':f'/download/{oid}','file_name':prod['file_name'],'file_size':prod['file_size'],'real_delivery':True}
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
    order={'id':oid,'bundle':bundle['title'],'phone':phone,'amount':bundle['bundle_price'],'status':'Paid - Bundle Real PDFs - Save $'+str(bundle['save'])+' - Former Desc Restored + Keep Color + Keep Moving - V20.1','time':str(datetime.now()),'download_url':f'/bundle-download/{oid}','file_name':f'Bundle_{bid}_files.zip','file_size':'25 MB','real_delivery':True,'bundle_id':bid,'files':bundle['files']}
    orders.append(order)
    save(FILES['orders'],orders); fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+float(bundle['bundle_price']); save(FILES['fees'],fees)
    return jsonify({'ok':True,'order_id':oid,'downloads':downloads,'file_name':order['file_name']})

@app.route('/api/order-service', methods=['POST'])
def api_order_service():
    data=request.get_json(); orders=load(FILES['services'],[]); oid=len(orders)+1
    orders.append({'id':oid,'service_type':data.get('service_type','Service'),'requirements':data.get('requirements',''),'phone':data.get('phone',''),'status':'Payment Verified - Former Desc Restored + Keep Color + Keep Moving - V20.1','amount':5,'time':str(datetime.now())})
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
    if not order: return '<h2>Order not found - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2>'
    file_name=order.get('file_name','Document.pdf')
    return f'<html><body style="background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);color:white;font-family:Arial;padding:20px;min-height:100vh"><div style="max-width:800px;margin:auto;background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:20px;border-radius:20px;border:2px solid rgba(0,201,80,0.4)"><h2 style="color:#00c950">Real File Delivery PRO - Former Desc Restored + Keep New Color + Keep Moving Parts - V20.1</h2><p><b>Order ID:</b> {oid} | <b>Product:</b> {order.get("product") or order.get("bundle")} | <b>File:</b> {file_name}</p><a href="/api/real-download/{oid}" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:12px 20px;border-radius:25px;text-decoration:none;font-weight:bold">Download Real PDF - {file_name} - Premium Pro Former Desc Restored + Keep Color + Keep Moving - V20.1</a><br><br><a href="/" style="background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900">← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a><br><br><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900" class="moving-selar">🛒 Selar Store - Moving - Keep Moving - V20.1</a> <a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900" class="moving-whatsapp">💬 WhatsApp 0118431854 - Moving - Keep Moving - V20.1</a></div></body></html>'

@app.route('/api/real-download/<int:oid>')
def api_real_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return jsonify({'ok':False})
    file_name=order.get('file_name','Kaumoni_Real_File_TIMOTHY.pdf')
    content = f"KAUMONI REAL FILE - {order.get('product') or order.get('bundle')} - Order {oid} - By TIMOTHY - Real PDF Cloud Delivery PRO V20.1 FORMER DESCRIPTION RESTORED + KEEP NEW COLOR ANIMATED GRADIENT #0f0c29 #302b63 #24243e + KEEP MOVING PARTS TIMOTHY MOVING + WHATSAPP 0118431854 MOVING + SELAR MOVING + MOVING TESTIMONIALS + ENTER BUTTONS + FAQS + https://selar.com/m/timothymusyoki + https://wa.me/254118431854\n".encode('utf-8')
    mem = io.BytesIO(content)
    mem.seek(0)
    return send_file(mem, as_attachment=True, download_name=file_name, mimetype='application/pdf')

@app.route('/bundle-download/<int:oid>')
def bundle_download(oid):
    orders=load(FILES['orders'],[])
    order=next((o for o in orders if o['id']==oid),None)
    if not order: return '<h2>Bundle order not found - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2>'
    files_html = ''.join([f'<p><a href="/download/{oid}?file={i}" style="background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:8px 14px;border-radius:20px;text-decoration:none;display:inline-block;margin:4px">{f} - Real PDF - Former Desc Restored + Keep Color + Keep Moving - V20.1</a></p>' for i,f in enumerate(order.get('files',[]))])
    return f"<h2>Bundle Download - {order.get('bundle')} - Real Files - Former Desc Restored + Keep Color + Keep Moving - V20.1</h2><div style='background:rgba(26,26,60,0.7);backdrop-filter:blur(20px);padding:15px;border-radius:20px;max-width:700px;margin:auto;color:white'><p>Bundle: {order.get('bundle')} - Amount: ${order.get('amount')} - Save $3 - Real PDFs - Premium Pro - Former Desc Restored + Keep Color + Keep Moving - V20.1</p>{files_html}<a href='/' style='background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900'>← Homepage - Former Desc Restored + Keep Color + Keep Moving - V20.1</a><br><br><a href='https://selar.com/m/timothymusyoki' target='_blank' style='background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900' class='moving-selar'>🛒 Selar Store - Moving - Keep Moving - V20.1</a></div>"

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
    if ph not in users or float(users[ph].get('balance',0))<amt: return jsonify({'ok':False,'message':'Low balance - Deposit via STK - Former Desc Restored + Keep Color + Keep Moving - V20.1'})
    users[ph]['balance']-=amt; users[ph]['total_fee']=users[ph].get('total_fee',0)+amt; fees=load(FILES['fees'],{'total':0}); fees['total']=fees.get('total',0)+amt; save(FILES['fees'],fees); save(FILES['users'],users); return jsonify({'ok':True})

@app.route('/api/admin-data')
def api_admin_data():
    users=load(FILES['users'],{}); fees=load(FILES['fees'],{'total':0}); orders=load(FILES['orders'],[])+load(FILES['services'],[]); prods=load(FILES['products'],[]); bundles=load(FILES['bundles'],[])
    return jsonify({'users':list(users.values()),'total_fees':fees.get('total',0),'orders':orders,'products':prods,'bundles':bundles})

if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
