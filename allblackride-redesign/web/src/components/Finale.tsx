import { CONTACT } from '../data/content';

const BROW_L = 'M 120 70 C 200 52, 300 46, 380 52';
const BROW_R = 'M 880 70 C 800 52, 700 46, 620 52';

/** Motion 05 — headlight wake. Pinned: LED brows ignite, beams open across the floor, then the ask. */
export function Finale({ bookHref }: { bookHref: string }) {
  return (
    <section id="finale" className="finale" data-pin aria-label="Book">
      <div className="stage pinned fin-stage">
        <svg className="led" viewBox="0 0 1000 120" aria-hidden="true">
          {[BROW_L, BROW_R].map((d) => (
            <g key={d}>
              <path d={d} fill="none" stroke="#DCE7FF" strokeOpacity=".25" strokeWidth="14" strokeLinecap="round" />
              <path d={d} fill="none" stroke="#F4F8FF" strokeWidth="3.5" strokeLinecap="round" />
            </g>
          ))}
        </svg>
        <div className="beam" aria-hidden="true" />
        <div className="fin-type">
          <span className="mono">Any hour · any terminal · any occasion</span>
          <h2 className="wide fin-h2">
            Your car
            <br />
            <span className="serif">is ready.</span>
          </h2>
          <div className="fin-actions">
            <a className="cta" href={bookHref}>
              Book a ride
            </a>
            <a className="ghost" href={CONTACT.phoneHref}>
              Call {CONTACT.phoneDisplay}
            </a>
          </div>
        </div>
      </div>
    </section>
  );
}
