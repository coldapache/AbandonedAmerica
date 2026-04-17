# Abandoned America

A crowdsourced, AI-assisted effort to map **every** abandoned, blighted, and non-contributing (ABNC) property in the United States.

**The goal is total national coverage.** Not 30 properties. Not 300. Every abandoned storefront, every condemned factory, every blighted commercial corridor, every vacant lot where a building used to stand — in every city, every county, all 50 states. This is a living database that grows continuously as AI agents and human contributors sweep the country, one corridor at a time.

**The idea is simple:** AI coding agents (Claude Code, OpenClaw, Codex, etc.) can clone this project, search for abandoned properties in any area, add them to the CSV database, and submit a pull request. The map viewer renders everything in real time — no backend, no API keys. As the database scales from hundreds to thousands to hundreds of thousands of properties, the full scope of America's abandonment crisis becomes visible for the first time.

---

## Quick Start

```bash
git clone git@github.com:coldapache/AbandonedAmerica.git
cd AbandonedAmerica
```

```bash
# Start the dev server (enables human verification feature):
python server.py
# Then open http://localhost:8080 in your browser
```

The dev server serves static files and provides an API endpoint for the "Confirm Abandoned" button in the UI. You can also use any static HTTP server (`python -m http.server 8080`) for read-only viewing, but the human confirmation feature requires `server.py`.

Opening `index.html` directly as a file won't work due to browser CORS restrictions on CSV loading.

---

## Project Structure

```
AbandonedAmerica/
  index.html                                          # Map viewer (single-file, zero deps besides CDN)
  Abandoned America - Abandoned or Unused Properties.csv  # The database
  WHY.md                                              # Why this project matters
  SOURCES.md                                          # Where to find data (national, state, local source guide)
  README.md                                           # This file (agent instructions)
  CLAUDE.md                                           # Claude Code project context
```

---

## The Database

The entire database is a single CSV file. Every row is one property. The columns are strictly defined below.

### Schema

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `address` | string | YES | Full street address. Format: `123 Main St, City, ST 12345` |
| `lat` | number | YES | Decimal latitude. Range: 24.0 to 49.5 (contiguous US). Min 6 decimal places. |
| `lon` | number | YES | Decimal longitude (negative). Range: -125.0 to -66.5. Use minus sign `-`, not en-dash. |
| `city` | string | YES | City name, proper case (e.g. `Hampton`, `Norfolk`) |
| `state` | string | YES | 2-letter US state abbreviation, uppercase (e.g. `VA`, `CA`, `TX`) |
| `zip` | string | YES | 5-digit US ZIP code. Must be valid for the state. |
| `type` | enum | YES | Property type. Must be one of the values below. |
| `status` | enum | YES | Property status. Must be one of the values below. |
| `owner` | string | NO | Property owner from tax/property records. Uppercase preferred. |
| `assessment` | string | NO | Tax assessed value. Format: `$1,234,567` with dollar sign and commas. |
| `link` | string | YES | Google Maps URL. Must start with `https://www.google.com/maps`. Include Street View link when available. |
| `source` | string | NO | URL to the source of the property data (city website, county records portal, news article, etc.) |
| `notes` | string | NO | Free-text observations about the property: confidence level, estimated vacancy duration, visual condition, ambiguity notes, or anything relevant that doesn't fit other columns. |
| `human_confirmed` | string | NO | Set to `HUMAN CONFIRMED` when a human has visually verified the property is abandoned via the UI. Only written through the viewer's "Confirm Abandoned" button — never set manually in the CSV. |

### Allowed `type` Values

| Value | Description |
|-------|-------------|
| `COMMERCIAL` | General commercial property (stores, dealerships, strip malls) |
| `COMMERCIAL OFFICE` | Office buildings, office parks |
| `HOSPITALITY` | Hotels, motels, inns |
| `INDUSTRIAL` | Factories, industrial yards, plants |
| `INSTITUTIONAL` | Schools, churches, government buildings, hospitals |
| `MIXED USE` | Combined retail/office/residential |
| `RESIDENTIAL` | Houses, apartments, duplexes, townhomes |
| `RESTAURANT` | Restaurants, diners, fast food |
| `RETAIL` | Retail storefronts, pharmacies, standalone retail |
| `WAREHOUSE` | Warehouses, storage facilities, distribution centers |

### Allowed `status` Values

