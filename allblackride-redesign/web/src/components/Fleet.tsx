import type { CSSProperties } from 'react';
import { FLEET } from '../data/content';
import { Car } from './Car';
import { ArrowRight } from './icons';

/**
 * Motion 03 — drive-by. While pinned, a 300%-wide row slides left so each car crosses the screen;
 * wheels spin with `--spin`, the outlined class name drifts at a parallax speed behind it.
 */
export function Fleet({ bookHref }: { bookHref: string }) {
  return (
    <section id="fleet" className="fleet" data-pin aria-label="Fleet">
      <div className="stage pinned fleet-stage">
        <div className="fleet-head wrap">
          <h2 className="wide h2">
            Three ways
            <br />
            to <span className="serif">arrive.</span>
          </h2>
          <div className="fleet-aside">
            <p>Mercedes-Benz and BMW, maintained to the highest standard. Professional chauffeurs only.</p>
            <div className="fleet-progress" aria-hidden="true">
              <span className="seg"><i /></span>
              <span className="seg"><i /></span>
              <span className="seg"><i /></span>
            </div>
          </div>
        </div>

        <div className="fleet-viewport">
          <div className="fleet-row">
            {FLEET.map((f, i) => (
              <article key={f.model} className="slide" aria-label={f.cls} style={{ '--i': i } as CSSProperties}>
                <div className="ghostname wide" aria-hidden="true">
                  {f.ghost}
                </div>
                <Car model={f.model} alt={`${f.vehicle} — side profile`} />
                <div className="specs">
                  <div className="spec">
                    <span className="mono">{f.num} / 03</span>
                    <span className="wide spec-cls">{f.cls}</span>
                  </div>
                  <div className="spec">
                    <span className="mono">Vehicle</span>
                    <span>{f.vehicle}</span>
                  </div>
                  <div className="spec">
                    <span className="mono">Seats</span>
                    <span>{f.seats}</span>
                  </div>
                  <div className="spec">
                    <span className="mono">Best for</span>
                    <span>{f.bestFor}</span>
                  </div>
                  <a className="ghost reserve" href={bookHref}>
                    Reserve <ArrowRight />
                  </a>
                </div>
                <p className="slide-copy">{f.copy}</p>
              </article>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
