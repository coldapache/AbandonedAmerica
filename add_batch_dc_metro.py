import csv
from collections import Counter

new_properties = [
    # FORMER LANDOVER MALL - 87-acre demolished retail site
    {
        'address': '2730 Brightseat Rd, Landover, MD 20785',
        'lat': '38.920000', 'lon': '-76.856110',
        'city': 'Landover', 'state': 'MD', 'zip': '20785',
        'type': 'RETAIL', 'status': 'DEMOLISHED',
        'owner': '', 'assessment': '',
        'link': 'https://www.google.com/maps/@38.921000,-76.854500,3a,75y,270h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://en.wikipedia.org/wiki/Landover_Mall',
        'notes': 'Former Landover Mall. 87-acre site demolished 2006. Mar 2022 SV shows vast empty parking lot with chain-link fencing. Proposed $5B data center project (Brightseat Tech Park) announced Oct 2024 but paused due to public opposition. Site has been vacant lot for 20 years. Adjacent to FedExField.'
    },
    # POTOMAC RIVER GENERATING STATION - decommissioned coal power plant
    {
        'address': '1400 N Royal St, Alexandria, VA 22314',
        'lat': '38.819000', 'lon': '-77.041500',
        'city': 'Alexandria', 'state': 'VA', 'zip': '22314',
        'type': 'INDUSTRIAL', 'status': 'ABANDONED',
        'owner': 'HRP GROUP', 'assessment': '',
        'link': 'https://www.google.com/maps/@38.819200,-77.042800,3a,75y,90h,90t/data=!3m6!1e1!3m4!1s0x0:0x0!2e0!7i16384!8i8192',
        'source': 'https://www.alexandriava.gov/neighborhood-development/potomac-river-generating-station-prgs-power-plant-redevelopment-old-town',
        'notes': 'Potomac River Generating Station. Former coal-fired power plant built 1948, decommissioned 2012. 20-acre waterfront site. Purchased by HRP Group 2020. Demolition planned 2027, mixed-use redevelopment with 2000 residential units by 2029-2030. Environmental remediation ongoing. No street-level SV coverage (fenced site). Old Town North.'
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
