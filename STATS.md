# Abandoned America — Stats & Methodology

A snapshot of what the database currently holds and how it got there.

> **Snapshot date:** 2026-07-24 (post-convergence)
> **Source:** [`Abandoned America - Abandoned or Unused Properties.csv`](Abandoned%20America%20-%20Abandoned%20or%20Unused%20Properties.csv)
> **Live view:** open `index.html` in a browser and look at the **Dashboard** tab.

---

## At a glance

| Metric | Value |
|---|---|
| **Properties cataloged** | **2,648** |
| **Total assessed value** | **$1,279,339,285** (~$1.28B) |
| **Properties with assessment data** | 2,248 (84.9%) |
| **Average assessment** (where known) | $569,101 |
| **Cities covered** | 112 |
| **States covered** | 49 |
| **Government-owned** | 242 (9.1%, ~$148.7M assessed) |
| **Human-verified** | 76 (2.9%) |

This snapshot reflects the **2026-07-24 convergence**, which merged every
outstanding work branch into `main` after a row-level audit. ~850 rows whose
producer classes had been measured as sustained false-positive sources were
removed, and the remainder corrected. See "Convergence" below.

These numbers grow continuously as agents add batches. Re-run the
snapshot script (below) to refresh.

---

## By status

| Status | Count | Assessed total |
|---|---:|---:|
| `VACANT` | 1,006 | $628,900,886 |
| `ABANDONED` | 625 | $360,365,155 |
| `CONDEMNED` | 534 | $149,022,299 |
| `PROBABLY VACANT` | 281 | $55,671,785 |
| `CHRONICALLY VACANT` | 202 | $85,379,160 |

> `DEMOLISHED` is **not hunted** — demolition is a resolution, not an
> ongoing problem. The schema permits it for legacy/historical reasons
> but new contributions should never use it. See "Rules" below.

---

## By type

| Type | Count |
|---|---:|
| `RESIDENTIAL` | 1,986 |
| `COMMERCIAL` | 287 |
| `INSTITUTIONAL` | 84 |
| `RETAIL` | 73 |
| `MIXED USE` | 68 |
| `COMMERCIAL OFFICE` | 56 |
| `INDUSTRIAL` | 43 |
| `WAREHOUSE` | 23 |
| `RESTAURANT` | 14 |
| `HOSPITALITY` | 14 |

---

## Top states (by abandoned assessed value)

| State | Properties | Assessed total |
|---|---:|---:|
| NC | 38 | $265,828,987 |
| DC | 143 | $198,189,702 |
| PA | 409 | $126,935,271 |
| NJ | 282 | $101,162,800 |
| VA | 96 | $90,224,646 |
| MA | 27 | $59,234,900 |
| TN | 153 | $55,328,880 |
| WA | 41 | $48,060,900 |
| WI | 142 | $46,583,827 |
| NY | 26 | $37,936,002 |
| MO | 288 | $34,485,623 |
| CA | 67 | $31,917,917 |

North Carolina leads on $ despite only 38 records because most are
fully assessed large-footprint commercial/institutional parcels
(former malls, decommissioned schools, etc.). The contrast with
states like MO/NY — many small residential parcels — shows up clearly.

---

## Top cities (by abandoned assessed value)

| City | Properties | Assessed total |
|---|---:|---:|
| Washington, DC | 143 | $198,189,702 |
| Charlotte, NC | 19 | $124,950,400 |
| Raleigh, NC | 3 | $100,564,906 |
| Paterson, NJ | 190 | $96,703,400 |
| Philadelphia, PA | 103 | $96,398,000 |
| Boston, MA | 25 | $59,234,900 |
| Nashville, TN | 52 | $54,316,000 |
| Milwaukee, WI | 142 | $46,583,827 |
| Seattle, WA | 40 | $44,935,800 |
| Durham, NC | 4 | $40,101,181 |
| New York, NY | 25 | $37,436,002 |
| Richmond, VA | 53 | $34,336,000 |
| Newport News, VA | 8 | $28,538,800 |
| Los Angeles, CA | 41 | $27,915,733 |
| Indianapolis, IN | 125 | $26,663,900 |

---

## Top government owners

Properties whose `owner` field matches government / municipal patterns
(`CITY OF`, `COUNTY OF`, `REDEVELOPMENT`, `HOUSING AUTHORITY`,
`LAND BANK`, `URBAN RENEWAL`, etc.).

| Owner | Properties | Assessed total |
|---|---:|---:|
| CITY OF DURHAM | 1 | $38,891,314 |
| STATE OF TENNESSEE | 2 | $29,763,500 |
| CITY OF RALEIGH | 1 | $27,567,751 |
| CITY OF NEWPORT NEWS SCHOOL BOARD | 1 | $17,133,100 |
| NORFOLK ECONOMIC DEVELOPMENT AUTHORITY | 1 | $14,647,200 |
| HOUSING AUTHORITY CITY OF GARY | 1 | $2,088,300 |
| BIRMINGHAM LAND BANK AUTHORITY | 13 | $1,913,300 |
| CITY OF PHILA | 1 | $1,826,200 |
| CITY OF NORFOLK | 3 | $1,655,900 |
| CITY OF NEWARK | 1 | $1,551,300 |
| PHILADELPHIA REDEVELOPMENT AUTHORITY | 1 | $1,451,500 |
| URBAN REDEVELOPMENT AUTHORITY OF PITTSBURGH | 4 | $1,280,200 |

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

## Convergence (2026-07-24)

All outstanding work branches were merged into `main` in one operation. The repo
had accumulated **459 branches editing the same CSV**, many forked from old
versions of `main`, so a plain `git merge` would have reverted thousands of rows.

Instead each branch was diffed against **its own merge-base with `main`** and the
intents were reconciled per row:

| Action | Rows | Reason |
|---|---:|---|
| Removed | 851 | Audit campaigns: producer classes measured as sustained false-positive sources, plus stale/rehabbed records and vacant lots |
| Corrected | 386 | Field fixes (coordinates, links, owner, assessment) |
| Added | 63 | Official condemnation lists, land bank parcels, named landmarks |
| Added but rejected | 446 | Re-imported a producer class that had been burned as unverified |
| Conflict, main kept | 64 | Both sides changed the row; `main`'s version retained |

`3,436 → 2,648` rows. Every branch is now recorded as an ancestor of `main`
(564/564 remote branches contained), so no branch can silently diverge again.

**Producer classes that were burned** (whole classes removed for sustained high
false-positive rates, verified by repeated Street View audits): Buffalo/Rochester
NY VBR (100% FP), Lexington LFUCG 581H (125 rows), Chicago Cook County 2017 REO,
Akron scouted, Hampton VA, Clarksville MCGTN, Philadelphia L&I bulk violations,
Cleveland active-condemnations (86% FP), NYC Storefront Tracker, Covington/
Owensboro LINK-GIS absentee-LLC rotation, low-value-ratio pattern (94 rows).

**Tooling:** `tools/converge.py` performs the merge and is re-runnable;
`tools/validate-csv.py` enforces the schema; `tools/converge-report.json` lists
every accepted and rejected row together with the branch that proposed it, so
any dropped addition can be re-litigated individually.

**Do not re-import** rows sourced from the burned classes above without visual
confirmation (`CLAUDE.md` rule: no property from a list alone).

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

*Snapshot generated 2026-07-24 after the convergence. The numbers above are
point-in-time and will be out of date almost immediately — the project is
actively growing. See the live dashboard for current figures.*
