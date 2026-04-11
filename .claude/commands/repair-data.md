# Repair Data

Find and fill in missing attributes for existing properties in the ABNC database. This command scans the CSV for incomplete records and uses web search + Playwright to look up the missing information.

## Input

The user may provide:
- A specific address to repair
- A specific field to focus on (e.g., "fill in missing owners")
- "all" to scan and repair all incomplete records
- A city name to repair records in that city

## Steps

### 1. Identify incomplete records

Read the CSV and find properties with missing data. Prioritize by importance:

**High priority gaps (affects data quality):**
- Missing `source` - no way to verify the data
- Missing `owner` - key property record info
- Missing `assessment` - key financial data

**Medium priority gaps:**
- Generic Google Maps link (no Street View) - should upgrade to Street View link
- Missing or incomplete address formatting

Report what you found:
```
Found 15 properties with missing data:
  - 12 missing owner
  - 10 missing assessment
  - 7 missing source
  - 5 with no Street View link
```

Ask the user which gaps to prioritize, or repair all.

### 2. Plan your research approach

Before diving in, make a plan:
- Group properties by city/county (so you can batch-search the same assessor site)
- Identify which county assessor websites to use
- Note which properties are near each other (can verify multiple in one Google Maps session)

### 3. For each property needing repair

**To find Owner and Assessment:**
1. Web search for "[county] property tax records" or "[county] assessor"
2. Navigate to the county assessor website using Playwright
3. Search for the property by address
4. Extract the owner name and assessed value
5. Copy the source URL

**To find/upgrade Google Maps link:**
1. Navigate to Google Maps and search for the address
2. Enter Street View if available
3. Look around 360 degrees to find and confirm the property
4. Copy the full URL with Street View parameters

**To add Source:**
1. If you used a county assessor site, that's the source
2. If the property was from a condemned/blighted list, link to that list
3. If from a news article, link to the article

### 4. Update the CSV

Use Python to update specific fields without disturbing other data:

```python
import csv

with open('Abandoned America - Abandoned or Unused Properties.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

# Update specific row
for r in rows:
    if r['address'] == 'TARGET ADDRESS':
        r['owner'] = 'NEW OWNER NAME'
        r['assessment'] = '$XXX,XXX'
        r['source'] = 'https://...'

fieldnames = ['address','lat','lon','city','state','zip','type','status','owner','assessment','link','source']
with open('Abandoned America - Abandoned or Unused Properties.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
    writer.writeheader()
    writer.writerows(rows)
```

### 5. Validate

After repairs, run `/validate-csv` to ensure nothing was broken.

### 6. Commit as a data repair PR

```bash
git checkout -b repair-data-[city]-[state]
git add "Abandoned America - Abandoned or Unused Properties.csv"
git commit -m "Repair: fill missing owner/assessment/source for [N] properties in [City], [State]"
git push origin repair-data-[city]-[state]
gh pr create --title "Data repair: [N] properties in [City], [State]" --body "Filled in missing fields for [N] properties. Sources: [list assessor sites used]"
```

## Important

- Only fill in data you can verify from authoritative sources
- Do not guess or estimate assessment values
- Owner names should match official records (usually uppercase)
- Always include the source URL so others can verify your additions
- If you cannot find data for a field, leave it empty rather than guessing
