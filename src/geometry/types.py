"""Core geometry types."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable, List, Sequence, Tuple

Point = Tuple[float, float]
LinearRing = List[Point]
Polygon = List[LinearRing]


@dataclass(frozen=True)
class Zone:
    """A GeoJSON polygon or multipolygon represented as polygons of rings."""

    polygons: List[Polygon]
    crs: str = "EPSG:4326"

    def all_rings(self) -> Iterable[LinearRing]:
        for polygon in self.polygons:
            for ring in polygon:
                yield ring


class GridType(str, Enum):
    CELLS = "cells"
    STRIPS = "strips"
    RAKES = "rakes"


@dataclass(frozen=True)
class Grid:
    """Generated grid elements for a zone."""

    grid_type: GridType
    cells: Sequence[Polygon]
    crs: str
