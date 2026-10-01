import { CONTACT } from '../data/content';
import { BookingForm } from './BookingForm';
import { Car } from './Car';
import { ArrowRight } from './icons';

/**
 * Motion 01 + 02. While pinned, `--p` runs 0 → 1:
 *   q1 (0–.28)  a band of light sweeps nose to tail and the car brightens
 *   q2 (.3–.5)  headline and booking dock drift away, the car rolls forward
 *   q3 (.5–.9)  the camera pushes into the rear side window
 *   q4 (.84–.96) black glass, "Step inside."
 */
export function Hero({ time }: { time: string }) {
  return (
    <section id="hero" className="hero" data-pin aria-label="Introduction">
      <div id="top" className="stage pinned hero-stage">
        <div className="hero-pool" aria-hidden="true" />

        <div className="hero-type wrap-inner">
          <div className="hero-titles">
            <div className="mono intro-fade hero-kicker">
              <span>Private chauffeurs</span>
              <span>Auckland · Aotearoa NZ</span>
              <span className="live-dot">● Available 24/7</span>
              <span>Auckland {time}</span>
            </div>
            <h1 className="wide hero-h1">
              <span className="h1-line">
                <span>Arrive</span>
              </span>
              <span className="h1-line">
                <span>
                  <span className="serif hero-in">in</span> silence.
                </span>
              </span>
            </h1>
          </div>
          <p className="intro-fade d2 hero-lede">
            Airport transfers, hourly hire, city-to-city and private tours — in a Mercedes-Benz or BMW, with a professional chauffeur.
          </p>
        </div>

        <div className="hero-carzone">
          <div className="hero-rig">
            <Car model="sclass" alt="Mercedes-Benz S-Class, side profile, lit by a single line of light" className="intro-car" sweep="hero-sweep" />
            <div className="bloom bloom-head" aria-hidden="true">
              <i />
            </div>
            <div className="bloom bloom-tail" aria-hidden="true">
              <i />
            </div>
          </div>
        </div>
        <div className="hero-floor" aria-hidden="true" />

        <BookingForm variant="dock" id="book" className="hero-dock dock-in" />

        <div className="mhero-cta">
          <a className="cta" href="#book-m">
            Get a quote <ArrowRight />
          </a>
          <a className="ghost" href={CONTACT.phoneHref} aria-label={`Call ${CONTACT.phoneDisplay}`}>
            Call
          </a>
        </div>

        <div className="hero-black" aria-hidden="true">
          <span className="mono">The fleet</span>
          <span className="serif hero-step">Step inside.</span>
        </div>
      </div>
    </section>
  );
}

/** Phones only: the full form gets its own block straight after the hero. */
export function MobileBooking() {
  return (
    <section id="book-m" className="mbook" aria-label="Book a ride">
      <div className="mbook-head">
        <span className="mono">Book a ride · available 24/7</span>
        <h2 className="wide">
          Where <span className="serif">to?</span>
        </h2>
      </div>
      <BookingForm variant="mobile" />
    </section>
  );
}
