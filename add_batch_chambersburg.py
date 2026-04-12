import csv
from collections import Counter

new_properties = [
    # CHAMBERSBURG, PA - Abandoned shopping mall

    # Chambersburg Mall - enclosed mall, fully abandoned June 2023
    {
        'address': '3055 Black Gap Rd, Chambersburg, PA 17202',
        'lat': '39.955000', 'lon': '-77.575000',
        'city': 'Chambersburg', 'state': 'PA', 'zip': '17202',
        'type': 'RETAIL', 'status': 'ABANDONED',
        'owner': 'NAMDAR REALTY GROUP', 'assessment': '',
        'link': 'https://www.google.com/maps/@39.9535,-77.5750,3a,75y,0h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Chambersburg_Mall',
        'notes': 'Chambersburg Mall. Enclosed shopping mall near Scotland, PA off I-81 Exit 20. Opened 1982, peaked at 75+ stores in 1990s-2000s. Last tenant (Black Rose) closed Jun 30, 2023. Owned by Namdar Realty Group. Major roof leaks and collapsed ceilings reported — dangerous conditions requiring condemnation. Building still standing as of 2025 with no demolition or redevelopment plans. Oct 2015 SV from parking lot shows mall structure (SV predates closure).'
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
