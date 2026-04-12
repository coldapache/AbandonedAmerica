import csv

NEW_PROPERTIES = [
    # === PINE BLUFF, AR (expanding AR from 1 entry) ===
    {
        "address": "207 W 2nd Ave, Pine Bluff, AR 71601",
        "lat": "34.228420", "lon": "-92.004510",
        "city": "Pine Bluff", "state": "AR", "zip": "71601",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/207+W+2nd+Ave,+Pine+Bluff,+AR+71601/@34.228420,-92.004510,17z",
        "source": "https://en.wikipedia.org/wiki/Saenger_Theatre_(Pine_Bluff,_Arkansas)",
        "notes": "Saenger Theatre. Designed by Emile Weil, opened Nov 17 1924. 'Showplace of the South.' Closed 1975. Water damage and vandalism. National Register 1995. City council approved roof/plumbing renovation 2023. SE corner W 2nd Ave & Pine St."
    },
    {
        "address": "440 S Main St, Pine Bluff, AR 71601",
        "lat": "34.225470", "lon": "-92.003510",
        "city": "Pine Bluff", "state": "AR", "zip": "71601",
        "type": "HOSPITALITY", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/440+S+Main+St,+Pine+Bluff,+AR+71601/@34.225470,-92.003510,17z",
        "source": "https://en.wikipedia.org/wiki/Hotel_Pines",
        "notes": "Hotel Pines. Designed by George R. Mann (architect of Arkansas State Capitol). Center of Pine Bluff social life for 50+ years. Closed 1970 when passenger rail ended. National Register 1979. NW corner Main & W 5th Ave."
    },
    {
        "address": "623 W 2nd Ave, Pine Bluff, AR 71601",
        "lat": "34.228473", "lon": "-92.008821",
        "city": "Pine Bluff", "state": "AR", "zip": "71601",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/623+W+2nd+Ave,+Pine+Bluff,+AR+71601/@34.228473,-92.008821,17z",
        "source": "https://en.wikipedia.org/wiki/National_Guard_Armory-Pine_Bluff",
        "notes": "National Guard Armory. Built 1931-32. Listed on National Register of Historic Places. Former military facility in downtown Pine Bluff. Part of Downtown Pine Bluff Historic Commercial District."
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
