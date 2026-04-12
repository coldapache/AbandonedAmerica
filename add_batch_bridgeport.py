import csv
from collections import Counter

new_properties = [
    # CHERRY ST FACTORY COMPLEX - massive abandoned industrial complex
    {
        'address': '62 Cherry St, Bridgeport, CT 06605',
        'lat': '41.167890', 'lon': '-73.196350',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06605',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.167890,-73.196350,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Cherry St factory complex. Massive multi-story brick factory building, iron gates, no activity. Jun 2023 SV. Part of cluster of abandoned industrial buildings on Cherry St.'
    },
    {
        'address': '72 Cherry St, Bridgeport, CT 06605',
        'lat': '41.168200', 'lon': '-73.196100',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06605',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.168200,-73.196100,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Cherry St factory complex. Massive brick industrial building, all windows boarded/covered with plywood, overgrown weeds at base. Jun 2023 SV.'
    },
    {
        'address': '80 Cherry St, Bridgeport, CT 06605',
        'lat': '41.168500', 'lon': '-73.195850',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06605',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.168500,-73.195850,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Cherry St factory complex. Industrial building with all windows boarded with metal/plywood panels. Jun 2023 SV. Same complex as 62-72 Cherry St.'
    },
    # 1325 RAILROAD AVE - overgrown industrial lot
    {
        'address': '1325 Railroad Ave, Bridgeport, CT 06605',
        'lat': '41.168100', 'lon': '-73.196700',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06605',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.168100,-73.196700,3a,75y,270h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Dense overgrown vegetation covering lot/building adjacent to Cherry St factory complex. Jun 2019 SV. Near Remington Arms site.'
    },
    # 812 BARNUM AVE - Former Remington Arms factory (DEMOLISHED)
    {
        'address': '812 Barnum Ave, Bridgeport, CT 06608',
        'lat': '41.184230', 'lon': '-73.181550',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06608',
        'type': 'INDUSTRIAL', 'status': 'DEMOLISHED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.184230,-73.181550,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Former Remington Arms / UMC factory. Massive industrial complex demolished. Jul 2024 SV shows cleared site with dirt mounds and excavator. Environmental cleanup ongoing. Historic munitions factory operational 1867-1988.'
    },
    # 227 MIDDLE ST - Davidson Fabric Factory
    {
        'address': '227 Middle St, Bridgeport, CT 06604',
        'lat': '41.179400', 'lon': '-73.195500',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06604',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.179400,-73.195500,3a,75y,90h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Former Davidson Fabric Factory. Large deteriorating multi-story brick industrial building with peeling paint and green shuttered windows. Nov 2020 SV. Long-vacant manufacturing facility.'
    },
    # 307 CENTER ST - demolished commercial building
    {
        'address': '307 Center St, Bridgeport, CT 06604',
        'lat': '41.180200', 'lon': '-73.195800',
        'city': 'Bridgeport', 'state': 'CT', 'zip': '06604',
        'type': 'COMMERCIAL', 'status': 'DEMOLISHED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.180200,-73.195800,3a,75y,0h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Chain-link fenced lot with deteriorating blue/teal commercial building visible in Nov 2020 SV. Demolition reportedly started June 2025. Site awaiting redevelopment.'
    },
    # 510 GRAND AVE, NEW HAVEN - English Station power plant
    {
        'address': '510 Grand Ave, New Haven, CT 06513',
        'lat': '41.305800', 'lon': '-72.893400',
        'city': 'New Haven', 'state': 'CT', 'zip': '06513',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@41.305800,-72.893400,3a,75y,180h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'English Station power plant. Former United Illuminating coal-fired power plant, decommissioned 1992. Smokestacks visible behind graffiti-covered concrete perimeter wall. Fenced off, no activity. Aug 2024 SV. Environmental contamination site. One of New Havens most prominent abandoned industrial landmarks.'
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
