"""Side-profile car artwork drawn to real proportions (1200x400 canvas, ground at y=380).

S-Class W223 ~5.18 m long, 1.50 m high, 3.11 m wheelbase  -> 211 px/m
V-Class      ~5.14 m long, 1.88 m high, 3.20 m wheelbase  -> 190 px/m
EQS          ~5.22 m long, 1.51 m high, 3.21 m wheelbase  -> 211 px/m
"""
import math, json

def arch_bottom(front, rear, r_arch, y=348):
    (fx, fy), (rx, ry) = front, rear
    d = lambda cy: math.sqrt(r_arch**2 - (y - cy)**2)
    return (f"L {fx + d(fy):.1f} {y} A {r_arch} {r_arch} 0 1 0 {fx - d(fy):.1f} {y} "
            f"L {rx + d(ry):.1f} {y} A {r_arch} {r_arch} 0 1 0 {rx - d(ry):.1f} {y} Z")

CARS = {
 "sclass": dict(
   wheels=[(293, 304, 76), (948, 304, 76)], arch=88, sill=348, roof=60,
   top="M 78 348 C 60 344, 52 320, 52 296 L 54 226 C 55 194, 60 178, 82 166 C 120 155, 170 152, 214 150 C 278 138, 332 92, 420 76 C 490 63, 620 59, 702 70 C 762 80, 812 132, 846 170 C 930 178, 1040 186, 1112 198 C 1136 203, 1148 222, 1150 248 L 1150 296 C 1150 322, 1142 340, 1124 348",
   rim="M 82 166 C 120 155, 170 152, 214 150 C 278 138, 332 92, 420 76 C 490 63, 620 59, 702 70 C 762 80, 812 132, 846 170 C 930 178, 1040 186, 1112 198 C 1136 203, 1148 222, 1150 248",
   glass="M 256 168 C 300 150, 352 104, 430 90 C 500 79, 612 76, 690 86 C 738 94, 782 136, 812 168 Z",
   pillars=["M 582 80 L 596 80 L 600 170 L 586 170 Z", "M 372 100 L 380 98 L 392 170 L 384 170 Z"],
   doors=["M 828 172 C 834 230, 842 280, 858 312", "M 590 170 L 598 346", "M 400 170 C 398 230, 392 270, 381 304"],
   handles=[(752, 206), (512, 206)], belt=170,
   shoulder="M 60 212 C 300 204, 700 198, 1128 212",
   crease="M 878 266 C 700 262, 520 260, 362 256",
   mirror="M 806 172 C 808 156, 836 150, 854 156 L 852 172 Z",
   head="M 1050 196 C 1090 199, 1126 206, 1146 222 L 1144 232 C 1120 222, 1086 214, 1046 210 Z", drl="M 1058 199 C 1094 202, 1124 209, 1141 222",
   tail="M 56 184 C 82 176, 122 170, 166 168 L 166 180 C 122 182, 84 188, 58 198 Z",
   extras=["M 1100 320 L 1146 316", "M 84 336 L 146 336"]),
 "vclass": dict(
   wheels=[(302, 315, 65), (910, 315, 65)], arch=76, sill=352, roof=26,
   top="M 128 352 C 116 348, 112 330, 112 310 L 112 104 C 112 56, 128 34, 160 30 L 760 26 C 800 26, 826 36, 846 56 C 880 100, 930 160, 962 192 C 1010 200, 1060 212, 1080 226 C 1092 236, 1096 256, 1096 278 L 1094 320 C 1092 338, 1084 348, 1072 352",
   rim="M 112 104 C 112 56, 128 34, 160 30 L 760 26 C 800 26, 826 36, 846 56 C 880 100, 930 160, 962 192 C 1010 200, 1060 212, 1080 226 C 1092 236, 1096 256, 1096 278",
   glass="M 136 176 L 138 62 C 138 52, 146 46, 160 46 L 752 42 C 788 42, 812 54, 832 76 L 906 176 Z",
   pillars=["M 326 44 L 342 44 L 342 176 L 326 176 Z", "M 594 42 L 610 42 L 612 176 L 596 176 Z", "M 136 46 L 152 46 L 150 176 L 136 176 Z"],
   doors=["M 880 182 C 884 230, 880 270, 846 296", "M 604 176 L 606 352", "M 360 176 C 360 230, 368 270, 376 300", "M 360 186 L 600 186"],
   handles=[(820, 206), (580, 210)], belt=176,
   shoulder="M 112 204 C 400 200, 800 200, 1090 238",
   crease="M 974 266 C 700 262, 400 260, 150 258",
   mirror="M 916 178 C 918 162, 946 156, 964 162 L 962 178 Z",
   head="M 1010 204 C 1046 208, 1076 218, 1092 234 L 1090 244 C 1070 232, 1040 224, 1006 218 Z", drl="M 1016 206 C 1048 210, 1074 219, 1088 233",
   tail="M 112 118 L 128 118 L 128 214 L 112 214 Z",
   extras=["M 1060 330 L 1092 326", "M 130 340 L 200 340"]),
 "eqs": dict(
   wheels=[(267, 302, 78), (944, 302, 78)], arch=90, sill=348, roof=60,
   top="M 74 348 C 58 344, 50 322, 50 298 L 52 240 C 54 214, 64 196, 88 186 C 126 174, 176 168, 224 160 C 304 140, 382 90, 470 72 C 540 58, 620 58, 680 66 C 760 78, 840 136, 900 176 C 980 188, 1060 196, 1118 206 C 1140 212, 1150 230, 1150 256 L 1150 300 C 1150 324, 1142 340, 1124 348",
   rim="M 88 186 C 126 174, 176 168, 224 160 C 304 140, 382 90, 470 72 C 540 58, 620 58, 680 66 C 760 78, 840 136, 900 176 C 980 188, 1060 196, 1118 206 C 1140 212, 1150 230, 1150 256",
   glass="M 236 176 C 312 150, 392 102, 476 86 C 548 74, 626 74, 680 82 C 752 94, 816 140, 868 178 Z",
   pillars=["M 588 76 L 602 76 L 606 178 L 592 178 Z"],
   doors=["M 872 182 C 874 230, 868 270, 856 298", "M 598 178 L 606 346", "M 380 176 C 380 230, 372 270, 359 300"],
   handles=[(778, 212), (530, 212)], belt=178,
   shoulder="M 60 236 C 300 222, 700 214, 1130 222",
   crease="M 860 270 C 700 266, 520 264, 368 260",
   mirror="M 864 180 C 866 164, 894 158, 912 164 L 910 180 Z",
   head="M 1064 202 C 1100 206, 1132 214, 1148 228 L 1146 236 C 1124 224, 1094 218, 1058 214 Z", drl="M 1070 204 C 1104 208, 1130 216, 1144 228",
   tail="M 54 206 C 100 194, 160 182, 226 170 L 228 180 C 164 192, 104 204, 56 220 Z",
   extras=["M 1100 322 L 1146 318", "M 80 336 L 150 336"]),
}

