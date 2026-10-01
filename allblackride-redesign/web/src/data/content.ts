import bodySclass from '../assets/cars/body-sclass.svg';
import bodyVclass from '../assets/cars/body-vclass.svg';
import bodyEqs from '../assets/cars/body-eqs.svg';
import carSclass from '../assets/cars/car-sclass.svg';
import carVclass from '../assets/cars/car-vclass.svg';
import carEqs from '../assets/cars/car-eqs.svg';

export type CarModel = 'sclass' | 'vclass' | 'eqs';

/** Layered artwork per model. Wheel centres are in the 1200×400 artwork's coordinate space. */
export const CARS: Record<CarModel, { body: string; full: string; wheelX: [number, number] }> = {
  sclass: { body: bodySclass, full: carSclass, wheelX: [300, 900] },
  vclass: { body: bodyVclass, full: carVclass, wheelX: [300, 905] },
  eqs: { body: bodyEqs, full: carEqs, wheelX: [300, 900] },
};

export const CONTACT = {
  phoneDisplay: '+64 21 595 696',
  phoneHref: 'tel:+6421595696',
  email: 'Info@allblackride.com',
  city: 'Auckland, New Zealand',
};

export const NAV = [
  { id: 'fleet', label: 'Fleet' },
  { id: 'services', label: 'Services' },
  { id: 'journeys', label: 'Tours' },
  { id: 'join', label: 'Drive with us' },
] as const;

export type SectionId = (typeof NAV)[number]['id'];

export const RIDE_TYPES = [
  { label: 'Airport transfer', drop: 'Drop-off', pickupHint: 'Flight no. or address', dropHint: 'Address or terminal' },
  { label: 'Hourly chauffeur', drop: 'Duration', pickupHint: 'Start address', dropHint: 'e.g. 4 hours' },
  { label: 'City to city', drop: 'Destination city', pickupHint: 'From', dropHint: 'e.g. Rotorua' },
  { label: 'Private tour', drop: 'Tour', pickupHint: 'Hotel or address', dropHint: 'Paihia, Rotorua, Taupō…' },
] as const;

export const FLEET = [
  {
    model: 'sclass' as CarModel,
    num: '01',
    cls: 'Business Class',
    ghost: 'Business',
    vehicle: 'Mercedes-Benz S-Class or equivalent',
    seats: 'Up to 3',
    bestFor: 'Airport · corporate',
    copy: 'The quiet back seat between the terminal and the boardroom. Discreet, punctual, exactly on time.',
  },
  {
    model: 'vclass' as CarModel,
    num: '02',
    cls: 'First Class',
    ghost: 'First',
    vehicle: 'Mercedes-Benz V-Class or equivalent',
    seats: 'Up to 6',
    bestFor: 'Groups · weddings',
    copy: 'Room for the whole party and their luggage — family arrivals, wedding parties and teams travelling together.',
  },
  {
    model: 'eqs' as CarModel,
    num: '03',
    cls: 'Executive',
    ghost: 'Executive',
    vehicle: 'Mercedes-Benz EQS or BMW i7',
    // TODO(client): confirm seat count — the current site says 6, which an EQS / i7 does not seat.
    seats: '[Confirm seats]',
    bestFor: 'Silent, all-electric',
    copy: 'Fully electric flagship saloons. The calmest way to cross the city — no engine note, just the road.',
  },
];

/** Close-up crops shown beside the services list; `crop` maps to a transform in the stylesheet. */
export const SERVICES = [
  { num: '01', title: 'Airport transfers', body: 'Flight tracking, meet & greet at arrivals, and a car at the kerb whatever time you land.', crop: { src: carSclass, cls: 'c0', label: 'LED headlight' }, toTours: false },
  { num: '02', title: 'Hourly chauffeur', body: 'Your car and driver by the hour — multiple stops, back-to-back meetings, a day in the city.', crop: { src: carSclass, cls: 'c1', label: 'Chrome detailing' }, toTours: false },
  { num: '03', title: 'City to city', body: 'Long-distance transfers across the North Island, without the drive.', crop: { src: carEqs, cls: 'c2', label: 'Wheel & brake' }, toTours: false },
  { num: '04', title: 'Events & weddings', body: 'Weddings, parties, red carpets and private functions — arrive the way the day deserves.', crop: { src: carVclass, cls: 'c3', label: 'Rear light signature' }, toTours: false },
  { num: '05', title: 'Private tours', body: 'A private chauffeur, a customised itinerary and local knowledge of where to stop.', crop: { src: carEqs, cls: 'c4', label: 'Mirror & glasshouse' }, toTours: true },
];

/** Drive times are approximate and should be confirmed by the client. */
export const STOPS = [
  { name: 'Paihia', sub: 'Bay of Islands', time: '≈ 3 h north', home: false },
  { name: 'Auckland', sub: 'Home base · AKL', time: 'Start', home: true },
  { name: 'Hamilton', sub: 'Waikato', time: '≈ 1.5 h south', home: false },
  { name: 'Rotorua', sub: 'Geothermal country', time: '≈ 3 h south', home: false },
  { name: 'Taupō', sub: 'Lake Taupō', time: '≈ 3.5 h south', home: false },
];

export const MARQUEE = [
  { text: 'Flight tracking' },
  { text: 'meet & greet', serif: true },
  { text: 'Professional chauffeurs only' },
  { text: '24 / 7', serif: true },
  { text: 'Auckland · Hamilton · Paihia · Rotorua · Taupō' },
  { text: 'door to door', serif: true },
];
