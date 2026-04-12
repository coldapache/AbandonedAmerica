import csv
from collections import Counter

new_properties = [
    # LOUISVILLE, KY - Major vacant downtown office buildings

    # Starks Building - 14-story office, vacant since 2020
    {
        'address': '455 S 4th St, Louisville, KY 40202',
        'lat': '38.252003', 'lon': '-85.757262',
        'city': 'Louisville', 'state': 'KY', 'zip': '40202',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@38.2528,-85.7572,3a,90y,180h,110t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.wdrb.com/news/louisville-inches-closer-to-reviving-downtown-with-plan-for-vacant-buildings/article_86721f24-eb28-11ef-9d52-53c945810373.html',
        'notes': 'Starks Building. 14-story landmark office building at 4th St and Muhammad Ali Blvd. Built 1913, expanded 1923. Fully vacant since 2020 after last tenant Eddie Merlot\'s closed during protests/riots and did not reopen. $100M mixed-use redevelopment proposed by developer Jeff Underhill (264 affordable apartments, art studios, galleries) — seeking $18.6M from city Conservation Fund, construction not started. Louisville\'s 4th Street Live! entertainment district obscures SV coverage — building confirmed vacant via multiple news sources.'
    },

    # Kentucky Home Life Building - 20-story office, vacant since 2022
    {
        'address': '239 S 5th St, Louisville, KY 40202',
        'lat': '38.254534', 'lon': '-85.758500',
        'city': 'Louisville', 'state': 'KY', 'zip': '40202',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@38.2538,-85.7588,3a,90y,350h,110t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.wdrb.com/news/louisville-police-city-officials-clear-trespassers-from-vacant-kentucky-home-life-building/article_dd3cbc04-4058-11ef-8a29-dbbdb7b83e85.html',
        'notes': 'Kentucky Home Life Building. 20-story, 235-ft office tower at 5th and Jefferson, across from Louisville Metro Hall. Original 1912 structure (Brinton B. Davis, architect) expanded with 20-story addition. Possibly largest vacant structure in downtown Louisville. Last tenants left Feb 2022 citing lack of security/maintenance. Jul 2024 police raided building to remove trespassers who had been stealing wiring/metal, causing a major gas leak. Building undergoing foreclosure. Aug 2024 SV from S 5th St shows building.'
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
