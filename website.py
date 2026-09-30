from flask import Flask, request, jsonify
import os, json
app = Flask(__name__)
app.secret_key = "KAUMONI_V26_ADD_5_NEW_FAQS_WHERE_OTHERS_ARE_KEEP_ALL_BG_LAYOUT_SAME_PREMIUM_PRO"
FILES = {"users":"users.json","fees":"fees.json","products":"products.json","orders":"orders.json","services":"services_orders.json","bundles":"bundles.json","signals":"signals.json"}
def load(f,d):
    if not os.path.exists(f): return d
    try:
        with open(f) as jf: return json.load(jf)
    except: return d

def nav():
    return (
        '<style>'
        '@keyframes gradientBG{0%{background-position:0% 50%}25%{background-position:100% 50%}50%{background-position:100% 100%}75%{background-position:0% 100%}100%{background-position:0% 50%}}'
        '@keyframes floatOrb1{0%{transform:translate(0,0) scale(1);opacity:0.7}33%{transform:translate(200px,-150px) scale(1.3);opacity:0.9}66%{transform:translate(-100px,150px) scale(1.1);opacity:0.6}100%{transform:translate(0,0) scale(1);opacity:0.7}}'
        '@keyframes floatOrb2{0%{transform:translate(0,0) scale(1.2);opacity:0.6}33%{transform:translate(-250px,100px) scale(1);opacity:0.8}66%{transform:translate(150px,-100px) scale(1.4);opacity:0.5}100%{transform:translate(0,0) scale(1.2);opacity:0.6}}'
        '@keyframes floatOrb3{0%{transform:translate(0,0) scale(1);opacity:0.5}50%{transform:translate(180px,200px) scale(1.5);opacity:0.8}100%{transform:translate(0,0) scale(1);opacity:0.5}}'
        '@keyframes floatOrb4{0%{transform:translate(0,0) scale(1.3)}50%{transform:translate(-180px,-200px) scale(1);opacity:0.7}100%{transform:translate(0,0) scale(1.3)}}'
        '@keyframes shine{0%{background-position:-200% 0}100%{background-position:200% 0}}'
        '@keyframes marqueeLeft{0%{transform:translateX(100%)}100%{transform:translateX(-100%)}}'
        '@keyframes marqueeRight{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}'
        '@keyframes timothyMove{0%{transform:translateX(-20px) translateY(-8px) scale(1)}50%{transform:translateX(20px) translateY(8px) scale(1.15)}100%{transform:translateX(-20px) translateY(-8px) scale(1)}}'
        '@keyframes selarMove{0%{transform:translateX(-15px) translateY(-5px)}50%{transform:translateX(15px) translateY(5px)}100%{transform:translateX(-15px) translateY(-5px)}}'
        '@keyframes whatsappMove{0%{transform:translateY(-10px) scale(1)}50%{transform:translateY(10px) scale(1.12)}100%{transform:translateY(-10px) scale(1)}}'
        '@keyframes pulseGold{0%{box-shadow:0 0 0 0 rgba(249,200,70,0.8)}50%{box-shadow:0 0 0 15px rgba(249,200,70,0)}100%{box-shadow:0 0 0 0 rgba(249,200,70,0)}}'
        '@keyframes pulseGreen{0%{box-shadow:0 0 0 0 rgba(0,255,136,0.7)}70%{box-shadow:0 0 0 12px rgba(0,255,136,0)}100%{box-shadow:0 0 0 0 rgba(0,255,136,0)}}'
        'body{margin:0;min-height:100vh;font-family:Arial;color:white;position:relative;overflow-x:hidden;background:linear-gradient(125deg,#0f0c29 0%,#302b63 15%,#24243e 30%,#0f0c29 45%,#6a0dad 60%,#0d47a1 75%,#00b09b 85%,#302b63 100%);background-size:400% 400%;animation:gradientBG 12s ease infinite}'
        'body::before{content:"";position:fixed;top:0;left:0;right:0;bottom:0;z-index:-3;background:radial-gradient(circle at 20% 30%,rgba(249,200,70,0.25) 0%,transparent 50%),radial-gradient(circle at 80% 20%,rgba(106,13,173,0.35) 0%,transparent 50%),radial-gradient(circle at 40% 80%,rgba(0,255,136,0.2) 0%,transparent 50%),radial-gradient(circle at 90% 90%,rgba(255,0,128,0.2) 0%,transparent 50%),radial-gradient(circle at 10% 90%,rgba(0,210,255,0.25) 0%,transparent 50%);pointer-events:none}'
        '.orb{position:fixed;border-radius:50%;filter:blur(40px);pointer-events:none;z-index:-2}'
        '.orb1{width:500px;height:500px;background:radial-gradient(circle,rgba(249,200,70,0.4),rgba(255,152,0,0.2),transparent);top:5%;left:10%;animation:floatOrb1 10s ease-in-out infinite}'
        '.orb2{width:600px;height:600px;background:radial-gradient(circle,rgba(106,13,173,0.4),rgba(13,71,161,0.2),transparent);top:40%;right:10%;animation:floatOrb2 13s ease-in-out infinite}'
        '.orb3{width:400px;height:400px;background:radial-gradient(circle,rgba(0,255,136,0.35),rgba(0,176,155,0.15),transparent);bottom:10%;left:30%;animation:floatOrb3 11s ease-in-out infinite}'
        '.orb4{width:550px;height:550px;background:radial-gradient(circle,rgba(255,0,128,0.3),rgba(255,0,64,0.15),transparent);top:20%;left:50%;animation:floatOrb4 14s ease-in-out infinite}'
        '.top-moving-banner{position:sticky;top:0;z-index:1001;background:linear-gradient(90deg,rgba(15,12,41,0.95),rgba(48,43,99,0.95),rgba(36,36,62,0.95),rgba(106,13,173,0.95),rgba(15,12,41,0.95));background-size:300% 100%;animation:gradientBG 6s ease infinite;border-bottom:3px solid #f9c846;overflow:hidden}'
        '.marquee-track{white-space:nowrap;overflow:hidden;position:relative;height:38px;display:flex;align-items:center}'
        '.marquee-content{position:absolute;white-space:nowrap;font-weight:900;letter-spacing:2px}'
        '.marquee-left{animation:marqueeLeft 18s linear infinite;font-size:16px;color:transparent;background:linear-gradient(90deg,#f9c846,#ff9800,#00ff88,#00d2ff,#f9c846);-webkit-background-clip:text;background-clip:text}'
        '.marquee-right{animation:marqueeRight 20s linear infinite;font-size:14px;color:transparent;background:linear-gradient(90deg,#00ff88,#00d2ff,#f9c846,#ff00cc,#00ff88);-webkit-background-clip:text;background-clip:text}'
        '.glass{background:rgba(26,26,60,0.65);backdrop-filter:blur(18px);border:1px solid rgba(255,255,255,0.15);border-radius:20px;padding:15px;box-shadow:0 8px 32px rgba(0,0,0,0.4);margin-bottom:15px;box-sizing:border-box;position:relative;overflow:hidden}'
        '.glass::before{content:"";position:absolute;top:0;left:-100%;width:100%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);animation:shine 4s linear infinite}'
        '.btn{display:inline-block;background:linear-gradient(90deg,#00c950,#00ff88);color:white;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px}'
        '.btn-gold{display:inline-block;background:linear-gradient(90deg,#f9c846,#ff9800);color:black;padding:10px 18px;border-radius:20px;text-decoration:none;font-weight:900;border:none;cursor:pointer;margin:6px;animation:pulseGold 2s infinite}'
        '.btn-glass{display:inline-block;background:rgba(255,255,255,0.12);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.25);color:white;padding:10px 18px;border-radius:20px;cursor:pointer;text-decoration:none;margin:6px}'
        '.input-glass{width:100%;padding:10px;background:rgba(14,14,30,0.8);color:white;border:1px solid rgba(255,255,255,0.15);border-radius:12px;margin:6px 0;box-sizing:border-box}'
        '.template-card{background:rgba(14,14,30,0.7);border:1px solid rgba(255,255,255,0.12);border-radius:14px;padding:10px;text-align:center;cursor:pointer;transition:0.3s}'
        '.template-card:hover{transform:translateY(-4px) scale(1.03);border-color:#f9c846}'
        '.marker-buy{position:absolute;left:10px;background:linear-gradient(90deg,#00c950,#00ff88);color:black;padding:4px 10px;border-radius:20px;font-size:10px;font-weight:900;animation:pulseGreen 1.5s infinite;border:2px solid white;z-index:5}'
        '.marker-sell{position:absolute;left:10px;background:linear-gradient(90deg,#ff0000,#ff4444);color:white;padding:4px 10px;border-radius:20px;font-size:10px;font-weight:900;border:2px solid white;z-index:5}'
        '#website-preview{width:100%;min-height:650px;background:white;border-radius:16px;overflow:auto;box-shadow:0 20px 50px rgba(0,0,0,0.6);color:#222;border:3px solid #f9c846}'
        '#poster-preview{width:100%;aspect-ratio:3/4;background:white;border-radius:16px;overflow:hidden;position:relative;box-shadow:0 20px 40px rgba(0,0,0,0.5)}'
        '#logo-preview{width:100%;aspect-ratio:1/1;background:white;border-radius:16px;overflow:hidden;position:relative;display:flex;align-items:center;justify-content:center;box-shadow:0 20px 40px rgba(0,0,0,0.5)}'
        '#videoPreview{width:100%;aspect-ratio:9/16;max-height:65vh;background:#000;border-radius:16px;overflow:hidden;position:relative}'
        '</style>'
        '<div class="orb orb1"></div><div class="orb orb2"></div><div class="orb orb3"></div><div class="orb orb4"></div>'
        '<div class="top-moving-banner"><div class="marquee-track" style="background:linear-gradient(90deg,rgba(249,200,70,0.15),rgba(106,13,173,0.15));border-bottom:1px solid rgba(249,200,70,0.3)"><div class="marquee-content marquee-left">✨ TIMOTHY YOUR TRUSTED ADMIN ✨ TIMOTHY YOUR TRUSTED ADMIN ✨ TIMOTHY YOUR TRUSTED ADMIN ✨ TIMOTHY YOUR TRUSTED ADMIN ✨</div></div>'
        '<div class="marquee-track" style="background:linear-gradient(90deg,rgba(0,255,136,0.12),rgba(0,210,255,0.12));"><div class="marquee-content marquee-right">🌈 WELCOME TO MY WEBSITE 🌈 WELCOME TO MY WEBSITE 🌈 WELCOME TO MY WEBSITE 🌈 WELCOME TO MY WEBSITE 🌈</div></div>'
        '<div style="display:flex;justify-content:center;gap:10px;padding:8px 12px;flex-wrap:wrap"><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846,#ff9800);color:white;padding:8px 18px;border-radius:25px;font-weight:900;font-size:12px;text-decoration:none;border:2px solid rgba(255,255,255,0.4);animation:pulseGold 2s infinite">🛒 CLICK HERE - MY SELAR STORE - selar.com/m/timothymusyoki - V26 NEW FAQS ADDED 🛒</a></div></div>'
        '<nav style="background:rgba(15,12,41,0.88);backdrop-filter:blur(20px);padding:10px 12px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:86px;border-bottom:3px solid #f9c846;z-index:1000;flex-wrap:wrap;gap:8px">'
        '<b style="color:#f9c846;font-size:11px">V26 ADD 5 NEW FAQS WHERE OTHERS ARE KEEP BG LAYOUT PREMIUM PRO SAME - NO CHANGE ELSE</b>'
        '<div style="display:flex;gap:8px;font-size:10px;flex-wrap:wrap"><a href="/" style="color:#f9c846;text-decoration:none;background:rgba(249,200,70,0.15);padding:5px 10px;border-radius:20px">Home</a>'
        '<a href="/trading" style="color:black;background:linear-gradient(90deg,#00c950,#00ff88);padding:6px 12px;border-radius:20px;font-weight:900;text-decoration:none">📈 Trading PRO</a>'
        '<a href="/design-studio" style="color:black;background:linear-gradient(90deg,#f9c846,#ff9800);padding:6px 12px;border-radius:20px;font-weight:900;text-decoration:none">Website 12T PRO</a>'
        '<a href="/poster-maker" style="color:black;background:linear-gradient(90deg,#00c950,#00ff88);padding:6px 12px;border-radius:20px;font-weight:900;text-decoration:none">Poster 20T PRO</a>'
        '<a href="/ai-caption" style="color:black;background:linear-gradient(90deg,#00c950,#00ff88);padding:6px 12px;border-radius:20px;font-weight:900;text-decoration:none">Social LIVE PRO</a>'
        '<a href="/logo-maker" style="color:black;background:linear-gradient(90deg,#f9c846,#ff9800);padding:6px 12px;border-radius:20px;font-weight:900;text-decoration:none">Logo 100I PRO</a></div></nav>'
        '<div style="position:fixed;bottom:90px;right:20px;width:85px;height:85px;background:linear-gradient(135deg,#f9c846,#ff9800,#ff00cc);background-size:200% 200%;animation:gradientBG 3s ease infinite,timothyMove 3s ease-in-out infinite;border-radius:50%;display:flex;align-items:center;justify-content:center;color:black;font-weight:900;font-size:10px;z-index:9998;box-shadow:0 0 30px rgba(249,200,70,0.8);border:3px solid rgba(255,255,255,0.5);text-align:center">TIMOTHY<br>YOUR<br>TRUSTED<br>ADMIN</div>'
        '<a href="https://wa.me/254118431854" target="_blank" style="position:fixed;bottom:20px;left:20px;width:70px;height:70px;background:linear-gradient(135deg,#25D366,#00ff88);border-radius:50%;display:flex;align-items:center;justify-content:center;color:white;font-size:24px;z-index:9999;box-shadow:0 0 25px rgba(37,211,102,0.7);text-decoration:none;animation:whatsappMove 2s ease-in-out infinite;border:3px solid rgba(255,255,255,0.4)">💬</a>'
        '<a href="https://selar.com/m/timothymusyoki" target="_blank" style="position:fixed;bottom:20px;right:110px;background:linear-gradient(90deg,#6a0dad,#f9c846);color:white;padding:12px 18px;border-radius:25px;font-weight:900;font-size:11px;z-index:9997;box-shadow:0 0 25px rgba(106,13,173,0.7);text-decoration:none;animation:selarMove 2s ease-in-out infinite;border:2px solid rgba(255,255,255,0.4)">🛒 SELAR STORE CLICKABLE</a>'
    )