| Value | Description |
|-------|-------------|
| `ABANDONED` | Property is abandoned. Signs of neglect, deterioration, no active use. |
| `CHRONICALLY VACANT` | Has been empty for an extended period (1+ years). No signs of returning to use. |
| `CONDEMNED` | Officially condemned by local government. Cannot be legally occupied. |
| `DEMOLISHED` | Structure has been torn down. May be an empty lot. |
| `PROBABLY VACANT` | Appears vacant based on visual/web evidence, but not confirmed through official records. |
| `VACANT` | Currently unoccupied. Structurally sound. No active business or residents. |

### Rules

- **No duplicate properties.** Before adding a property, search the CSV for the address.
- **All coordinates must be verified.** Use Google Maps to confirm lat/lon matches the address.
- **All properties must have a Google Maps link.** Street View links are strongly preferred.
- **Street View must show the actual property.** When you click "Open in Google Maps" or view the Street View embed, the building described in the record must be visible. If the Street View shows a different building, a residential street when the property is industrial, or a location blocks away from the address, the link/coordinates are wrong and must be fixed. This is the #1 data quality issue — coordinates from geocoders often land on the street or a neighboring parcel, not on the actual building.
- **Status must be from the enum.** Do not invent new statuses.
- **Type must be from the enum.** If a property doesn't fit, use the closest match.
- **Assessments from official tax records only.** Do not estimate.
- **Use the minus sign (`-`) for negative longitude.** Not an en-dash or em-dash.
- **Owner names in uppercase** when sourced from official records.
- **Include source URLs whenever possible** so others can verify the data.
- **Business closure ≠ building abandonment.** A business marked "CLOSED" on Yelp or Google does not qualify. The physical building must be verifiably vacant and unused. Visual verification via Google Maps/Street View is required for every property.
- **Do not add DEMOLISHED properties.** Demolition is a resolution — the blight problem has been addressed. Only add properties where a structure still stands. Existing DEMOLISHED entries in the database are kept as historical records, but agents should not hunt for or add new ones.

---

## For AI Agents: How to Contribute

This section is written for Claude Code, OpenClaw, Codex, and any AI coding assistant. If you are an AI agent, follow these steps.

### Step 1: Set Up

```bash
git clone git@github.com:coldapache/AbandonedAmerica.git
cd AbandonedAmerica
git checkout -b add-properties-[city]-[state]
```

### Step 2: Choose a Target Area

Pick a city, county, or region to research. The goal is full national coverage, so **every area is a valid target.** Prioritize:
- Areas with zero existing coverage in the database (check first — fill gaps before deepening existing cities)
- Cities known for high vacancy rates (Detroit, Baltimore, St. Louis, Cleveland, Gary, Camden, East St. Louis, Flint, etc.)
- Declining industrial and coal towns (Rust Belt, Appalachia, Mississippi Delta)
- Rural counties with shrinking populations
- Commercial corridors with visible blight (downtowns, old retail strips, industrial parks)
- The area where your user lives or requests

### Step 3: Check for Existing Coverage

Before researching, check what's already in the database:

```bash
grep -i "[city name]" "Abandoned America - Abandoned or Unused Properties.csv"
```

This tells you what's already been cataloged so you don't duplicate work.

### Step 4: Research Properties

**See [`SOURCES.md`](SOURCES.md) for a full guide to national, state, and local data sources.** It includes a search playbook for finding the right portals in any city/county.

For each target area, do ALL of the following — not just one. This is a single comprehensive workflow, not a menu of options.

#### Start with the easy money

Go after official government lists first. If a city or county publishes a list of condemned, blighted, or nuisance properties with a recent date — those are slam dunks. Take them, source them, and add them. But you STILL must verify each one has a working Google Maps link with valid coordinates before it goes in the database.

#### The full workflow

1. **Government Property Records** — Search for official condemned, blighted, and vacant property lists:
   - "[city] condemned properties list"
   - "[city] blighted properties"
   - "[city] code enforcement demolition list"
   - "[county] tax delinquent properties"
   - "[city] vacant property registry"
   - If you find an official list with recent dates, these are high-confidence adds — source the list URL

2. **Tax Assessment Records** — Look up the county assessor/GIS portal:
   - Search for "[county] property tax records" or "[county] GIS"
   - Find properties with very low assessments relative to their area
   - Find properties owned by "CITY OF..." or "COUNTY OF..." (often seized)
   - Pull owner names and assessed values for every property you add

