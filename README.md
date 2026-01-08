# MFF

## Geometry module

The `src/geometry/` module exposes two core types:

- `Zone`: a GeoJSON Polygon or MultiPolygon represented as a list of polygons, each with one exterior ring and optional interior rings (holes).
- `Grid`: generated polygons for grid cells, strips, or rakes.

### Input format

The module expects a GeoJSON `Polygon` or `MultiPolygon` payload. Coordinates must be expressed as `[x, y]` pairs and follow the GeoJSON structure:

- **Polygon**: `{"type": "Polygon", "coordinates": [ [ [x, y], ... ], [ [x, y], ... ] ] }` where the first ring is the exterior, the others are holes.
- **MultiPolygon**: `{"type": "MultiPolygon", "coordinates": [ [ [ [x, y], ... ] ] , ... ] }`.

Rings must be closed (first position equals last position), the exterior ring must be counterclockwise, interior rings must be clockwise, and no ring may self-intersect.

### Projection

By default, coordinates are assumed to be in **WGS84 (EPSG:4326)**. You can override this when calling the GeoJSON parser by passing a different CRS identifier string (for example `EPSG:2154` for metric coordinates in Lambert 93).
