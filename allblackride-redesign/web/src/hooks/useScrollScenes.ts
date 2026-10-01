import { useEffect, useRef, type RefObject } from 'react';

const HEADER = 72;
const clamp = (v: number) => Math.max(0, Math.min(1, v));

interface Options {
  /** Called on phones with the services row nearest the middle of the screen (there is no hover on touch). */
  onServiceInView?: (index: number) => void;
  narrowQuery?: string;
}

/**
 * Drives every scroll sequence on the page by writing one CSS variable, `--p` (0 → 1), per scene.
 * All motion itself lives in CSS `calc()`, so React never re-renders during scroll.
 *
 *  - `[data-pin]`              a tall track whose first child is a sticky stage; p = progress through the track
 *  - `[data-scene="enter"]`    p rises as the element enters the viewport
 *  - `[data-scene="through"]`  p runs from first to last visible pixel
 *
 * It also writes `--sp` (page progress) and `data-active` (current nav section) on the root.
 */
export function useScrollScenes(rootRef: RefObject<HTMLElement | null>, sections: readonly string[], opts: Options = {}) {
  const optsRef = useRef(opts);
  optsRef.current = opts;

  useEffect(() => {
    const root = rootRef.current;
    if (!root) return;
    root.setAttribute('data-live', '');

    const narrowMq = window.matchMedia(optsRef.current.narrowQuery ?? '(max-width: 860px)');
    let raf = 0;
    let lastService = -1;

    const update = () => {
      raf = 0;
      const vh = window.innerHeight;
      const doc = document.documentElement;
      root.style.setProperty('--sp', clamp(window.scrollY / Math.max(1, doc.scrollHeight - vh)).toFixed(4));

      root.querySelectorAll<HTMLElement>('[data-pin]').forEach((track) => {
        const stage = track.firstElementChild as HTMLElement | null;
        if (!stage || getComputedStyle(stage).position !== 'sticky') {
          track.style.removeProperty('--p');
          return;
        }
        const r = track.getBoundingClientRect();
        const run = r.height - stage.offsetHeight;
        track.style.setProperty('--p', clamp((HEADER - r.top) / Math.max(1, run)).toFixed(4));
      });

      root.querySelectorAll<HTMLElement>('[data-scene]').forEach((el) => {
        const r = el.getBoundingClientRect();
        const p =
          el.dataset.scene === 'through' ? clamp((vh - r.top) / (vh + r.height)) : clamp((vh - r.top) / (vh * 0.85));
        el.style.setProperty('--p', p.toFixed(4));
      });

      let active = '';
      for (const id of sections) {
        const el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top < vh * 0.45) active = id;
      }
      if (root.dataset.active !== active) root.dataset.active = active;

      if (narrowMq.matches && optsRef.current.onServiceInView) {
        let best = -1;
        let dist = Infinity;
        root.querySelectorAll<HTMLElement>('.svc').forEach((row, i) => {
          const r = row.getBoundingClientRect();
          const d = Math.abs(r.top + r.height / 2 - vh * 0.62);
          if (r.bottom > 0 && r.top < vh && d < dist) {
            dist = d;
            best = i;
          }
        });
        if (best >= 0 && best !== lastService) {
          lastService = best;
          optsRef.current.onServiceInView(best);
        }
      }
    };

    const schedule = () => {
      if (!raf) raf = requestAnimationFrame(update);
    };

    window.addEventListener('scroll', schedule, { passive: true });
    window.addEventListener('resize', schedule);
    narrowMq.addEventListener('change', schedule);
    // Fonts change line heights, and therefore track positions.
    document.fonts?.ready.then(schedule);
    update();

    return () => {
      window.removeEventListener('scroll', schedule);
      window.removeEventListener('resize', schedule);
      narrowMq.removeEventListener('change', schedule);
      if (raf) cancelAnimationFrame(raf);
      root.removeAttribute('data-live');
    };
  }, [rootRef, sections]);
}
