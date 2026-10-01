import { CONTACT } from '../data/content';

export function Footer({ bookHref, time }: { bookHref: string; time: string }) {
  return (
    <footer className="footer">
      <div id="join" className="join wrap">
        <div className="join-text">
          <span className="mono">Drive with us</span>
          <span className="join-line">
            Independent chauffeur? <span className="serif">Join the network.</span>
          </span>
        </div>
        {/* TODO(client): link to the partner application form */}
        <a className="ghost" href="#join">
          Apply to partner
        </a>
      </div>

      <div className="foot-cols wrap">
        <div className="foot-col">
          <span className="mono">Contact</span>
          <a href={`mailto:${CONTACT.email}`}>{CONTACT.email}</a>
          <a href={CONTACT.phoneHref}>{CONTACT.phoneDisplay}</a>
          <span>{CONTACT.city}</span>
        </div>
        <div className="foot-col">
          <span className="mono">Services</span>
          <a href="#services">Airport transfers</a>
          <a href="#services">Hourly chauffeur</a>
          <a href="#services">City to city</a>
          <a href="#services">Events &amp; weddings</a>
        </div>
        <div className="foot-col">
          <span className="mono">Tours</span>
          <a href="#journeys">Auckland</a>
          <a href="#journeys">Hamilton</a>
          <a href="#journeys">Paihia</a>
          <a href="#journeys">Rotorua · Taupō</a>
        </div>
        <div className="foot-col">
          <span className="mono">Company</span>
          <a href={bookHref}>Book a ride</a>
          <a href="#fleet">Fleet</a>
          <a href="#join">Join our team</a>
        </div>
      </div>

      <div className="wordmark wide wrap" aria-hidden="true">
        ALL BLACK RIDE
      </div>

      <div className="legal mono wrap">
        <span>© All BlackRide · Auckland NZ</span>
        <span>Auckland {time} · on the road 24/7</span>
        <span className="legal-links">
          {/* TODO(client): privacy and terms pages */}
          <a href="#join">Privacy</a>
          <a href="#join">Terms</a>
          <a href="#top" className="to-top">
            Back to top ↑
          </a>
        </span>
      </div>
    </footer>
  );
}
