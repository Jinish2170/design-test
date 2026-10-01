B = {
 'body-sclass': '/_blob/19da95d507139f386ded00bb68fc293a', 'body-vclass': '/_blob/abbbd75f1d897d9101161db9719196cf', 'body-eqs': '/_blob/ece3adde7e8ed1c4c8e7d2dab306ca52',
 'car-sclass': '/_blob/8677e72bf12f9df38d9d902add4159a6', 'car-vclass': '/_blob/1eeeac7fd67120939a466096c1ede7b3', 'car-eqs': '/_blob/753abd4e415880613bc447611295f607',
 'mask-sclass': '/_blob/1fd7b97953a42c6538f99a5b348aa297', 'mask-vclass': '/_blob/a38e09f8f80b2f1053cc1af07e8f7744', 'mask-eqs': '/_blob/e072cfe8de8ce0058192ac3ab9542a75',
 'wheel': '/_blob/847a3b26855b906ab8cdabb89d8d3af4'}
WX = {'sclass': (300, 900), 'vclass': (300, 905), 'eqs': (300, 900)}
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&amp;family=Instrument+Serif:ital@0;1&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet">'

def car(model, alt, extra_cls='', sweep_cls='idle', style=''):
    """Layered car: body, two spinning wheels, light sweep clipped to the body."""
    wheels = ''.join(
        f'<img class="wheel" src="{B["wheel"]}" alt="" style="position: absolute; left: {(x - 62) / 12:.3f}%; top: 59.5%; width: 10.333%; height: 31%">'
        for x in WX[model])
    return (f'<div class="car {extra_cls}" style="position: relative; aspect-ratio: 3 / 1; {style}">'
            f'<img class="body" src="{B["body-" + model]}" alt="{alt}" style="position: absolute; inset: 0; width: 100%; height: 100%">'
            f'{wheels}<div class="sweep m-{model} {sweep_cls}"></div>'
            f'<img class="reflect" src="{B["car-" + model]}" alt="" style="position: absolute; left: 0; top: 88%; width: 100%; height: 100%"></div>')

