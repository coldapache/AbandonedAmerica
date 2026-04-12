import csv
from collections import Counter

new_properties = [
    # DETROIT, MI - Gratiot Ave corridor abandoned commercial buildings

    # 2703 Gratiot Ave - 3-story commercial, ornate upper facade, vacant
    {
        'address': '2703 Gratiot Ave, Detroit, MI 48207',
        'lat': '42.353561', 'lon': '-83.031430',
        'city': 'Detroit', 'state': 'MI', 'zip': '48207',
        'type': 'COMMERCIAL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.3538676,-83.031057,3a,75y,135.28h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '3-story commercial building with ornate decorative terra cotta upper-floor facade. Ground floor storefronts covered/boarded, "2700" visible on building. Upper windows deteriorated. Adjacent to other vacant storefronts. Near Zeidman\'s Jewelry & Loan. Sep 2025 SV.'
    },

    # 2661 Gratiot Ave - 2-story brick commercial row, storefronts boarded
    {
        'address': '2661 Gratiot Ave, Detroit, MI 48207',
        'lat': '42.353214', 'lon': '-83.031654',
        'city': 'Detroit', 'state': 'MI', 'zip': '48207',
        'type': 'COMMERCIAL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.3534384,-83.0313389,3a,75y,131.51h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Row of 2-story brick commercial buildings. Multiple storefronts boarded up with plywood, upper windows dark or covered. Continuous block of vacancy along east side of Gratiot Ave between Chene St and Hale St. Sep 2025 SV.'
    },

    # 2616 Gratiot Ave - 2-story concrete commercial, all windows boarded
    {
        'address': '2616 Gratiot Ave, Detroit, MI 48207',
        'lat': '42.352781', 'lon': '-83.031766',
        'city': 'Detroit', 'state': 'MI', 'zip': '48207',
        'type': 'COMMERCIAL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.3526657,-83.0318445,3a,75y,137.21h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '2-story concrete/stucco commercial building at corner with traffic light. All upper windows boarded, ground floor sealed. Billboard on roof. Adjacent building to west partially demolished/deteriorated. Sep 2025 SV.'
    },

    # 2299 Gratiot Ave - 2-story commercial, storefronts sealed
    {
        'address': '2299 Gratiot Ave, Detroit, MI 48207',
        'lat': '42.351145', 'lon': '-83.033020',
        'city': 'Detroit', 'state': 'MI', 'zip': '48207',
        'type': 'COMMERCIAL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.3520593,-83.0322405,3a,75y,317.51h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': '2-story brown/tan brick commercial building at corner. Ground floor storefronts sealed with roll-down gates or plywood. Upper windows blank/sealed. Vacant lot to the west. Active liquor store adjacent to the east. Sep 2025 SV.'
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
