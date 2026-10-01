import type { CSSProperties } from 'react';
import { STOPS } from '../data/content';

const ROUTE_H = 'M 120 120 C 200 120, 260 70, 360 70 S 520 140, 600 140 S 760 60, 840 60 S 1000 130, 1080 120';
const ROUTE_V = 'M 50 12 C 92 50, 8 78, 50 112 S 92 176, 50 208 S 8 270, 50 304 S 92 366, 50 392';
const H_POINTS = [[120, 120], [360, 70], [600, 140], [840, 60], [1080, 120]];
const V_Y = [12, 112, 208, 304, 392];
/** Share of the route travelled when the marker reaches each stop. */
const THRESHOLDS = [0, 0.22, 0.46, 0.7, 0.95];

const stopStyle = (i: number) => ({ '--t': THRESHOLDS[i] }) as CSSProperties;

/**
 * Motion 04 — route draw. Pinned: the headline reveals line by line, the road draws itself, a
 * glowing marker travels it and each stop lights up as it is reached. Horizontal on desktop,
 * a vertical road on phones.
 */
export function Tours({ bookHref }: { bookHref: string }) {
  return (
    <section id="journeys" className="tours" data-pin aria-label="Tours">
      <div className="stage pinned route-stage">
        <div className="wrap">
          <div className="rt-head" data-scene="enter">
            <h2 className="wide h2">
              <span className="rt-line">
                <span>North Island,</span>
              </span>
              <span className="rt-line">
                <span className="serif">door to door.</span>
              </span>
            </h2>
            <p className="rt-copy">Private tours and long-distance transfers from Auckland — north to the Bay of Islands, south to the lakes.</p>
          </div>

          <div className="route-h">
            <div className="route-h-inner">
              <svg viewBox="0 0 1200 200" width="100%" aria-hidden="true" className="route-svg">
                <defs>
                  <linearGradient id="rt" x1="0" y1="0" x2="1" y2="0">
                    <stop offset="0" stopColor="#EDEAE4" stopOpacity=".35" />
                    <stop offset="1" stopColor="#DCE7FF" />
                  </linearGradient>
                </defs>
                <path d={ROUTE_H} fill="none" stroke="rgba(237,234,228,0.12)" strokeWidth="1.5" strokeDasharray="4 8" />
                <path className="route-draw" pathLength={1} d={ROUTE_H} fill="none" stroke="url(#rt)" strokeWidth="2.5" strokeLinecap="round" />
                {H_POINTS.map(([x, y], i) => (
                  <g key={i} className="stop" style={stopStyle(i)}>
                    <circle cx={x} cy={y} r={STOPS[i].home ? 22 : 16} fill="#DCE7FF" fillOpacity={STOPS[i].home ? 0.14 : 0.12} />
                    <circle cx={x} cy={y} r={STOPS[i].home ? 7 : 5} fill={STOPS[i].home ? '#ffffff' : '#EDEAE4'} />
                  </g>
                ))}
                <g className="route-car">
                  <circle r="26" fill="#DCE7FF" fillOpacity=".10" />
                  <circle r="11" fill="#DCE7FF" fillOpacity=".25" />
                  <circle r="4.5" fill="#ffffff" />
                </g>
              </svg>
              <ol className="stops-h">
                {STOPS.map((s, i) => (
                  <li key={s.name} className="stop" style={stopStyle(i)}>
                    <span className="wide stop-name">{s.name}</span>
                    <span className="stop-sub">{s.sub}</span>
                    <span className={`mono stop-time${s.home ? ' home' : ''}`}>{s.time}</span>
                  </li>
                ))}
              </ol>
            </div>
          </div>

          <div className="route-v">
            <svg viewBox="0 0 100 404" width="100" height="404" aria-hidden="true" className="route-v-svg">
              <defs>
                <linearGradient id="rtv" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0" stopColor="#EDEAE4" stopOpacity=".35" />
                  <stop offset="1" stopColor="#DCE7FF" />
                </linearGradient>
              </defs>
              <path d={ROUTE_V} fill="none" stroke="rgba(237,234,228,0.12)" strokeWidth="1.5" strokeDasharray="4 8" />
              <path className="route-draw" pathLength={1} d={ROUTE_V} fill="none" stroke="url(#rtv)" strokeWidth="2.5" strokeLinecap="round" />
              {V_Y.map((y, i) => (
                <g key={i} className="stop" style={stopStyle(i)}>
                  <circle cx="50" cy={y} r={STOPS[i].home ? 18 : 14} fill="#DCE7FF" fillOpacity=".13" />
                  <circle cx="50" cy={y} r={STOPS[i].home ? 6.5 : 4.5} fill={STOPS[i].home ? '#ffffff' : '#EDEAE4'} />
                </g>
              ))}
              <g className="route-car-v">
                <circle r="22" fill="#DCE7FF" fillOpacity=".10" />
                <circle r="9" fill="#DCE7FF" fillOpacity=".25" />
                <circle r="4" fill="#ffffff" />
              </g>
            </svg>
            <ol className="stops-v">
              {STOPS.map((s, i) => (
                <li key={s.name} className="stop" style={{ ...stopStyle(i), top: V_Y[i] }}>
                  <span className="stop-v-text">
                    <span className="wide stop-name">{s.name}</span>
                    <span className="stop-sub">{s.sub}</span>
                  </span>
                  <span className={`mono stop-time${s.home ? ' home' : ''}`}>{s.time}</span>
                </li>
              ))}
            </ol>
          </div>

          <div className="rt-cta">
            <a className="cta" href={bookHref}>
              Plan a private tour
            </a>
            <a className="ghost" href={bookHref}>
              City-to-city quote
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