CSS = f'''body{{margin:0;background:#070708}}
.abr,.abr *{{box-sizing:border-box}}
.abr{{font-family:'Archivo',system-ui,sans-serif;color:#EDEAE4;background:#070708;-webkit-font-smoothing:antialiased;overflow-x:clip;text-wrap:pretty}}
.abr a{{color:#EDEAE4;text-decoration:none}}.abr a:hover{{color:#ffffff}}
.wide{{font-stretch:125%}}
.serif{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;font-stretch:100%;letter-spacing:0;text-transform:none}}
.mono{{font-family:'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.1em;text-transform:uppercase}}
h1,h2,h3{{text-wrap:balance}}
.abr ::selection{{background:#EDEAE4;color:#070708}}
.abr :focus-visible{{outline:2px solid #DCE7FF;outline-offset:3px;border-radius:8px}}
.fld input:focus-visible,.fld select:focus-visible{{outline:none}}
.mono{{font-variant-numeric:tabular-nums}}
.grain{{position:fixed;inset:0;pointer-events:none;z-index:70;opacity:.07;mix-blend-mode:overlay;background-image:url(/_blob/6ce71ac03f6a4fa8a2c1f899febb47b2);background-size:240px 240px}}
.cta svg,.ghost svg{{transition:transform .35s cubic-bezier(.2,.7,.1,1)}}
.cta:hover svg,.ghost:hover svg{{transform:translateX(4px)}}
.fld input::-webkit-calendar-picker-indicator{{filter:invert(1);opacity:.4;cursor:pointer}}
.fld input::-webkit-calendar-picker-indicator:hover{{opacity:.8}}
/* nav: active section + scroll progress */
.navlinks a{{position:relative;transition:color .3s}}
.navlinks a::after{{content:'';position:absolute;left:0;right:0;bottom:-9px;height:1px;background:#EDEAE4;transform:scaleX(0);transform-origin:0 50%;transition:transform .45s cubic-bezier(.2,.7,.1,1)}}
.navlinks a:hover::after{{transform:scaleX(1)}}
[data-active="fleet"] .navlinks a[href="#fleet"],[data-active="services"] .navlinks a[href="#services"],[data-active="journeys"] .navlinks a[href="#journeys"],[data-active="join"] .navlinks a[href="#join"]{{color:#EDEAE4}}
[data-active="fleet"] .navlinks a[href="#fleet"]::after,[data-active="services"] .navlinks a[href="#services"]::after,[data-active="journeys"] .navlinks a[href="#journeys"]::after,[data-active="join"] .navlinks a[href="#join"]::after{{transform:scaleX(1)}}
.sprog{{position:absolute;left:0;bottom:-1px;width:100%;height:1px;background:linear-gradient(90deg,rgba(220,231,255,.2),#DCE7FF);transform-origin:0 50%;transform:scaleX(var(--sp,0));pointer-events:none}}
.mnav{{position:fixed;top:72px;left:0;right:0;bottom:0;z-index:60;background:rgba(7,7,8,.97);backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);display:flex;flex-direction:column;padding:28px 20px 36px;gap:0;overflow-y:auto}}
.mnav a.mlink{{display:flex;justify-content:space-between;align-items:center;min-height:64px;border-bottom:1px solid rgba(237,234,228,.1);font-size:30px;font-weight:700;font-stretch:125%;text-transform:uppercase;letter-spacing:-.01em}}
/* intro on load (plays once, also on the canvas) */
@keyframes rise{{from{{transform:translateY(108%)}}to{{transform:none}}}}
@keyframes fadein{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
@keyframes carin{{from{{opacity:0;transform:translateX(-5%)}}to{{opacity:1;transform:none}}}}
@keyframes ignite{{0%,40%{{opacity:0}}44%{{opacity:1}}48%{{opacity:.15}}54%{{opacity:1}}100%{{opacity:1}}}}
.h1-line{{display:block;overflow:hidden;padding-bottom:.05em;margin-bottom:-.05em}}
.h1-line > span{{display:block;animation:rise 1.15s cubic-bezier(.2,.7,.1,1) both}}
.h1-line:nth-child(2) > span{{animation-delay:.12s}}
.intro-fade{{animation:fadein 1s .55s cubic-bezier(.2,.7,.1,1) both}}
.intro-fade.d2{{animation-delay:.75s}}.intro-fade.d3{{animation-delay:.9s}}
@keyframes dockin{{from{{filter:opacity(0);translate:0 22px}}to{{filter:opacity(1);translate:0 0}}}}
.dock-in{{animation:dockin 1.1s .65s cubic-bezier(.2,.7,.1,1) backwards}}
.intro-car{{animation:carin 1.9s .2s cubic-bezier(.2,.7,.1,1) both}}
.bloom{{position:absolute;pointer-events:none;mix-blend-mode:screen}}
.bloom > i{{position:absolute;inset:0;display:block;animation:ignite 2.4s .2s both}}
.hero-stage .bloom{{opacity:calc(.45 + var(--q1) * .55)}}
.sep{{flex-shrink:0;width:22px;height:2px;border-radius:2px;align-self:center;background:#DCE7FF;opacity:.55;box-shadow:0 0 12px rgba(220,231,255,.7)}}
.sent{{display:flex;align-items:center;gap:10px;font-size:14px;color:#CFCAC2}}

/* ---------- car rig ---------- */
.car .wheel{{transform:rotate(calc(var(--spin, 0) * 1deg))}}
.sweep{{position:absolute;inset:0;pointer-events:none;mix-blend-mode:screen;background:linear-gradient(100deg,transparent 0 44%,rgba(205,222,255,.06) 47%,rgba(255,255,255,.34) 50%,rgba(205,222,255,.06) 53%,transparent 56% 100%);background-size:260% 100%;background-repeat:no-repeat;background-position:110% 0;-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat}}
.m-sclass{{-webkit-mask-image:url({B["mask-sclass"]});mask-image:url({B["mask-sclass"]})}}
.m-vclass{{-webkit-mask-image:url({B["mask-vclass"]});mask-image:url({B["mask-vclass"]})}}
.m-eqs{{-webkit-mask-image:url({B["mask-eqs"]});mask-image:url({B["mask-eqs"]})}}
.idle{{animation:idle 9s cubic-bezier(.6,0,.3,1) infinite}}
@keyframes idle{{0%{{background-position:-10% 0}}45%,100%{{background-position:110% 0}}}}
.reflect{{transform:scaleY(-1);opacity:.1;pointer-events:none;-webkit-mask-image:linear-gradient(to top,#000 0%,transparent 18%);mask-image:linear-gradient(to top,#000 0%,transparent 18%)}}

/* ---------- controls ---------- */
.tab{{font:inherit;cursor:pointer;border:1px solid rgba(237,234,228,.16);background:transparent;color:#B9B4AC;padding:0 16px;min-height:44px;border-radius:999px;font-size:13px;transition:all .25s;white-space:nowrap}}
.tab:hover{{color:#EDEAE4;border-color:rgba(237,234,228,.4)}}
.tab.on{{background:#EDEAE4;color:#070708;border-color:#EDEAE4}}
.fld{{display:flex;flex-direction:column;gap:4px;min-width:0}}
.fld label{{font-family:'IBM Plex Mono',monospace;font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:#8E8A83}}
.fld input,.fld select{{font:inherit;font-size:15px;color:#EDEAE4;background:transparent;border:0;border-bottom:1px solid rgba(237,234,228,.2);padding:6px 0 8px;min-height:44px;outline:none;color-scheme:dark;width:100%;border-radius:0}}
.fld input::placeholder{{color:#8A867F}}
.fld input:focus,.fld select:focus{{border-bottom-color:#EDEAE4}}
.cta{{display:inline-flex;align-items:center;justify-content:center;gap:12px;min-height:52px;padding:0 26px;border-radius:999px;background:#EDEAE4;color:#070708 !important;font-weight:600;font-size:15px;border:0;cursor:pointer;transition:transform .3s,background .3s;white-space:nowrap;font-family:inherit}}
.cta:hover{{background:#fff;transform:translateY(-1px)}}
.ghost{{display:inline-flex;align-items:center;gap:10px;min-height:52px;padding:0 24px;border-radius:999px;border:1px solid rgba(237,234,228,.25);font-size:15px;white-space:nowrap}}
.ghost:hover{{border-color:#EDEAE4}}

/* ---------- pinned tracks: static by default (canvas, phones), pinned only when live on desktop ---------- */
.stage{{position:relative;overflow:hidden}}
#hero{{--p:.3}}
#fleet{{--p:0}}
#services{{--p:1}}
#journeys{{--p:1}}
#finale{{--p:1}}
.marq-wrap{{--p:.25}}
@media (min-width:861px){{
  [data-live] #hero{{height:320vh}}
  [data-live] #fleet{{height:360vh}}
  [data-live] #finale{{height:200vh}}
  [data-live] #journeys{{height:250vh}}
  [data-live] .route-stage{{padding-top:clamp(28px,4vh,56px) !important;padding-bottom:clamp(28px,4vh,56px) !important}}
  [data-live] .pinned{{position:sticky;top:72px;height:calc(100vh - 72px) !important;min-height:620px !important}}
  [data-live] .fleet-row{{flex-direction:row !important;flex-shrink:0;width:300% !important;height:100%;transform:translateX(calc(var(--e) * -33.3333%))}}
  [data-live] .slide{{width:33.3333%;min-height:0 !important;border-top:0 !important;padding-top:0 !important;padding-bottom:24px !important;justify-content:center !important}}
  [data-live] .slide .car{{width:min(980px, 90%, calc((100vh - 560px) * 3)) !important}}
  [data-live] .slide .ghostname{{top:50% !important;margin-top:-140px}}
  [data-live] .slide .ghostname{{transform:translateX(calc((var(--p) * 2 - var(--i)) * -22%))}}
  [data-live] .fleet-progress{{display:flex !important}}
}}

/* ---------- 01 + 02: hero light sweep, then push through the glass ---------- */
.hero-stage{{--q1:clamp(0,calc(var(--p) / .28),1);--q2:clamp(0,calc((var(--p) - .3) / .2),1);--q3:clamp(0,calc((var(--p) - .5) / .4),1);--q4:clamp(0,calc((var(--p) - .84) / .12),1);--spin:calc(var(--q2) * 300)}}
.hero-stage .car .body{{filter:brightness(calc(.55 + var(--q1) * .45))}}
.hero-sweep{{background-position:calc(110% - var(--q1) * 120%) 0}}
.hero-type{{opacity:calc(1 - var(--q2) * 1.3);transform:translateY(calc(var(--q2) * -70px))}}
.hero-dock{{opacity:calc(1 - var(--q2) * 1.6);transform:translateY(calc(var(--q2) * 60px))}}
.hero-rig{{transform-origin:43% 34%;transform:translateX(calc(var(--q2) * -3%)) scale(calc(1 + var(--q2) * .14 + var(--q3) * var(--q3) * var(--q3) * 30))}}
.hero-pool{{opacity:calc(.55 + var(--q1) * .45 - var(--q3))}}
.hero-black{{opacity:var(--q4)}}
.hero-black span{{transform:translateY(calc((1 - var(--q4)) * 24px))}}
.hero-scrollcue{{opacity:calc(1 - var(--q2) * 3)}}

/* ---------- marquee ---------- */
.marq{{transform:translateX(calc(var(--p) * -36%));will-change:transform}}

/* ---------- 03: drive-by fleet ---------- */
.fleet-stage{{--e:clamp(0,calc((var(--p) - .06) / .82 * 2),2);--spin:calc(var(--p) * 2400)}}
.slide:nth-child(1){{--i:0}}.slide:nth-child(2){{--i:1}}.slide:nth-child(3){{--i:2}}
.seg{{flex-grow:1;height:2px;background:rgba(237,234,228,.16);position:relative;overflow:hidden}}
.seg i{{position:absolute;inset:0;background:#EDEAE4;transform-origin:0 50%}}
.seg:nth-child(1) i{{transform:scaleX(clamp(0,calc(var(--e) + .02),1))}}
.seg:nth-child(2) i{{transform:scaleX(clamp(0,calc(var(--e) - 1 + .02),1))}}
.seg:nth-child(3) i{{transform:scaleX(clamp(0,calc((var(--p) - .88) / .1),1))}}

/* ---------- services: staggered entrance + detail crops ---------- */
.svc{{opacity:clamp(0,calc(var(--p) * 3.2 - var(--i) * .45),1);transform:translateY(calc((1 - clamp(0,calc(var(--p) * 3.2 - var(--i) * .45),1)) * 36px))}}
.svc:nth-child(1){{--i:0}}.svc:nth-child(2){{--i:1}}.svc:nth-child(3){{--i:2}}.svc:nth-child(4){{--i:3}}.svc:nth-child(5){{--i:4}}
.svc .arw{{transition:transform .4s,opacity .4s;opacity:.35}}
.svc.on .arw,.svc:hover .arw{{transform:translateX(6px);opacity:1}}
.svc .stitle{{transition:color .4s}}
.svc:not(.on) .stitle{{color:#8E8A83}}
.svc.on{{border-top-color:#EDEAE4 !important}}
.crop{{position:relative;overflow:hidden;aspect-ratio:16 / 11;border-radius:20px;background:radial-gradient(80% 70% at 50% 40%,#18181c,#0a0a0c 75%);border:1px solid rgba(237,234,228,.08)}}
.crop img{{position:absolute;left:0;top:0;width:320%;max-width:none;opacity:0;transition:opacity .7s,transform 1.2s cubic-bezier(.2,.7,.1,1)}}
.crop img.on{{opacity:1}}
.c0{{transform:translate(-75%,-28.8%)}}.c0:not(.on){{transform:translate(-73%,-28.8%)}}
.c1{{transform:translate(-28.4%,-27.8%)}}.c1:not(.on){{transform:translate(-26%,-27.8%)}}
.c2{{transform:translate(-59.4%,-42.8%)}}.c2:not(.on){{transform:translate(-57%,-42.8%)}}
.c3{{transform:translate(0%,-17.8%)}}.c3:not(.on){{transform:translate(2%,-17.8%)}}
.c4{{transform:translate(-56.4%,-18.8%)}}.c4:not(.on){{transform:translate(-54%,-18.8%)}}

/* ---------- 04: route draw ---------- */
#journeys{{--q:clamp(0,calc((var(--p) - .04) / .78),1)}}
.rt-head{{--k:clamp(0,calc(var(--p) * 1.4),1)}}
.rt-line{{display:block;overflow:hidden;padding-bottom:.06em}}
.rt-line > span{{display:block;transform:translateY(calc((1 - var(--k)) * 110%));transition:transform .2s linear}}
.rt-line:nth-child(3) > span{{transform:translateY(calc((1 - clamp(0,calc(var(--k) * 1.3 - .3),1)) * 110%))}}
.rt-copy{{opacity:clamp(0,calc(var(--k) * 1.5 - .5),1)}}
.route-car{{offset-path:path("M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120");offset-distance:calc(var(--q) * 100%);offset-rotate:0deg;opacity:clamp(0,calc(var(--q) * 20),1)}}
.rt-cta{{opacity:clamp(0,calc((var(--q) - .82) * 6),1);transform:translateY(calc((1 - clamp(0,calc((var(--q) - .82) * 6),1)) * 16px))}}
.route-draw{{stroke-dasharray:1;stroke-dashoffset:calc(1 - var(--q))}}
.stop{{opacity:clamp(.2,calc((var(--q) - var(--t)) * 14 + .2),1)}}
.s1{{--t:0}}.s2{{--t:.22}}.s3{{--t:.46}}.s4{{--t:.7}}.s5{{--t:.95}}

/* ---------- 05: headlight wake ---------- */
.fin-stage{{--q:clamp(0,calc((var(--p) - .08) / .7),1)}}
.led{{opacity:clamp(0,calc(var(--q) * 3.5 - .3),1)}}
.beam{{opacity:calc(clamp(0,calc((var(--q) - .2) / .5),1) * .95);transform:scaleX(calc(.25 + var(--q) * .75)) scaleY(calc(.1 + var(--q) * .9));transform-origin:50% 0}}
.fin-type{{opacity:clamp(0,calc(var(--q) * 2.2 - .9),1);transform:translateY(calc((1 - var(--q)) * 30px))}}

@media (max-width:860px){{
  .navlinks{{display:none !important}}
  .navright{{gap:10px !important}}
  .menu{{display:inline-flex !important}}
  .hero-stage{{min-height:0 !important;padding-bottom:28px !important}}
  .hero-carzone{{position:relative !important;inset:auto !important;margin:24px 0 8px}}
  .hero-dock{{position:relative !important;left:auto !important;right:auto !important;bottom:auto !important}}
  .hero-black,.hero-scrollcue{{display:none !important}}
  .two-col{{grid-template-columns:minmax(0,1fr) !important}}
  .crop-col{{position:relative !important;top:auto !important}}
  .slide{{padding-top:100px !important;min-height:0 !important}}
  .slide .ghostname{{top:20px !important}}
}}
@media (max-width:420px){{.mark{{display:none}}.navbook{{padding:0 16px !important}}}}
@media (prefers-reduced-motion:reduce){{.idle,.h1-line > span,.intro-fade,.intro-car,.bloom > i,.dock-in{{animation:none !important}}}}
'''

