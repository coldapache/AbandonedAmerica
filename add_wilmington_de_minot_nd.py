import csv

NEW_PROPERTIES = [
    # === WILMINGTON, DE (0 -> 1 entry — NEW STATE #44: Delaware) ===
    {
        "address": "2505 Pennsylvania Ave, Wilmington, DE 19806",
        "lat": "39.760173", "lon": "-75.574822",
        "city": "Wilmington", "state": "DE", "zip": "19806",
        "type": "RESIDENTIAL", "status": "VACANT",
        "owner": "WILMINGTON NEIGHBORHOOD CONSERVANCY LAND BANK CORP",
        "assessment": "$672,200",
        "link": "https://www.google.com/maps/place/2505+Pennsylvania+Ave,+Wilmington,+DE+19806/@39.760173,-75.574822,17z",
        "source": "https://www3.newcastlede.gov/parcel/Details/Default.aspx?ParcelKey=156805",
        "notes": "Gibraltar mansion. Grand 3-story stone mansion built 1844 by industrialist Joseph Shipley. Named for its commanding hilltop position. 7,000+ sqft on 1.86 acres. National Register of Historic Places 1976. Served as Delaware Governor's mansion 1963-1965. Vacant and deteriorating for years; roof damage, overgrown grounds. Transferred to Wilmington Land Bank. Assessed $672,200 (tax exempt, land bank-owned) per New Castle County 2025. Parcel 2601220004."
    },
    # === MINOT, ND (0 -> 1 entry — NEW STATE #45: North Dakota) ===
    {
        "address": "123 1st St SW, Minot, ND 58701",
        "lat": "48.235157", "lon": "-101.294484",
        "city": "Minot", "state": "ND", "zip": "58701",
        "type": "COMMERCIAL OFFICE", "status": "VACANT",
        "owner": "BIG M MINOT LLC",
        "assessment": "$14,700,000",
        "link": "https://www.google.com/maps/place/123+1st+St+SW,+Minot,+ND+58701/@48.235157,-101.294484,17z",
        "source": "https://minot.northdakotaassessors.com/parcel/cbf4c5aeedfe445ef117a4a6fe4651cf",
        "notes": "Big M Building (former Midwest Federal Savings Bank). 8-story office high-rise with basement and sub-basement, built 1962. Steel frame, structural glass-tinted exterior. 70,890 sqft gross building area, 10,948 sqft lot (0.251 acres). Iconic rooftop 'M' sign. Opened as Minot Federal Bank 1963. Shuttered for years. Purchased Dec 2021 by Big M Minot LLC (tied to EPIC Companies) for $525,000. EPIC went bankrupt 2024; construction stopped, 2024 taxes unpaid. City hired outside attorneys to address the building Feb 2026. Zoning C3/Central Business, Renaissance Zone. Assessed $14,700,000 (land $77K, improvement $14.6M) per Minot City Assessor. Parcel MI24.238.060.0150."
    },
]

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing = list(reader)

existing_addresses = {r["address"].strip().lower() for r in existing}
added = []
skipped = []
for prop in NEW_PROPERTIES:
    if prop["address"].strip().lower() in existing_addresses:
        skipped.append(prop["address"])
    else:
        added.append(prop)
        existing.append(prop)

with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(existing)

print(f"Added {len(added)} properties, skipped {len(skipped)} duplicates")
for a in added:
    print(f"  + {a['address']} ({a['status']}) [{a['city']}, {a['state']}]")
for s in skipped:
    print(f"  SKIP: {s}")
