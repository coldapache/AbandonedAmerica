import csv
from collections import Counter

new_properties = [
    # GARY, IN - Major abandoned landmarks

    # City Methodist Church - 9-story Gothic ruin, Gary's most iconic abandoned building
    {
        'address': '577 Washington St, Gary, IN 46402',
        'lat': '41.600392', 'lon': '-87.338341',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'INSTITUTIONAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5998,-87.3384,3a,75y,200h,110t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.preserveindiana.com/pixpages/nw_ind/garypix.html',
        'notes': 'City Methodist Church. 9-story English Gothic church completed 1926, cost over $1M. Congregation peaked at 3,000. Closed 1975 due to declining attendance. Badly damaged by fire 1997. National Register of Historic Places. Also included Seaman Hall (community center), 1,000-seat theater, offices, dining hall, gymnasium. Google Maps interior photosphere shows spectacular ruin — collapsed roof, exposed Gothic arches, debris-filled nave. Gary\'s most iconic abandoned building. Proposed "ruin garden park" concept discussed but no construction. Apr 2024 SV.'
    },

    # US Post Office - Art Moderne federal building, abandoned since 1970s
    {
        'address': '601 Massachusetts St, Gary, IN 46402',
        'lat': '41.599850', 'lon': '-87.335470',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'INSTITUTIONAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.59985,-87.33547,3a,75y,180h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://livingnewdeal.org/sites/old-post-office-gary-in/',
        'notes': 'United States Post Office. Massive Art Moderne style building at E 6th Ave and Massachusetts St. Built 1936 with federal Treasury Department funds as a New Deal project. Designed by architect Howard Lovewell Cheney. Closed 1970s. Added to National Register of Historic Places 1994 as part of Gary City Center Historic District. Apr 2024 SV shows large concrete/stone building with broken windows throughout, heavy graffiti, no signs of activity. One of the most significant abandoned federal buildings in the Midwest.'
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
