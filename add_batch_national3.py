import csv
from collections import Counter

new_properties = [
    # BUFFALO, NY - Abandoned industrial bakery

    # Wonder Bread Factory - 5-story, 198,600 SF industrial bakery, abandoned since 2004
    {
        'address': '356 Fougeron St, Buffalo, NY 14211',
        'lat': '42.908260', 'lon': '-78.825857',
        'city': 'Buffalo', 'state': 'NY', 'zip': '14211',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '356 FOUGERON INC', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.9083,-78.8259,3a,75y,270h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.buffalorising.com/2025/03/times-a-tickin-for-the-wonder-bread-building/',
        'notes': 'Wonder Bread Factory. 5-story, 198,600 SF reinforced concrete industrial bakery with mushroom columns, built 1914. Operated by Interstate Bakeries, closed Oct 2004 when parent filed bankruptcy. Last 150 employees left. National Register of Historic Places. Purchased Sep 2020 by developer Harry Stinson (356 Fougeron Inc) for planned $30M apartment conversion, later changed to startup office incubator — neither project started. Mar 2025 report: roof covered in ice, each floor has inch+ of standing water, but concrete structure still very solid. Sep 2014 SV from 358 Fougeron shows cream/tan factory building. Building confirmed still standing Mar 2025.'
    },

    # DULUTH, GA - Vacant enclosed shopping mall

    # Gwinnett Place Mall - 1.3M SF enclosed mall, fully vacant March 2025
    {
        'address': '2100 Pleasant Hill Rd, Duluth, GA 30096',
        'lat': '33.956991', 'lon': '-84.133144',
        'city': 'Duluth', 'state': 'GA', 'zip': '30096',
        'type': 'RETAIL', 'status': 'VACANT',
        'owner': 'GWINNETT COUNTY', 'assessment': '',
        'link': 'https://www.google.com/maps/@33.9555,-84.1345,3a,75y,30h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Gwinnett_Place_Mall',
        'notes': 'Gwinnett Place Mall. 1.3 million SF enclosed regional mall on 39 acres. Opened 1984, peaked with 200+ stores. Last anchors (both Macy\'s stores) closed Mar 23, 2025. Gwinnett County Urban Redevelopment Agency purchased mall for $23M in 2021. County also bought former Sears anchor for $11.5M in Sep 2025, bringing total owned to 87.5 acres. Plans for demolition and "Global Villages" mixed-use redevelopment announced Feb 2023, but no construction started. Nov 2018 SV from parking lot shows mall building. Famous as filming location (Stranger Things Starcourt Mall).'
    },

    # NEW ORLEANS, LA - Abandoned industrial power plant

    # Market Street Power Plant - 160,000 SF, abandoned since 1973
    {
        'address': '1600 S Peters St, New Orleans, LA 70130',
        'lat': '29.930561', 'lon': '-90.064784',
        'city': 'New Orleans', 'state': 'LA', 'zip': '70130',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@29.9306,-90.0648,3a,75y,90h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Market_Street_Power_Plant',
        'notes': 'Market Street Power Plant. Historic defunct power plant complex, 160,000+ SF across 7 buildings on Mississippi River bank between Warehouse District and Lower Garden District. Built 1905 by New Orleans Railway & Light Co, expanded over decades. Last produced power 1973 — 53 years abandoned. Lauricella Land Co, Brian Gibbs Development, and Cypress Equities closed investment deal 2022. Planned Fall 2024 opening as entertainment/retail/hotel venue never materialized. May 2025 renovation put on hold pending state tax credits. No visible construction. Sep 2025 SV from S Peters St shows massive graffiti-covered brick industrial building with security fencing.'
    },

    # JACKSON, MS - Abandoned enclosed shopping mall

    # Metrocenter Mall - 1.25M SF, Mississippi's largest mall, abandoned
    {
        'address': '3645 Hwy 80 W, Jackson, MS 39209',
        'lat': '32.299720', 'lon': '-90.251670',
        'city': 'Jackson', 'state': 'MS', 'zip': '39209',
        'type': 'RETAIL', 'status': 'ABANDONED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@32.2997,-90.2517,3a,75y,180h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Metrocenter_Mall_(Jackson,_Mississippi)',
        'notes': 'Metrocenter Mall. Mississippi\'s largest enclosed shopping mall, 1,250,000 SF on two levels with four anchor spaces. Opened Mar 1, 1978, near junction of I-20 and I-220/US-49. Last anchor (Sears) closed Jan 2012. Mall officially closed Aug 15, 2018. Last retail tenant (Burlington) left Feb 2022. City offices vacated 2024, making building completely empty. Ring road deteriorating, doors boarded with plywood. May 2025 Randy Travis and wife announced investment plans but no details or construction. May 2023 SV from ring road shows abandoned mall facade with standing water, broken windows, overgrown vegetation.'
    },

    # BESSEMER, AL - Vacant enclosed shopping mall

    # West Lake Mall - 323,000 SF mall, vacant since 2009
    {
        'address': '1036 Westlake Mall, Bessemer, AL 35020',
        'lat': '33.389978', 'lon': '-86.978564',
        'city': 'Bessemer', 'state': 'AL', 'zip': '35020',
        'type': 'RETAIL', 'status': 'VACANT',
        'owner': 'RANGE LIGHT INVESTMENT PARTNERS', 'assessment': '',
        'link': 'https://www.google.com/maps/@33.3900,-86.9786,3a,75y,180h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://bhamnow.com/2025/06/02/vacant-bessemer-mall-to-get-new-life/',
        'notes': 'West Lake Mall (The Mall at Westlake). 323,000 SF single-level enclosed mall on 40-acre parcel north of Bessemer Superhighway, south of I-20/59. Built 1969 by Mel Simon. Had Sears, JCPenney, Grant\'s, Loveman\'s anchors. Last tenant (Bruno\'s) closed 2009 when chain filed bankruptcy — vacant 17 years. Auto dealer Anthony Underwood purchased for $950K in 2006. Range Light Investment Partners later purchased for $3M with plans for Marvel City Business Park (industrial/manufacturing suites), but no construction started as of Jun 2025. Oct 2018 SV shows vacant concrete-walled building with empty lot.'
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
