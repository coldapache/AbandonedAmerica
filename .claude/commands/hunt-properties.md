# Hunt Properties

Search for abandoned, blighted, condemned, and vacant properties in a target area. Uses web search to find property lists, Playwright to scrape government records and visually confirm via Google Maps, then adds verified properties to the CSV database.

## Input

The user will provide:
- A city and state (e.g., "Detroit, MI")
- OR a county and state (e.g., "Wayne County, MI")
- OR "nearby" to use the area already represented in the CSV

## Steps

### 0. Build a research plan

Before doing anything, construct a plan and present it to the user:

1. **Target area**: What city/county/region are we researching?
2. **Existing coverage**: How many properties are already in the database for this area?
3. **Known sources**: What government websites, assessor portals, or public records are available for this area?
4. **Approach**: Will you start with official condemned/blighted lists, or tax records, or drive Google Maps Street View?
5. **Estimated scope**: How many properties do you expect to find?

The user may also give you hints:
- "There's a bunch of abandoned stuff on Main Street" - go look at that area first
- "The city has a blight tracker" - search for that specific tool
- "Check the county assessor" - start with tax records
- Specific addresses they know about - verify those first, then expand outward

Present the plan and get confirmation before proceeding. The user knows their area and may have valuable local knowledge.

### 1. Check existing coverage

First, read `Abandoned America - Abandoned or Unused Properties.csv` and check how many properties already exist for the target area. Report this to the user so they know the starting point.

```
grep -i "[city]" "Abandoned America - Abandoned or Unused Properties.csv" | wc -l
```

### 2. Web search for property lists

Use WebSearch to find official sources of abandoned/blighted/condemned property data. Search for ALL of these queries (adjust city/county name):

```
"[city] [state] condemned properties list"
"[city] [state] blighted properties"
"[city] [state] vacant property registry"
"[city] [state] code enforcement demolition"
"[county] [state] tax delinquent properties"
"[city] [state] abandoned buildings list"
"[city] [state] nuisance properties"
"[city] [state] unsafe structures list"
site:gov [city] condemned vacant properties"
```

Collect URLs from the search results. Prioritize:
1. Official city/county government sites (.gov domains)
2. County GIS/property assessment portals
3. Local news articles about blight/abandonment
4. Community blight tracking sites

### 3. Scrape property data from sources

For each promising URL, use Playwright to visit the page and extract property data:

**Step 3a: Navigate to the source**
Use `mcp__plugin_playwright_playwright__browser_navigate` to visit the URL.

**Step 3b: Get the page content**
Use `mcp__plugin_playwright_playwright__browser_snapshot` to read the page structure.
If the page has tables of properties, extract: addresses, statuses, owners, assessed values.

**Step 3c: Handle pagination**
If the list spans multiple pages, navigate through them systematically. Don't miss data.

**Step 3d: Handle interactive maps/GIS portals**
Some counties have GIS portals. If you find one:
- Look for filter options to show condemned/vacant properties
- Extract addresses from the map markers or search results
- Get assessment and owner data from property detail pages

### 4. For each potential property, verify via Google Maps

**Step 4a: Search Google Maps for the address**
Navigate to:
```
https://www.google.com/maps/search/[ADDRESS]
```

**Step 4b: Get coordinates**
From the Google Maps URL or page content, extract the latitude and longitude.

**Step 4c: Enter Street View**
Try to get a Street View of the property. Take a screenshot.

**Step 4d: Visual assessment**
Look at the screenshot and assess whether the property shows signs of abandonment:
- Boarded windows, broken glass
- Overgrown lot, debris
- Deteriorating structure
- Empty/abandoned appearance
- No signs of business activity

**Step 4e: Get the Google Maps link**
Copy the full Google Maps URL (with Street View if available) for the `link` field.

### 5. Check for duplicates

Before adding any property, check if it already exists in the CSV:
- Exact address match
- Similar addresses at the same coordinates (e.g., "123 Main St" vs "123 Main Street")
- Same coordinates within 0.0005 degrees

Skip any duplicates.

### 6. Build CSV rows

For each verified, non-duplicate property, build a CSV row following the schema EXACTLY:

```
address,lat,lon,city,state,zip,type,status,owner,assessment,link
```

