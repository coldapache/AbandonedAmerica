import csv
from collections import Counter

new_properties = [
    # BLUEFIELD WV - downtown commercial blight
    # 116 Bland St - vacant storefront
    {
        'address': '116 Bland St, Bluefield, WV 24701',
        'lat': '37.269500', 'lon': '-81.222500',
        'city': 'Bluefield', 'state': 'WV', 'zip': '24701',
        'type': 'RETAIL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.269500,-81.222500,3a,75y,270h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Downtown Bluefield. Dec 2025 SV shows vacant storefront with missing/broken windows and exposed interior. Checkered tile base, deteriorating multi-story brick building. Part of Bland St commercial corridor blight. Bland Ferri Building (210) and CWA Building (200) nearby are slated for demolition.'
    },
    # 400 Federal St - demolished 400 block (former Montgomery Ward)
    {
        'address': '400 Federal St, Bluefield, WV 24701',
        'lat': '37.268569', 'lon': '-81.222028',
        'city': 'Bluefield', 'state': 'WV', 'zip': '24701',
        'type': 'COMMERCIAL', 'status': 'DEMOLISHED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.268800,-81.222800,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://wvmetronews.com/2024/07/28/bluefields-400-block-demolition-project-creating-space-for-opportunities-downtown/',
        'notes': 'Former 400 block of Federal St. Multiple commercial buildings including 8-story Montgomery Ward demolished Feb-Jul 2024 by city. Jun 2024 SV shows active demolition with excavator. Site is now cleared lot awaiting redevelopment as community park/green space.'
    },
    # ~210 Federal St - closed storefronts
    {
        'address': '210 Federal St, Bluefield, WV 24701',
        'lat': '37.269277', 'lon': '-81.222496',
        'city': 'Bluefield', 'state': 'WV', 'zip': '24701',
        'type': 'COMMERCIAL', 'status': 'PROBABLY VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.269000,-81.223200,3a,75y,90h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Downtown Bluefield commercial corridor. Jun 2024 SV shows closed storefronts with green roll-down gate and darkened windows facing Scott St. American flag and flower basket on light post but no signs of active business. Adjacent brick building also appears vacant.'
    },
]

csv_path = 'Abandoned America - Abandoned or Unused Properties.csv'
with open(csv_path, 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    existing = list(reader)
    fieldnames = reader.fieldnames

# Check for duplicates
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
