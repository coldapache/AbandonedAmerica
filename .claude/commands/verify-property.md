# Verify Property

Verify that a property in the ABNC database actually exists at the listed address and shows signs of abandonment/blight/vacancy. Uses Playwright to visit Google Maps, take screenshots, and confirm the property visually.

## Input

The user will provide either:
- A specific address to verify
- A row number from the CSV
- "all" to verify all unverified properties
- A city name to verify all properties in that city

## Steps

### 1. Load the CSV and identify target properties

Read `Abandoned America - Abandoned or Unused Properties.csv` using the Read tool. Parse it to identify which property or properties to verify based on the user's input.

### 2. For each property, navigate to Google Maps

Use Playwright to verify the property. Follow this sequence exactly:

**Step 2a: Navigate to the property's Google Maps link**

Use `mcp__plugin_playwright_playwright__browser_navigate` to go to the property's `link` field from the CSV. If the link is empty or broken, construct one from coordinates:
```
https://www.google.com/maps/place/[ADDRESS]/@[LAT],[LON],17z
```

Wait for the page to load fully.

**Step 2b: Take a screenshot of the map/street view**

Use `mcp__plugin_playwright_playwright__browser_take_screenshot` to capture what's shown. This gives you a visual of the property location.

**Step 2c: Try to enter Street View if not already there**

If the page loaded to a map view (not Street View), look for the Street View pegman or click on the Street View imagery. The goal is to get a ground-level view of the property. Take another screenshot once in Street View.

**Step 2d: Look around 360 degrees**

IMPORTANT: The property may not be directly in front of you when Street View loads. You need to look around:
- Pan the view left, right, and behind you. The building might be across the street or off to the side.
- Click forward/backward along the street to get different angles.
- Some properties are set back from the road or behind other structures.
- Try to identify the specific building by address number, signage, or matching it to the satellite view.
- Take screenshots from multiple angles to build a complete picture.
- If the Street View imagery is old, check if a newer capture is available (look for the date in the bottom of Street View).

**Step 2e: Check for address confirmation**

Look at the page content using `mcp__plugin_playwright_playwright__browser_snapshot` to confirm:
- The address shown by Google Maps matches the CSV address
- The coordinates shown match the CSV lat/lon (within ~0.001 degrees)

### 3. Analyze the visual evidence

Look at the screenshots and assess whether the property shows signs of:

**Indicators of abandonment/blight:**
- Boarded up windows or doors
- Broken or missing windows
- Overgrown vegetation / unkempt landscaping
- Peeling paint / severe deterioration
- Collapsed or damaged roof
- Graffiti
- Debris or trash accumulation
- Empty parking lot with weeds growing through
- "For Sale" signs that appear weathered/old
- Faded or removed business signage
- Chain-link fencing around the property
- No signs of recent activity

**Indicators the property might NOT be abandoned:**
- Well-maintained exterior
- Cars in the parking lot
- Lights on
- Active business signage
- People visible
- Recent construction or renovation

### 4. Record your findings

For each property, report:

```
ADDRESS: [address from CSV]
STATUS IN CSV: [current status]
GOOGLE MAPS CONFIRMS ADDRESS: YES/NO
VISUAL ASSESSMENT: [what you see in the screenshots]
APPEARS ABANDONED/BLIGHTED: YES/NO/UNCLEAR
CONFIDENCE: HIGH/MEDIUM/LOW
NOTES: [any additional observations]
STREET VIEW DATE: [if visible in Google Maps, note the imagery date]
```

### 5. Flag discrepancies

If you find issues, report them clearly:
- **Address mismatch** - Google Maps shows a different location than the CSV address
- **Status mismatch** - Property appears active/occupied but is listed as ABANDONED
- **Demolished but listed as ABANDONED** - Empty lot where a building should be
- **Coordinates wrong** - Map centers on wrong location for the address

If the property status needs updating, ask the user whether to update the CSV.

### 6. Save screenshots (optional)

If the user wants documentation, save screenshots to a `screenshots/` directory with filenames based on the address.

## Important Notes

- Google Maps Street View imagery may be outdated (check the date in the bottom of Street View)
- Some properties may not have Street View coverage
- If Google Maps requires consent/cookie dialogs, click through them
- Take your time - wait for pages to fully load before screenshotting
- If Playwright has issues, fall back to using the claude-in-chrome tools instead
