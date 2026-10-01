import math, json
def arches(xs, cy=306, r=76, y=320):
    d = math.sqrt(r*r-(y-cy)**2)
    return [(x+d, x-d) for x in xs]
def bottom(front_end, xs):
    (f1,f2),(r1,r2) = arches(xs)[::-1]
    return f"L {f1:.1f} 320 A 76 76 0 1 0 {f2:.1f} 320 L {r1:.1f} 320 A 76 76 0 1 0 {r2:.1f} 320 Z"
CARS = {
 "sclass": dict(xs=(300,900),
  top="M 108 316 C 98 300, 96 280, 102 262 L 110 236 C 114 226, 128 220, 160 217 L 236 212 C 290 196, 350 156, 430 136 C 510 118, 640 116, 712 124 C 770 132, 820 170, 862 202 C 930 210, 1010 218, 1066 230 C 1094 236, 1104 252, 1104 274 C 1104 298, 1096 312, 1080 318",
  glass="M 262 208 C 322 170, 380 148, 440 140 C 525 128, 640 128, 702 136 C 750 144, 790 172, 822 202 Z",
  pillars=[(352,5),(575,7)], belt=208, doors=[352,575,818],
  shoulder="M 104 254 C 400 246, 800 240, 1100 250",
  mirror="M 806 208 C 810 196, 834 190, 848 196 L 846 210 Z",
  head="M 1028 232 C 1060 234, 1088 240, 1101 252 L 1099 263 C 1080 257, 1052 251, 1024 247 Z", led="M 1030 233 C 1060 235, 1088 241, 1100 252",
  tail="M 103 246 L 162 238 L 164 251 L 105 259 Z"),
 "vclass": dict(xs=(300,905),
  top="M 106 316 C 96 300, 96 276, 100 256 L 108 150 C 110 126, 124 114, 156 112 L 770 108 C 808 108, 836 122, 864 150 L 944 208 C 1004 220, 1062 232, 1088 248 C 1102 262, 1102 298, 1084 318",
  glass="M 136 200 L 141 138 C 142 130, 148 126, 162 126 L 760 122 C 796 122, 818 136, 840 158 L 904 206 Z",
  pillars=[(340,9),(575,9),(792,8)], belt=204, doors=[340,575,800],
  shoulder="M 102 236 C 400 230, 800 228, 1094 254",
  mirror="M 900 208 C 904 196, 928 190, 942 196 L 940 212 Z",
  head="M 1040 236 C 1068 240, 1090 248, 1099 260 L 1097 270 C 1080 264, 1058 256, 1036 250 Z", led="M 1042 237 C 1068 241, 1090 249, 1098 260",
  tail="M 100 168 L 112 168 L 110 238 L 99 238 Z"),
 "eqs": dict(xs=(300,900),
  top="M 110 316 C 98 300, 98 280, 104 264 C 116 248, 160 236, 224 228 C 334 162, 444 122, 604 118 C 724 116, 824 160, 904 206 C 980 222, 1052 236, 1088 252 C 1104 266, 1104 300, 1084 318",
  glass="M 258 222 C 346 168, 454 134, 604 130 C 704 128, 794 168, 862 208 Z",
  pillars=[(362,6),(590,7)], belt=214, doors=[362,590,850],
  shoulder="M 106 266 C 400 254, 800 248, 1100 262",
  mirror="M 846 212 C 850 200, 874 194, 888 200 L 886 214 Z",
  head="M 1040 240 C 1068 244, 1092 254, 1101 266 L 1099 274 C 1082 268, 1060 260, 1036 254 Z", led="M 1042 241 C 1068 245, 1092 255, 1100 266",
  tail="M 105 262 C 160 252, 200 246, 240 240 L 242 248 C 200 254, 160 260, 107 270 Z"),
}
WHEEL_DEFS = '''<radialGradient id="tire" cx="0.5" cy="0.5" r="0.5"><stop offset="0.7" stop-color="#050506"/><stop offset="0.9" stop-color="#18181b"/><stop offset="1" stop-color="#0a0a0b"/></radialGradient>
<linearGradient id="spoke" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e4e7ec"/><stop offset="0.5" stop-color="#8a8e96"/><stop offset="1" stop-color="#3a3c41"/></linearGradient>
<linearGradient id="lip" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f2f4f7"/><stop offset="0.45" stop-color="#6d7178"/><stop offset="1" stop-color="#2a2b2f"/></linearGradient>
<radialGradient id="barrel" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#1d1e22"/><stop offset="1" stop-color="#08080a"/></radialGradient>'''
def wheel_group():
    s = ['<circle r="60" fill="url(#tire)"/>',
         '<path d="M -50 -26 A 56 56 0 0 1 22 -52" fill="none" stroke="#fff" stroke-opacity="0.16" stroke-width="2.5" stroke-linecap="round"/>',
         '<circle r="44" fill="url(#barrel)"/>',
         '<circle r="31" fill="#141518" stroke="#2c2d31" stroke-width="1"/>',
         '<path d="M -26 -14 A 30 30 0 0 1 -6 -29 L -4 -21 A 22 22 0 0 0 -19 -10 Z" fill="#3b3d42"/>']
    for i in range(5):
        a = i*72
        for off in (-7, 7):
            s.append(f'<path transform="rotate({a+off})" d="M -2.6 -10 L 2.6 -10 L 4.2 -41 L -4.2 -41 Z" fill="url(#spoke)"/>')
    s += ['<circle r="42" fill="none" stroke="url(#lip)" stroke-width="3.2"/>',
          '<circle r="44.5" fill="none" stroke="#000" stroke-opacity="0.6" stroke-width="1.2"/>',
          '<circle r="10" fill="#1c1d21" stroke="url(#lip)" stroke-width="1.6"/>',
          '<circle r="3.2" fill="#9aa0a8"/>']
    return "\n".join(s)

