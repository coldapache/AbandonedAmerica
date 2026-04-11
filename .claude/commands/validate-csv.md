# Validate CSV

Run a comprehensive validation of the entire ABNC property database CSV. Checks for schema violations, duplicates, data quality issues, and optionally verifies Google Maps links.

## Steps

### 1. Load and parse the CSV

Read `Abandoned America - Abandoned or Unused Properties.csv` and parse it with Python's csv module. Report total row count.

### 2. Schema validation

For every row, check:

- **Required fields present**: address, lat, lon, city, state, zip, type, status, link
- **Status is valid enum**: ABANDONED, CHRONICALLY VACANT, CONDEMNED, DEMOLISHED, PROBABLY VACANT, VACANT
- **Type is valid enum**: COMMERCIAL, COMMERCIAL OFFICE, HOSPITALITY, INDUSTRIAL, INSTITUTIONAL, MIXED USE, RESIDENTIAL, RESTAURANT, RETAIL, WAREHOUSE
- **Latitude is valid**: parseable as float, range 24.0 to 49.5
- **Longitude is valid**: parseable as float, range -125.0 to -66.5, uses minus sign not en-dash
- **ZIP is 5 digits**: matches regex `^\d{5}$`
- **State is 2-letter code**: matches regex `^[A-Z]{2}$`
- **Link starts with** `https://www.google.com/maps`
- **Assessment format**: if present, matches `$` followed by digits and commas

### 3. Duplicate detection

Check for:
- **Exact address duplicates**: same address string appears twice
- **Near-coordinate duplicates**: two properties within 0.0003 degrees (~30 meters)
- **Similar addresses**: fuzzy match (e.g., "123 Main St" vs "123 Main Street")

### 4. Data quality checks

- **Missing owner AND assessment**: flag properties with neither (lower priority data)
- **Coordinates vs. city mismatch**: verify lat/lon is plausibly in the listed city/state
- **Empty link fields**: any missing Google Maps links

### 5. Report

Output a report like:

```
=== ABNC Database Validation Report ===

Total properties: 71
Valid rows: 68
Issues found: 3

ERRORS (must fix):
  Row 15: Invalid status "Abandned" (typo)
  Row 42: Longitude uses en-dash instead of minus sign

WARNINGS (should fix):
  Row 8 and Row 9: Possible duplicates (same address, 3m apart)
  Rows 60-65: Missing owner and assessment data

STATS:
  By status: ABANDONED=32, CONDEMNED=20, VACANT=7, ...
  By state: VA=71
  By city: Hampton=59, Norfolk=8, Newport News=4
  Properties with owner: 45/71
  Properties with assessment: 42/71
```

### 6. Auto-fix (with user permission)

If fixable issues are found (typos in enums, whitespace, en-dashes), ask the user if you should auto-fix them. Apply fixes using Python csv module to maintain formatting.