def slide(i, model, num, cls, ghost, mdl, pax, best, copy):
    return f'''<article class="slide" aria-label="{cls}" style="position: relative; flex-shrink: 0; min-height: 600px; display: flex; flex-direction: column; justify-content: flex-end; align-items: center; gap: 22px; padding: 150px clamp(20px, 4vw, 56px); border-top: 1px solid rgba(237,234,228,0.08)">
<div class="ghostname wide" aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 24px; text-align: center; font-size: clamp(72px, 11vw, 168px); font-weight: 900; line-height: 1; letter-spacing: -0.03em; text-transform: uppercase; color: transparent; -webkit-text-stroke: 1px rgba(237,234,228,0.1); white-space: nowrap; pointer-events: none">{ghost}</div>
{car(model, f"{mdl} — side profile", style="width: min(980px, 94%); z-index: 1")}
<div style="position: relative; z-index: 1; width: min(980px, 100%); display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 18px 28px; align-items: end; border-top: 1px solid rgba(237,234,228,0.12); padding-top: 20px; margin-top: 30px">
<div style="display: flex; flex-direction: column; gap: 6px"><span class="mono" style="font-size: 10.5px; color: #8E8A83">{num} / 03</span><span class="wide" style="font-size: 24px; font-weight: 700; text-transform: uppercase; line-height: 1">{cls}</span></div>
<div style="display: flex; flex-direction: column; gap: 6px"><span class="mono" style="font-size: 10.5px; color: #8E8A83">Vehicle</span><span style="font-size: 15px">{mdl}</span></div>
<div style="display: flex; flex-direction: column; gap: 6px"><span class="mono" style="font-size: 10.5px; color: #8E8A83">Seats</span><span style="font-size: 15px">{pax}</span></div>
<div style="display: flex; flex-direction: column; gap: 6px"><span class="mono" style="font-size: 10.5px; color: #8E8A83">Best for</span><span style="font-size: 15px">{best}</span></div>
<a class="ghost" href="#book" style="justify-self: start; min-height: 48px">Reserve {ARROW}</a>
</div>
<p style="position: relative; z-index: 1; margin: 0; width: min(980px, 100%); font-size: 15px; line-height: 1.6; color: #A39E96">{copy}</p>
</article>'''

