# All BlackRide — React app

A production React build of the homepage design in `../design`. It has the same layout, scroll motion, intro and phone
behaviour as the design.

**Stack:** React 19, Vite 8, TypeScript (strict). No UI or animation library is used. Fonts are self-hosted through Fontsource.

```bash
npm install
npm run dev        # http://localhost:5173
npm run build      # type-check + production build → dist/
npm run preview    # serve dist/ locally
```

`base: './'` in `vite.config.ts` keeps every asset URL relative, so `dist/` can be deployed to any static host or
sub-path (Netlify, Vercel, S3, cPanel).

## How the scroll motion works

`src/hooks/useScrollScenes.ts` is the only code that runs on scroll. On each animation frame it writes one CSS
variable, `--p` (0 → 1), onto each scene, and React does not re-render. Every animation is plain CSS `calc()` on
`--p`, in the **MOTION** section of `src/styles/global.css`.

| Attribute | Meaning |
|---|---|
| `data-pin` | A tall track whose first child is a sticky stage. `--p` is progress through the track. |
| `data-scene="enter"` | `--p` rises as the element enters the viewport. |
| `data-scene="through"` | `--p` runs from the element's first visible pixel to its last. |

The hook also sets `--sp` (page scroll progress, used by the line under the header) and `data-active` (the current
nav section) on the root. On phones it reports the services row nearest the middle of the screen, which drives the
close-up there because phones have no hover.

`[data-live]` is only set once JavaScript runs. Without it, every section renders its designed rest state, so
nothing is hidden if the script fails.

| Section | Component | Track length (desktop / phone) |
|---|---|---|
| Light sweep → through the glass | `Hero.tsx` | 320vh / 250vh |
| Drive-by fleet (cars park, wheels spin) | `Fleet.tsx` | 360vh / 300vh |
| Services stagger + close-ups | `Services.tsx` | — |
| Route draw (vertical on phones) | `Tours.tsx` | 250vh / 230vh |
| Headlight wake | `Finale.tsx` | 200vh / 170vh |

## Structure

```
src/
  App.tsx                 page composition, booking-link target, menu state
  data/content.ts         all copy, fleet, services, stops, contact details
  hooks/useScrollScenes   scroll → CSS variables
  hooks/useAucklandTime   live Pacific/Auckland clock
  hooks/useMediaQuery
  components/             Header, Hero (+ MobileBooking), BookingForm, Car, Marquee,
                          Fleet, Services, Tours, Finale, Footer, icons
  assets/cars/            layered SVG car artwork, light-sweep masks, grain texture
  styles/global.css       tokens → base → components → motion → live → phones
```

## Car artwork

`Car.tsx` stacks four layers for each model:
1. the body
2. two wheel images that rotate with `--spin`
3. a band of light clipped to the body silhouette by `mask-sclass.svg` (and the other masks)
4. a faint floor reflection

To use real photography, replace the body with a cut-out photo and the wheels with cut-out wheels, and regenerate the
mask from the photo's outline. No component code changes.

## Before going live

- **Booking form:** `BookingForm.tsx` only shows a confirmation and sends nothing. Wire `onSubmit` to the dispatch channel (email API, WhatsApp Business or a booking system).
- **Executive seats:** the seat count is `[Confirm seats]` in `content.ts`.
- **Drive times:** the times in `STOPS` are approximate.
- **Placeholder links:** the Privacy, Terms and "Apply to partner" links point to `#join` (each marked `TODO(client)`).
- **Older Safari:** before version 16, it doesn't support the CSS that moves the car marker along the tours route. The marker stays at the start; everything else still works.
