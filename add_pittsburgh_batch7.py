import csv

# Pittsburgh batch 7 - 8 more condemned commercial properties from full WPRDC scan
# Remaining finds from systematic assessor cross-reference
properties = [
    {
        'address': '437 Chalfont St, Pittsburgh, PA 15210',
        'lat': 40.416904,
        'lon': -79.998917,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'DUNCAN JASMINE',
        'assessment': '$40,300',
        'link': 'https://www.google.com/maps/search/437+Chalfont+St+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Beltzhoover neighborhood.',
    },
    {
        'address': '11 Carrie St, Pittsburgh, PA 15212',
        'lat': 40.461440,
        'lon': -80.002142,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15212',
        'type': 'RESTAURANT',
        'status': 'CONDEMNED',
        'owner': 'GROSS LAWRENCE J & GLORIA M',
        'assessment': '$36,100',
        'link': 'https://www.google.com/maps/search/11+Carrie+St+Pittsburgh+PA+15212',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Former bar. Fineview neighborhood.',
    },
    {
        'address': '427 N Braddock Ave, Pittsburgh, PA 15208',
        'lat': 40.451134,
        'lon': -79.892418,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15208',
        'type': 'RETAIL',
        'status': 'CONDEMNED',
        'owner': 'CITY OF PITTSBURGH',
        'assessment': '$33,500',
        'link': 'https://www.google.com/maps/search/427+N+Braddock+Ave+Pittsburgh+PA+15208',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Small retail. City-owned. Homewood South neighborhood.',
    },
    {
        'address': '7082 Lemington Ave, Pittsburgh, PA 15206',
        'lat': 40.469138,
        'lon': -79.896717,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15206',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'COOPER EUGENE',
        'assessment': '$32,200',
        'link': 'https://www.google.com/maps/search/7082+Lemington+Ave+Pittsburgh+PA+15206',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with store above. Lincoln-Lemington-Belmar neighborhood.',
    },
    {
        'address': '29 Noblestown Rd, Pittsburgh, PA 15220',
        'lat': 40.439659,
        'lon': -80.034989,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15220',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'BOEN EARL D',
        'assessment': '$23,700',
        'link': 'https://www.google.com/maps/search/29+Noblestown+Rd+Pittsburgh+PA+15220',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with store above. West End neighborhood.',
    },
    {
        'address': '1148 Province St, Pittsburgh, PA 15212',
        'lat': 40.457640,
        'lon': -79.989727,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15212',
        'type': 'WAREHOUSE',
        'status': 'CONDEMNED',
        'owner': 'FLETCHER JEFFREY',
        'assessment': '$17,300',
        'link': 'https://www.google.com/maps/search/1148+Province+St+Pittsburgh+PA+15212',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office/warehouse. Troy Hill neighborhood.',
    },
    {
        'address': '7608 Frankstown Ave, Pittsburgh, PA 15208',
        'lat': 40.455613,
        'lon': -79.889705,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15208',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'HARVIN BRUCE',
        'assessment': '$14,000',
        'link': 'https://www.google.com/maps/search/7608+Frankstown+Ave+Pittsburgh+PA+15208',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial building. Frankstown Ave corridor in Homewood South.',
    },
    {
        'address': '632 Fort Duquesne Blvd, Pittsburgh, PA 15222',
        'lat': 40.443500,
        'lon': -80.002800,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15222',
        'type': 'COMMERCIAL OFFICE',
        'status': 'VACANT',
        'owner': 'MARK CUBAN',
        'assessment': '',
        'link': 'https://www.google.com/maps/search/632+Fort+Duquesne+Blvd+Pittsburgh+PA+15222',
        'source': 'https://www.downtowncdc.org/easter-seals-building-for-sale/',
        'notes': 'Former Easter Seals HQ. 9-story building built 1917. Vacant for years. Owned by Mark Cuban. 139-apartment conversion announced 2022 but status unclear.',
    },
]

csv_path = 'Abandoned America - Abandoned or Unused Properties.csv'
with open(csv_path, 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    existing = list(reader)

existing_addrs = set()
for row in existing:
    for k in row:
        if 'address' in k.lower():
            existing_addrs.add(row[k].upper())
            break

new_rows = []
for p in properties:
    if p['address'].upper() in existing_addrs:
        print(f"DUPLICATE SKIPPED: {p['address']}")
        continue
    new_rows.append(p)

print(f"Existing records: {len(existing)}")
print(f"New properties to add: {len(new_rows)}")
for r in new_rows:
    print(f"  {r['address']} | {r['type']} | {r['status']} | {r['assessment'] or 'N/A'}")

with open(csv_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    for row in new_rows:
        writer.writerow([
            row['address'], f"{row['lat']:.6f}", f"{row['lon']:.6f}", row['city'],
            row['state'], row['zip'], row['type'], row['status'],
            row['owner'], row['assessment'], row['link'],
            row['source'], row['notes']
        ])

print(f"\nDone! Added {len(new_rows)} properties.")
