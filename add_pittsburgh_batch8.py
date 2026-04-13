import csv

# Pittsburgh batch 8 - 11 condemned commercial/institutional properties
# From background LLC/INC/CORP owner scan of WPRDC condemned database
properties = [
    {
        'address': '1640 Saw Mill Run Blvd, Pittsburgh, PA 15210',
        'lat': 40.396449,
        'lon': -79.998750,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'LADANI & UKANI ENTERPRISE LLC',
        'assessment': '$525,000',
        'link': 'https://www.google.com/maps/search/1640+Saw+Mill+Run+Blvd+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Former convenience store/gas station. Saw Mill Run corridor in Brookline.',
    },
    {
        'address': '1500 Bingham St, Pittsburgh, PA 15203',
        'lat': 40.429329,
        'lon': -79.983260,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15203',
        'type': 'WAREHOUSE',
        'status': 'CONDEMNED',
        'owner': 'SOUTHSIDE REH LLC',
        'assessment': '$326,700',
        'link': 'https://www.google.com/maps/search/1500+Bingham+St+Pittsburgh+PA+15203',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office/warehouse. South Side Flats neighborhood.',
    },
    {
        'address': '1018 Bidwell St, Pittsburgh, PA 15233',
        'lat': 40.452712,
        'lon': -80.020261,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15233',
        'type': 'INSTITUTIONAL',
        'status': 'CONDEMNED',
        'owner': 'RESACA ASSOCIATES LLC',
        'assessment': '$288,647',
        'link': 'https://www.google.com/maps/search/1018+Bidwell+St+Pittsburgh+PA+15233',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned church. Manchester neighborhood.',
    },
    {
        'address': '1919 Mary St, Pittsburgh, PA 15203',
        'lat': 40.426115,
        'lon': -79.978513,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15203',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': '1919 MARY STREET LLC',
        'assessment': '$239,000',
        'link': 'https://www.google.com/maps/search/1919+Mary+St+Pittsburgh+PA+15203',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial garage. South Side Flats neighborhood.',
    },
    {
        'address': '1410 Grotto St, Pittsburgh, PA 15206',
        'lat': 40.467605,
        'lon': -79.895865,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15206',
        'type': 'INSTITUTIONAL',
        'status': 'CONDEMNED',
        'owner': 'BETHEL CHURCH OF GOD IN CHRIST OF PITTSBURGH',
        'assessment': '$152,200',
        'link': 'https://www.google.com/maps/search/1410+Grotto+St+Pittsburgh+PA+15206',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned church. Lincoln-Lemington-Belmar neighborhood.',
    },
    {
        'address': '2539 Perrysville Ave, Pittsburgh, PA 15214',
        'lat': 40.470860,
        'lon': -80.008895,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15214',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'PRF 100 LLC',
        'assessment': '$127,300',
        'link': 'https://www.google.com/maps/search/2539+Perrysville+Ave+Pittsburgh+PA+15214',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Perrysville Ave corridor in Perry South.',
    },
    {
        'address': '3022 Viola St, Pittsburgh, PA 15214',
        'lat': 40.476916,
        'lon': -80.011035,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15214',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'ONEOFF LLC',
        'assessment': '$61,200',
        'link': 'https://www.google.com/maps/search/3022+Viola+St+Pittsburgh+PA+15214',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial building. Perry North neighborhood.',
    },
    {
        'address': '400 Greentree Rd, Pittsburgh, PA 15220',
        'lat': 40.435883,
        'lon': -80.034022,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15220',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'WEST SIDE DEVELOPMENT LLC',
        'assessment': '$58,700',
        'link': 'https://www.google.com/maps/search/400+Greentree+Rd+Pittsburgh+PA+15220',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with store above. West End neighborhood.',
    },
    {
        'address': '1417 Adams St, Pittsburgh, PA 15233',
        'lat': 40.458231,
        'lon': -80.028372,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15233',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': '1417 ADAMS ST LLC',
        'assessment': '$47,500',
        'link': 'https://www.google.com/maps/search/1417+Adams+St+Pittsburgh+PA+15233',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Manchester neighborhood.',
    },
    {
        'address': '650 Herron Ave, Pittsburgh, PA 15219',
        'lat': 40.452566,
        'lon': -79.964325,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'HERRON VILLAGE LLC',
        'assessment': '$43,600',
        'link': 'https://www.google.com/maps/search/650+Herron+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Upper Hill District.',
    },
    {
        'address': '722 Sterrett St, Pittsburgh, PA 15208',
        'lat': 40.455774,
        'lon': -79.894461,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15208',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'R T HOMEWOOD LLC',
        'assessment': '$35,000',
        'link': 'https://www.google.com/maps/search/722+Sterrett+St+Pittsburgh+PA+15208',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office with apartments above. Homewood South neighborhood.',
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
    print(f"  {r['address']} | {r['type']} | {r['status']} | {r['assessment']}")

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
