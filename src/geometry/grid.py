"""Grid generation strategies."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

from .types import Grid, GridType, LinearRing, Point, Polygon, Zone


@dataclass(frozen=True)
class GridSpec:
    spacing: float


def _bbox(zone: Zone) -> Tuple[float, float, float, float]:
    xs: List[float] = []
    ys: List[float] = []
    for ring in zone.all_rings():
        xs.extend(point[0] for point in ring)
        ys.extend(point[1] for point in ring)
    if not xs or not ys:
        raise ValueError("Zone has no coordinates")
    return min(xs), min(ys), max(xs), max(ys)


def _rectangle(min_x: float, min_y: float, max_x: float, max_y: float) -> Polygon:
    ring: LinearRing = [
        (min_x, min_y),
        (max_x, min_y),
        (max_x, max_y),
        (min_x, max_y),
        (min_x, min_y),
    ]
    return [ring]


def generate_cells(zone: Zone, spec: GridSpec) -> Sequence[Polygon]:
    min_x, min_y, max_x, max_y = _bbox(zone)
    cells: List[Polygon] = []
    x = min_x
    while x < max_x:
        y = min_y
        next_x = min(x + spec.spacing, max_x)
        while y < max_y:
            next_y = min(y + spec.spacing, max_y)
            cells.append(_rectangle(x, y, next_x, next_y))
            y = next_y
        x = next_x
    return cells


def generate_strips(zone: Zone, spec: GridSpec) -> Sequence[Polygon]:
    min_x, min_y, max_x, max_y = _bbox(zone)
    strips: List[Polygon] = []
    x = min_x
    while x < max_x:
        next_x = min(x + spec.spacing, max_x)
        strips.append(_rectangle(x, min_y, next_x, max_y))
        x = next_x
    return strips


def generate_rakes(zone: Zone, spec: GridSpec) -> Sequence[Polygon]:
    min_x, min_y, max_x, max_y = _bbox(zone)
    rakes: List[Polygon] = []
    y = min_y
    while y < max_y:
        next_y = min(y + spec.spacing, max_y)
        rakes.append(_rectangle(min_x, y, max_x, next_y))
        y = next_y
    return rakes


def generate_grid(zone: Zone, grid_type: GridType, spec: GridSpec) -> Grid:
    if grid_type == GridType.CELLS:
        cells = generate_cells(zone, spec)
    elif grid_type == GridType.STRIPS:
        cells = generate_strips(zone, spec)
    elif grid_type == GridType.RAKES:
        cells = generate_rakes(zone, spec)
    else:
        raise ValueError(f"Unsupported grid type: {grid_type}")
    return Grid(grid_type=grid_type, cells=cells, crs=zone.crs)