def defs(c):
    top, sill = c["roof"], c["sill"]
    return f'''<defs>
<linearGradient id="bodyg" gradientUnits="userSpaceOnUse" x1="0" y1="{top}" x2="0" y2="{sill}">
 <stop offset="0" stop-color="#2b2d33"/><stop offset="0.28" stop-color="#16171b"/><stop offset="0.5" stop-color="#0a0a0c"/>
 <stop offset="0.72" stop-color="#0d0e11"/><stop offset="0.82" stop-color="#16171b"/><stop offset="1" stop-color="#050506"/></linearGradient>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8eefc" stop-opacity="0.22"/><stop offset="1" stop-color="#e8eefc" stop-opacity="0"/></linearGradient>
<linearGradient id="horizon" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfd8e6" stop-opacity="0"/><stop offset="0.55" stop-color="#cfd8e6" stop-opacity="0.11"/><stop offset="1" stop-color="#cfd8e6" stop-opacity="0"/></linearGradient>
<linearGradient id="falloff" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#000" stop-opacity="0.6"/><stop offset="0.3" stop-color="#000" stop-opacity="0"/><stop offset="0.72" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity="0.5"/></linearGradient>
<linearGradient id="softbox" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="0.07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<linearGradient id="glassg" gradientUnits="userSpaceOnUse" x1="0" y1="{top}" x2="0" y2="{c["belt"]}"><stop offset="0" stop-color="#1d2433"/><stop offset="0.55" stop-color="#0b0e15"/><stop offset="1" stop-color="#040508"/></linearGradient>
<linearGradient id="chrome" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7c818a" stop-opacity="0.5"/><stop offset="0.6" stop-color="#f3f5f8"/><stop offset="1" stop-color="#7c818a" stop-opacity="0.6"/></linearGradient>
<linearGradient id="rimlight" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0.05"/><stop offset="0.35" stop-color="#fff" stop-opacity="0.3"/><stop offset="0.6" stop-color="#fff" stop-opacity="0.95"/><stop offset="0.85" stop-color="#fff" stop-opacity="0.35"/><stop offset="1" stop-color="#fff" stop-opacity="0.1"/></linearGradient>
<linearGradient id="shoulder" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0.08"/><stop offset="0.62" stop-color="#fff" stop-opacity="0.75"/><stop offset="1" stop-color="#fff" stop-opacity="0.15"/></linearGradient>
<linearGradient id="tailg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ff7a5e"/><stop offset="0.5" stop-color="#e2321f"/><stop offset="1" stop-color="#7a0f06"/></linearGradient>
<radialGradient id="shadow" cx="0.5" cy="0.5" r="0.5"><stop offset="0" stop-color="#000" stop-opacity="0.95"/><stop offset="0.65" stop-color="#000" stop-opacity="0.6"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<radialGradient id="liner" cx="0.5" cy="0.6" r="0.5"><stop offset="0" stop-color="#000"/><stop offset="1" stop-color="#0b0b0d"/></radialGradient>
</defs>'''

