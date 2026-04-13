import csv

NEW_PROPERTIES = [
    # === PORTLAND, ME (0 -> 1 entry — NEW STATE #42: Maine) ===
    {
        "address": "477 Congress St, Portland, ME 04101",
        "lat": "43.657018", "lon": "-70.259804",
        "city": "Portland", "state": "ME", "zip": "04101",
        "type": "COMMERCIAL OFFICE", "status": "VACANT",
        "owner": "TT MAINE VENTURE LLC",
        "assessment": "$5,148,100",
        "link": "https://www.google.com/maps/place/477+Congress+St,+Portland,+ME+04101/@43.657018,-70.259804,17z",
        "source": "https://assessors.portlandmaine.gov/Datalets/Datalet.aspx?sIndex=0&idx=1",
        "notes": "Time & Temperature Building (Chapman Building). 12-story office building completed 1924 by architect John Calvin Stevens. Iconic rooftop time/temperature sign. Multi-use commercial (Land Use Code 27). 13,837 SF lot, 0.3177 acres. Owned by TT Maine Venture LLC (Dallas TX) since Dec 2018. Mostly vacant; several redevelopment plans have stalled over the years. Assessed $5,148,100 (land $1,434,700, bldg $3,713,400) per Portland ME Assessor 2026. Parcel 037 F022001."
    },
    # === BUTTE, MT (0 -> 1 entry — NEW STATE #43: Montana) ===
    {
        "address": "40 E Broadway St, Butte, MT 59701",
        "lat": "46.013736", "lon": "-112.534828",
        "city": "Butte", "state": "MT", "zip": "59701",
        "type": "COMMERCIAL OFFICE", "status": "VACANT",
        "owner": "BIG SKY OPPORTUNITY FUND LLC",
        "assessment": "$892,200",
        "link": "https://www.google.com/maps/place/40+E+Broadway+St,+Butte,+MT+59701/@46.013736,-112.534828,17z",
        "source": "https://itax.tylertech.com/ButteSilverBowMT/detail.aspx?taxid=0002784840",
        "notes": "Former NorthWestern Energy headquarters. Five conjoined office buildings, low-rise (1-4 stories). 14,615 sqft lot, 0.34 acres. NorthWestern relocated to new $25M office building in Butte. Purchased Jun 2022 by Big Sky Opportunity Fund LLC via instrument #724855. Developer abandoned efforts to find tenants. Market value $892,200 (taxable $14,900) per Butte-Silver Bow County 2025. Geo Code 01-1197-13-1-15-23-0000."
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