**Column rules (MUST FOLLOW):**
- `address`: Full address with city, state, ZIP. Quote if contains commas.
- `lat`: Decimal latitude, 6+ decimal places. Range: 24.0-49.5.
- `lon`: Decimal longitude, negative, using minus sign `-`. Range: -125.0 to -66.5.
- `city`: Proper case city name.
- `state`: 2-letter uppercase state abbreviation.
- `zip`: 5-digit ZIP code, valid for state.
- `type`: MUST be one of: COMMERCIAL, COMMERCIAL OFFICE, HOSPITALITY, INDUSTRIAL, INSTITUTIONAL, MIXED USE, RESIDENTIAL, RESTAURANT, RETAIL, WAREHOUSE
- `status`: MUST be one of: ABANDONED, CHRONICALLY VACANT, CONDEMNED, DEMOLISHED, PERMANENTLY CLOSED, PROBABLY VACANT, VACANT
- `owner`: Uppercase. From official records only. Leave empty if unknown.
- `assessment`: Format $X,XXX,XXX. From tax records only. Leave empty if unknown.
- `link`: Google Maps URL starting with https://www.google.com/maps

### 7. Append to CSV

Add the new rows to the end of `Abandoned America - Abandoned or Unused Properties.csv`.

Use Python to ensure proper CSV formatting:
```python
import csv
# read existing, append new rows, write back
```

### 8. Validate

After adding, run validation:
```python
import csv
VALID_STATUS = {'ABANDONED','CHRONICALLY VACANT','CONDEMNED','DEMOLISHED','PERMANENTLY CLOSED','PROBABLY VACANT','VACANT'}
VALID_TYPE = {'COMMERCIAL','COMMERCIAL OFFICE','HOSPITALITY','INDUSTRIAL','INSTITUTIONAL','MIXED USE','RESIDENTIAL','RESTAURANT','RETAIL','WAREHOUSE'}

with open('Abandoned America - Abandoned or Unused Properties.csv') as f:
    for i, r in enumerate(csv.DictReader(f), 2):
        assert r['status'] in VALID_STATUS, f"Row {i}: bad status {r['status']}"
        assert r['type'] in VALID_TYPE, f"Row {i}: bad type {r['type']}"
        assert 24.0 <= float(r['lat']) <= 49.5, f"Row {i}: bad lat"
        assert -125.0 <= float(r['lon']) <= -66.5, f"Row {i}: bad lon"
        assert r['link'].startswith('https://www.google.com/maps'), f"Row {i}: bad link"
```

### 9. Report results

Tell the user:
- How many new properties were found and added
- Which sources yielded results
- Any properties that couldn't be verified
- Summary by status (e.g., "12 ABANDONED, 5 CONDEMNED, 3 VACANT")

### 10. Commit and PR (if user approves)

**IMPORTANT: Keep PRs to ~20 properties max.** This ensures reviewers can scan every entry for data quality. If you found more than 20 properties, split them into multiple PRs (e.g., `add-properties-detroit-mi-1`, `add-properties-detroit-mi-2`).

```bash
git checkout -b add-properties-[city]-[state]
git add "Abandoned America - Abandoned or Unused Properties.csv"
git commit -m "Add [N] ABNC properties in [City], [State]"
git push origin add-properties-[city]-[state]
gh pr create --title "Add [N] properties in [City], [State]" --body "..."
```

## Tips for finding good data

- **County assessor websites** are goldmines. They often have searchable databases.
- **Cities with blight ordinances** usually publish lists of condemned/nuisance properties.
- **Tax lien/delinquent lists** often correlate with abandoned properties.
- **Google Maps satellite view** can reveal large abandoned commercial properties (empty parking lots, deteriorating roofs).
- **Local news** often covers "worst abandoned buildings" or demolition plans.
- **Zillow/Redfin** sometimes show long-listed properties that are likely vacant.
- Start with downtown/central areas - abandonment tends to cluster there.

## Important constraints

- Only add properties you can verify actually exist and appear abandoned/blighted/vacant
- Do not add properties that appear occupied, maintained, or active
- Do not fabricate or estimate assessment values
- Do not guess at owner names
- When in doubt about a property's status, use PROBABLY VACANT
- Respect rate limits when scraping websites
- If a government site blocks automated access, note it and move on