def wheel_inner(R):
    """Wheel centred on (0,0), tyre radius R. 20-inch-style multi-spoke, plain centre cap."""
    rim = R * 0.72
    s = [f'<circle r="{R}" fill="#060607"/>',
         f'<circle r="{R-1.5}" fill="none" stroke="#1d1e21" stroke-width="3"/>',
         f'<circle r="{(R+rim)/2:.1f}" fill="none" stroke="#121315" stroke-width="{R-rim-6:.1f}"/>',
         f'<path d="M {-R*0.86:.1f} {-R*0.42:.1f} A {R*0.96:.1f} {R*0.96:.1f} 0 0 1 {R*0.2:.1f} {-R*0.94:.1f}" fill="none" stroke="#fff" stroke-opacity="0.13" stroke-width="2.5" stroke-linecap="round"/>',
         f'<circle r="{rim}" fill="#0c0d10"/>',
         f'<circle r="{rim*0.74:.1f}" fill="#1a1b1f" stroke="#2a2b30" stroke-width="1"/>',
         f'<circle r="{rim*0.74:.1f}" fill="none" stroke="#0e0f12" stroke-width="2" stroke-dasharray="1.5 5"/>',
         f'<path d="M {-rim*0.66:.1f} {-rim*0.34:.1f} A {rim*0.74:.1f} {rim*0.74:.1f} 0 0 1 {-rim*0.18:.1f} {-rim*0.72:.1f} L {-rim*0.12:.1f} {-rim*0.5:.1f} A {rim*0.52:.1f} {rim*0.52:.1f} 0 0 0 {-rim*0.46:.1f} {-rim*0.24:.1f} Z" fill="#3a3c42"/>']
    hub = rim * 0.2
    for i in range(5):
        a = i * 72
        for off in (-8.5, 8.5):
            s.append(f'<path transform="rotate({a+off})" d="M {-hub*0.28:.2f} {-hub:.2f} L {hub*0.28:.2f} {-hub:.2f} L {rim*0.075:.2f} {-rim*0.97:.2f} L {-rim*0.075:.2f} {-rim*0.97:.2f} Z" fill="url(#spoke)"/>')
            s.append(f'<path transform="rotate({a+off})" d="M {hub*0.28:.2f} {-hub:.2f} L {rim*0.075:.2f} {-rim*0.97:.2f}" stroke="#000" stroke-opacity="0.5" stroke-width="0.8"/>')
    s += [f'<circle r="{rim}" fill="none" stroke="url(#lip)" stroke-width="{rim*0.07:.1f}"/>',
          f'<circle r="{rim+1.5:.1f}" fill="none" stroke="#000" stroke-opacity="0.7" stroke-width="1.2"/>',
          f'<circle r="{hub:.1f}" fill="#16171a" stroke="url(#lip)" stroke-width="1.6"/>',
          f'<circle r="{hub*0.45:.1f}" fill="#8f949c"/>']
    return "\n".join(s)

