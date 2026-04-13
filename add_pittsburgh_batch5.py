import csv

# Pittsburgh batch 5 - 11 condemned commercial/mixed-use properties across multiple corridors
# All from WPRDC condemned database + Allegheny County assessor
properties = [
    {
        'address': '1325 5th Ave, Pittsburgh, PA 15219',
        'lat': 40.438864,
        'lon': -79.987369,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'URBAN REDEVELOPMENT AUTHORITY OF PITTSBURGH',
        'assessment': '$281,600',
        'link': 'https://www.google.com/maps/search/1325+5th+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. URA-owned. Crawford-Roberts neighborhood.',
    },
    {
        'address': '3100 Brighton Rd, Pittsburgh, PA 15212',
        'lat': 40.473956,
        'lon': -80.028828,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15212',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'LESKO GEORGE',
        'assessment': '$132,200',
        'link': 'https://www.google.com/maps/search/3100+Brighton+Rd+Pittsburgh+PA+15212',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office with apartments above. Brighton Rd corridor in Marshall-Shadeland.',
    },
    {
        'address': '7315 Frankstown Ave, Pittsburgh, PA 15208',
        'lat': 40.456997,
        'lon': -79.893391,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15208',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'PALMER FLOYD',
        'assessment': '$79,500',
        'link': 'https://www.google.com/maps/search/7315+Frankstown+Ave+Pittsburgh+PA+15208',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Frankstown Ave corridor in Homewood North.',
    },
    {
        'address': '2420 Brownsville Rd, Pittsburgh, PA 15210',
        'lat': 40.386631,
        'lon': -79.982072,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'RETAIL',
        'status': 'CONDEMNED',
        'owner': 'NEPAL SURAJ',
        'assessment': '$61,800',
        'link': 'https://www.google.com/maps/search/2420+Brownsville+Rd+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Small detached retail. Brownsville Rd corridor in Carrick.',
    },
    {
        'address': '620 E Ohio St, Pittsburgh, PA 15212',
        'lat': 40.454151,
        'lon': -79.998402,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15212',
        'type': 'RETAIL',
        'status': 'VACANT',
        'owner': 'HISTORIC DEUTSCHTOWN DEVELOPMENT CORPORATION',
        'assessment': '$60,000',
        'link': 'https://www.google.com/maps/search/620+E+Ohio+St+Pittsburgh+PA+15212',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Vacant since 2008. Small retail. East Ohio St corridor in Deutschtown. $4.9M redevelopment plan announced 2021 but not yet started.',
    },
    {
        'address': '1501 5th Ave, Pittsburgh, PA 15219',
        'lat': 40.438755,
        'lon': -79.984866,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'FIELDS DAVID L',
        'assessment': '$50,000',
        'link': 'https://www.google.com/maps/search/1501+5th+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with store above. Crawford-Roberts neighborhood.',
    },
    {
        'address': '7203 Frankstown Ave, Pittsburgh, PA 15208',
        'lat': 40.457511,
        'lon': -79.895951,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15208',
        'type': 'RETAIL',
        'status': 'CONDEMNED',
        'owner': 'THOMAS WILLIAM & DARLENE L CALDWELL',
        'assessment': '$30,400',
        'link': 'https://www.google.com/maps/search/7203+Frankstown+Ave+Pittsburgh+PA+15208',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Small detached retail. Frankstown Ave corridor in Homewood North.',
    },
    {
        'address': '611 Lincoln Ave, Pittsburgh, PA 15206',
        'lat': 40.461912,
        'lon': -79.907557,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15206',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'LE KEVIN',
        'assessment': '$28,000',
        'link': 'https://www.google.com/maps/search/611+Lincoln+Ave+Pittsburgh+PA+15206',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Larimer neighborhood.',
    },
    {
        'address': '2219 Brownsville Rd, Pittsburgh, PA 15210',
        'lat': 40.390835,
        'lon': -79.985921,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'NEPAL DEWAKAR',
        'assessment': '$21,000',
        'link': 'https://www.google.com/maps/search/2219+Brownsville+Rd+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office with apartments above. Brownsville Rd corridor in Carrick.',
    },
    {
        'address': '8036 Frankstown Ave, Pittsburgh, PA 15221',
        'lat': 40.455289,
        'lon': -79.883400,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15221',
        'type': 'RETAIL',
        'status': 'CONDEMNED',
        'owner': 'TIPTON ERIC & ADORATION BOYD',
        'assessment': '$15,300',
        'link': 'https://www.google.com/maps/search/8036+Frankstown+Ave+Pittsburgh+PA+15221',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Small detached retail. Frankstown Ave corridor in East Hills.',
    },
    {
        'address': '2007 Centre Ave, Pittsburgh, PA 15219',
        'lat': 40.444147,
        'lon': -79.980227,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'NEW GRANADA DEVELOP LLC',
        'assessment': '$14,100',
        'link': 'https://www.google.com/maps/search/2007+Centre+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial auxiliary building. Centre Ave corridor in Middle Hill District.',
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