BODY_DEFS = '''<linearGradient id="bodyg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#202126"/><stop offset="0.35" stop-color="#0b0b0d"/><stop offset="0.72" stop-color="#060607"/><stop offset="1" stop-color="#0e0e11"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity="0.20"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="horizon" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfd8e6" stop-opacity="0"/><stop offset="0.5" stop-color="#cfd8e6" stop-opacity="0.085"/><stop offset="1" stop-color="#cfd8e6" stop-opacity="0"/></linearGradient>
<linearGradient id="falloff" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0.55"/><stop offset="0.35" stop-color="#000" stop-opacity="0"/><stop offset="0.7" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.45"/></linearGradient>
<linearGradient id="glassg" x1="0" y1="0" x2="0.4" y2="1"><stop offset="0" stop-color="#1a2130"/><stop offset="0.5" stop-color="#0b0e14"/><stop offset="1" stop-color="#05060a"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8d929b" stop-opacity="0.5"/><stop offset="0.55" stop-color="#eef1f5"/><stop offset="1" stop-color="#7c818a" stop-opacity="0.6"/></linearGradient>
<linearGradient id="rimlight" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.3" stop-color="#fff" stop-opacity="0.22"/><stop offset="0.58" stop-color="#fff" stop-opacity="0.95"/><stop offset="0.8" stop-color="#fff" stop-opacity="0.3"/><stop offset="1" stop-color="#fff" stop-opacity="0.05"/></linearGradient>
<linearGradient id="shoulder" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0.04"/><stop offset="0.62" stop-color="#fff" stop-opacity="0.55"/><stop offset="1" stop-color="#fff" stop-opacity="0.1"/></linearGradient>
<linearGradient id="tailg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff6a50"/><stop offset="1" stop-color="#9a1408"/></linearGradient>
<radialGradient id="shadow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000" stop-opacity="0.95"/><stop offset="0.7" stop-color="#000" stop-opacity="0.6"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>'''

def build(name, c, with_wheels):
    body = c["top"] + " " + bottom(None, c["xs"])
    xs = c["xs"]
    liners = "".join(f'<circle cx="{x}" cy="306" r="75" fill="#020203"/>' for x in xs)
    doors = "".join(f'<path d="M {x} {c["belt"]+2} C {x+2} 250, {x+3} 290, {x+2} 318" fill="none" stroke="#000" stroke-width="2.2"/><path d="M {x+2} {c["belt"]+2} C {x+4} 250, {x+5} 290, {x+4} 318" fill="none" stroke="#fff" stroke-opacity="0.06" stroke-width="1"/>' for x in c["doors"])
    handles = "".join(f'<rect x="{x-70}" y="{c["belt"]+24}" width="38" height="5" rx="2.5" fill="#0a0a0c" stroke="url(#chrome)" stroke-width="0.9"/>' for x in c["doors"][1:])
    pillars = "".join(f'<rect x="{x-w}" y="100" width="{2*w}" height="130" fill="#030304"/>' for x,w in c["pillars"])
    b = c["belt"]
    wheels = ""
    if with_wheels:
        wheels = "".join(f'<g transform="translate({x} 300)">{wheel_group()}</g>' for x in xs)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400">
