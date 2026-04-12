import csv
from collections import Counter

new_properties = [
    # BUFFALO, NY - Buffalo Grand Hotel

    # Buffalo Grand Hotel - 486-room hotel, vacant since 2022 fire
    {
        'address': '120 Church St, Buffalo, NY 14202',
        'lat': '42.884238', 'lon': '-78.881898',
        'city': 'Buffalo', 'state': 'NY', 'zip': '14202',
        'type': 'HOSPITALITY', 'status': 'VACANT',
        'owner': 'HARRY STINSON', 'assessment': '',
        'link': 'https://www.google.com/maps/@42.8842,-78.8819,3a,75y,180h,100t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.wgrz.com/article/money/business/buffalo-moves-to-seize-vacant-buffalo-grand-hotel/71-3f149497-5f1e-4e5b-ad8a-888012005643',
        'notes': 'Buffalo Grand Hotel (formerly Adams Mark, formerly Hilton). 486-room hotel, downtown Buffalo\'s largest. Opened late 1970s. Vacant since 2022 after 2021 arson fire gutted the ballroom area. Owner Harry Stinson has 18 code violations, $89K unpaid taxes/sewer fees. City of Buffalo filed legal action Jun 2025 to seize property due to neglect. Stinson received insurance payout Dec 2024 but no repairs made. Sep 2025 SV shows large multi-story hotel building standing vacant, no activity. Absence of hotel hampering city\'s convention business.'
    },

    # HOUSTON, TX - ExxonMobil Building

    # 800 Bell St - 44-story vacant office tower, 1.2M sq ft
    {
        'address': '800 Bell St, Houston, TX 77002',
        'lat': '29.754194', 'lon': '-95.369601',
        'city': 'Houston', 'state': 'TX', 'zip': '77002',
        'type': 'COMMERCIAL OFFICE', 'status': 'VACANT',
        'owner': 'BELL BUSINESS INVESTMENTS', 'assessment': '',
        'link': 'https://www.google.com/maps/@29.7542,-95.3705,3a,75y,90h,120t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/ExxonMobil_Building',
        'notes': 'ExxonMobil Building (Humble Oil Building). 44-story, 1,200,000 sq ft International Style office tower designed by Welton Becket. Built 1962-63. Vacant since 2015 when ExxonMobil moved to Spring TX campus. Acquired 2023 by Bell Business Investments (Isaac Jacobowitz/Carnegie Management) for apartment conversion. Filed Chapter 11 bankruptcy Oct 2025 after conversion plans collapsed. Avoided foreclosure Dec 2025 with $16.1M payoff. Court filings describe water damage, broken windows, moldy drywall. Listed on National Register of Historic Places 2025. Interior photosphere shows gutted floors. Mar 2026 SV shows tower standing in downtown Houston. One of largest vacant buildings in Texas.'
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
