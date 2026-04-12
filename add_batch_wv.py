import csv
from collections import Counter

new_properties = [
    # WELCH, WV - McDowell County coal town downtown blight
    # Boarded storefronts block on Virginia Ave
    {
        'address': '50 Virginia Ave, Welch, WV 24801',
        'lat': '37.431104', 'lon': '-81.584064',
        'city': 'Welch', 'state': 'WV', 'zip': '24801',
        'type': 'COMMERCIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.431200,-81.585600,3a,75y,90h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Downtown Welch commercial block. Mar 2025 SV shows multiple boarded storefronts with deteriorating aluminum siding and cardboard/plywood over windows. McDowell County seat, population declined from 6600 (1950) to under 2000. Coal economy collapse.'
    },
    # Empty storefront on McDowell St
    {
        'address': '75 McDowell St, Welch, WV 24801',
        'lat': '37.432155', 'lon': '-81.585715',
        'city': 'Welch', 'state': 'WV', 'zip': '24801',
        'type': 'RETAIL', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.432400,-81.585700,3a,75y,270h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Downtown Welch. Mar 2025 SV shows large empty storefront with glass windows revealing completely vacant interior. Deteriorating brick building on main commercial street.'
    },
    # Deteriorating brick commercial block
    {
        'address': '56 McDowell St, Welch, WV 24801',
        'lat': '37.432974', 'lon': '-81.585585',
        'city': 'Welch', 'state': 'WV', 'zip': '24801',
        'type': 'COMMERCIAL', 'status': 'PROBABLY VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@37.432974,-81.585585,3a,75y,90h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': '',
        'notes': 'Downtown Welch. Mar 2025 SV shows multiple multi-story brick commercial buildings with deteriorating exteriors, debris in parking area. Adjacent to active WIC office at 28 McDowell, but most commercial buildings on block appear underused or vacant.'
    },
    # WHEELING, WV - McLure Hotel (CONDEMNED)
    {
        'address': '1200 Market St, Wheeling, WV 26003',
        'lat': '40.067222', 'lon': '-80.722434',
        'city': 'Wheeling', 'state': 'WV', 'zip': '26003',
        'type': 'HOSPITALITY', 'status': 'CONDEMNED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@40.067100,-80.722200,3a,75y,270h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.theintelligencer.net/news/top-headlines/2024/11/city-of-wheeling-condemns-mclure-hotel/',
        'notes': 'McLure Hotel. Historic hotel built 1852, operated as Ramada/OYO. Condemned Nov 2024 by City of Wheeling. Code violations: mold, fire safety, sewage, electrical. Tenants evicted. Health dept permits suspended indefinitely. Prospective buyer from Arkansas in negotiations as of Dec 2024. 9-story landmark building on Market St.'
    },
    # WHEELING - Wheeling-Pitt Building (vacant 12-story office)
    {
        'address': '1134 Market St, Wheeling, WV 26003',
        'lat': '40.068207', 'lon': '-80.722582',
        'city': 'Wheeling', 'state': 'WV', 'zip': '26003',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@40.068207,-80.722582,3a,75y,270h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.wheelingwv.gov/news/post/11147/',
        'notes': 'Former Wheeling-Pittsburgh Steel headquarters. 12-story office building vacant since RG Steel bankruptcy in 2012. Sep 2025 SV shows building behind iron fencing. Announced conversion to 128 market-rate apartments but renovation timeline uncertain. Downtown Wheeling landmark.'
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
