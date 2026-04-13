import csv

NEW_PROPERTIES = [
    # === TUMWATER, WA (0 -> 1 entry — NEW STATE #46: Washington) ===
    {
        "address": "100 Custer Way SW, Tumwater, WA 98501",
        "lat": "47.021111", "lon": "-122.902778",
        "city": "Tumwater", "state": "WA", "zip": "98501",
        "type": "INDUSTRIAL", "status": "ABANDONED",
        "owner": "TUMWATER DEVELOPMENT LLC",
        "assessment": "$3,125,100",
        "link": "https://www.google.com/maps/place/100+Custer+Way+SW,+Tumwater,+WA+98501/@47.021111,-122.902778,17z",
        "source": "https://tcproperty.co.thurston.wa.us/ascendweb/ParcelInfoPayTaxes.aspx?parcel_number=45700600000",
        "notes": "Old Brewhouse Tower, Olympia Brewery complex. Original four-story brewhouse built 1896, part of the Olympia Beer production campus. Brewery closed 2003 after SABMiller acquisition. 7.20 acre parcel with brewery structures. Fire damaged administration building Oct 2018 (partial collapse). PCB oil spill from vandalized transformer Feb 2019. Washington Trust for Historic Preservation Most Endangered list. New Market Historic District, National Register of Historic Places. Owned by Tumwater Development LLC (Brea CA) who purchased parcels in 2015. No redevelopment progress. Assessed $3,125,100 (land $2,130K, improvement $995K) per Thurston County 2026. Parcel 45700600000."
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