WHEEL_DEFS = '''<linearGradient id="spoke" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#eef0f4"/><stop offset="0.5" stop-color="#9196a0"/><stop offset="1" stop-color="#3a3c42"/></linearGradient>
<linearGradient id="lip" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f6f7f9"/><stop offset="0.45" stop-color="#70747c"/><stop offset="1" stop-color="#26272b"/></linearGradient>'''

def build(name, c, with_wheels):
    (rx, ry, rr), (fx, fy, fr) = c["wheels"]
    body = c["top"] + " " + arch_bottom((fx, fy), (rx, ry), c["arch"], c["sill"])
    A = c["arch"]
    liners = "".join(f'<circle cx="{x}" cy="{y}" r="{A-1}" fill="url(#liner)"/>' for x, y, _ in c["wheels"])
    flares = "".join(f'<path d="M {x-A*0.92:.1f} {y-A*0.36:.1f} A {A+1} {A+1} 0 0 1 {x+A*0.92:.1f} {y-A*0.36:.1f}" fill="none" stroke="#fff" stroke-opacity="0.16" stroke-width="1.4"/>' for x, y, _ in c["wheels"])
    doors = "".join(f'<path d="{d}" fill="none" stroke="#000" stroke-width="2.2"/><path d="{d}" transform="translate(1.6 0)" fill="none" stroke="#fff" stroke-opacity="0.07" stroke-width="1"/>' for d in c["doors"])
    handles = "".join(f'<rect x="{x}" y="{y}" width="42" height="6" rx="3" fill="#0a0a0c" stroke="url(#chrome)" stroke-width="0.9"/>' for x, y in c["handles"])
    pillars = "".join(f'<path d="{p}" fill="#030304"/>' for p in c["pillars"])
    extras = "".join(f'<path d="{e}" stroke="#fff" stroke-opacity="0.12" stroke-width="1.2" stroke-linecap="round"/>' for e in c["extras"])
    wheels = ""
    if with_wheels:
        wheels = "".join(f'<g transform="translate({x} {y})">{wheel_inner(r)}</g>' for x, y, r in c["wheels"])
    sh_l, sh_r = rx - 160, fx + 200
    b = c["belt"]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400">
{defs(c)}
<defs>{WHEEL_DEFS}<clipPath id="bc"><path d="{body}"/></clipPath><clipPath id="gc"><path d="{c["glass"]}"/></clipPath><clipPath id="above"><rect x="0" y="0" width="1200" height="{c["sill"]+1}"/></clipPath></defs>
<ellipse cx="{(sh_l+sh_r)/2}" cy="381" rx="{(sh_r-sh_l)/2}" ry="16" fill="url(#shadow)"/>
<ellipse cx="{rx}" cy="380" rx="{rr*1.1:.0f}" ry="7" fill="#000"/><ellipse cx="{fx}" cy="380" rx="{fr*1.1:.0f}" ry="7" fill="#000"/>
<g clip-path="url(#above)">{liners}</g>
<path d="{body}" fill="url(#bodyg)"/>
<g clip-path="url(#bc)">
 <rect x="0" y="{b-4}" width="1200" height="40" fill="url(#sky)"/>
 <rect x="0" y="{(b+c["sill"])/2+6:.0f}" width="1200" height="34" fill="url(#horizon)"/>
 <rect x="0" y="{c["sill"]-34}" width="1200" height="40" fill="#000" fill-opacity="0.42"/>
 <rect x="380" y="0" width="420" height="400" fill="url(#softbox)"/>
 <rect x="0" y="0" width="1200" height="400" fill="url(#falloff)"/>
 {flares}
