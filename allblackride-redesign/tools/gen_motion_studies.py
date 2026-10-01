import json
S='/_blob/0971ac2d773b13e7762ca01a1d2e473a'; V='/_blob/039db1e074b8c6e65caa4478426dba6c'; E='/_blob/561a1839b88234038cfc4784725fcd5c'
MS='/_blob/ee2bc438c8b9af6837a9fc734d6bc895'; MV='/_blob/07553efac52a43f3655f0318f1a239fe'; ME='/_blob/73528bf2b51631a6bf33736e15013ffc'
ARROW='<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'

BASE_CSS = f'''body{{margin:0;background:#070708}}
.st,.st *{{box-sizing:border-box}}
.st{{font-family:'Archivo',system-ui,sans-serif;color:#EDEAE4;-webkit-font-smoothing:antialiased}}
.wide{{font-stretch:125%}}
.serif{{font-family:'Instrument Serif',Georgia,serif;font-style:italic;font-weight:400;font-stretch:100%}}
.mono{{font-family:'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase}}
.sweep{{position:absolute;inset:0;pointer-events:none;mix-blend-mode:screen;background:linear-gradient(100deg,transparent 0 44%,rgba(205,222,255,.06) 47%,rgba(255,255,255,.36) 50%,rgba(205,222,255,.06) 53%,transparent 56% 100%);background-size:260% 100%;background-repeat:no-repeat;-webkit-mask-size:100% 100%;mask-size:100% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat}}
.m-s{{-webkit-mask-image:url({MS});mask-image:url({MS})}}
.m-v{{-webkit-mask-image:url({MV});mask-image:url({MV})}}
.m-e{{-webkit-mask-image:url({ME});mask-image:url({ME})}}
.reflect{{transform:scaleY(-1);opacity:.1;-webkit-mask-image:linear-gradient(to top,#000 0%,transparent 18%);mask-image:linear-gradient(to top,#000 0%,transparent 18%)}}
.scrub{{-webkit-appearance:none;appearance:none;flex-grow:1;height:44px;background:transparent;cursor:pointer;margin:0}}
.scrub::-webkit-slider-runnable-track{{height:2px;background:rgba(237,234,228,.22);border-radius:2px}}
.scrub::-webkit-slider-thumb{{-webkit-appearance:none;width:18px;height:18px;border-radius:50%;background:#EDEAE4;margin-top:-8px;box-shadow:0 0 0 6px rgba(237,234,228,.12)}}
.scrub::-moz-range-track{{height:2px;background:rgba(237,234,228,.22)}}
.scrub::-moz-range-thumb{{width:18px;height:18px;border-radius:50%;background:#EDEAE4;border:0}}
.play{{font:inherit;font-size:13px;min-height:44px;min-width:96px;padding:0 18px;border-radius:999px;border:1px solid rgba(237,234,228,.25);background:transparent;color:#EDEAE4;cursor:pointer;display:inline-flex;align-items:center;justify-content:center;gap:8px}}
.play:hover{{border-color:#EDEAE4}}
.key{{font:inherit;text-align:left;cursor:pointer;background:transparent;border:0;border-top:1px solid rgba(237,234,228,.14);color:#6F6B65;padding:12px 0 0;min-height:44px;display:flex;flex-direction:column;gap:6px;transition:color .3s,border-color .3s}}
.key.on{{color:#EDEAE4;border-top-color:#EDEAE4}}
.key:hover{{color:#CFCAC2}}
@media (prefers-reduced-motion:reduce){{*{{transition:none !important;animation:none !important}}}}
'''