SVC = [
 ('01', 'Airport transfers', 'Flight tracking, meet &amp; greet at arrivals, and a car at the kerb whatever time you land.', '#book'),
 ('02', 'Hourly chauffeur', 'Your car and driver by the hour — multiple stops, back-to-back meetings, a day in the city.', '#book'),
 ('03', 'City to city', 'Long-distance transfers across the North Island, without the drive.', '#book'),
 ('04', 'Events &amp; weddings', 'Weddings, parties, red carpets and private functions — arrive the way the day deserves.', '#book'),
 ('05', 'Private tours', 'A private chauffeur, a customised itinerary and local knowledge of where to stop.', '#journeys'),
]
CROPS = [('car-sclass', 'c0', 'LED headlight detail'), ('car-sclass', 'c1', 'Door handle and chrome trim detail'), ('car-eqs', 'c2', 'Wheel detail'), ('car-vclass', 'c3', 'Rear light detail'), ('car-eqs', 'c4', 'Mirror and glasshouse detail')]

svc_rows = '\n'.join(f'''<a class="svc {{{{s{i}}}}}" href="{h}" onMouseEnter="{{{{h{i}}}}}" onFocus="{{{{h{i}}}}}" style="display: grid; grid-template-columns: 44px minmax(0, 1fr) auto; gap: 8px 20px; align-items: start; padding: 26px 4px; border-top: 1px solid rgba(237,234,228,0.12); transition: border-color .4s">
<span class="mono" style="font-size: 11px; color: #8A867F; padding-top: 8px">{n}</span>
<span style="display: flex; flex-direction: column; gap: 8px"><span class="wide stitle" style="font-size: clamp(22px, 2.4vw, 32px); font-weight: 650; text-transform: uppercase; letter-spacing: -0.01em; line-height: 1.05">{t}</span><span style="font-size: 15px; line-height: 1.6; color: #A39E96; max-width: 520px">{d}</span></span>
<span class="arw" aria-hidden="true" style="padding-top: 6px"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>
</a>''' for i, (n, t, d, h) in enumerate(SVC))
crop_imgs = ''.join(f'<img class="{c} {{{{s{i}}}}}" src="{B[m]}" alt="{a}">' for i, (m, c, a) in enumerate(CROPS))

PAD = 'clamp(20px, 4vw, 56px)'
H2 = 'margin: 0; font-size: clamp(38px, 5.4vw, 80px); line-height: 0.92; font-weight: 750; letter-spacing: -0.02em; text-transform: uppercase'

html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>All BlackRide — Home</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONTS}
<style>
{CSS}
</style>
</helmet>

<div class="abr" data-abr-root="1">
<div class="grain" aria-hidden="true"></div>

<header style="position: sticky; top: 0; z-index: 50; height: 72px; background: rgba(7,7,8,0.78); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); border-bottom: 1px solid rgba(237,234,228,0.08)">
<nav aria-label="Primary" style="max-width: 1440px; height: 72px; margin: 0 auto; padding: 0 {PAD}; display: flex; align-items: center; justify-content: space-between; gap: 24px">
<a href="#top" aria-label="All BlackRide home" style="display: flex; align-items: center; gap: 12px">
<svg class="mark" width="30" height="12" viewBox="0 0 30 12" aria-hidden="true"><path d="M1 9 C 8 4, 18 2, 29 3" fill="none" stroke="#EDEAE4" stroke-width="2" stroke-linecap="round"></path></svg>
<span style="display: flex; align-items: baseline; gap: 5px; font-size: 16px; letter-spacing: 0.08em; white-space: nowrap"><span class="wide" style="font-weight: 800">ALL BLACK</span><span class="wide" style="font-weight: 300">RIDE</span></span>
</a>
<div class="navlinks" style="display: flex; align-items: center; gap: 34px; font-size: 14px; color: #B9B4AC">
<a href="#fleet">Fleet</a><a href="#services">Services</a><a href="#journeys">Tours</a><a href="#join">Drive with us</a>
</div>
<div class="navright" style="display: flex; align-items: center; gap: 18px">
<a class="mono navlinks" href="tel:+6421595696" style="display: flex; font-size: 12px; color: #B9B4AC">+64 21 595 696</a>
<a class="cta navbook" href="#book" style="min-height: 44px; padding: 0 20px; font-size: 14px">Book a ride</a>
<button class="menu" type="button" aria-label="{{{{menuLabel}}}}" aria-expanded="{{{{menuExpanded}}}}" aria-controls="mnav" onClick="{{{{toggleMenu}}}}" style="display: none; width: 44px; height: 44px; align-items: center; justify-content: center; background: transparent; border: 1px solid rgba(237,234,228,0.2); border-radius: 999px; color: #EDEAE4; cursor: pointer"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="{{{{menuIcon}}}}"></path></svg></button>
</div>
</nav>
<span class="sprog" aria-hidden="true"></span>
</header>
<sc-if value="{{{{menuOpen}}}}" hint-placeholder-val="{{{{false}}}}">
<div class="mnav" id="mnav">
<a class="mlink" href="#fleet" onClick="{{{{closeMenu}}}}">Fleet {ARROW}</a>
<a class="mlink" href="#services" onClick="{{{{closeMenu}}}}">Services {ARROW}</a>
<a class="mlink" href="#journeys" onClick="{{{{closeMenu}}}}">Tours {ARROW}</a>
<a class="mlink" href="#join" onClick="{{{{closeMenu}}}}">Drive with us {ARROW}</a>
<div style="display: flex; flex-direction: column; gap: 12px; margin-top: 32px">
<a class="cta" href="#book" onClick="{{{{closeMenu}}}}">Book a ride</a>
<a class="ghost" href="tel:+6421595696" style="justify-content: center">Call +64 21 595 696</a>
<span class="mono" style="font-size: 10.5px; color: #8E8A83; text-align: center; margin-top: 8px">Auckland {{{{nz}}}} · on the road 24/7</span>
</div>
</div>
</sc-if>

