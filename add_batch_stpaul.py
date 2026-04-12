import csv
from collections import Counter

new_properties = [
    # ST. PAUL, MN - Alliance Bank Center

    # Alliance Bank Center - 16-story office tower, abruptly vacated March 2025
    {
        'address': '55 E 5th St, St. Paul, MN 55101',
        'lat': '44.946628', 'lon': '-93.092606',
        'city': 'St. Paul', 'state': 'MN', 'zip': '55101',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': 'MADISON EQUITIES', 'assessment': '',
        'link': 'https://www.google.com/maps/@44.9465,-93.0935,3a,75y,60h,110t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.axios.com/local/twin-cities/2025/04/11/alliance-bank-tower-st-paul-vacancy',
        'notes': 'Alliance Bank Center. 16-story, 300,000 sq ft office tower at E 5th St and Cedar St in downtown St. Paul. Abruptly vacated Mar 2025 when owner Madison Equities sent tenants 2-day notice to evacuate, declaring inability to pay utilities. Subsequently vandalized — intruders broke in, emptied fire extinguishers, trashed floors. City limited downtown skyway access through building. St. Paul Downtown Development Corp purchased bank note Oct 2025. Building valued at less than a third of 2019 purchase price. Closed for the foreseeable future for safety. Aug 2024 SV shows tower from Cedar St side.'
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