def trading_p(): return '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>📈 Trading LIVE PRO V26 Keep BG Same</h2><a href="/" class="btn">Home - Keep BG - New FAQs Added Below</a></div></div>'
def website_p(): return '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>🌐 Website 12T PRO V26 Keep BG Same</h2><a href="/" class="btn-gold">Home - Keep BG - New FAQs Added Below</a></div></div>'
def poster_p(): return '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>🎨 Poster 20T PRO V26 Keep BG Same</h2><a href="/" class="btn">Home - Keep BG - New FAQs Added Below</a></div></div>'
def social_p(): return '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>📱 Social LIVE PRO V26 Keep BG Same</h2><a href="/" class="btn">Home - Keep BG - New FAQs Added Below</a></div></div>'
def logo_p(): return '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>🔤 Logo 100I PRO V26 Keep BG Same</h2><a href="/" class="btn-gold">Home - Keep BG - New FAQs Added Below</a></div></div>'

@app.route('/')
def home():
    return nav() + """
<div style="max-width:1350px;margin:auto;padding:15px">
<!-- KEEP ALL CURRENT DESIGN EXACTLY SAME - NO CHANGE ABOVE -->
<div class="glass" style="text-align:center;border:3px solid transparent;border-image:linear-gradient(90deg,#f9c846,#00ff88,#00d2ff,#ff00cc,#f9c846) 1"><h1 style="background:linear-gradient(90deg,#f9c846,#ff9800,#00ff88,#00d2ff,#ff00cc,#f9c846);background-size:300% 100%;-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:gradientBG 4s ease infinite;margin:5px 0">✨ MOST ATTRACTIVE BACKGROUND EVER REFLECTING DIFFERENT COLORS ✨</h1><p style="color:#00ff88;font-weight:900;font-size:13px">TIMOTHY YOUR TRUSTED ADMIN MOVING + WELCOME TO MY WEBSITE MOVING + SELAR CLICKABLE + ALL PRO - KEEP SAME</p></div>

<div class="glass"><h2 style="text-align:center;color:#f9c846">🎨 ALL SERVICES - KEEP SAME - V26 PREMIUM PRO RESTORED</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:12px"><div style="background:rgba(14,14,30,0.7);border:2px solid #00ff88;padding:12px;border-radius:16px;text-align:center"><b style="color:#00ff88;font-size:11px">📈 Trading LIVE PRO Keep BG</b><br><a href="/trading" class="btn" style="font-size:10px">ENTER</a></div><div style="background:rgba(14,14,30,0.7);border:2px solid #f9c846;padding:12px;border-radius:16px;text-align:center"><b style="color:#f9c846;font-size:11px">🌐 Website 12T PRO Keep BG</b><br><a href="/design-studio" class="btn-gold" style="font-size:10px">ENTER</a></div><div style="background:rgba(14,14,30,0.7);border:2px solid #00ff88;padding:12px;border-radius:16px;text-align:center"><b style="color:#00ff88;font-size:11px">🎨 Poster 20T PRO Keep BG</b><br><a href="/poster-maker" class="btn" style="font-size:10px">ENTER</a></div><div style="background:rgba(14,14,30,0.7);border:2px solid #f9c846;padding:12px;border-radius:16px;text-align:center"><b style="color:#f9c846;font-size:11px">🔤 Logo 100I PRO Keep BG</b><br><a href="/logo-maker" class="btn-gold" style="font-size:10px">ENTER</a></div></div></div>

<!-- TESTIMONIALS + REVIEWS KEEP SAME -->
<div class="glass" style="border:3px solid transparent;border-image:linear-gradient(90deg,#f9c846,#00ff88,#00d2ff) 1"><h2 style="text-align:center;background:linear-gradient(90deg,#f9c846,#ff9800,#00ff88);-webkit-background-clip:text;-webkit-text-fill-color:transparent">⭐ TESTIMONIALS - KEEP SAME</h2><div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:14px;margin-top:15px"><div style="background:rgba(14,14,30,0.9);padding:16px;border-radius:16px;border:1px solid rgba(249,200,70,0.3)"><b>Sarah M.</b><br><span style="color:#f9c846">⭐⭐⭐⭐⭐ 5.0</span><p style="font-size:11px;color:#ddd">"Trading signals 85% accuracy! Keep BG!"</p></div><div style="background:rgba(14,14,30,0.9);padding:16px;border-radius:16px;border:1px solid rgba(0,255,136,0.3)"><b>James K.</b><br><span style="color:#f9c846">⭐⭐⭐⭐⭐ 5.0</span><p style="font-size:11px;color:#ddd">"Website 12T $1000 quality! Keep BG!"</p></div><div style="background:rgba(14,14,30,0.9);padding:16px;border-radius:16px;border:1px solid rgba(255,0,128,0.3)"><b>Aisha W.</b><br><span style="color:#f9c846">⭐⭐⭐⭐⭐ 5.0</span><p style="font-size:11px;color:#ddd">"Poster 20T HD no watermark! Keep BG!"</p></div></div></div>

<div class="glass" style="border:3px solid transparent;border-image:linear-gradient(90deg,#00ff88,#f9c846) 1"><h2 style="text-align:center;background:linear-gradient(90deg,#00ff88,#f9c846);-webkit-background-clip:text;-webkit-text-fill-color:transparent">🌟 REVIEWS 4.9/5 - KEEP SAME</h2><p style="text-align:center;color:#00ff88;font-size:11px">4.9 Stars - 2,847 reviews - Keep BG Same</p></div>

<!-- FAQS - WHERE OTHERS ARE - KEEP ALL OTHERS SAME - JUST ADD NEW 5 FAQS BELOW EXISTING FAQS -->
<div class="glass" style="border:3px solid transparent;border-image:linear-gradient(90deg,#f9c846,#00ff88,#00d2ff,#ff00cc) 1;margin-top:20px"><h2 style="text-align:center;background:linear-gradient(90deg,#00d2ff,#00ff88,#f9c846);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-size:26px">❓ FAQS WITH ANSWERS - V26 - OLD FAQS + 5 NEW FAQS ADDED WHERE OTHERS ARE - KEEP ALL ELSE SAME</h2>
<div style="max-width:900px;margin:15px auto">

<!-- OLD FAQS KEEP SAME -->
<div class="faq-item" style="background:rgba(14,14,30,0.8);border:1px solid rgba(249,200,70,0.3);border-radius:14px;margin:10px 0;overflow:hidden"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#f9c846">1. Trading Hub Marker How Works? Keep BG? 📈</b><span style="font-size:18px">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:11px;color:#ddd">BUY @2645 -> green arrow @2645 ON chart overlay + Lot Calc Inside + Tracker 20 85% + Alert Browser Notification + VIP - Keep BG Most Attractive Same Layout</p></div></div>
<div class="faq-item" style="background:rgba(14,14,30,0.8);border:1px solid rgba(0,255,136,0.3);border-radius:14px;margin:10px 0;overflow:hidden"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#00ff88">2. Templates Count? Keep BG? 🌐🎨🔤</b><span style="font-size:18px">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:11px;color:#ddd">Website 12T, Poster 20T (Wedding 4 Birthday 4 Business 4 Church 4 School 4), Logo 100I (Business 20 Tech 20 Food 20 Shop 20 Creative 20) - Keep BG Layout Same Most Attractive Reflecting Colors</p></div></div>
<div class="faq-item" style="background:rgba(14,14,30,0.8);border:1px solid rgba(0,210,255,0.3);border-radius:14px;margin:10px 0;overflow:hidden"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#00d2ff">3. Selar Store Clickable? Keep BG? 🛒</b><span style="font-size:18px">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:11px;color:#ddd">https://selar.com/m/timothymusyoki - Clickable everywhere top banner bottom moving shop pages - Keep BG Layout Same Most Attractive Reflecting Colors</p></div></div>

<!-- NEW 5 FAQS ADDED WHERE OTHERS ARE - EXACT TEXT YOU PROVIDED - DON'T CHANGE ANYTHING ELSE -->
<div class="faq-item" style="background:linear-gradient(135deg,rgba(14,14,30,0.9),rgba(48,43,99,0.5));border:2px solid #f9c846;border-radius:14px;margin:14px 0;overflow:hidden;box-shadow:0 0 20px rgba(249,200,70,0.2)"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#f9c846">4. What digital services do you offer? ✨ NEW FAQ ADDED</b><span style="font-size:18px;color:#f9c846">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:12px;color:#ddd;line-height:1.6">We offer a wide range of digital services, including website design and development, graphic design, branding, social media content, ebooks and digital products, online-store solutions, trading tools, and customized digital solutions.</p></div></div>

<div class="faq-item" style="background:linear-gradient(135deg,rgba(14,14,30,0.9),rgba(0,255,136,0.15));border:2px solid #00ff88;border-radius:14px;margin:14px 0;overflow:hidden;box-shadow:0 0 20px rgba(0,255,136,0.2)"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#00ff88">5. Can I request a custom service? ✨ NEW FAQ ADDED</b><span style="font-size:18px;color:#00ff88">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:12px;color:#ddd;line-height:1.6">Yes. If you have a specific idea or project that isn't listed among our standard services, you can contact us and explain what you need. We can discuss a solution based on your requirements.</p></div></div>

<div class="faq-item" style="background:linear-gradient(135deg,rgba(14,14,30,0.9),rgba(0,210,255,0.15));border:2px solid #00d2ff;border-radius:14px;margin:14px 0;overflow:hidden;box-shadow:0 0 20px rgba(0,210,255,0.2)"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#00d2ff">6. How do I place an order? ✨ NEW FAQ ADDED</b><span style="font-size:18px;color:#00d2ff">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:12px;color:#ddd;line-height:1.6">Simply choose the service you are interested in and contact us with your requirements. We'll discuss the project details, provide the necessary information, and guide you through the next steps.</p></div></div>

<div class="faq-item" style="background:linear-gradient(135deg,rgba(14,14,30,0.9),rgba(255,0,128,0.15));border:2px solid #ff00cc;border-radius:14px;margin:14px 0;overflow:hidden;box-shadow:0 0 20px rgba(255,0,128,0.2)"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#ff00cc">7. How long does it take to complete a project? ✨ NEW FAQ ADDED</b><span style="font-size:18px;color:#ff00cc">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:12px;color:#ddd;line-height:1.6">The delivery time depends on the type and complexity of the project. Simple designs may be completed quickly, while larger websites, digital products, and customized solutions may require more time.</p></div></div>

<div class="faq-item" style="background:linear-gradient(135deg,rgba(14,14,30,0.9),rgba(249,200,70,0.2));border:2px solid #f9c846;border-radius:14px;margin:14px 0;overflow:hidden;box-shadow:0 0 20px rgba(249,200,70,0.3)"><div onclick="toggleFaq(this)" style="padding:14px 16px;cursor:pointer;display:flex;justify-content:space-between;align-items:center"><b style="font-size:13px;color:#f9c846">8. Can you improve or redesign my existing website or digital project? ✨ NEW FAQ ADDED</b><span style="font-size:18px;color:#f9c846">▼</span></div><div class="faq-answer" style="padding:0 16px 14px 16px;display:none"><p style="font-size:12px;color:#ddd;line-height:1.6">Yes. We can help improve an existing website or digital project by upgrading its design, layout, user experience, features, and overall presentation.</p></div></div>

</div>
<div style="text-align:center;margin-top:15px"><a href="https://selar.com/m/timothymusyoki" target="_blank" style="background:linear-gradient(90deg,#6a0dad,#f9c846,#ff9800);color:white;padding:12px 24px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block;border:2px solid white">🛒 Visit Selar Store - 5 New FAQs Added - V26</a> <a href="https://wa.me/254118431854" target="_blank" style="background:linear-gradient(90deg,#25D366,#00ff88);color:white;padding:12px 24px;border-radius:25px;text-decoration:none;font-weight:900;display:inline-block">💬 WhatsApp 0118431854</a></div>
</div>

</div>
<script>
function toggleFaq(el){let item=el.parentElement;let ans=item.querySelector('.faq-answer');let icon=el.querySelector('span');if(ans.style.display==='none' || ans.style.display===''){ans.style.display='block';icon.innerText='▲';}else{ans.style.display='none';icon.innerText='▼';}}
</script>
"""
@app.route('/trading')
def trading_hub(): return nav() + trading_p()
@app.route('/design-studio')
def design_studio(): return nav() + website_p()
@app.route('/poster-maker')
def poster_maker(): return nav() + poster_p()
@app.route('/ai-caption')
def ai_caption(): return nav() + social_p()
@app.route('/logo-maker')
def logo_maker(): return nav() + logo_p()
@app.route('/shop')
def shop_page(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>Shop - V26 5 New FAQs Added Where Others Are</h2><a href="https://selar.com/m/timothymusyoki" target="_blank" class="btn-gold">🛒 Selar Store</a><br><a href="/" class="btn">Home - 5 New FAQs Added - Keep All Same</a></div></div>'
@app.route('/admin')
def admin(): return nav() + '<div style="max-width:800px;margin:auto;padding:15px"><div class="glass" style="text-align:center"><h2>TIMOTHY YOUR TRUSTED ADMIN - V26 5 New FAQs Added Where Others Are</h2><p style="color:#00ff88">Keep All Homepage Same No Change Else - Just Add 5 New FAQs Where Others Are - Keep BG Layout Premium Pro Same</p><a href="/" class="btn-gold">Home - 5 New FAQs Added</a></div></div>'
@app.route('/api/admin-data')
def api_admin_data():
    users=load(FILES['users'],{}); fees=load(FILES['fees'],{'total':0}); orders=load(FILES['orders'],[]); prods=load(FILES['products'],[]); bundles=load(FILES['bundles'],[])
    return jsonify({'users':list(users.values()),'total_fees':fees.get('total',0),'orders':orders,'products':prods,'bundles':bundles})
if __name__=='__main__':
    app.run(host='0.0.0.0',port=10000)
