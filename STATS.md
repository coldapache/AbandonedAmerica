# Abandoned America — Stats & Methodology

A snapshot of what the database currently holds and how it got there.

> **Snapshot date:** 2026-05-20
> **Source:** [`Abandoned America - Abandoned or Unused Properties.csv`](Abandoned%20America%20-%20Abandoned%20or%20Unused%20Properties.csv)
> **Live view:** open `index.html` in a browser and look at the **Dashboard** tab.

---

## At a glance

| Metric | Value |
|---|---|
| **Properties cataloged** | **2,607** |
| **Total assessed value** | **$1,096,392,833** (~$1.10B) |
| **Properties with assessment data** | 2,098 (80.5%) |
| **Average assessment** (where known) | $522,590 |
| **Cities covered** | 111 |
| **States covered** | 49 |
| **Government-owned** | 279 (10.7%, ~$100.7M assessed) |
| **Human-verified** | 30 (1.2%) |

These numbers grow continuously as agents add batches. Re-run the
snapshot script (below) to refresh.

---

## By status

| Status | Count | Assessed total |
|---|---:|---:|
| `VACANT` | 1,108 | $534,289,841 |
| `ABANDONED` | 646 | $352,457,472 |
| `CONDEMNED` | 405 | $67,807,529 |
| `PROBABLY VACANT` | 252 | $49,707,371 |
| `CHRONICALLY VACANT` | 196 | $92,130,620 |

> `DEMOLISHED` is **not hunted** — demolition is a resolution, not an
> ongoing problem. The schema permits it for legacy/historical reasons
> but new contributions should never use it. See "Rules" below.

---

## By type

| Type | Count |
|---|---:|
| `RESIDENTIAL` | 1,965 |
| `COMMERCIAL` | 281 |
| `MIXED USE` | 71 |
| `RETAIL` | 65 |
| `COMMERCIAL OFFICE` | 59 |
| `INSTITUTIONAL` | 56 |
| `INDUSTRIAL` | 51 |
| `WAREHOUSE` | 31 |
| `HOSPITALITY` | 15 |
| `RESTAURANT` | 13 |

---

## Top states (by abandoned assessed value)

| State | Properties | Assessed total |
|---|---:|---:|
| NC | 22 | $257,527,587 |
| VA | 128 | $183,527,156 |
| DC | 100 | $140,833,022 |
| PA | 349 | $123,506,571 |
| NJ | 336 | $118,317,400 |
| WI | 120 | $43,685,727 |
| MO | 346 | $34,653,359 |
| OH | 153 | $27,099,300 |
| IN | 119 | $26,335,800 |
| NY | 207 | $20,227,020 |

North Carolina leads on $ despite only 22 records because all 22 are
fully assessed large-footprint commercial/institutional parcels
(former malls, decommissioned schools, etc.). The contrast with
states like MO/NY — many small residential parcels — shows up clearly.

---

## Top cities (by abandoned assessed value)

| City | Properties | Assessed total |
|---|---:|---:|
| Washington, DC | 100 | $140,833,022 |
| Charlotte, NC | 3 | $116,649,000 |
| Paterson, NJ | 233 | $115,087,600 |
| Raleigh, NC | 3 | $100,564,906 |
| Hampton, VA | 53 | $99,581,400 |
| Philadelphia, PA | 101 | $94,940,300 |
| Milwaukee, WI | 120 | $43,685,727 |
| Durham, NC | 4 | $40,101,181 |
| Newport News, VA | 8 | $28,538,800 |
| Richmond, VA | 33 | $28,108,000 |
| Cleveland, OH | 121 | $27,099,300 |
| Indianapolis, IN | 100 | $22,498,600 |
| St. Louis, MO | 8 | $21,162,097 |
| Pittsburgh, PA | 93 | $20,624,731 |
| Norfolk, VA | 17 | $19,973,100 |

---

## Top government owners

Properties whose `owner` field matches government / municipal patterns
(`CITY OF`, `COUNTY OF`, `REDEVELOPMENT`, `HOUSING AUTHORITY`,
`LAND BANK`, `URBAN RENEWAL`, etc.).

| Owner | Properties | Assessed total |
|---|---:|---:|
| City of Durham | 1 | $38,891,314 |
| City of Raleigh | 1 | $27,567,751 |
| City of Newport News School Board | 1 | $17,133,100 |
| Housing Authority City of Gary | 1 | $2,088,300 |
| Land Reutilization Authority (St. Louis) | 199 | $1,713,084 |
| City of Norfolk | 3 | $1,655,900 |
| Philadelphia Redevelopment Authority | 1 | $1,451,500 |
| Urban Redevelopment Authority of Pittsburgh | 4 | $1,280,200 |
| Gary Housing Authority | 2 | $1,254,700 |
| City of Atlanta | 2 | $1,033,520 |

Government ownership is meaningful because these entities have legal
authority to dispose of properties (auction, redevelopment grants,
demolition) without finding an absent private owner. They represent
the most actionable slice of the inventory.

---

## Methodology

### Data sources

Properties enter the database from a mix of structured and unstructured
sources. Roughly in order of reliability:

