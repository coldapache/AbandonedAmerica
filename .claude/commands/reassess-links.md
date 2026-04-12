# Reassess Links

Scan existing properties in the database and identify cases where the Google Maps link, Street View, or coordinates don't match the address. Then fix them using browser automation. This is the #1 data quality issue in the database.

## Input

The user will provide either:
- A specific address to reassess
- A city name to reassess all properties in that city (e.g., "Bridgeport, CT")
- "all" to scan the entire database
- "bad-panos" to find all entries with placeholder pano IDs (`0x0:0x0`)

## Common Problems This Fixes

1. **Placeholder pano IDs** — Links containing `!1s0x0:0x0!2e0` load to whatever Google picks, often the wrong location
2. **Geocoder drift** — Census Geocoder coordinates land on the street or a neighboring parcel, not the building
3. **Address/Street View mismatch** — Street View header shows a different address than the CSV record
4. **Demolished since listed** — Property was abandoned when added but has since been torn down or redeveloped
5. **Coordinate swaps** — Lat/lon transposed or off by a digit

## Steps

### 1. Load the CSV and identify targets

Read `Abandoned America - Abandoned or Unused Properties.csv`. Based on the user's input, select which properties to check.

**Auto-detection of likely bad entries:**
- Any link containing `0x0:0x0` — these are placeholder pano IDs that will never show the right location
- Any link that is just bare coordinates without a real pano ID (pattern: `!1s0x0` or missing `!1s` entirely)
- Properties where the `link` field is empty or doesn't start with `https://www.google.com/maps`

Report how many properties match and which ones before proceeding.

### 2. For each property, verify the link shows the right place

Use Playwright to check each property:

**Step 2a: Navigate to the property's current Google Maps link**
```
mcp__plugin_playwright_playwright__browser_navigate → [property's link field]
```
Wait for load. Take a screenshot.

**Step 2b: Check what address Google Maps says we're looking at**
Use `mcp__plugin_playwright_playwright__browser_snapshot` to read the page. Look for:
- The address shown in the info card/header (e.g., "436 Columbia St" in the top-left)
- Compare it to the CSV address (e.g., "72 Cherry St")
- If they don't match → this link is broken

**Step 2c: Record the mismatch**
```
CSV ADDRESS: 72 Cherry St, Bridgeport, CT 06605
LINK SHOWS: 436 Columbia St, Bridgeport, CT
VERDICT: MISMATCH — link points to wrong location
```

### 3. For each mismatched property, find the correct location

**Step 3a: Search Google Maps for the actual address**
Navigate to:
```
https://www.google.com/maps/search/[FULL ADDRESS FROM CSV]
```
Wait for the result to load. Take a screenshot.

**Step 3b: Check if the address resolves**
- If Google Maps finds the address and shows a pin → proceed to get coordinates and Street View
- If Google Maps says "can't find this address" or shows a general area → the address may be wrong, or the property may have been demolished and the address retired

**Step 3c: Enter Street View at the correct location**
Click into Street View at the resolved address. Look for the building described in the notes field. Take a screenshot.

**Step 3d: Assess current condition**
- Does a building still stand at this address?
- Does it match the description in the notes? (e.g., "massive brick industrial building")
- If the site is now a green lawn, parking lot, or new construction → the property has been demolished/redeveloped

**Step 3e: Get the corrected data**
If the building still exists:
1. Copy the new Google Maps URL from the browser (should contain a real pano ID like `!1sABCDEF...`)
2. Extract the correct lat/lon from the URL or by right-clicking the pin
3. Note what the Street View actually shows

If the building has been demolished/redeveloped:
1. Flag it for status change to DEMOLISHED
2. Note what's there now in the notes

### 4. Fix the CSV

For each property that needs correction, update the CSV:

**If link/coordinates were wrong but building exists:**
- Update `link` with the new Street View URL (must contain a real pano ID)
- Update `lat` and `lon` with corrected coordinates
- Add to `notes`: "Link/coordinates corrected [date]."

**If the property has been demolished/redeveloped:**
- Change `status` to `DEMOLISHED`
- Update `notes` with what's there now (e.g., "Site redeveloped as green space as of Jul 2024 SV. Previously: massive brick factory.")
- Keep the old link/coordinates — they document where it was

**If the address doesn't exist / can't be found:**
- Flag for user review — don't delete, but report it

### 5. Report results

For each property checked, report:

```
ADDRESS: [csv address]
PREVIOUS LINK: [old link]
ISSUE: [what was wrong]
ACTION: [what was fixed, or flagged for review]
NEW LINK: [if updated]
```

Summary:
- X properties checked
- X links corrected (building still standing, link fixed)
- X properties flagged as DEMOLISHED (redeveloped since listed)
- X properties flagged for review (address not found)

### 6. Validate and save

After all corrections:
1. Write the updated CSV
2. Run enum/coordinate/link validation
3. Report the changes for user review before committing

## Tips

- **Placeholder pano IDs are the fastest wins.** Search for `0x0:0x0` in the CSV to find them instantly.
- **Street View date matters.** If Street View shows Jun 2023 imagery but the area was redeveloped in 2024, the old imagery may still show the building. Check the Street View date and compare with the notes.
- **Use satellite view as a tiebreaker.** If Street View is ambiguous, switch to satellite to see if a building footprint exists.
- **Batch by city.** Running this on all Bridgeport properties at once is more efficient than one at a time.
- **Don't delete records.** Even if a property was demolished, keep it as a DEMOLISHED historical record. The only exception is if the address was completely wrong (never existed).
