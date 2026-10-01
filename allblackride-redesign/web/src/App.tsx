import { useCallback, useRef, useState } from 'react';
import { Fleet } from './components/Fleet';
import { Finale } from './components/Finale';
import { Footer } from './components/Footer';
import { Header } from './components/Header';
import { Hero, MobileBooking } from './components/Hero';
import { Marquee } from './components/Marquee';
import { Services } from './components/Services';
import { Tours } from './components/Tours';
import { NAV } from './data/content';
import { useAucklandTime } from './hooks/useAucklandTime';
import { useMediaQuery } from './hooks/useMediaQuery';
import { useScrollScenes } from './hooks/useScrollScenes';

const NARROW = '(max-width: 860px)';
const SECTION_IDS = NAV.map((n) => n.id);

export default function App() {
  const rootRef = useRef<HTMLDivElement>(null);
  const [service, setService] = useState(0);
  const [menuOpen, setMenuOpen] = useState(false);
  const narrow = useMediaQuery(NARROW);
  const time = useAucklandTime();

  // On phones the booking form lives in its own block after the hero.
  const bookHref = narrow ? '#book-m' : '#book';

  useScrollScenes(rootRef, SECTION_IDS, { onServiceInView: setService, narrowQuery: NARROW });

  const toggleMenu = useCallback(() => setMenuOpen((o) => !o), []);
  const closeMenu = useCallback(() => setMenuOpen(false), []);

  return (
    <div className="abr" ref={rootRef}>
      <div className="grain" aria-hidden="true" />
      <Header bookHref={bookHref} menuOpen={menuOpen} onToggleMenu={toggleMenu} onCloseMenu={closeMenu} time={time} />
      <main>
        <Hero time={time} />
        <MobileBooking />
        <Marquee />
        <Fleet bookHref={bookHref} />
        <Services active={service} onActivate={setService} bookHref={bookHref} />
        <Tours bookHref={bookHref} />
        <Finale bookHref={bookHref} />
      </main>
      <Footer bookHref={bookHref} time={time} />
    </div>
  );
}
