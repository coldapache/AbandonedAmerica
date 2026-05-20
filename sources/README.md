# Sources

Every data source we've used (or identified as usable) to research ABNC properties across the US lives here. Updated as we expand into new regions.

## Files

- **`sources.csv`** — Master catalog. Every government registry, open-data portal, land bank, assessor, news source, and community list we know about.
- **`data/`** — Raw data dumps pulled from upstream sources. Use these as candidate pools to mine for new properties; do not append directly to the main CSV without per-property verification.

## sources.csv schema

| Column | Description |
|---|---|
| `name` | Human-readable source name |
| `url` | Canonical URL (registry page, API root, or data download) |
| `scope` | `national` / `state` / `regional` / `county` / `city` |
| `state` | Two-letter state code (blank for national) |
| `city_or_county` | Locality name |
| `category` | `registry` / `open_data` / `code_enforcement` / `assessor` / `land_bank` / `parcel_gis` / `tax_records` / `municipal_code` / `community_blog` / `news` / `research` / `directory` / `receivership_program` / `brownfields` / `redevelopment` / `surplus_property` / `foreclosure` / `dashboard` / `commercial_listings` / `community_list` / `visual_verification` / `vacancy_aggregate` / `state_program` / `permits` / `records` / `land_records` |
| `format` | `HTML` / `PDF` / `CSV` / `JSON` / `XLSX` / `SHP` / `Socrata` / `ArcGIS` / `CARTO_API` / `Accela` / `CitizenServe` / `interactive_map` / `dashboard` |
| `access` | `open_api` / `public_html` / `downloadable` / `records_request` / `login_required` |
| `record_count` | Approximate record count if known |
| `notes` | Distinguishing details, gotchas, or pro tips |

## Tier-1 sources (gold-standard, downloadable + structured)

These return real address data without records requests:

- **Reading PA Certified Blighted Properties** — 400+ city-certified buildings, downloadable XLSX
- **LA Vacant Building Abatement (Socrata)** — 730 active LADBS abatement cases, JSON/CSV via `data.lacity.org/resource/q3ak-s5hy`
- **Seattle Code Complaints (Socrata)** — 4,110 records tagged "Vacant Building" with lat/lon, via `data.seattle.gov/resource/ez4a-iug7`
- **Philadelphia OPA CARTO API** — query exterior_condition 6-7 for worst-rated buildings citywide
- **Berks County PA ArcGIS FeatureServer** — owner + assessment + geometry for every parcel
- **Sacramento Vacant Building Cases (CitizenServe)** — ~150 active cases, scrapable

## Tier-2 sources (program exists, list available on request)

- **SF DBI Vacant Building Registry** — ~700 buildings, list maintained by DBI
- **Hartford Blight Remediation Team** — 400+ properties, FOIA-only
- **Klamath Falls Housing Blight** — 157 properties on internal list (2025)
- **Vallejo Vacant Real Property** — registry under VMC Ch 7.62
- **Richmond CA Vacant Dwellings** — RMC §6.38 registry
- **Spokane Vacant Property Registry** — 2014 ordinance; FOIA via public records
- **Anchorage Vacant Building Registry** — AO 2016-81

## How to extend this

When you research a new city:
1. Check if `sources.csv` already has a row for that city.
2. If yes, use it. If no, find the city's code enforcement / vacant building program and add a row.
3. If the city has open data, prioritize Socrata or ArcGIS APIs over scraping HTML.
4. Record any record counts you observe — they help us prioritize where to mine next.
