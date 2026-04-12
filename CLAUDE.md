# CLAUDE.md - Project Context for AI Agents

## What This Project Is

Abandoned America is a crowdsourced national database of abandoned, blighted, and non-contributing (ABNC) properties. The database is a single CSV file. The viewer is a single HTML file. There is no backend.

## Key Files

- `Abandoned America - Abandoned or Unused Properties.csv` - THE database. Every row = one property.
- `index.html` - Map viewer. Leaflet + PapaParse + MarkerCluster. No build step. Open in browser.
- `README.md` - Full instructions, data schema, contribution workflow.
- `.claude/commands/hunt-properties.md` - Slash command: find new ABNC properties in a target area using web search + Playwright
- `.claude/commands/verify-property.md` - Slash command: verify existing properties via Playwright + Google Maps Street View
- `.claude/commands/validate-csv.md` - Slash command: comprehensive data quality validation

## Data Schema (Strict)

CSV columns: `address,lat,lon,city,state,zip,type,status,owner,assessment,link,source,notes`

### Allowed `status` values (EXACT - do not deviate):
- `ABANDONED`
- `CHRONICALLY VACANT`
- `CONDEMNED`
- `DEMOLISHED`
- `PROBABLY VACANT`
- `VACANT`

### Allowed `type` values (EXACT - do not deviate):
- `COMMERCIAL`
- `COMMERCIAL OFFICE`
- `HOSPITALITY`
- `INDUSTRIAL`
- `INSTITUTIONAL`
- `MIXED USE`
- `RESIDENTIAL`
- `RESTAURANT`
- `RETAIL`
- `WAREHOUSE`

## Critical Rules

1. Never add a property that already exists in the CSV (check address first)
2. Never invent status or type values outside the enums above
3. Always include a Google Maps link (Street View preferred)
4. Coordinates must be verified against the address via Google Maps
5. Use minus sign `-` for negative longitude, never en-dash
6. Assessment values must come from official tax records, not estimates
7. Owner names in uppercase when from official records
8. ZIP codes must be 5 digits and valid for the state
9. Latitude range: 24.0 to 49.5 (contiguous US)
10. Longitude range: -125.0 to -66.5 (contiguous US)
11. Do not add DEMOLISHED properties — demolition is a resolution, not an ongoing problem. Only add properties where a structure still stands.

## Contribution Workflow

1. Create a branch: `add-properties-[city]-[state]`
2. Research properties via government records, tax records, Google Maps
3. Add rows to the CSV following the schema exactly
4. Validate: no duplicates, valid enums, valid coordinates, valid links
5. Commit and push
6. Open a PR with source information

## Data Completeness Requirements

Every property MUST have all of these to be considered complete:
- Address, city, state, ZIP, lat, lon (the basics)
- A valid status and type from the enums
- A Google Maps link (Street View link strongly preferred)
- Coordinates that are verified to match the address

Properties SHOULD have (agents should make best effort to find):
- Owner name from tax/property records
- Tax assessed value from county records
- Source URL linking to where the property data was found

Agents should use Playwright/browser automation to visually verify properties appear abandoned, blighted, or vacant before adding them. Do not add properties based solely on a list without visual confirmation.

## When Modifying the Viewer

- `index.html` is self-contained. All CSS/JS is inline.
- Uses CDN: Leaflet 1.9.4, Leaflet.markercluster 1.5.3, PapaParse 5.4.1
- Map tiles: CartoDB Dark (default), OpenStreetMap, Esri Satellite
- Marker clustering is required - the database will grow to thousands of properties
- Viewport-based marker loading caps at 500 visible markers
- No API keys required
- Must work when opened as a local file (no server needed)
