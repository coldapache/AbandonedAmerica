import csv
from collections import Counter

new_properties = [
    # MEMPHIS, TN - Downtown blighted commercial buildings

    # Dermon Building - 10-story historic office tower, vacant since ~2010
    {
        'address': '46 N B.B. King Blvd, Memphis, TN 38103',
        'lat': '35.145801', 'lon': '-90.049666',
        'city': 'Memphis', 'state': 'TN', 'zip': '38103',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': 'DERMON BUILDING OZ LLC', 'assessment': '',
        'link': 'https://www.google.com/maps/@35.1458,-90.0500,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Dermon_Building',
        'notes': 'Dermon Building. 10-story office building with distinctive glazed terra cotta facade (brown, yellow, green, white). Built 1925 by Dave Dermon, listed on National Register of Historic Places. Vacant since approximately 2010. 99,960 sq ft. Purchased Sep 2022 by Dermon Building OZ LLC for $1.5M. Downtown Memphis Commission approved plans Feb 2024 for 150-room Holiday Inn Express hotel conversion ($22.3M project) but construction never started — stalled post-COVID. Sep 2025 SV shows boarded ground-floor storefronts, no construction activity. Adjacent to Hotel Indigo on BB King Blvd.'
    },

    # Jefferson Plaza - 12-story office tower, vacant 10+ years
    {
        'address': '147 Jefferson Ave, Memphis, TN 38103',
        'lat': '35.146680', 'lon': '-90.050352',
        'city': 'Memphis', 'state': 'TN', 'zip': '38103',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': 'TCH KNOXVILLE LLC', 'assessment': '$853,480',
        'link': 'https://www.google.com/maps/@35.1470,-90.0504,3a,75y,180h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://downtownmemphis.com/post/whats-happening-with-some-of-downtown-memphis-most-prominent-blighted-buildings',
        'notes': 'Jefferson Plaza. 12-story mid-century office tower at Jefferson Ave and 2nd St, built 1954. 101,600 sq ft. Vacant 10+ years. Sold Dec 2025 for $3.1M to TCH Knoxville LLC (previously Trident Capital of America LLC for $2.8M). New roof installation underway but no construction or renovation of interior. May 2025 SV shows "Jefferson Plaza" signage, large murals painted on boarded ground-floor storefronts, dark empty upper-floor windows. Listed on Downtown Memphis Commission blighted buildings watchlist.'
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
