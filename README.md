# Abandoned America

A crowdsourced, AI-assisted national database and map viewer for abandoned, blighted, and non-contributing (ABNC) properties across the United States.

**The idea is simple:** AI coding agents (Claude Code, OpenClaw, Codex, etc.) can clone this project, search for abandoned properties in any area, add them to the CSV database, and submit a pull request. Over time, this builds a comprehensive national picture of property abandonment, blight, and vacancy.

---

## Quick Start

```bash
git clone git@github.com:coldapache/AbandonedAmerica.git
cd AbandonedAmerica
```

```bash
# To view the app locally, serve via HTTP:
python -m http.server 8765
# Then open http://localhost:8765 in your browser
```

You can also just open `index.html` directly in your browser for basic viewing, or use any static file server.

Open `index.html` in a browser. That's it. No build step, no backend, no API keys. The app loads the CSV and renders an interactive map.

---

## Project Structure

```
AbandonedAmerica/
  index.html                                          # Map viewer (single-file, zero deps besides CDN)
  Abandoned America - Abandoned or Unused Properties.csv  # The database
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
| `PERMANENTLY CLOSED` | Business permanently closed. Building may still be structurally sound. |
| `PROBABLY VACANT` | Appears vacant based on visual/web evidence, but not confirmed through official records. |
| `VACANT` | Currently unoccupied. Structurally sound. No active business or residents. |

### Rules

- **No duplicate properties.** Before adding a property, search the CSV for the address.
- **All coordinates must be verified.** Use Google Maps to confirm lat/lon matches the address.
- **All properties must have a Google Maps link.** Street View links are strongly preferred.
- **Status must be from the enum.** Do not invent new statuses.
- **Type must be from the enum.** If a property doesn't fit, use the closest match.
- **Assessments from official tax records only.** Do not estimate.
- **Use the minus sign (`-`) for negative longitude.** Not an en-dash or em-dash.
- **Owner names in uppercase** when sourced from official records.
- **Include source URLs whenever possible** so others can verify the data.

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

Pick a city, county, or region to research. Good starting points:
- The area where your user lives
- Cities known for high vacancy rates (Detroit, Baltimore, St. Louis, Cleveland, Gary, Camden, etc.)
- Rural areas with declining populations
- Any area the user requests

### Step 3: Check for Existing Coverage

Before researching, check what's already in the database:

```bash
grep -i "[city name]" "Abandoned America - Abandoned or Unused Properties.csv"
```

This tells you what's already been cataloged so you don't duplicate work.

### Step 4: Research Properties

Use multiple methods to find abandoned/blighted properties:

#### Method A: Government Property Records
- Search for "[city] condemned properties list"
- Search for "[city] blighted properties"
- Search for "[city] code enforcement demolition list"
- Search for "[county] tax delinquent properties"
- Search for "[city] vacant property registry"
- Many cities publish lists of condemned, vacant, or blighted properties

#### Method B: Tax Assessment Records
- Search for "[county] property tax records" or "[county] GIS"
- Look for properties with very low assessments relative to their area
- Look for properties owned by "CITY OF..." or "COUNTY OF..." (often seized properties)
- Cross-reference with Google Maps to verify abandonment

#### Method C: Google Maps Visual Confirmation
- Use Google Maps Street View to visually confirm property condition
- Look for: boarded windows, overgrown lots, collapsed roofs, graffiti, demolition debris
- Check multiple years of Street View imagery when available
- Screenshot the Street View for documentation

#### Method D: News and Community Reports
- Search for "[city] abandoned buildings"
- Search for "[address] condemned" or "[address] demolished"
- Local news often covers blight and demolition

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

```bash
git add "Abandoned America - Abandoned or Unused Properties.csv"
git commit -m "Add [N] ABNC properties in [City], [State]"
git push origin add-properties-[city]-[state]
gh pr create --title "Add [N] properties in [City], [State]" --body "Added [N] abandoned/blighted/vacant properties in [City], [State]. Sources: [list sources]"
```

---

## Claude Code Slash Commands

This repo ships with ready-to-use Claude Code commands in `.claude/commands/`. After cloning, these are available as slash commands:

### `/hunt-properties` - Find New Properties

Takes a city/state and autonomously:
1. Web searches for condemned/blighted/vacant property lists from government sources
2. Scrapes property data from county assessor sites, GIS portals, code enforcement lists
3. Uses **Playwright browser automation** to visit Google Maps for each property
4. Gets coordinates, Street View screenshots, and visual confirmation of abandonment
5. Checks for duplicates against the existing CSV
6. Adds verified properties with all required fields
7. Validates the entire CSV after adding
8. Commits and opens a PR

```
/hunt-properties Detroit, MI
/hunt-properties Baltimore, MD
/hunt-properties Gary, IN
```

### `/verify-property` - Verify Existing Properties

Uses **Playwright browser automation** to visually confirm properties:
1. Navigates to the Google Maps link for a property
2. Takes screenshots of the Street View
3. Analyzes the visual evidence for signs of abandonment (boarded windows, overgrown lots, collapsed roofs, debris, etc.)
4. Confirms the address and coordinates match
5. Flags discrepancies (address mismatch, property appears occupied, demolished, etc.)
6. Reports confidence level for each property

```
/verify-property 1709 N King St, Hampton, VA 23669
/verify-property all
/verify-property Hampton
```

### `/validate-csv` - Data Quality Check

Comprehensive validation of the entire database:
1. Checks all required fields are present
2. Validates all status and type values against the allowed enums
3. Validates coordinates are within US bounds
4. Checks ZIP codes, state abbreviations, Google Maps links
5. Detects duplicate addresses and near-coordinate duplicates
6. Reports data completeness (missing owner, assessment fields)
7. Offers to auto-fix correctable issues

```
/validate-csv
```

### For Other AI Agents (Non-Claude-Code)

If you're using a different AI coding agent, the instructions in `.claude/commands/*.md` are plain markdown files. Read them and follow the steps manually. The key capabilities needed are:
- **Web search** to find government property records
- **Browser automation** (Playwright, Puppeteer, Selenium) to scrape data and visit Google Maps
- **Screenshot analysis** to visually confirm property condition
- **CSV read/write** to update the database

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

Millions of properties across America sit abandoned, condemned, or chronically vacant. They:
- Reduce neighboring property values
- Attract crime and illegal dumping
- Create fire and safety hazards
- Waste land that could house people or businesses
- Cost cities millions in demolition and maintenance

This project aims to make the scale of the problem visible. By mapping every abandoned property we can find, we create a tool for communities, journalists, researchers, and policymakers to understand and address urban decay.

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