<!-- 01 LIGHT SWEEP + 02 THROUGH THE GLASS -->
<section id="hero" data-pin="1" aria-label="Introduction">
<div id="top" class="stage pinned hero-stage" style="min-height: 860px; padding: clamp(32px, 4vw, 56px) {PAD} 0">
<div class="hero-pool" style="position: absolute; left: 50%; top: -25%; width: 130%; height: 100%; transform: translateX(-50%); background: radial-gradient(45% 50% at 50% 50%, rgba(205,218,240,0.11), rgba(205,218,240,0) 70%); pointer-events: none"></div>

<div class="hero-type" style="position: relative; z-index: 2; max-width: 1440px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 24px 48px">
<div style="display: flex; flex-direction: column; gap: 20px">
<div class="mono intro-fade" style="display: flex; flex-wrap: wrap; gap: 8px 26px; font-size: 11px; color: #8E8A83"><span>Private chauffeurs</span><span>Auckland · Aotearoa NZ</span><span style="color: #EDEAE4">● Available 24/7</span><span>Auckland {{{{nz}}}}</span></div>
<h1 class="wide" style="margin: 0; font-weight: 800; font-size: clamp(50px, 8.4vw, 132px); line-height: 0.86; letter-spacing: -0.025em; text-transform: uppercase"><span class="h1-line"><span>Arrive</span></span><span class="h1-line"><span><span class="serif" style="font-size: 1.08em; color: #CFCAC2">in</span> silence.</span></span></h1>
</div>
<p class="intro-fade d2" style="margin: 0 0 10px; max-width: 330px; font-size: 16px; line-height: 1.6; color: #A39E96">Airport transfers, hourly hire, city-to-city and private tours — in a Mercedes-Benz or BMW, with a professional chauffeur.</p>
</div>

<div class="hero-carzone" style="position: absolute; left: 0; right: 0; bottom: 196px; display: flex; justify-content: center; pointer-events: none">
<div class="hero-rig" style="position: relative; width: min(1160px, 90%, calc((100vh - 440px) * 3)); min-width: min(680px, 100%)">
{car("sclass", "Mercedes-Benz S-Class, side profile, lit by a single line of light", extra_cls="intro-car", sweep_cls="hero-sweep")}
<div class="bloom" aria-hidden="true" style="left: 82%; top: 44%; width: 14%; height: 32%"><i style="background: radial-gradient(closest-side, rgba(228,238,255,0.55), rgba(228,238,255,0.12) 50%, rgba(228,238,255,0) 100%)"></i></div>
<div class="bloom" aria-hidden="true" style="left: 4%; top: 48%; width: 13%; height: 28%"><i style="background: radial-gradient(closest-side, rgba(255,80,58,0.5), rgba(255,80,58,0.1) 50%, rgba(255,80,58,0) 100%)"></i></div>
</div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 196px; height: 1px; background: linear-gradient(90deg, rgba(237,234,228,0), rgba(237,234,228,0.18), rgba(237,234,228,0)); pointer-events: none"></div>

<form id="book" class="hero-dock dock-in" aria-label="Book a ride" onSubmit="{{{{onSubmit}}}}" style="position: absolute; z-index: 3; left: {PAD}; right: {PAD}; bottom: 28px; max-width: 1180px; margin: 0 auto; padding: 16px 22px 20px; background: rgba(16,16,19,0.86); backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px); border: 1px solid rgba(237,234,228,0.12); border-radius: 22px; display: flex; flex-direction: column; gap: 12px">
<div role="tablist" aria-label="Ride type" style="display: flex; flex-wrap: wrap; gap: 8px">
<sc-for list="{{{{tabs}}}}" as="t" hint-placeholder-count="4">
<button type="button" role="tab" aria-selected="{{{{t.sel}}}}" class="tab {{{{t.cls}}}}" onClick="{{{{t.pick}}}}">{{{{t.label}}}}</button>
</sc-for>
</div>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 150px), 1fr)); gap: 12px 24px; align-items: end">
<div class="fld"><label for="pu">Pick-up</label><input id="pu" type="text" placeholder="{{{{puHint}}}}"></div>
<div class="fld"><label for="dr">{{{{dropLabel}}}}</label><input id="dr" type="text" placeholder="{{{{dropHint}}}}"></div>
<div class="fld"><label for="dt">Date</label><input id="dt" type="date"></div>
<div class="fld"><label for="tm">Time</label><input id="tm" type="time"></div>
<div class="fld"><label for="px">Passengers</label><select id="px"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></div>
<button type="submit" class="cta" style="width: 100%">{{{{submitLabel}}}} {ARROW}</button>
</div>
<sc-if value="{{{{sent}}}}" hint-placeholder-val="{{{{false}}}}"><div class="sent" role="status"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#DCE7FF" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"></path></svg>Request received — we&#39;ll call or text to confirm your ride and price.</div></sc-if>
</form>

<div class="hero-black" aria-hidden="true" style="position: absolute; inset: 0; z-index: 4; background: #050506; display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 16px; pointer-events: none">
<span class="mono" style="font-size: 11px; color: #8E8A83">The fleet</span>
<span class="serif" style="font-size: clamp(56px, 8vw, 120px); line-height: 1">Step inside.</span>
</div>
</div>
</section>

