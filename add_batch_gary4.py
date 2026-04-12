import csv
from collections import Counter

new_properties = [
    # GARY, IN - Major abandoned landmarks batch 2

    # Palace Theater - 3,000-seat atmospheric theater, abandoned 1972
    {
        'address': '791 Broadway, Gary, IN 46402',
        'lat': '41.596791', 'lon': '-87.337043',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5968,-87.3370,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Palace_Theater_(Gary,_Indiana)',
        'notes': 'Palace Theater. 3,000-seat atmospheric theater designed by John Eberson, built 1925. Renaissance facade with ornate entrance and "PALACE" marquee. Closed 1972. Vacant 50+ years. $85M redevelopment plan announced 2024 by BWI LLC (The Palace Lofts — 251 housing units + retail) but delayed — developer unable to secure tax credits, no construction started as of 2026. National Register of Historic Places. Apr 2024 SV shows boarded storefronts, marquee intact.'
    },

    # Mahencha Apartments - 4-story Renaissance Revival, abandoned 1984
    {
        'address': '1900 W 5th Ave, Gary, IN 46407',
        'lat': '41.602025', 'lon': '-87.360667',
        'city': 'Gary', 'state': 'IN', 'zip': '46407',
        'type': 'RESIDENTIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.6023,-87.3612,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://sometimes-interesting.com/the-mahencha-apartments-of-gary-indiana/',
        'notes': 'Mahencha Apartments. 4-story Renaissance Revival apartment building with Spanish-inspired facade and asymmetrical tower, built 1928. Purchased by former Mayor Richard Hatcher 1978. Operations shut down 1984. $3.5M renovation announced 2001 but funding never materialized. Building in "development purgatory" — demolition considered more likely than restoration. Across from former Horace Mann High School on W 5th Ave (US-20). May 2024 SV from Arthur St shows building still standing, surrounded by vacant lots.'
    },

    # Knights of Columbus Building - 10-story brick, National Register
    {
        'address': '333 W 5th Ave, Gary, IN 46402',
        'lat': '41.601985', 'lon': '-87.341276',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'MIXED USE', 'status': 'PROBABLY VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.6012,-87.3413,3a,90y,350h,105t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Knights_of_Columbus_Building_(Gary,_Indiana)',
        'notes': 'Knights of Columbus Building. 10-story brick building designed by Harry L. Porter and Ralph McNally (Cleveland), built 1925. Served as hotel, clubhouse, restaurant, and sport facility. National Register of Historic Places (1984), part of Gary City Center Historic District. Apr 2024 SV from Jefferson St shows distinctive stepped tower still standing, no visible signage or activity. Adjacent to Gary Public Library. Current occupancy unclear — building appears dark but not obviously boarded.'
    },

    # Horace Mann High School - massive 3-story school, closed 2004
    {
        'address': '524 Garfield St, Gary, IN 46402',
        'lat': '41.600995', 'lon': '-87.359454',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'INSTITUTIONAL', 'status': 'ABANDONED',
        'owner': 'GARY HOUSING AUTHORITY', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.6020,-87.3595,3a,75y,160h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://abandonedatlas.com/horace-mann-high-school/',
        'notes': 'Horace Mann High School. Massive 3-story red brick classical school completed 1928. Housed up to 2,500 students. Featured gymnasium, theater, swimming pool. Closed summer 2004 due to declining enrollment. Sold to Gary Housing Authority 2021 for $5,000. Future uncertain — undergoing inspections. One of Indiana\'s largest abandoned schools. Across W 5th Ave from Mahencha Apartments. May 2024 SV from 5th Ave shows large building still standing behind vegetation.'
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
