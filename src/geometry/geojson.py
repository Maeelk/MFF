"""GeoJSON parsing utilities for Zone objects."""

from __future__ import annotations

import json
from typing import Any, Dict, List

from .types import Polygon, Zone
from .validators import GeometryError, validate_polygons


class GeoJSONError(ValueError):
    """Raised when GeoJSON data cannot be parsed into a Zone."""


def _parse_polygon_coords(coords: Any) -> Polygon:
    if not isinstance(coords, list):
        raise GeoJSONError("Polygon coordinates must be a list")
    polygon: Polygon = []
    for ring in coords:
        if not isinstance(ring, list):
            raise GeoJSONError("Linear ring must be a list of positions")
        polygon.append([tuple(position) for position in ring])
    return polygon


def zone_from_geojson(data: Dict[str, Any], crs: str = "EPSG:4326") -> Zone:
    if "type" not in data:
        raise GeoJSONError("GeoJSON must include a 'type' field")

    geo_type = data["type"]
    if geo_type == "Polygon":
        polygons = [_parse_polygon_coords(data.get("coordinates"))]
    elif geo_type == "MultiPolygon":
        coords = data.get("coordinates")
        if not isinstance(coords, list):
            raise GeoJSONError("MultiPolygon coordinates must be a list")
        polygons = [_parse_polygon_coords(polygon) for polygon in coords]
    else:
        raise GeoJSONError("GeoJSON must be of type Polygon or MultiPolygon")

    try:
        validate_polygons(polygons)
    except GeometryError as exc:
        raise GeoJSONError(str(exc)) from exc

    return Zone(polygons=polygons, crs=crs)


def zone_from_geojson_str(payload: str, crs: str = "EPSG:4326") -> Zone:
    return zone_from_geojson(json.loads(payload), crs=crs)