<div class="marq-wrap" data-scene="through" style="border-top: 1px solid rgba(237,234,228,0.08); border-bottom: 1px solid rgba(237,234,228,0.08); padding: 24px 0; overflow: hidden">
<div class="marq wide" aria-label="Included with every ride" style="display: flex; gap: 40px; white-space: nowrap; font-size: clamp(22px, 2.8vw, 38px); font-weight: 300; color: #8A867F; text-transform: uppercase; width: max-content">
<span>Flight tracking</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">meet &amp; greet</span><span class="sep" aria-hidden="true"></span><span>Professional chauffeurs only</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">24 / 7</span><span class="sep" aria-hidden="true"></span><span>Auckland · Hamilton · Paihia · Rotorua · Taupō</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">door to door</span><span class="sep" aria-hidden="true"></span><span>Flight tracking</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">meet &amp; greet</span><span class="sep" aria-hidden="true"></span><span>Professional chauffeurs only</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">24 / 7</span><span class="sep" aria-hidden="true"></span><span>Auckland · Hamilton · Paihia · Rotorua · Taupō</span><span class="sep" aria-hidden="true"></span><span class="serif" style="color: #EDEAE4">door to door</span>
</div>
</div>

<!-- 03 DRIVE-BY FLEET -->
<section id="fleet" data-pin="1" aria-label="Fleet">
<div class="stage pinned fleet-stage" style="display: flex; flex-direction: column">
<div style="position: relative; z-index: 2; width: 100%; max-width: 1440px; margin: 0 auto; padding: clamp(40px, 5vw, 64px) {PAD} 16px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 20px 40px">
<h2 class="wide" style="{H2}">Three ways<br>to <span class="serif" style="font-size: 1.1em">arrive.</span></h2>
<div style="display: flex; flex-direction: column; gap: 14px; width: min(340px, 100%)">
<p style="margin: 0; font-size: 15px; line-height: 1.6; color: #A39E96">Mercedes-Benz and BMW, maintained to the highest standard. Professional chauffeurs only.</p>
<div class="fleet-progress" aria-hidden="true" style="display: none; gap: 8px"><span class="seg"><i></i></span><span class="seg"><i></i></span><span class="seg"><i></i></span></div>
</div>
</div>
<div style="position: relative; flex-grow: 1; min-height: 0; display: flex; align-items: stretch">
<div class="fleet-row" style="display: flex; flex-direction: column; width: 100%">
{slide(0, "sclass", "01", "Business Class", "Business", "Mercedes-Benz S-Class or equivalent", "Up to 3", "Airport · corporate", "The quiet back seat between the terminal and the boardroom. Discreet, punctual, exactly on time.")}
{slide(1, "vclass", "02", "First Class", "First", "Mercedes-Benz V-Class or equivalent", "Up to 6", "Groups · weddings", "Room for the whole party and their luggage — family arrivals, wedding parties and teams travelling together.")}
{slide(2, "eqs", "03", "Executive", "Executive", "Mercedes-Benz EQS or BMW i7", "[Confirm seats]", "Silent, all-electric", "Fully electric flagship saloons. The calmest way to cross the city — no engine note, just the road.")}
</div>
</div>
</div>
</section>

<!-- SERVICES -->
<section id="services" data-scene="enter" aria-label="Services" style="max-width: 1440px; margin: 0 auto; padding: clamp(90px, 10vw, 150px) {PAD}">
<div class="two-col" style="display: grid; grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr); gap: clamp(32px, 6vw, 96px); align-items: start">
<div class="crop-col" style="position: sticky; top: 112px; display: flex; flex-direction: column; gap: 28px">
<h2 class="wide" style="{H2}">Every kind<br>of <span class="serif" style="font-size: 1.1em">journey.</span></h2>
<div class="crop">{crop_imgs}<div style="position: absolute; left: 18px; bottom: 16px" class="mono"><span style="font-size: 10.5px; color: #A39E96">{{{{cropLabel}}}}</span></div></div>
</div>
<div style="display: flex; flex-direction: column; border-bottom: 1px solid rgba(237,234,228,0.12)">
{svc_rows}
</div>
</div>
</section>

<!-- 04 ROUTE DRAW -->
<section id="journeys" data-pin="1" aria-label="Tours" style="background: #0B0B0D; border-top: 1px solid rgba(237,234,228,0.06); border-bottom: 1px solid rgba(237,234,228,0.06)">
<div class="stage pinned route-stage" style="display: flex; flex-direction: column; justify-content: center; padding: clamp(90px, 10vw, 140px) 0">
<div style="width: 100%; max-width: 1440px; margin: 0 auto; padding: 0 {PAD}">
<div class="rt-head" data-scene="enter" style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: flex-end; gap: 24px; margin-bottom: 40px">
<h2 class="wide" style="{H2}"><span class="rt-line"><span>North Island,</span></span><span class="rt-line"><span class="serif" style="font-size: 1.1em">door to door.</span></span></h2>
<p class="rt-copy" style="margin: 0; max-width: 380px; font-size: 16px; line-height: 1.6; color: #A39E96">Private tours and long-distance transfers from Auckland — north to the Bay of Islands, south to the lakes.</p>
</div>
<div style="overflow-x: auto; padding-bottom: 8px">
<div style="min-width: 760px">
<svg viewBox="0 0 1200 200" width="100%" aria-hidden="true" style="display: block; overflow: visible">
<defs><linearGradient id="rt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#EDEAE4" stop-opacity=".35"></stop><stop offset="1" stop-color="#DCE7FF"></stop></linearGradient></defs>
<path d="M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120" fill="none" stroke="rgba(237,234,228,0.12)" stroke-width="1.5" stroke-dasharray="4 8"></path>
<path class="route-draw" pathLength="1" d="M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120" fill="none" stroke="url(#rt)" stroke-width="2.5" stroke-linecap="round"></path>
<g class="stop s1"><circle cx="120" cy="120" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="120" cy="120" r="5" fill="#EDEAE4"></circle></g>
<g class="stop s2"><circle cx="360" cy="70" r="22" fill="#DCE7FF" fill-opacity=".14"></circle><circle cx="360" cy="70" r="7" fill="#ffffff"></circle></g>
<g class="stop s3"><circle cx="600" cy="140" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="600" cy="140" r="5" fill="#EDEAE4"></circle></g>
<g class="stop s4"><circle cx="840" cy="60" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="840" cy="60" r="5" fill="#EDEAE4"></circle></g>
<g class="route-car"><circle r="26" fill="#DCE7FF" fill-opacity=".10"></circle><circle r="11" fill="#DCE7FF" fill-opacity=".25"></circle><circle r="4.5" fill="#ffffff"></circle></g>
<g class="stop s5"><circle cx="1080" cy="120" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="1080" cy="120" r="5" fill="#EDEAE4"></circle></g>
</svg>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 16px; margin-top: 18px; text-align: center">
<div class="stop s1" style="display: flex; flex-direction: column; gap: 6px"><span class="wide" style="font-size: 20px; font-weight: 650; text-transform: uppercase">Paihia</span><span style="font-size: 14px; color: #A39E96">Bay of Islands</span><span class="mono" style="font-size: 10.5px; color: #8E8A83">≈ 3 h north</span></div>
<div class="stop s2" style="display: flex; flex-direction: column; gap: 6px"><span class="wide" style="font-size: 20px; font-weight: 650; text-transform: uppercase">Auckland</span><span style="font-size: 14px; color: #A39E96">Home base · AKL</span><span class="mono" style="font-size: 10.5px; color: #EDEAE4">Start</span></div>
<div class="stop s3" style="display: flex; flex-direction: column; gap: 6px"><span class="wide" style="font-size: 20px; font-weight: 650; text-transform: uppercase">Hamilton</span><span style="font-size: 14px; color: #A39E96">Waikato</span><span class="mono" style="font-size: 10.5px; color: #8E8A83">≈ 1.5 h south</span></div>
<div class="stop s4" style="display: flex; flex-direction: column; gap: 6px"><span class="wide" style="font-size: 20px; font-weight: 650; text-transform: uppercase">Rotorua</span><span style="font-size: 14px; color: #A39E96">Geothermal country</span><span class="mono" style="font-size: 10.5px; color: #8E8A83">≈ 3 h south</span></div>
<div class="stop s5" style="display: flex; flex-direction: column; gap: 6px"><span class="wide" style="font-size: 20px; font-weight: 650; text-transform: uppercase">Taupō</span><span style="font-size: 14px; color: #A39E96">Lake Taupō</span><span class="mono" style="font-size: 10.5px; color: #8E8A83">≈ 3.5 h south</span></div>
</div>
</div>
</div>
<div class="rt-cta" style="display: flex; flex-wrap: wrap; gap: 14px; margin-top: 48px"><a class="cta" href="#book">Plan a private tour</a><a class="ghost" href="#book">City-to-city quote</a></div>
</div>
</div>
</section>

