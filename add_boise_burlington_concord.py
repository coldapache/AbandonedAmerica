import csv

NEW_PROPERTIES = [
    # === BOISE, ID (0 -> 1 entry — NEW STATE #35: Idaho) ===
    {
        "address": "3311 W State St, Boise, ID 83703",
        "lat": "43.636589", "lon": "-116.230358",
        "city": "Boise", "state": "ID", "zip": "83703",
        "type": "INSTITUTIONAL", "status": "VACANT",
        "owner": "STATE OF IDAHO (ITD GENERAL SERVICES)",
        "assessment": "",
        "link": "https://www.google.com/maps/place/3311+W+State+St,+Boise,+ID+83703/@43.636589,-116.230358,17z",
        "source": "https://idahocapitalsun.com/2024/12/19/renovations-to-itds-boise-hq-will-cost-at-least-64m-not-32m-new-report-shows/",
        "notes": "Idaho Transportation Department former headquarters. Built 1961, 45-acre state-owned campus. Flooded Jan 2, 2022; contaminated with asbestos and mold. All employees displaced. Vacant since 2022. $64-69M renovation estimate; Legislature funded $42.1M so far. Assessed $0 (state-owned, tax exempt) per Ada County Assessor parcel R3786000159."
    },
    # === BURLINGTON, VT (0 -> 1 entry — NEW STATE #36: Vermont) ===
    {
        "address": "68 Pearl St, Burlington, VT 05401",
        "lat": "44.480373", "lon": "-73.216709",
        "city": "Burlington", "state": "VT", "zip": "05401",
        "type": "RESTAURANT", "status": "VACANT",
        "owner": "68 PEARL STREET LLC",
        "assessment": "$361,300",
        "link": "https://www.google.com/maps/place/68+Pearl+St,+Burlington,+VT+05401/@44.480373,-73.216709,17z",
        "source": "https://property.burlingtonvt.gov/Details/?rsn=12489",
        "notes": "Former Bove's restaurant. Iconic Burlington Italian restaurant since 1941, closed Dec 2015 after 75 years. Officially registered as Vacant Building since 2019 per city permits. Boarded up, graffiti-covered. Condition: Fair, 69.95% depreciation. 5,838 sqft retail w/ apartments, 4,416 sqft lot. Owner (Bove family via LLC) proposed hotel/housing redevelopment but no progress. Assessed $361,300 (bldg $153K, land $208K) per Burlington Assessor 2025."
    },
    # === CONCORD, NH (0 -> 1 entry — NEW STATE #37: New Hampshire) ===
    {
        "address": "270 Loudon Rd, Concord, NH 03301",
        "lat": "43.222858", "lon": "-71.492344",
        "city": "Concord", "state": "NH", "zip": "03301",
        "type": "RETAIL", "status": "VACANT",
        "owner": "ONYX STEEPLEGATE CONCORD LLC",
        "assessment": "$12,599,900",
        "link": "https://www.google.com/maps/place/270+Loudon+Rd,+Concord,+NH+03301/@43.222858,-71.492344,17z",
        "source": "https://gis.vgsi.com/concordnh/Parcel.aspx?pid=9470",
        "notes": "Steeplegate Mall. Enclosed shopping mall built 1990, 8 buildings. Sold Oct 2023 to Onyx Partners (Needham MA) for $18.18M. All tenants evicted Jan 2024 for planned demolition/redevelopment (625 apartments + Costco). Demolition stalled by JCPenney lease lawsuit. Mall shuttered and vacant. Was Concord's largest taxpayer at $72M assessed (2010). Now $12.6M. Assessed $12,599,900 (bldg $3.5M, land $9M) per Concord Assessor 2025."
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
