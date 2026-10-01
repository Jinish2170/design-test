import type { ReactNode } from 'react';
import wheel from '../assets/cars/wheel.svg';
import { CARS, type CarModel } from '../data/content';

interface CarProps {
  model: CarModel;
  alt: string;
  className?: string;
  /** `idle` = a slow automatic light sweep; any other class drives the sweep from scroll. */
  sweep?: string;
  children?: ReactNode;
}

/**
 * A layered car: body artwork, two wheels that spin with `--spin`, a band of light clipped to the
 * body silhouette, and a faint floor reflection. Same rig for every model so photography can be
 * swapped in later (cut-out body + wheels + mask).
 */
export function Car({ model, alt, className = '', sweep = 'idle', children }: CarProps) {
  const art = CARS[model];
  return (
    <div className={`car ${className}`}>
      <img className="car-body" src={art.body} alt={alt} draggable={false} />
      {art.wheels.map(([x, y, r]) => {
        // wheel.svg is a 160×160 sprite with a 76px tyre radius
        const size = (r * 160) / 76;
        return (
          <img
            key={x}
            className="wheel"
            src={wheel}
            alt=""
            draggable={false}
            style={{ left: `${(x - size / 2) / 12}%`, top: `${(y - size / 2) / 4}%`, width: `${size / 12}%`, height: `${size / 4}%` }}
          />
        );
      })}
      <div className={`sweep m-${model} ${sweep}`} />
      <img className="reflect" src={art.full} alt="" draggable={false} />
      {children}
    </div>
  );
}