def board(num, title, sub, default, keys, stage_css, stage_html):
    keys_json = json.dumps(keys)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Motion {num} — {title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&amp;family=Instrument+Serif:ital@0;1&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap" rel="stylesheet">
<style>
{BASE_CSS}
[data-stage]{{--p:{default}}}
{stage_css}
</style>
</helmet>
<div class="st" style="width: 1200px; height: 780px; background: #070708; padding: 32px 32px 28px; display: flex; flex-direction: column; gap: 20px">
<div style="display: flex; justify-content: space-between; align-items: baseline; gap: 24px">
<div style="display: flex; align-items: baseline; gap: 18px">
<span class="mono" style="font-size: 11px; color: #8E8A83">Motion {num}</span>
<h1 class="wide" style="margin: 0; font-size: 26px; font-weight: 700; text-transform: uppercase; letter-spacing: -0.01em">{title}</h1>
</div>
<span class="mono" style="font-size: 11px; color: #8E8A83">{sub}</span>
</div>
<div data-stage="1" style="position: relative; height: 520px; border-radius: 22px; overflow: hidden; background: #050506; border: 1px solid rgba(237,234,228,0.08)">
{stage_html}
</div>
<div style="display: flex; align-items: center; gap: 18px">
<button type="button" class="play" onClick="{{{{onPlay}}}}">{{{{playLabel}}}}</button>
<label for="scrub" class="mono" style="font-size: 10.5px; color: #8E8A83; white-space: nowrap">Scroll</label>
<input id="scrub" class="scrub" type="range" min="0" max="1000" step="1" value="{{{{pct}}}}" onChange="{{{{onScrub}}}}">
<span class="mono" style="font-size: 12px; width: 48px; text-align: right">{{{{pctLabel}}}}</span>
</div>
<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px">
<sc-for list="{{{{keys}}}}" as="k" hint-placeholder-count="4">
<button type="button" class="key {{{{k.cls}}}}" onClick="{{{{k.go}}}}"><span class="mono" style="font-size: 10.5px">{{{{k.label}}}}</span><span style="font-size: 13px; line-height: 1.4">{{{{k.text}}}}</span></button>
</sc-for>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1200,"height":780}}}}'>
class Component extends DCLogic {{
  constructor(props) {{
    super(props);
    this.state = {{ p: {default}, playing: false }};
  }}
  componentDidMount() {{ this.apply(); }}
  componentDidUpdate() {{ this.apply(); }}
  componentWillUnmount() {{ if (this.raf) cancelAnimationFrame(this.raf); }}
  apply() {{
    const el = document.querySelector('[data-stage]');
    if (el) el.style.setProperty('--p', this.state.p.toFixed(4));
  }}
  stop() {{ if (this.raf) cancelAnimationFrame(this.raf); this.raf = null; }}
  play() {{
    if (this.state.playing) {{ this.stop(); this.setState({{ playing: false }}); return; }}
    const from = this.state.p >= 0.995 ? 0 : this.state.p;
    const start = performance.now();
    const loop = (t) => {{
      const p = Math.min(1, from + (t - start) / 4500);
      this.setState({{ p, playing: p < 1 }});
      if (p < 1) this.raf = requestAnimationFrame(loop);
    }};
    this.setState({{ playing: true }});
    this.raf = requestAnimationFrame(loop);
  }}
  renderVals() {{
    const p = this.state.p;
    const K = {keys_json};
    return {{
      pct: Math.round(p * 1000),
      pctLabel: Math.round(p * 100) + '%',
      playLabel: this.state.playing ? 'Pause' : 'Play',
      onPlay: () => this.play(),
      onScrub: (e) => {{ this.stop(); this.setState({{ p: Number(e.target.value) / 1000, playing: false }}); }},
      keys: K.map((k) => ({{ label: Math.round(k.at * 100) + '%', text: k.text, cls: p >= k.at - 0.001 ? 'on' : '', go: () => {{ this.stop(); this.setState({{ p: k.at, playing: false }}); }} }})),
    }};
  }}
}}
</script>
</body>
</html>
'''

files = {}

# 01 LIGHT SWEEP
files['Motion1-LightSweep.dc.html'] = board('01','Light sweep','Hero · scroll 0 → 85% of hero height', .42,
 [{"at":0,"text":"Car sits in darkness; only the LED line and tail lamp read."},{"at":.3,"text":"A soft-box band enters at the nose and travels the roofline."},{"at":.6,"text":"Body fully described; headline begins to lift away."},{"at":.9,"text":"Car drives forward and scales — hand-off to the booking console."}],
 '''.ls-dark{filter:brightness(calc(.35 + var(--p) * .9))}