<defs>{BODY_DEFS}{WHEEL_DEFS}
<clipPath id="bc"><path d="{body}"/></clipPath>
<clipPath id="gc"><path d="{c["glass"]}"/></clipPath>
<clipPath id="above"><rect x="0" y="0" width="1200" height="321"/></clipPath>
</defs>
<ellipse cx="600" cy="360" rx="540" ry="22" fill="url(#shadow)"/>
<g clip-path="url(#above)">{liners}</g>
<path d="{body}" fill="url(#bodyg)"/>
<g clip-path="url(#bc)">
<rect x="0" y="{b}" width="1200" height="26" fill="url(#sky)"/>
<rect x="0" y="262" width="1200" height="32" fill="url(#horizon)"/>
<rect x="0" y="296" width="1200" height="30" fill="#000" fill-opacity="0.35"/>
<rect x="0" y="0" width="1200" height="400" fill="url(#falloff)"/>
</g>
<path d="{c["glass"]}" fill="url(#glassg)"/>
<g clip-path="url(#gc)">
<path d="M 380 100 L 470 100 L 380 240 L 290 240 Z" fill="#fff" fill-opacity="0.05"/>
<path d="M 520 100 L 548 100 L 458 240 L 430 240 Z" fill="#fff" fill-opacity="0.035"/>
<path d="M 720 100 L 800 100 L 720 240 L 640 240 Z" fill="#fff" fill-opacity="0.04"/>
{pillars}
</g>
<path d="{c["glass"]}" fill="none" stroke="url(#chrome)" stroke-width="2.2" stroke-linejoin="round"/>
<path d="{c["mirror"]}" fill="#0b0b0d" stroke="#fff" stroke-opacity="0.22" stroke-width="0.9"/>
<path d="{c["shoulder"]}" fill="none" stroke="#fff" stroke-opacity="0.05" stroke-width="7"/>
<path d="{c["shoulder"]}" fill="none" stroke="url(#shoulder)" stroke-width="1.3"/>
<path d="M {xs[0]+78} 314 L {xs[1]-78} 314" stroke="#fff" stroke-opacity="0.12" stroke-width="1"/>
{doors}
{handles}
<path d="{c["top"]}" fill="none" stroke="#fff" stroke-opacity="0.06" stroke-width="10" stroke-linecap="round"/>
<path d="{c["top"]}" fill="none" stroke="url(#rimlight)" stroke-width="2.2" stroke-linecap="round"/>
<rect x="122" y="310" width="44" height="6" rx="3" fill="#1a1b1e" stroke="url(#chrome)" stroke-width="0.8"/>
<path d="{c["head"]}" fill="#0d1015" stroke="#fff" stroke-opacity="0.25" stroke-width="0.8"/>
<path d="{c["led"]}" fill="none" stroke="#dfe9ff" stroke-opacity="0.25" stroke-width="12" stroke-linecap="round"/>
<path d="{c["led"]}" fill="none" stroke="#f6f9ff" stroke-width="2.6" stroke-linecap="round"/>
<path d="{c["tail"]}" fill="#e5402f" fill-opacity="0.18" stroke="#ff4a36" stroke-opacity="0.3" stroke-width="10" stroke-linejoin="round"/>
<path d="{c["tail"]}" fill="url(#tailg)"/>
{wheels}
</svg>'''
    return svg, body

meta = {}
for n, c in CARS.items():
    full, body = build(n, c, True)
    open(f"car-{n}.svg","w").write(full)
    nb, _ = build(n, c, False)
    open(f"body-{n}.svg","w").write(nb)
    open(f"mask-{n}.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400"><path d="{body}" fill="#fff"/></svg>')
    meta[n] = c["xs"]
open("wheel.svg","w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-62 -62 124 124" width="124" height="124"><defs>{WHEEL_DEFS}</defs>{wheel_group()}</svg>')
print(json.dumps(meta))
