import csv
from collections import Counter

new_properties = [
    # ROCHESTER, NY - Abandoned 16-story psychiatric hospital tower

    # Terrence Building - 16-story brutalist tower, abandoned since 1995
    {
        'address': '1201 Elmwood Ave, Rochester, NY 14620',
        'lat': '43.123610', 'lon': '-77.606390',
        'city': 'Rochester', 'state': 'NY', 'zip': '14620',
        'type': 'INSTITUTIONAL', 'status': 'ABANDONED',
        'owner': 'NEW YORK STATE', 'assessment': '',
        'link': 'https://www.google.com/maps/@43.1225,-77.6060,3a,75y,10h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Terrence_Building',
        'notes': 'Terrence Building. 16-story, 160-ft brutalist reinforced concrete tower on Rochester Psychiatric Center campus. Opened 1959 as Rochester State Hospital psychiatric ward with 1,000 beds. Closed 1995. Vacant 31 years. Graffiti-covered, deteriorating, 6 elevators inoperable. 2019 arson fire. Developer Bob Morgan proposed $32M demolition and 110-room Hyatt House hotel 2015, city council approved demolition 2017, project stalled 2019. Estimated redevelopment cost risen to $32M+. Jul 2025 SV from south clearly shows massive abandoned tower looming over campus grounds.'
    },

    # TULSA, OK - Abandoned enclosed shopping mall

    # Tulsa Promenade Mall - 926K SF, closed Sep 2023, condemned
    {
        'address': '4107 S Yale Ave, Tulsa, OK 74135',
        'lat': '36.104301', 'lon': '-95.922258',
        'city': 'Tulsa', 'state': 'OK', 'zip': '74135',
        'type': 'RETAIL', 'status': 'ABANDONED',
        'owner': 'KOHAN RETAIL INVESTMENT GROUP', 'assessment': '',
        'link': 'https://www.google.com/maps/@36.1043,-95.9223,3a,75y,270h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Tulsa_Promenade',
        'notes': 'Tulsa Promenade Mall (formerly Southroads Mall). 926,426 SF enclosed regional mall at 41st St and S Yale Ave. Opened 1974, renamed Tulsa Promenade 2007. Closed Sep 17, 2023 after owner Mike Kohan (Kohan Retail Investment Group) failed to address fire suppression and alarm code violations. City deemed mall "unfit for human occupancy." Jun 2025 storm ripped part of facade. $800K in delinquent property taxes (2021-2024), narrowly avoided auction May 2025. Interior trashed — unlocked doors, scattered trash, evidence of homelessness, fires reported. No redevelopment plans as of late 2025. Feb 2025 SV from 41st & Yale shows mall area.'
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
states = Counter(p['state'] for p in to_add)
print(f'By state: {dict(states)}')