.ls-band{background-position:calc(110% - var(--p) * 120%) 0}
.ls-car{transform:translate3d(calc(clamp(0,calc((var(--p) - .6) / .4),1) * 18%),0,0) scale(calc(1 + clamp(0,calc((var(--p) - .6) / .4),1) * .1))}
.ls-type{opacity:calc(1 - clamp(0,calc((var(--p) - .5) / .4),1));transform:translateY(calc(clamp(0,calc((var(--p) - .5) / .4),1) * -60px))}
.ls-pool{opacity:calc(.2 + var(--p) * .8)}''',
 f'''<div class="ls-pool" style="position: absolute; left: 50%; top: -30%; width: 110%; height: 100%; transform: translateX(-50%); background: radial-gradient(45% 45% at 50% 50%, rgba(205,218,240,0.12), rgba(205,218,240,0) 70%)"></div>
<div class="ls-type" style="position: absolute; left: 44px; top: 40px; display: flex; flex-direction: column; gap: 14px">
<span class="mono" style="font-size: 11px; color: #8E8A83">Private chauffeurs · Auckland</span>
<span class="wide" style="font-size: 84px; font-weight: 800; line-height: 0.88; text-transform: uppercase; letter-spacing: -0.02em">Arrive<br><span class="serif" style="text-transform: none; color: #CFCAC2">in</span> silence.</span>
</div>
<div class="ls-car" style="position: absolute; left: 50%; bottom: 46px; width: 980px; margin-left: -490px; aspect-ratio: 3 / 1">
<img class="ls-dark" src="{S}" alt="S-Class silhouette" style="position: absolute; inset: 0; width: 100%; height: 100%">
<div class="sweep m-s ls-band"></div>
<img class="reflect" src="{S}" alt="" style="position: absolute; left: 0; top: 90%; width: 100%; height: 100%">
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 46px; height: 1px; background: linear-gradient(90deg, rgba(237,234,228,0), rgba(237,234,228,0.2), rgba(237,234,228,0))"></div>''')

# 02 THROUGH THE GLASS
files['Motion2-ThroughTheGlass.dc.html'] = board('02','Through the glass','Hero → Fleet transition · sticky 150vh', .35,
 [{"at":0,"text":"Hero at rest: car side-on, headline above."},{"at":.35,"text":"Camera pushes in toward the rear side window."},{"at":.7,"text":"The tinted glass fills the frame — a black wipe made of the car itself."},{"at":1,"text":"Next section is revealed behind the glass: the fleet."}],
 '''[data-stage]{--z:clamp(0,calc(var(--p) / .8),1)}
.tg-car{transform-origin:42% 47%;transform:scale(calc(1 + var(--z) * var(--z) * var(--z) * 26));opacity:calc(1 - clamp(0,calc((var(--p) - .82) / .12),1))}
.tg-type{opacity:calc(1 - var(--p) * 3)}
.tg-next{opacity:clamp(0,calc((var(--p) - .78) / .2),1);transform:scale(calc(1.08 - clamp(0,calc((var(--p) - .78) / .2),1) * .08))}''',
 f'''<div class="tg-next" style="position: absolute; inset: 0; background: radial-gradient(70% 60% at 50% 45%, #17171b, #0b0b0d 70%); display: flex; flex-direction: column; justify-content: center; padding: 0 56px; gap: 18px">
<span class="mono" style="font-size: 11px; color: #8E8A83">01 / 03 — Business Class</span>
<span class="wide" style="font-size: 72px; font-weight: 700; line-height: 0.92; text-transform: uppercase; letter-spacing: -0.02em">Three ways<br>to <span class="serif" style="text-transform: none">arrive.</span></span>
<img src="{V}" alt="V-Class silhouette" style="position: absolute; right: -40px; bottom: 40px; width: 640px">
</div>
<div class="tg-type" style="position: absolute; left: 44px; top: 40px; z-index: 2">
<span class="wide" style="font-size: 64px; font-weight: 800; line-height: 0.9; text-transform: uppercase; letter-spacing: -0.02em">Arrive<br><span class="serif" style="text-transform: none; color: #CFCAC2">in</span> silence.</span>
</div>
<div class="tg-car" style="position: absolute; inset: 0; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 40px">
<div style="position: relative; width: 980px; aspect-ratio: 3 / 1">
<img src="{S}" alt="S-Class silhouette" style="position: absolute; inset: 0; width: 100%; height: 100%">
</div>
</div>''')

