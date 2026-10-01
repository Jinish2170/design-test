import { useState, type FormEvent } from 'react';
import { RIDE_TYPES } from '../data/content';
import { ArrowRight, Check } from './icons';

interface BookingFormProps {
  variant: 'dock' | 'mobile';
  id?: string;
  className?: string;
}

/**
 * Quote request form. Submission is a front-end stub: wire `onSubmit` to the dispatch channel
 * (email API, WhatsApp Business, booking system) before going live.
 */
export function BookingForm({ variant, id, className = '' }: BookingFormProps) {
  const [type, setType] = useState(0);
  const [sent, setSent] = useState(false);
  const t = RIDE_TYPES[type];
  const p = variant === 'mobile' ? 'm-' : '';
  const today = new Date().toISOString().slice(0, 10);

  const onSubmit = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    // const data = Object.fromEntries(new FormData(e.currentTarget)); → send to dispatch
    setSent(true);
  };

  return (
    <form id={id} className={`booking booking-${variant} ${className}`} aria-label="Book a ride" onSubmit={onSubmit}>
      <div className="ride-types" role="group" aria-label="Ride type">
        {RIDE_TYPES.map((r, i) => (
          <button key={r.label} type="button" className={`tab${i === type ? ' on' : ''}`} aria-pressed={i === type} onClick={() => setType(i)}>
            {r.label}
          </button>
        ))}
      </div>
      <input type="hidden" name="rideType" value={t.label} />
      <div className="fields">
        <div className="fld fld-wide">
          <label htmlFor={`${p}pu`}>Pick-up</label>
          <input id={`${p}pu`} name="pickup" type="text" placeholder={t.pickupHint} autoComplete="street-address" required />
        </div>
        <div className="fld fld-wide">
          <label htmlFor={`${p}dr`}>{t.drop}</label>
          <input id={`${p}dr`} name="dropoff" type="text" placeholder={t.dropHint} />
        </div>
        <div className="fld">
          <label htmlFor={`${p}dt`}>Date</label>
          <input id={`${p}dt`} name="date" type="date" min={today} />
        </div>
        <div className="fld">
          <label htmlFor={`${p}tm`}>Time</label>
          <input id={`${p}tm`} name="time" type="time" />
        </div>
        <div className="fld">
          <label htmlFor={`${p}px`}>Passengers</label>
          <select id={`${p}px`} name="passengers" defaultValue="1">
            {[1, 2, 3, 4, 5, 6].map((n) => (
              <option key={n}>{n}</option>
            ))}
          </select>
        </div>
        <button type="submit" className="cta submit">
          {sent ? 'Request sent' : 'Get my quote'} <ArrowRight />
        </button>
      </div>
      {sent && (
        <div className="sent" role="status">
          <Check />
          Request received — we'll call or text to confirm your ride and price.
        </div>
      )}
    </form>
  );
}
