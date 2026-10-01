import { useEffect, useState } from 'react';

const fmt = (() => {
  try {
    return new Intl.DateTimeFormat('en-NZ', {
      timeZone: 'Pacific/Auckland',
      hour: '2-digit',
      minute: '2-digit',
      hour12: false,
    });
  } catch {
    return null;
  }
})();

const now = () => (fmt ? fmt.format(new Date()) : '');

/** Current Auckland time as HH:MM, refreshed every 15 s. */
export function useAucklandTime() {
  const [time, setTime] = useState(now);
  useEffect(() => {
    const id = window.setInterval(() => setTime(now()), 15_000);
    return () => window.clearInterval(id);
  }, []);
  return time;
}