# 03 DRIVE-BY FLEET
files['Motion3-DriveBy.dc.html'] = board('03','Drive-by fleet','Fleet · horizontal track pinned for 300vh', .5,
 [{"at":0,"text":"Business Class enters from the left, name set in outline behind."},{"at":.33,"text":"Cars move at road speed; the class names drift at half speed (parallax)."},{"at":.66,"text":"First Class takes the frame; spec readout swaps in place."},{"at":1,"text":"Executive arrives last and parks; the track releases."}],
 '''.db-cars{transform:translateX(calc(var(--p) * -66.6667%))}
.db-names{transform:translateX(calc(var(--p) * -33.3333%))}
.db-blur{filter:blur(calc(sin(var(--p) * 3.1416 * 3) * sin(var(--p) * 3.1416 * 3) * 1.6px))}''',
 f'''<div class="db-names" style="position: absolute; top: 40px; left: 0; display: flex; width: 300%; white-space: nowrap">
<span class="wide" style="width: 33.333%; text-align: center; font-size: 120px; font-weight: 900; line-height: 1; text-transform: uppercase; color: transparent; -webkit-text-stroke: 1px rgba(237,234,228,0.16)">Business</span>
<span class="wide" style="width: 33.333%; text-align: center; font-size: 120px; font-weight: 900; line-height: 1; text-transform: uppercase; color: transparent; -webkit-text-stroke: 1px rgba(237,234,228,0.16)">First</span>
<span class="wide" style="width: 33.333%; text-align: center; font-size: 120px; font-weight: 900; line-height: 1; text-transform: uppercase; color: transparent; -webkit-text-stroke: 1px rgba(237,234,228,0.16)">Executive</span>
</div>
<div class="db-cars db-blur" style="position: absolute; left: 0; bottom: 60px; width: 300%; display: flex">
<div style="width: 33.333%; display: flex; flex-direction: column; align-items: center; gap: 14px"><div style="position: relative; width: 860px; aspect-ratio: 3 / 1"><img src="{S}" alt="S-Class" style="position: absolute; inset: 0; width: 100%; height: 100%"></div><span class="mono" style="font-size: 11px; color: #A39E96">01 · S-Class · up to 3</span></div>
<div style="width: 33.333%; display: flex; flex-direction: column; align-items: center; gap: 14px"><div style="position: relative; width: 860px; aspect-ratio: 3 / 1"><img src="{V}" alt="V-Class" style="position: absolute; inset: 0; width: 100%; height: 100%"></div><span class="mono" style="font-size: 11px; color: #A39E96">02 · V-Class · up to 6</span></div>
<div style="width: 33.333%; display: flex; flex-direction: column; align-items: center; gap: 14px"><div style="position: relative; width: 860px; aspect-ratio: 3 / 1"><img src="{E}" alt="EQS" style="position: absolute; inset: 0; width: 100%; height: 100%"></div><span class="mono" style="font-size: 11px; color: #A39E96">03 · EQS / i7 · electric</span></div>
</div>
<div style="position: absolute; left: 0; right: 0; bottom: 100px; height: 1px; background: rgba(237,234,228,0.1)"></div>''')

