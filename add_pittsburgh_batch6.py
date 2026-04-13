import csv

# Pittsburgh batch 6 - 12 condemned commercial/institutional properties from full WPRDC scan
# All cross-referenced: WPRDC condemned database + Allegheny County assessor + Census Geocoder
properties = [
    {
        'address': '1250 Liverpool St, Pittsburgh, PA 15233',
        'lat': 40.455557,
        'lon': -80.024931,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15233',
        'type': 'INSTITUTIONAL',
        'status': 'CONDEMNED',
        'owner': 'MANCHESTER EDUCATIONAL FOUNDATION',
        'assessment': '$988,200',
        'link': 'https://www.google.com/maps/search/1250+Liverpool+St+Pittsburgh+PA+15233',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned church. Assessed at $988.2K. Manchester neighborhood.',
    },
    {
        'address': '1208 Grandview Ave, Pittsburgh, PA 15211',
        'lat': 40.437914,
        'lon': -80.018357,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15211',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': '1208 SUMMIT VIEW LLC',
        'assessment': '$709,400',
        'link': 'https://www.google.com/maps/search/1208+Grandview+Ave+Pittsburgh+PA+15211',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Grandview Ave corridor in Mount Washington.',
    },
    {
        'address': '921 Saw Mill Run Blvd, Pittsburgh, PA 15220',
        'lat': 40.428126,
        'lon': -80.023676,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15220',
        'type': 'WAREHOUSE',
        'status': 'CONDEMNED',
        'owner': 'BARK REAL ESTATE LLC',
        'assessment': '$581,100',
        'link': 'https://www.google.com/maps/search/921+Saw+Mill+Run+Blvd+Pittsburgh+PA+15220',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Office/warehouse. Saw Mill Run corridor in Duquesne Heights.',
    },
    {
        'address': '4749 Plummer St, Pittsburgh, PA 15201',
        'lat': 40.475479,
        'lon': -79.958288,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15201',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'COEN REAL ESTATE HOLDINGS 2 LLC',
        'assessment': '$162,100',
        'link': 'https://www.google.com/maps/search/4749+Plummer+St+Pittsburgh+PA+15201',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Central Lawrenceville neighborhood.',
    },
    {
        'address': '2162 Wylie Ave, Pittsburgh, PA 15219',
        'lat': 40.445601,
        'lon': -79.977091,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'WILLIAMS HARRY & CLAUDETTE',
        'assessment': '$120,900',
        'link': 'https://www.google.com/maps/search/2162+Wylie+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Wylie Ave corridor in Middle Hill District.',
    },
    {
        'address': '3016 Ashlyn St, Pittsburgh, PA 15204',
        'lat': 40.455230,
        'lon': -80.055721,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15204',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'PORTER CHRISTY',
        'assessment': '$119,300',
        'link': 'https://www.google.com/maps/search/3016+Ashlyn+St+Pittsburgh+PA+15204',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial building. Sheraden neighborhood.',
    },
    {
        'address': '501 Brushton Ave, Pittsburgh, PA 15221',
        'lat': 40.450069,
        'lon': -79.891369,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15221',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'CITY OF PITTSBURGH',
        'assessment': '$94,700',
        'link': 'https://www.google.com/maps/search/501+Brushton+Ave+Pittsburgh+PA+15221',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Commercial garage. City-owned. Homewood South neighborhood.',
    },
    {
        'address': '2405 Saw Mill Run Blvd, Pittsburgh, PA 15227',
        'lat': 40.384672,
        'lon': -79.994711,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15227',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': '3230 WAINBELL AVENUE LLC',
        'assessment': '$90,000',
        'link': 'https://www.google.com/maps/search/2405+Saw+Mill+Run+Blvd+Pittsburgh+PA+15227',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with offices above. Saw Mill Run corridor in Overbrook.',
    },
    {
        'address': '3300 Webster Ave, Pittsburgh, PA 15219',
        'lat': 40.452841,
        'lon': -79.964557,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15219',
        'type': 'COMMERCIAL OFFICE',
        'status': 'CONDEMNED',
        'owner': 'CITY OF PITTSBURGH',
        'assessment': '$75,800',
        'link': 'https://www.google.com/maps/search/3300+Webster+Ave+Pittsburgh+PA+15219',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. 1-2 story office building. City-owned. Upper Hill District.',
    },
    {
        'address': '1504 Saw Mill Run Blvd, Pittsburgh, PA 15210',
        'lat': 40.398821,
        'lon': -80.000265,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'MAHANEY HOWARD KEEGAN',
        'assessment': '$71,200',
        'link': 'https://www.google.com/maps/search/1504+Saw+Mill+Run+Blvd+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Saw Mill Run corridor in Brookline.',
    },
    {
        'address': '245 Spencer Ave, Pittsburgh, PA 15227',
        'lat': 40.389704,
        'lon': -79.976548,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15227',
        'type': 'MIXED USE',
        'status': 'CONDEMNED',
        'owner': 'BRICKLEY FAMILY LP',
        'assessment': '$67,900',
        'link': 'https://www.google.com/maps/search/245+Spencer+Ave+Pittsburgh+PA+15227',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Retail with apartments above. Carrick neighborhood.',
    },
    {
        'address': '2104 Arlington Ave, Pittsburgh, PA 15210',
        'lat': 40.417572,
        'lon': -79.977141,
        'city': 'Pittsburgh',
        'state': 'PA',
        'zip': '15210',
        'type': 'COMMERCIAL',
        'status': 'CONDEMNED',
        'owner': 'CITY OF PITTSBURGH',
        'assessment': '$52,600',
        'link': 'https://www.google.com/maps/search/2104+Arlington+Ave+Pittsburgh+PA+15210',
        'source': 'https://data.wprdc.org/dataset/condemned-properties',
        'notes': 'Condemned. Former lodge hall. City-owned. Arlington neighborhood.',
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
