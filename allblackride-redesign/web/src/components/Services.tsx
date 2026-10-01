import type { CSSProperties } from 'react';
import { SERVICES } from '../data/content';

interface ServicesProps {
  active: number;
  onActivate: (i: number) => void;
  bookHref: string;
}

/**
 * Rows fade in one after another as the section enters. The close-up on the left follows the
 * hovered/focused row on desktop, and the row nearest the middle of the screen on phones.
 */
export function Services({ active, onActivate, bookHref }: ServicesProps) {
  const crop = SERVICES[active].crop;
  return (
    <section id="services" className="services wrap" data-scene="enter" aria-label="Services">
      <div className="two-col">
        <div className="crop-col">
          <h2 className="wide h2">
            Every kind
            <br />
            of <span className="serif">journey.</span>
          </h2>
          <div className="crop">
            {SERVICES.map((s, i) => (
              <img key={s.num} className={`${s.crop.cls}${i === active ? ' on' : ''}`} src={s.crop.src} alt={i === active ? s.crop.label : ''} draggable={false} />
            ))}
            <span className="mono crop-label">
              {SERVICES[active].num} — {crop.label}
            </span>
          </div>
        </div>
        <div className="svc-list">
          {SERVICES.map((s, i) => (
            <a
              key={s.num}
              className={`svc${i === active ? ' on' : ''}`}
              href={s.toTours ? '#journeys' : bookHref}
              style={{ '--i': i } as CSSProperties}
              onMouseEnter={() => onActivate(i)}
              onFocus={() => onActivate(i)}
            >
              <span className="mono svc-num">{s.num}</span>
              <span className="svc-text">
                <span className="wide stitle">{s.title}</span>
                <span className="svc-body">{s.body}</span>
              </span>
              <span className="arw" aria-hidden="true">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.4" strokeLinecap="round" strokeLinejoin="round">
                  <path d="M5 12h14M13 6l6 6-6 6" />
                </svg>
              </span>
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}