# 04 ROUTE DRAW
files['Motion4-RouteDraw.dc.html'] = board('04','Route draw','Tours · draws as section crosses viewport', .55,
 [{"at":0,"text":"Dashed ghost road only; destinations dimmed."},{"at":.3,"text":"Line draws from Paihia; Auckland lights as home base."},{"at":.6,"text":"Hamilton and Rotorua ignite as the line reaches them."},{"at":.9,"text":"Taupō reached; tour CTA becomes active."}],
 '''[data-stage]{--q:clamp(0,calc(var(--p) / .9),1)}
.route-draw{stroke-dasharray:1;stroke-dashoffset:calc(1 - var(--q))}
.stop{opacity:clamp(.18,calc((var(--q) - var(--t)) * 14 + .18),1)}
.s1{--t:0}.s2{--t:.22}.s3{--t:.46}.s4{--t:.7}.s5{--t:.95}
.rd-cta{opacity:clamp(.3,calc((var(--q) - .9) * 10 + .3),1)}''',
 '''<div style="position: absolute; left: 44px; top: 40px">
<span class="wide" style="font-size: 52px; font-weight: 700; line-height: 0.92; text-transform: uppercase; letter-spacing: -0.02em">North Island,<br><span class="serif" style="text-transform: none">door to door.</span></span>
</div>
<div style="position: absolute; left: 20px; right: 20px; top: 210px">
<svg viewBox="0 0 1200 200" width="100%" aria-hidden="true" style="display: block; overflow: visible">
<defs><linearGradient id="rt" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#EDEAE4" stop-opacity=".35"></stop><stop offset="1" stop-color="#DCE7FF"></stop></linearGradient></defs>
<path d="M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120" fill="none" stroke="rgba(237,234,228,0.12)" stroke-width="1.5" stroke-dasharray="4 8"></path>
<path class="route-draw" pathLength="1" d="M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120" fill="none" stroke="url(#rt)" stroke-width="2.5" stroke-linecap="round"></path>
<g class="stop s1"><circle cx="120" cy="120" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="120" cy="120" r="5" fill="#EDEAE4"></circle></g>
<g class="stop s2"><circle cx="360" cy="70" r="22" fill="#DCE7FF" fill-opacity=".14"></circle><circle cx="360" cy="70" r="7" fill="#ffffff"></circle></g>
<g class="stop s3"><circle cx="600" cy="140" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="600" cy="140" r="5" fill="#EDEAE4"></circle></g>
<g class="stop s4"><circle cx="840" cy="60" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="840" cy="60" r="5" fill="#EDEAE4"></circle></g>
<g class="stop s5"><circle cx="1080" cy="120" r="16" fill="#DCE7FF" fill-opacity=".12"></circle><circle cx="1080" cy="120" r="5" fill="#EDEAE4"></circle></g>
</svg>
<div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; margin-top: 10px; text-align: center">
<div class="stop s1" style="display: flex; flex-direction: column; gap: 4px"><span class="wide" style="font-size: 18px; font-weight: 600; text-transform: uppercase">Paihia</span><span class="mono" style="font-size: 10px; color: #8E8A83">≈ 3 h north</span></div>
<div class="stop s2" style="display: flex; flex-direction: column; gap: 4px"><span class="wide" style="font-size: 18px; font-weight: 600; text-transform: uppercase">Auckland</span><span class="mono" style="font-size: 10px; color: #EDEAE4">Home base</span></div>
<div class="stop s3" style="display: flex; flex-direction: column; gap: 4px"><span class="wide" style="font-size: 18px; font-weight: 600; text-transform: uppercase">Hamilton</span><span class="mono" style="font-size: 10px; color: #8E8A83">≈ 1.5 h south</span></div>
<div class="stop s4" style="display: flex; flex-direction: column; gap: 4px"><span class="wide" style="font-size: 18px; font-weight: 600; text-transform: uppercase">Rotorua</span><span class="mono" style="font-size: 10px; color: #8E8A83">≈ 3 h south</span></div>
<div class="stop s5" style="display: flex; flex-direction: column; gap: 4px"><span class="wide" style="font-size: 18px; font-weight: 600; text-transform: uppercase">Taupō</span><span class="mono" style="font-size: 10px; color: #8E8A83">≈ 3.5 h south</span></div>
</div>
</div>
<a class="rd-cta" href="#" style="position: absolute; right: 44px; top: 52px; display: inline-flex; align-items: center; gap: 10px; min-height: 48px; padding: 0 22px; border-radius: 999px; background: #EDEAE4; color: #070708; font-weight: 600; font-size: 14px; text-decoration: none">Plan a private tour ''' + ARROW + '''</a>''')

