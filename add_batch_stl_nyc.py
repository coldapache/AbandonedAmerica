import csv
from collections import Counter

new_properties = [
    # ST. LOUIS, MO - One AT&T Center / 909 Chestnut

    # 909 Chestnut - 44-story vacant office tower, Missouri's largest building
    {
        'address': '909 Chestnut St, St. Louis, MO 63101',
        'lat': '38.627401', 'lon': '-90.194228',
        'city': 'St. Louis', 'state': 'MO', 'zip': '63101',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': 'GOLDMAN GROUP', 'assessment': '',
        'link': 'https://www.google.com/maps/@38.6280,-90.1942,3a,75y,200h,110t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/909_Chestnut_Street',
        'notes': 'One AT&T Center (909 Chestnut). 44-story, 588-ft office tower on the Gateway Mall. 1,400,000 sq ft — Missouri\'s largest building by area. Built 1985. Vacant since 2017 when AT&T did not renew lease after employee count fell from 4,800 to 2,000. Sold Apr 2024 to Boston-based Goldman Group for $3.6M (previously valued at $205M). $350M mixed-use plan announced for 600+ apartments, observation deck, automated parking. Renovation put on hold May 2025 when state tax credit bill was tabled. Jan 2026 SV shows black barriers at ground level, no construction activity. One of tallest vacant buildings in the world.'
    },

    # NEW YORK, NY - 161 Maiden Lane (1 Seaport)

    # 161 Maiden Lane - 60-story incomplete leaning skyscraper
    {
        'address': '161 Maiden Ln, New York, NY 10038',
        'lat': '40.705639', 'lon': '-74.005202',
        'city': 'New York', 'state': 'NY', 'zip': '10038',
        'type': 'RESIDENTIAL', 'status': 'VACANT',
        'owner': 'FORTIS PROPERTY GROUP', 'assessment': '',
        'link': 'https://www.google.com/maps/@40.7053,-74.0052,3a,75y,0h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/161_Maiden_Lane',
        'notes': '1 Seaport / Seaport Residences / "Leaning Tower of FiDi." 60-story, 670-ft unfinished residential skyscraper in Financial District. 200,000 sq ft, 80 planned condo units. Construction stalled ~2020 after 3-inch northward lean detected, caused by soil improvement foundation method instead of deep pilings. Only half of windows installed. $250M invested. Developer Fortis Property Group (Jonathan Landau) subject to lawsuits; court-appointed receiver since 2021. Nov 2024 SV shows scaffolding and construction barriers, no active work. Standing incomplete for 5+ years.'
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
