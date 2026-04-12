import csv
from collections import Counter

new_properties = [
    # GARY, IN - Broadway corridor abandoned commercial buildings

    # H. Gordon and Sons Department Store - 4-story, closed 1972
    {
        'address': '768 Broadway, Gary, IN 46402',
        'lat': '41.597168', 'lon': '-87.337196',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5972,-87.3370,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://autopsyofarchitecture.com/h-gordon-sons-department-store/',
        'notes': 'H. Gordon and Sons Department Store. 4-story Prairie School style building at 7th Ave and Broadway. Originally built 1923 as Elks lodge (designed by George W. Maher & Son), converted to department store 1934. Closed Sep 1972 due to declining downtown, crime. County welfare offices occupied 1973-unknown. Added to National Register of Historic Places 1994 (Gary City Center Historic District). Interior floors collapsed from water damage. Apr 2024 SV shows boarded storefronts, ornate entrance arch, broken upper windows.'
    },

    # 800 Broadway - 4-story brick commercial, abandoned
    {
        'address': '800 Broadway, Gary, IN 46402',
        'lat': '41.596539', 'lon': '-87.337195',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5965,-87.3370,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '4-story brick commercial building at NE corner of Broadway and 8th Ave. Broken and boarded windows, colorful murals painted on ground-floor storefronts. Part of continuous block of abandoned storefronts on east side of Broadway between 7th and 9th Ave. Apr 2024 SV. Adjacent to H. Gordon building (768 Broadway) to the north.'
    },

    # Sears, Roebuck & Company Building - massive Art Deco, abandoned 1974
    {
        'address': '824 Broadway, Gary, IN 46402',
        'lat': '41.596211', 'lon': '-87.337191',
        'city': 'Gary', 'state': 'IN', 'zip': '46402',
        'type': 'COMMERCIAL', 'status': 'PROBABLY VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.5960,-87.3370,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.abandonedamerica.us/gary-indiana',
        'notes': 'Former Sears, Roebuck & Company building. Massive 4-story Art Deco commercial building spanning Broadway from approximately 8th Ave south. Abandoned 1974. $6M renovation 1993 for Division of Family and Children offices — unclear if still in use. IU Northwest School of Arts mural project planned. Apr 2024 SV shows large facade with vertical pilasters and decorative cornices, all storefronts appear dark, no visible activity. Part of Gary City Center Historic District (National Register).'
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