</g>
<path d="{c["glass"]}" fill="url(#glassg)"/>
<g clip-path="url(#gc)">
 <rect x="0" y="{b-30}" width="1200" height="30" fill="#000" fill-opacity="0.35"/>
 <path d="M 380 0 L 470 0 L 370 240 L 280 240 Z" fill="#fff" fill-opacity="0.045"/>
 <path d="M 520 0 L 546 0 L 446 240 L 420 240 Z" fill="#fff" fill-opacity="0.03"/>
 <path d="M 700 0 L 790 0 L 690 240 L 600 240 Z" fill="#fff" fill-opacity="0.04"/>
 {pillars}
</g>
<path d="{c["glass"]}" fill="none" stroke="url(#chrome)" stroke-width="2.4" stroke-linejoin="round"/>
<path d="{c["mirror"]}" fill="#0c0c0e" stroke="#fff" stroke-opacity="0.25" stroke-width="0.9"/>
<path d="{c["shoulder"]}" fill="none" stroke="#fff" stroke-opacity="0.05" stroke-width="8"/>
<path d="{c["shoulder"]}" fill="none" stroke="url(#shoulder)" stroke-width="1.4"/>
<path d="{c["crease"]}" fill="none" stroke="#fff" stroke-opacity="0.09" stroke-width="1.1"/>
<path d="M {rx+A:.0f} {c["sill"]-6} L {fx-A:.0f} {c["sill"]-6}" stroke="#fff" stroke-opacity="0.12" stroke-width="1"/>
{doors}
{handles}
{extras}
<path d="{c["rim"]}" fill="none" stroke="#fff" stroke-opacity="0.06" stroke-width="10" stroke-linecap="round"/>
<path d="{c["rim"]}" fill="none" stroke="url(#rimlight)" stroke-width="2.2" stroke-linecap="round"/>
<path d="{c["head"]}" fill="#0e1117" stroke="#fff" stroke-opacity="0.28" stroke-width="0.8"/>
<path d="{c["drl"]}" fill="none" stroke="#dfe9ff" stroke-opacity="0.25" stroke-width="12" stroke-linecap="round"/>
<path d="{c["drl"]}" fill="none" stroke="#f6f9ff" stroke-width="2.6" stroke-linecap="round"/>
<path d="{c["tail"]}" fill="#e5402f" fill-opacity="0.16" stroke="#ff4a36" stroke-opacity="0.28" stroke-width="10" stroke-linejoin="round"/>
<path d="{c["tail"]}" fill="url(#tailg)"/>
{wheels}
</svg>'''
    return svg, body

meta = {}
for n, c in CARS.items():
    full, body = build(n, c, True); open(f"car-{n}.svg", "w").write(full)
    nb, _ = build(n, c, False); open(f"body-{n}.svg", "w").write(nb)
    open(f"mask-{n}.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="1200" height="400"><path d="{body}" fill="#fff"/></svg>')
    meta[n] = c["wheels"]
# Wheel sprite: tyre radius 76 inside a 160x160 box, centred.
open("wheel.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-80 -80 160 160" width="160" height="160"><defs>{WHEEL_DEFS}</defs>{wheel_inner(76)}</svg>')
json.dump(meta, open("wheels.json", "w"))
print(json.dumps(meta))
