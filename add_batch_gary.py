import csv
from collections import Counter

new_properties = [
    # GARY, IN - Midtown corridor abandoned commercial buildings

    # 200 E 21st Ave - 2-story brick commercial/industrial, abandoned
    {
        'address': '200 E 21st Ave, Gary, IN 46407',
        'lat': '41.580400', 'lon': '-87.334226',
        'city': 'Gary', 'state': 'IN', 'zip': '46407',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5804,-87.3342,3a,90y,335.6h,94.56t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '2-story brick commercial/industrial building at E 21st Ave near Front St. Boarded and broken windows, heavy graffiti on side wall, overgrown lot. Clearly abandoned. Apr 2024 SV. In Gary\'s Midtown area near the Indiana Main Street-designated corridor (Broadway to Harrison, 21st to 27th Ave).'
    },

    # 109 W 21st Ave - 3-story brick commercial/industrial, abandoned
    {
        'address': '109 W 21st Ave, Gary, IN 46407',
        'lat': '41.580283', 'lon': '-87.338048',
        'city': 'Gary', 'state': 'IN', 'zip': '46407',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5803,-87.3381,3a,75y,216.58h,102.48t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '3-story brick commercial/industrial building on W 21st Ave. All windows boarded or bricked up, no signs of activity. Clearly abandoned. Apr 2024 SV. Larger building than nearby 200 E 21st. In Gary\'s Midtown area.'
    },

    # 2100 Adams St - abandoned 2-story building
    {
        'address': '2100 Adams St, Gary, IN 46407',
        'lat': '41.580294', 'lon': '-87.339108',
        'city': 'Gary', 'state': 'IN', 'zip': '46407',
        'type': 'RESIDENTIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5803,-87.3391,3a,75y,255h,83.26t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Deteriorated 2-story frame building at Adams St and W 21st Ave. Severely weathered wood siding, no signs of occupancy. Adjacent abandoned brick building to the south also vacant. Apr 2024 SV. In Gary\'s heavily blighted Midtown area.'
    },
]

csv_path = 'Abandoned America - Abandoned or Unused Properties.csv'
with open(csv_path, 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    existing = list(reader)
    fieldnames = reader.fieldnames

existing_addrs = {r['address'].strip().lower() for r in existing}
dupes = []
to_add = []
for p in new_properties:
    if p['address'].strip().lower() in existing_addrs:
        dupes.append(p['address'])
    else:
        to_add.append(p)

if dupes:
    print(f'Skipping {len(dupes)} duplicates: {dupes}')

print(f'Existing: {len(existing)}')
existing.extend(to_add)

with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(existing)

print(f'New total: {len(existing)}')
print(f'Added: {len(to_add)} properties')
cities = Counter(p['city'] for p in to_add)
print(f'By city: {dict(cities)}')
