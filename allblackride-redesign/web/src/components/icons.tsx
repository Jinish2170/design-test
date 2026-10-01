export function ArrowRight({ size = 16, strokeWidth = 1.8 }: { size?: number; strokeWidth?: number }) {
  return (
    <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth={strokeWidth} strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M5 12h14M13 6l6 6-6 6" />
    </svg>
  );
}

export function Check() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#DCE7FF" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true">
      <path d="M5 12.5l4.5 4.5L19 7.5" />
    </svg>
  );
}

export function MenuIcon({ open }: { open: boolean }) {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" aria-hidden="true">
      <path d={open ? 'M6 6l12 12M18 6L6 18' : 'M4 8h16M4 16h16'} />
    </svg>
  );
}

/** The brand mark: a single line of light, like the LED brow of a headlight. */
export function LightMark() {
  return (
    <svg className="mark" width="30" height="12" viewBox="0 0 30 12" aria-hidden="true">
      <path d="M1 9 C 8 4, 18 2, 29 3" fill="none" stroke="#EDEAE4" strokeWidth="2" strokeLinecap="round" />
    </svg>
  );
}