# 05 HEADLIGHT WAKE
files['Motion5-HeadlightWake.dc.html'] = board('05','Headlight wake','Final CTA · sticky 120vh', .6,
 [{"at":0,"text":"Total black. The page goes quiet before the ask."},{"at":.25,"text":"Two LED brows ignite — the car, head-on, waking up."},{"at":.6,"text":"Beams open across the floor, lighting the headline."},{"at":.9,"text":"Book + call CTAs reach full contrast inside the light."}],
 '''[data-stage]{--q:clamp(0,calc(var(--p) / .85),1)}
.led{opacity:clamp(0,calc(var(--q) * 3.5 - .5),1)}
.beam{opacity:calc(clamp(0,calc((var(--q) - .2) / .5),1) * .95);transform:scaleX(calc(.25 + var(--q) * .75)) scaleY(calc(.1 + var(--q) * .9));transform-origin:50% 0}
.fin-type{opacity:clamp(0,calc(var(--q) * 2.2 - .9),1);transform:translateY(calc((1 - var(--q)) * 30px))}''',
 '''<svg class="led" viewBox="0 0 1000 120" aria-hidden="true" style="position: absolute; left: 100px; top: 40px; width: 1000px; overflow: visible">
<path d="M 120 70 C 200 52, 300 46, 380 52" fill="none" stroke="#DCE7FF" stroke-opacity=".25" stroke-width="14" stroke-linecap="round"></path>
<path d="M 120 70 C 200 52, 300 46, 380 52" fill="none" stroke="#F4F8FF" stroke-width="3.5" stroke-linecap="round"></path>
<path d="M 880 70 C 800 52, 700 46, 620 52" fill="none" stroke="#DCE7FF" stroke-opacity=".25" stroke-width="14" stroke-linecap="round"></path>
<path d="M 880 70 C 800 52, 700 46, 620 52" fill="none" stroke="#F4F8FF" stroke-width="3.5" stroke-linecap="round"></path>
</svg>
<div class="beam" style="position: absolute; top: 96px; left: 0; width: 100%; height: 440px; background: radial-gradient(30% 70% at 27% 0%, rgba(220,231,255,0.22), rgba(220,231,255,0) 70%), radial-gradient(30% 70% at 73% 0%, rgba(220,231,255,0.22), rgba(220,231,255,0) 70%)"></div>
<div class="fin-type" style="position: absolute; left: 0; right: 0; top: 190px; display: flex; flex-direction: column; align-items: center; gap: 24px; text-align: center">
<span class="mono" style="font-size: 11px; color: #A39E96">Any hour · any terminal · any occasion</span>
<span class="wide" style="font-size: 76px; font-weight: 800; line-height: 0.92; text-transform: uppercase; letter-spacing: -0.02em">Your car<br><span class="serif" style="text-transform: none">is ready.</span></span>
<div style="display: flex; gap: 12px"><a href="#" style="display: inline-flex; align-items: center; min-height: 48px; padding: 0 22px; border-radius: 999px; background: #EDEAE4; color: #070708; font-weight: 600; font-size: 14px; text-decoration: none">Book a ride</a><a href="tel:+6421595696" style="display: inline-flex; align-items: center; min-height: 48px; padding: 0 22px; border-radius: 999px; border: 1px solid rgba(237,234,228,0.25); color: #EDEAE4; font-size: 14px; text-decoration: none">Call +64 21 595 696</a></div>
</div>''')

for n, c in files.items():
    open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'design', n), 'w').write(c)
print(list(files))
