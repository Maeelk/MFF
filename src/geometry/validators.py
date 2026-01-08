"""Validation helpers for GeoJSON polygons."""

from __future__ import annotations

from typing import Iterable, List, Tuple

from .types import LinearRing, Point, Polygon


class GeometryError(ValueError):
    """Raised when a geometry is invalid."""


def ensure_ring_closed(ring: LinearRing) -> None:
    if len(ring) < 4:
        raise GeometryError("Linear ring must have at least 4 positions")
    if ring[0] != ring[-1]:
        raise GeometryError("Linear ring must be closed (first position == last position)")


def signed_area(ring: LinearRing) -> float:
    area = 0.0
    for (x1, y1), (x2, y2) in zip(ring, ring[1:]):
        area += (x1 * y2) - (x2 * y1)
    return area / 2.0


def is_counterclockwise(ring: LinearRing) -> bool:
    return signed_area(ring) > 0


def _segments(ring: LinearRing) -> Iterable[Tuple[Point, Point]]:
    for start, end in zip(ring, ring[1:]):
        yield start, end


def _orientation(a: Point, b: Point, c: Point) -> int:
    val = (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    if abs(val) < 1e-12:
        return 0
    return 1 if val > 0 else 2


def _on_segment(a: Point, b: Point, c: Point) -> bool:
    return (
        min(a[0], c[0]) <= b[0] <= max(a[0], c[0])
        and min(a[1], c[1]) <= b[1] <= max(a[1], c[1])
    )


def _segments_intersect(p1: Point, q1: Point, p2: Point, q2: Point) -> bool:
    o1 = _orientation(p1, q1, p2)
    o2 = _orientation(p1, q1, q2)
    o3 = _orientation(p2, q2, p1)
    o4 = _orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and _on_segment(p1, p2, q1):
        return True
    if o2 == 0 and _on_segment(p1, q2, q1):
        return True
    if o3 == 0 and _on_segment(p2, p1, q2):
        return True
    if o4 == 0 and _on_segment(p2, q1, q2):
        return True

    return False


def ensure_no_self_intersection(ring: LinearRing) -> None:
    segments = list(_segments(ring))
    for i, (a1, a2) in enumerate(segments[:-1]):
        for j, (b1, b2) in enumerate(segments[i + 1 :], start=i + 1):
            if abs(i - j) <= 1 or (i == 0 and j == len(segments) - 1):
                continue
            if _segments_intersect(a1, a2, b1, b2):
                raise GeometryError("Linear ring has a self-intersection")


def validate_polygon(polygon: Polygon) -> None:
    if not polygon:
        raise GeometryError("Polygon must contain at least one linear ring")
    for idx, ring in enumerate(polygon):
        ensure_ring_closed(ring)
        ensure_no_self_intersection(ring)
        if idx == 0 and not is_counterclockwise(ring):
            raise GeometryError("Exterior ring must be counterclockwise")
        if idx > 0 and is_counterclockwise(ring):
            raise GeometryError("Interior rings must be clockwise")


def validate_polygons(polygons: List[Polygon]) -> None:
    for polygon in polygons:
        validate_polygon(polygon)
