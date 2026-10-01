import { Fragment } from 'react';
import { MARQUEE } from '../data/content';

/** Drifts sideways with scroll (`data-scene="through"`), not on a timer. */
export function Marquee() {
  const items = [...MARQUEE, ...MARQUEE];
  return (
    <div className="marq-wrap" data-scene="through">
      <div className="marq wide" aria-label="Included with every ride">
        {items.map((m, i) => (
          <Fragment key={i}>
            {i > 0 && <span className="sep" aria-hidden="true" />}
            <span className={m.serif ? 'serif marq-hi' : undefined} aria-hidden={i >= MARQUEE.length || undefined}>
              {m.text}
            </span>
          </Fragment>
        ))}
      </div>
    </div>
  );
}
