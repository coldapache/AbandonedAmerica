import csv

NEW_PROPERTIES = [
    # === ALBUQUERQUE, NM (0 -> 1 entry — NEW STATE #32: New Mexico) ===
    {
        "address": "414 Central Ave SW, Albuquerque, NM 87102",
        "lat": "35.083360", "lon": "-106.642752",
        "city": "Albuquerque", "state": "NM", "zip": "87102",
        "type": "RETAIL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/414+Central+Ave+SW,+Albuquerque,+NM+87102/@35.083360,-106.642752,17z",
        "source": "https://citydesk.org/2024/02/25/long-vacant-buildings-irk-officials-business-owners/",
        "notes": "S. H. Kress Building. Art Deco department store built 1925 by S. H. Kress & Co. National Register 1984. Vacant since 1981 when parent company closed. Inherited by Anna Muller's sister after Muller died late 2020. One of downtown Albuquerque's most prominent long-vacant buildings. On Historic Route 66."
    },
    # === PHOENIX, AZ (0 -> 1 entry — NEW STATE #33: Arizona) ===
    {
        "address": "800 E Mineral Rd, Phoenix, AZ 85042",
        "lat": "33.356251", "lon": "-112.062859",
        "city": "Phoenix", "state": "AZ", "zip": "85042",
        "type": "RESIDENTIAL", "status": "VACANT",
        "owner": "ROJO ADOBE HACIENDA LLC",
        "assessment": "$1,980,860",
        "link": "https://www.google.com/maps/place/800+E+Mineral+Rd,+Phoenix,+AZ+85042/@33.356251,-112.062859,17z",
        "source": "https://savingplaces.org/places/mystery-castle",
        "notes": "Mystery Castle. 18-room handmade folk art residence built 1934-1945 by Boyce Luther Gulley for daughter Mary Lou. 8,000 sqft on 7.01 acres in South Mountain foothills. National Trust 2025 Most Endangered. Closed since 2023 after break-ins. $3.3M repairs needed. Sold 03/2026 to Rojo Adobe Hacienda LLC for $280K. FCV $1,980,860 (Tax Year 2027) per Maricopa County Assessor APN 300-71-002."
    },
    # === DES MOINES, IA (0 -> 1 entry — NEW STATE #34: Iowa) ===
    {
        "address": "5722 Hickman Rd, Des Moines, IA 50310",
        "lat": "41.614819", "lon": "-93.696460",
        "city": "Des Moines", "state": "IA", "zip": "50310",
        "type": "RESTAURANT", "status": "ABANDONED",
        "owner": "GEORGE KARAIDOS JR / KAREN K KARAIDOS",
        "assessment": "$119,000",
        "link": "https://www.google.com/maps/place/5722+Hickman+Rd,+Des+Moines,+IA+50310/@41.614819,-93.696460,17z",
        "source": "https://www.assess.co.polk.ia.us/cgi-bin/web/tt/infoqry.cgi?tt=card/card&dp=10007318002002",
        "notes": "George the Chili King Drive-In. Iconic Des Moines restaurant since 1952, featured on Diners Drive-Ins and Dives. Closed Oct 2019 when owner George Jr. passed away. Des Moines Heritage Trust endangered list. Iconic neon sign removed 2024. Brick/masonry, 970 sqft, 0.254 acre lot. Assessed $119,000 (land $107K, bldg $12K) per Polk County 2025."
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
