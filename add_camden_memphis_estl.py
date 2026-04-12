import csv

NEW_PROPERTIES = [
    # === CAMDEN, NJ (0 -> 1 entry — state #26: New Jersey) ===
    {
        "address": "616 S Broadway, Camden, NJ 08103",
        "lat": "39.937741", "lon": "-75.119258",
        "city": "Camden", "state": "NJ", "zip": "08103",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/616+S+Broadway,+Camden,+NJ+08103/@39.937741,-75.119258,17z",
        "source": "https://en.wikipedia.org/wiki/Camden_Free_Public_Library_Main_Building",
        "notes": "Camden Carnegie Library (Camden Free Public Library). Neo-Classical Revival, built 1905, funded by Andrew Carnegie. Abandoned 1986, roof collapsed, trees growing inside. National Register of Historic Places 1992. NJ Most Endangered. Conversion plans announced 2018 but stalled."
    },
    # === MEMPHIS, TN (4 -> 6 entries) ===
    {
        "address": "8 N Third St, Memphis, TN 38103",
        "lat": "35.145578", "lon": "-90.049814",
        "city": "Memphis", "state": "TN", "zip": "38103",
        "type": "COMMERCIAL OFFICE", "status": "VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/8+N+Third+St,+Memphis,+TN+38103/@35.145578,-90.049814,17z",
        "source": "https://en.wikipedia.org/wiki/Sterick_Building",
        "notes": "Sterick Building. Gothic Revival 31-story skyscraper, 365 ft, built 1929. Tallest in American South until 1957. Vacant since 1986. NE corner Third and Madison. Purchased 2023 by Constellation Properties, $300K TN Historic grant Apr 2024. Renovation planned but not yet started."
    },
    {
        "address": "46 N Third St, Memphis, TN 38103",
        "lat": "35.145706", "lon": "-90.049765",
        "city": "Memphis", "state": "TN", "zip": "38103",
        "type": "COMMERCIAL OFFICE", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/46+N+Third+St,+Memphis,+TN+38103/@35.145706,-90.049765,17z",
        "source": "https://en.wikipedia.org/wiki/Dermon_Building",
        "notes": "Dermon Building. 10-story Renaissance-detailed building, built 1925 for $800K. Colorful glazed terra cotta facade. National Register of Historic Places. Largely/completely vacant since 2010."
    },
    # === EAST ST. LOUIS, IL (0 -> 2 entries, expanding IL coverage) ===
    {
        "address": "417 Missouri Ave, East St Louis, IL 62201",
        "lat": "38.626398", "lon": "-90.159032",
        "city": "East St Louis", "state": "IL", "zip": "62201",
        "type": "COMMERCIAL OFFICE", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/417+Missouri+Ave,+East+St+Louis,+IL+62201/@38.626398,-90.159032,17z",
        "source": "https://en.wikipedia.org/wiki/Spivey_Building",
        "notes": "Spivey Building. Only skyscraper ever built in East St. Louis. 12 stories, built 1927 by newspaper owner Allen Spivey. Landmarks Illinois 2025 Most Endangered Historic Places. Downtown East St. Louis Historic District."
    },
    {
        "address": "240 Collinsville Ave, East St Louis, IL 62201",
        "lat": "38.627230", "lon": "-90.158817",
        "city": "East St Louis", "state": "IL", "zip": "62201",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/240+Collinsville+Ave,+East+St+Louis,+IL+62201/@38.627230,-90.158817,17z",
        "source": "https://en.wikipedia.org/wiki/Majestic_Theatre_(East_St._Louis)",
        "notes": "Majestic Theatre. Spanish Gothic theater designed by Boller Brothers, built 1928. Replaced 1907 theater that burned. Closed 1960s. Downtown East St. Louis Historic District."
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