1. **City-certified blight lists** — official lists where a city has
   formally declared a property blighted (e.g. City of Reading PA
   Certified Blighted Properties, Detroit BSEED Vacant Property
   Registry, Cleveland Active Condemnations, Milwaukee DNS Vacant
   Building registry). Strongest signal — already adjudicated.
2. **County GIS / parcel layers** — ArcGIS FeatureServers and
   parcel databases providing owner, assessed value, and geometry
   (e.g. Berks County PA, Philadelphia OPA, Allegheny County WPRDC).
   Used both for enrichment of leads and as candidate pools when
   filtered for indicators like exterior condition 7 (worst).
3. **Open-data vacant building portals** — Socrata / CKAN feeds from
   cities like Seattle (SDCI vacant building complaints), Los Angeles
   (LADBS vacant building abatement cases), Baltimore (Vacant Building
   Notices).
4. **State / federal aggregators** — HUD vacancy data, USDA Cropland
   Data Layer (for farm abandonment), state-level inventories.
5. **News articles & community reporting** — used for landmark
   properties (closed factories, abandoned hotels, historic blighted
   structures) and to fill gaps where structured sources are thin.
6. **AbandonedAmerica.us aggregator** — third-party photography site
   crawled for property leads.

A full catalog of ~177 sources across 13 jurisdictions lives in
[`sources/sources.csv`](sources/sources.csv) and accompanying
[`SOURCES.md`](SOURCES.md).

### Pipeline

Every batch follows a 5-stage pipeline (documented in
`.claude/skills/data-aggregation/SKILL.md`):

```
1. Source ingest    — pull from blight list / GIS / portal → JSON
2. Parcel lookup    — enrich with owner, assessment, coords via ArcGIS
3. Filter           — dedupe, drop $0 building value, drop exempt parcels
4. Curate + assemble— pick ~20, look up ZIPs, classify type, format row
5. Append           — write to master CSV with strict UTF-8 BOM + QUOTE_ALL
```

Intermediate JSON files at every stage make the pipeline restartable
and inspectable. Working files live under `temp/` (gitignored).

### Verification

CLAUDE.md rule #12: the Street View link must show the actual
described property. This is the #1 data quality problem in the
project. We enforce it through:

- **`sv-verify` skill** (`.claude/skills/sv-verify/`) — uses Playwright
  to open Street View at the property coordinates, parses the
  rewritten pano position from the URL, computes the forward-azimuth
  bearing from pano → property, and rebuilds a SV URL with the
  correct heading and a pano-ID lock. Screenshots go to
  `temp/images/sv-verify/` for human review.
- **Acceptance criterion:** the screenshot must show an *identifiable
  building*. Flat walls, sky, or unrelated active businesses mean the
  camera is aimed wrong (almost always 180° off — fix by flipping
  heading). Wrong-building cases mean the coordinates are wrong and
  need re-geocoding.
- **Human confirmation:** the viewer has a "Confirm Abandoned" button
  that flips `human_confirmed` to `HUMAN CONFIRMED` for properties a
  person has visually verified. Currently 1.2% verified — this is the
  metric we want to grow.

### Tooling

| Tool | Role |
|---|---|
| **Python** | All batch scripts, CSV manipulation, Socrata/ArcGIS API calls |
| **Playwright** | Visual verification, county assessor scraping when no API exists |
| **Census Geocoder** | Coordinate verification, address → lat/lon |
| **Nominatim** | ZIP code lookups from coordinates |
| **ArcGIS REST** | Parcel data from county GIS layers |
| **Leaflet + MarkerCluster** | Map viewer (frontend) |
| **PapaParse** | CSV parsing in the browser |

No backend service. No database. The CSV is the database.

### Quality rules

Enforced by `.claude/commands/validate-csv.md` and convention:

1. No duplicates — check address before adding
2. Lat/lon within CONUS bounds (24–50°N, 66–126°W)
3. Coordinates must visually match the property in Google Maps
4. Status and type must be from the strict enums
5. ZIP must be 5 digits, valid for the state
6. Assessment values come from official tax records, never estimates
7. Owner names UPPERCASE when from official records
8. Use `-` for negative longitude (never en-dash `–`)
9. `DEMOLISHED` is never added on new hunts — demolition is a resolution
10. Properties must have a Google Maps link; Street View preferred
11. Building value > $0 — guarantees a standing structure
12. Street View must show the actual property (the #1 data-quality rule)

---

## How to regenerate this snapshot

```bash
python -c "
import csv, re
from collections import Counter
CSV = 'Abandoned America - Abandoned or Unused Properties.csv'
def parse_amt(s):
    if not s: return 0
    try: return float(re.sub(r'[\$,\s]', '', str(s)))
    except: return 0
with open(CSV, encoding='utf-8-sig') as f:
    rows = list(csv.DictReader(f))
print(f'Total: {len(rows)}')
print(f'Assessed total: \${sum(parse_amt(r[\"assessment\"]) for r in rows):,.0f}')
"
```

Then update the tables above. The dashboard tab in the live viewer
shows the same numbers in real time without needing to re-run anything.

---

*Snapshot generated 2026-05-20. The numbers above are point-in-time and
will be out of date almost immediately — the project is actively
growing. See the live dashboard for current figures.*
