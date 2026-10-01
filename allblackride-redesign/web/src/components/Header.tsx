import { useEffect } from 'react';
import { CONTACT, NAV } from '../data/content';
import { ArrowRight, LightMark, MenuIcon } from './icons';

interface HeaderProps {
  bookHref: string;
  menuOpen: boolean;
  onToggleMenu: () => void;
  onCloseMenu: () => void;
  time: string;
}

export function Header({ bookHref, menuOpen, onToggleMenu, onCloseMenu, time }: HeaderProps) {
  useEffect(() => {
    if (!menuOpen) return;
    const onKey = (e: KeyboardEvent) => e.key === 'Escape' && onCloseMenu();
    document.addEventListener('keydown', onKey);
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', onKey);
      document.body.style.overflow = '';
    };
  }, [menuOpen, onCloseMenu]);

  return (
    <>
      <header className="site-header">
        <nav className="nav wrap" aria-label="Primary">
          <a href="#top" className="brand" aria-label="All BlackRide home">
            <LightMark />
            <span className="brand-word">
              <span className="wide brand-bold">ALL BLACK</span>
              <span className="wide brand-light">RIDE</span>
            </span>
          </a>
          <div className="navlinks">
            {NAV.map((n) => (
              <a key={n.id} href={`#${n.id}`}>
                {n.label}
              </a>
            ))}
          </div>
          <div className="navright">
            <a className="mono navlinks nav-phone" href={CONTACT.phoneHref}>
              {CONTACT.phoneDisplay}
            </a>
            <a className="cta cta-sm navbook" href={bookHref}>
              Book a ride
            </a>
            <button
              className="menu"
              type="button"
              aria-label={menuOpen ? 'Close menu' : 'Open menu'}
              aria-expanded={menuOpen}
              aria-controls="mnav"
              onClick={onToggleMenu}
            >
              <MenuIcon open={menuOpen} />
            </button>
          </div>
        </nav>
        <span className="sprog" aria-hidden="true" />
      </header>

      {menuOpen && (
        <div className="mnav" id="mnav">
          {NAV.map((n) => (
            <a key={n.id} className="mlink" href={`#${n.id}`} onClick={onCloseMenu}>
              {n.label} <ArrowRight />
            </a>
          ))}
          <div className="mnav-actions">
            <a className="cta" href={bookHref} onClick={onCloseMenu}>
              Book a ride
            </a>
            <a className="ghost ghost-center" href={CONTACT.phoneHref}>
              Call {CONTACT.phoneDisplay}
            </a>
            <span className="mono mnav-time">Auckland {time} · on the road 24/7</span>
          </div>
        </div>
      )}
    </>
  );
}
