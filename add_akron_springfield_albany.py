import csv

NEW_PROPERTIES = [
    # === AKRON, OH (0 -> 1 entry, expanding OH coverage) ===
    {
        "address": "1200 Firestone Parkway, Akron, OH 44301",
        "lat": "41.051865", "lon": "-81.529206",
        "city": "Akron", "state": "OH", "zip": "44301",
        "type": "INDUSTRIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1200+Firestone+Pkwy,+Akron,+OH+44301/@41.051865,-81.529206,17z",
        "source": "https://signalakron.org/city-asks-to-tear-down-most-of-historic-firestone-plant-1/",
        "notes": "Firestone Plant 1 (Firestone Tire & Rubber HQ). Built 1910, iconic clock tower. Vacant 10+ years, city-owned. High asbestos contamination. City seeking partial demolition, preserving facade and clock tower. Ohio Endangered Historic Sites list."
    },
    # === SPRINGFIELD, MA (0 -> 1 entry — state #27: Massachusetts) ===
    {
        "address": "1414 State St, Springfield, MA 01109",
        "lat": "42.120164", "lon": "-72.545878",
        "city": "Springfield", "state": "MA", "zip": "01109",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1414+State+St,+Springfield,+MA+01109/@42.120164,-72.545878,17z",
        "source": "https://springfieldpreservation.org/isolation-hospital-1414-state-street/",
        "notes": "Springfield Isolation Hospital. 5-story Art Deco, built 1930-31 by Kirkham & Parlett for tuberculosis treatment. Largest Art Deco building in Springfield. Unused for decades. Preservation Massachusetts 2022 Most Endangered. City acquired 17-acre campus for $1 from Vibra Healthcare."
    },
    # === ALBANY, NY (0 -> 1 entry, expanding NY coverage) ===
    {
        "address": "143 Montgomery St, Albany, NY 12207",
        "lat": "42.657203", "lon": "-73.744969",
        "city": "Albany", "state": "NY", "zip": "12207",
        "type": "WAREHOUSE", "status": "CONDEMNED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/143+Montgomery+St,+Albany,+NY+12207/@42.657203,-73.744969,17z",
        "source": "https://www.wamc.org/news/2024-02-01/central-warehouses-days-as-albanys-worst-eyesore-are-numbered-after-developer-abandons-plans",
        "notes": "Central Warehouse. Massive cold/dry storage facility built 1927. Albany's 'worst eyesore.' Mayor declared state of emergency Jan 2024 due to structural failure. Developer abandoned renovation plans. $60M Restore NY project initiated for demolition/remediation. Awarded $9.75M Round 1 Restore NY."
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