3. **Google Maps Link Verification** — REQUIRED for every property, no exceptions:
   - Navigate to the address in Google Maps and confirm it resolves to the correct location
   - Verify the coordinates match the address (not off by a block, not in the wrong city)
   - Get Street View if available — visually confirm abandonment indicators
   - Look for: boarded windows, overgrown lots, collapsed roofs, graffiti, demolition debris
   - The link must actually work. Test it. Broken links = broken data.

4. **Google Earth Historical Imagery** — Time-travel to verify abandonment timeline:
   - Use Google Earth's historical imagery slider to view the property across different years
   - Confirm the property has been deteriorating or vacant over time (not just a recent closure)
   - Note when the property first appeared abandoned — this strengthens the case
   - Compare current vs. past imagery to distinguish truly abandoned properties from those under renovation

5. **News and Community Reports** — Cross-reference with local coverage:
   - "[city] abandoned buildings"
   - "[address] condemned" or "[address] demolished"
   - Local news often covers blight and demolition

Even "easy money" properties from official lists MUST have verified, working Google Maps links with correct coordinates before being added. No exceptions.

### Step 5: Build Each Property Record

For each property found, gather:

1. **Address** - Full street address from property records
2. **Coordinates** - Get lat/lon from Google Maps (right-click the location)
3. **City, State, ZIP** - From the address
4. **Type** - Classify using the enum above
5. **Status** - Classify using the enum above
6. **Owner** - From tax/property records (if available)
7. **Assessment** - Tax assessed value from county records (if available)
8. **Google Maps link** - Navigate to the property in Google Maps, copy the URL. Street View links preferred.

### Step 6: Add to CSV

Append rows to the CSV file. Follow the schema exactly. Example:

```csv
"123 Main St, Detroit, MI 48201",42.3314,-83.0458,Detroit,MI,48201,COMMERCIAL,ABANDONED,DOE JOHN,"$45,000","https://www.google.com/maps/place/123+Main+St..."
```

### Step 7: Validate

Before committing, verify:
- [ ] No duplicate addresses in the CSV
- [ ] All lat/lon coordinates are valid numbers in the US range
- [ ] All statuses are from the allowed enum
- [ ] All types are from the allowed enum
- [ ] All Google Maps links are valid URLs
- [ ] ZIP codes are 5 digits and valid for the state
- [ ] CSV parses correctly (no broken quoting)

### Step 8: Submit a Pull Request

**Keep PRs to ~20 properties max.** This keeps them small enough for reviewers to scan every entry for data quality. If you find more than 20 properties, submit multiple PRs in batches.

**Include new sources in your PR.** If you discovered a new assessor portal, condemned list, GIS viewer, or any other useful data source for the area you researched, add it to `SOURCES.md` under the appropriate section. This helps the next agent who works on that area.

```bash
git add "Abandoned America - Abandoned or Unused Properties.csv" SOURCES.md
git commit -m "Add [N] ABNC properties in [City], [State]"
git push origin add-properties-[city]-[state]
gh pr create --title "Add [N] properties in [City], [State]" --body "Added [N] abandoned/blighted/vacant properties in [City], [State]. Sources: [list sources]"
```

---

## AI Agent Commands

This repo ships with detailed command instructions in `.claude/commands/`. These work automatically as slash commands in Claude Code. For any other AI agent, read the markdown files directly and follow the steps.

### How It Works

The `.claude/commands/` directory contains markdown files that define autonomous workflows. Each file is a complete, step-by-step playbook that any AI agent can follow:

```
.claude/commands/
  hunt-properties.md    # Find and add new ABNC properties for a target area
  verify-property.md    # Visually verify existing properties via Google Maps
  validate-csv.md       # Run comprehensive data quality checks on the CSV
  repair-data.md        # Fill in missing fields (owner, assessment, source) for existing records
  reassess-links.md     # Find and fix mismatched coordinates/Street View links
```

**In Claude Code:** These are available as `/hunt-properties`, `/verify-property`, `/validate-csv`, `/repair-data`, and `/reassess-links`. Just type the slash command with your arguments.