<!-- 05 HEADLIGHT WAKE -->
<section id="finale" data-pin="1" aria-label="Book">
<div class="stage pinned fin-stage" style="min-height: 760px; background: #050506; display: flex; flex-direction: column; align-items: center; justify-content: center">
<svg class="led" viewBox="0 0 1000 120" aria-hidden="true" style="position: absolute; left: 50%; top: 9%; width: min(1000px, 92%); transform: translateX(-50%); overflow: visible">
<path d="M 120 70 C 200 52, 300 46, 380 52" fill="none" stroke="#DCE7FF" stroke-opacity=".25" stroke-width="14" stroke-linecap="round"></path>
<path d="M 120 70 C 200 52, 300 46, 380 52" fill="none" stroke="#F4F8FF" stroke-width="3.5" stroke-linecap="round"></path>
<path d="M 880 70 C 800 52, 700 46, 620 52" fill="none" stroke="#DCE7FF" stroke-opacity=".25" stroke-width="14" stroke-linecap="round"></path>
<path d="M 880 70 C 800 52, 700 46, 620 52" fill="none" stroke="#F4F8FF" stroke-width="3.5" stroke-linecap="round"></path>
</svg>
<div class="beam" aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 11%; height: 89%; background: radial-gradient(30% 70% at 27% 0%, rgba(220,231,255,0.2), rgba(220,231,255,0) 70%), radial-gradient(30% 70% at 73% 0%, rgba(220,231,255,0.2), rgba(220,231,255,0) 70%); -webkit-mask-image: linear-gradient(to bottom, transparent, #000 22%); mask-image: linear-gradient(to bottom, transparent, #000 22%); pointer-events: none"></div>
<div class="fin-type" style="position: relative; z-index: 1; margin-top: 60px; padding: 0 20px; display: flex; flex-direction: column; align-items: center; gap: 26px; text-align: center">
<span class="mono" style="font-size: 11px; color: #A39E96">Any hour · any terminal · any occasion</span>
<h2 class="wide" style="margin: 0; font-size: clamp(42px, 6.4vw, 96px); line-height: 0.9; font-weight: 800; letter-spacing: -0.02em; text-transform: uppercase">Your car<br><span class="serif" style="font-size: 1.1em">is ready.</span></h2>
<div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 14px"><a class="cta" href="#book">Book a ride</a><a class="ghost" href="tel:+6421595696">Call +64 21 595 696</a></div>
</div>
</div>
</section>

<footer style="border-top: 1px solid rgba(237,234,228,0.08)">
<div id="join" style="max-width: 1440px; margin: 0 auto; padding: 52px {PAD}; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 24px; border-bottom: 1px solid rgba(237,234,228,0.08)">
<div style="display: flex; flex-direction: column; gap: 8px"><span class="mono" style="font-size: 11px; color: #8E8A83">Drive with us</span><span style="font-size: clamp(22px, 2.4vw, 32px); font-weight: 500">Independent chauffeur? <span class="serif" style="font-size: 1.15em">Join the network.</span></span></div>
<a class="ghost" href="#join">Apply to partner</a>
</div>
<div style="max-width: 1440px; margin: 0 auto; padding: 52px {PAD} 28px; display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 200px), 1fr)); gap: 36px; font-size: 15px; color: #A39E96">
<div style="display: flex; flex-direction: column; gap: 12px"><span class="mono" style="font-size: 10.5px; color: #8A867F">Contact</span><a href="mailto:Info@allblackride.com">Info@allblackride.com</a><a href="tel:+6421595696">+64 21 595 696</a><span>Auckland, New Zealand</span></div>
<div style="display: flex; flex-direction: column; gap: 12px"><span class="mono" style="font-size: 10.5px; color: #8A867F">Services</span><a href="#services">Airport transfers</a><a href="#services">Hourly chauffeur</a><a href="#services">City to city</a><a href="#services">Events &amp; weddings</a></div>
<div style="display: flex; flex-direction: column; gap: 12px"><span class="mono" style="font-size: 10.5px; color: #8A867F">Tours</span><a href="#journeys">Auckland</a><a href="#journeys">Hamilton</a><a href="#journeys">Paihia</a><a href="#journeys">Rotorua · Taupō</a></div>
<div style="display: flex; flex-direction: column; gap: 12px"><span class="mono" style="font-size: 10.5px; color: #8A867F">Company</span><a href="#book">Book a ride</a><a href="#fleet">Fleet</a><a href="#join">Join our team</a></div>
</div>
<div class="wide" aria-hidden="true" style="max-width: 1440px; margin: 28px auto 0; padding: 0 {PAD}; font-size: clamp(36px, 9vw, 136px); font-weight: 900; line-height: 0.82; letter-spacing: -0.03em; color: transparent; -webkit-text-stroke: 1px rgba(237,234,228,0.14); white-space: nowrap; overflow: hidden">ALL BLACK RIDE</div>
<div class="mono" style="max-width: 1440px; margin: 0 auto; padding: 22px {PAD} 34px; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; font-size: 10.5px; color: #8A867F"><span>© All BlackRide · Auckland NZ</span><span>Auckland {{{{nz}}}} · on the road 24/7</span><span style="display: flex; gap: 24px"><a href="#join" style="color: #8A867F">Privacy</a><a href="#join" style="color: #8A867F">Terms</a><a href="#top" style="color: #EDEAE4">Back to top ↑</a></span></div>
</footer>

</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1440,"height":__H__}}}}'>
class Component extends DCLogic {{
  constructor(props) {{
    super(props);
    this.state = {{ tab: 0, svc: 0, menuOpen: false, sent: false, nz: this.nzTime() }};
  }}
  nzTime() {{
    try {{ return new Intl.DateTimeFormat('en-NZ', {{ timeZone: 'Pacific/Auckland', hour: '2-digit', minute: '2-digit', hour12: false }}).format(new Date()); }} catch (e) {{ return ''; }}
  }}
  componentDidMount() {{
    this.clock = setInterval(() => {{ const nz = this.nzTime(); if (nz !== this.state.nz) this.setState({{ nz }}); }}, 15000);
    this.tick = () => {{
      if (this.raf) return;
      this.raf = requestAnimationFrame(() => {{ this.raf = null; this.update(); }});
    }};
    window.addEventListener('scroll', this.tick, {{ passive: true }});
    document.addEventListener('scroll', this.tick, {{ passive: true, capture: true }});
    window.addEventListener('resize', this.tick);
    this.update();
  }}
  componentWillUnmount() {{
    window.removeEventListener('scroll', this.tick);
    document.removeEventListener('scroll', this.tick, {{ capture: true }});
    window.removeEventListener('resize', this.tick);
    if (this.raf) cancelAnimationFrame(this.raf);
    clearInterval(this.clock);
  }}
  update() {{
    const root = document.querySelector('[data-abr-root]');
    if (!root) return;
    const vh = window.innerHeight;
    // On the canvas the frame is as tall as the page (or taller than any real screen): keep the designed rest states.
    const live = vh < 1600 && document.documentElement.scrollHeight > vh + 120;
    if (live !== root.hasAttribute('data-live')) {{
      if (live) root.setAttribute('data-live', '1'); else root.removeAttribute('data-live');
    }}
    if (!live) {{
      root.querySelectorAll('[data-pin], [data-scene]').forEach((el) => el.style.removeProperty('--p'));
      root.style.removeProperty('--sp');
      root.removeAttribute('data-active');
      return;
    }}
    const clamp = (v) => Math.max(0, Math.min(1, v));
    const doc = document.documentElement;
    root.style.setProperty('--sp', clamp(window.scrollY / Math.max(1, doc.scrollHeight - vh)).toFixed(4));
    let active = '';
    ['fleet', 'services', 'journeys', 'join'].forEach((id) => {{
      const el = document.getElementById(id);
      if (el && el.getBoundingClientRect().top < vh * 0.45) active = id;
    }});
    if (root.getAttribute('data-active') !== active) root.setAttribute('data-active', active);
    root.querySelectorAll('[data-pin]').forEach((el) => {{
      const stage = el.firstElementChild;
      const pinned = stage && getComputedStyle(stage).position === 'sticky';
      if (!pinned) {{ el.style.removeProperty('--p'); return; }}
      const r = el.getBoundingClientRect();
      const run = r.height - stage.offsetHeight;
      el.style.setProperty('--p', clamp((72 - r.top) / Math.max(1, run)).toFixed(4));
    }});
    root.querySelectorAll('[data-scene]').forEach((el) => {{
      const r = el.getBoundingClientRect();
      const p = el.getAttribute('data-scene') === 'through'
        ? clamp((vh - r.top) / (vh + r.height))
        : clamp((vh - r.top) / (vh * 0.85));
      el.style.setProperty('--p', p.toFixed(4));
    }});
  }}
  renderVals() {{
    const T = [
      {{ label: 'Airport transfer', drop: 'Drop-off', pu: 'Flight no. or address', dh: 'Address or terminal' }},
      {{ label: 'Hourly chauffeur', drop: 'Duration', pu: 'Start address', dh: 'e.g. 4 hours' }},
      {{ label: 'City to city', drop: 'Destination city', pu: 'From', dh: 'e.g. Rotorua' }},
      {{ label: 'Private tour', drop: 'Tour', pu: 'Hotel or address', dh: 'Paihia, Rotorua, Taupō…' }},
    ];
    const tab = this.state.tab;
    const svc = this.state.svc;
    const labels = ['LED headlight', 'Chrome detailing', 'Wheel &amp; brake', 'Rear light signature', 'Mirror &amp; glasshouse'];
    const v = {{
      tabs: T.map((t, i) => ({{ label: t.label, sel: i === tab ? 'true' : 'false', cls: i === tab ? 'on' : '', pick: () => this.setState({{ tab: i }}) }})),
      dropLabel: T[tab].drop, dropHint: T[tab].dh, puHint: T[tab].pu,
      nz: this.state.nz,
      menuOpen: this.state.menuOpen,
      menuExpanded: this.state.menuOpen ? 'true' : 'false',
      menuLabel: this.state.menuOpen ? 'Close menu' : 'Open menu',
      menuIcon: this.state.menuOpen ? 'M6 6l12 12M18 6L6 18' : 'M4 8h16M4 16h16',
      toggleMenu: () => this.setState({{ menuOpen: !this.state.menuOpen }}),
      closeMenu: () => this.setState({{ menuOpen: false }}),
      sent: this.state.sent,
      submitLabel: this.state.sent ? 'Request sent' : 'Get my quote',
      onSubmit: (e) => {{ e.preventDefault(); this.setState({{ sent: true }}); }},
      cropLabel: '0' + (svc + 1) + ' — ' + labels[svc].replace('&amp;', '&'),
    }};
    for (let i = 0; i < 5; i++) {{
      v['s' + i] = i === svc ? 'on' : '';
      v['h' + i] = () => {{ if (this.state.svc !== i) this.setState({{ svc: i }}); }};
    }}
    return v;
  }}
}}
</script>
</body>
</html>
'''
import sys
H = sys.argv[1] if len(sys.argv) > 1 else '6400'
open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'design', 'Main.dc.html'), 'w').write(html.replace('__H__', H))
print('written', len(html))