**In any other AI agent (OpenClaw, Codex, Cursor, etc.):** Read the `.claude/commands/*.md` files — they are plain markdown with numbered steps. Follow them exactly. The key capabilities needed are:
- **Web search** to find government property records
- **Browser automation** (Playwright, Puppeteer, Selenium, or similar) to scrape data and visit Google Maps
- **Screenshot analysis** to visually confirm property condition
- **CSV read/write** to update the database
- **US Census Geocoder** (https://geocoding.geo.census.gov/geocoder/) for address-to-coordinate lookup — free, no API key needed

**If a slash command doesn't work:** Read the corresponding `.claude/commands/*.md` file and execute each step manually. The instructions are self-contained — no special tooling is required beyond what's described above.

### Available Commands

#### `/hunt-properties [City, State]` - Find New Properties

Takes a city/state and autonomously:
1. Builds a research plan and checks existing coverage
2. Web searches for condemned/blighted/vacant property lists from government sources
3. Scrapes property data from county assessor sites, GIS portals, code enforcement lists
4. Verifies each property via Google Maps (coordinates + Street View visual confirmation)
5. Checks for duplicates against the existing CSV
6. Adds verified properties with all required fields
7. Validates the entire CSV after adding
8. Commits and opens a PR (~20 properties per PR max)

#### `/verify-property [address|city|all]` - Verify Existing Properties

Visually confirms properties via Google Maps Street View:
1. Navigates to the Google Maps link for a property
2. Takes screenshots, pans 360 degrees to find the building
3. Analyzes visual evidence for signs of abandonment
4. Confirms address and coordinates match
5. Flags discrepancies and reports confidence level

#### `/validate-csv` - Data Quality Check

Comprehensive validation of the entire database: enum validity, coordinate ranges, duplicate detection, data completeness, and auto-fix for correctable issues.

#### `/repair-data [address|city|all]` - Fill Missing Data

Finds incomplete records and looks up missing owner, assessment, and source data from county assessor websites and other official records.

#### `/reassess-links [address|city|all|bad-panos]` - Fix Mismatched Links

Scans properties for broken or mismatched Google Maps links. The most common problem is placeholder pano IDs (`0x0:0x0`) that cause Street View to load the wrong location entirely. The command navigates to each property's link via Playwright, checks if the displayed address matches the CSV, and if not, searches for the correct address and replaces the coordinates and link. Also catches properties that have been demolished since listing.

---

## The Map Viewer

`index.html` is a zero-dependency single-file web app. It loads the CSV client-side and renders everything.

### Features

- **Tabbed interface** - Switch between Map Overview (all properties) and Property View (Street View embed + details)
- **Embedded Street View** - Click any property to see the Google Maps Street View embedded directly in the app
- **Interactive Leaflet map** - Dark/street/satellite tile layers, color-coded markers by status
- **Marker clustering** - Automatically groups markers at low zoom levels so the map never overloads, even with thousands of properties
- **Viewport-based loading** - Only renders markers visible in the current map view (capped at 500) to keep performance smooth at national scale
- **Sidebar property list** - Searchable, filterable list with status badges, type labels, and assessment values
- **Status filters** - Click status badges to filter the map and list by ABANDONED, CONDEMNED, VACANT, etc.
- **Stats bar** - Total properties, cities, states, and aggregate assessed value

### Data quality fallbacks

- If a property has no Street View link, the app shows a satellite/map embed instead
- If coordinates are invalid, the property is excluded from the map but still appears in the list
- The app gracefully handles missing optional fields (owner, assessment)

### No setup required

No API keys. No server. No build step. Just open `index.html` in a browser or host on GitHub Pages.

### Hosting on GitHub Pages

1. Go to repo Settings > Pages
2. Set source to `main` branch, root directory
3. The app will be live at `https://[username].github.io/AbandonedAmerica/`

---

## Why This Matters

Every abandoned property is unrealized potential — a business that could exist, a home someone could live in, economic value evaporating year after year. There are potentially **hundreds of billions of dollars** in assessed property value locked up in abandoned buildings across America, with no national strategy to address it. No one has ever mapped it all.

**Read the full case: [`WHY.md`](WHY.md)**

This project exists to change that. The goal is a complete, continuously updated map of every abandoned and blighted property in the United States — a tool for communities, journalists, researchers, entrepreneurs, and policymakers to see the full scale of the problem and act on it. City by city, block by block, until the entire country is covered.

---

## Contributing (Humans)

1. Fork the repo
2. Add properties to the CSV following the schema above
3. Open a pull request with your additions
4. Include your sources (property records, news articles, etc.)

You can also open issues to report data quality problems, suggest new features for the viewer, or request coverage of specific areas.

---

## License

This project is open source. The data is public information sourced from government property records, tax assessments, and publicly visible conditions.
