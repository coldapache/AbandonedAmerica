"""
Add user-submitted Philadelphia properties to the CSV.
All in the Nicetown/Hunting Park neighborhood of North Philadelphia.
"""
import csv

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"
USER_SOURCE = "User-submitted via Google Maps Street View"

new_properties = [
    {
        "address": "3310 Fox St, Philadelphia, PA 19129",
        "lat": "40.006459", "lon": "-75.171119",
        "city": "Philadelphia", "state": "PA", "zip": "19129",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3310+Fox+St,+Philadelphia,+PA+19129/@40.006459,-75.171119,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; Nicetown/Hunting Park neighborhood"
    },
    {
        "address": "2412 W Hunting Park Ave, Philadelphia, PA 19129",
        "lat": "40.009072", "lon": "-75.168486",
        "city": "Philadelphia", "state": "PA", "zip": "19129",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2412+W+Hunting+Park+Ave,+Philadelphia,+PA+19129/@40.009072,-75.168486,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building on Hunting Park Ave commercial corridor"
    },
    {
        "address": "3537 N 24th St, Philadelphia, PA 19140",
        "lat": "40.009097", "lon": "-75.167848",
        "city": "Philadelphia", "state": "PA", "zip": "19140",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3537+N+24th+St,+Philadelphia,+PA+19140/@40.009097,-75.167848,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; Hunting Park neighborhood"
    },
    {
        "address": "2299 Ruffner St, Philadelphia, PA 19140",
        "lat": "40.010984", "lon": "-75.167613",
        "city": "Philadelphia", "state": "PA", "zip": "19140",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2299+Ruffner+St,+Philadelphia,+PA+19140/@40.010984,-75.167613,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; Hunting Park neighborhood"
    },
    {
        "address": "2212 Yelland St, Philadelphia, PA 19140",
        "lat": "40.011628", "lon": "-75.165112",
        "city": "Philadelphia", "state": "PA", "zip": "19140",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2212+Yelland+St,+Philadelphia,+PA+19140/@40.011628,-75.165112,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; Hunting Park neighborhood"
    },
]

# Read existing CSV
with open(CSV_FILE, 'r', newline='', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing_rows = list(reader)

# Check for duplicates
existing_addresses = {r['address'].lower().strip() for r in existing_rows}
to_add = []
for prop in new_properties:
    addr_lower = prop['address'].lower().strip()
    if addr_lower in existing_addresses:
        print(f"DUPLICATE - skipping: {prop['address']}")
    else:
        to_add.append(prop)

print(f"\nAdding {len(to_add)} new properties (skipped {len(new_properties) - len(to_add)} duplicates)")

all_rows = existing_rows + to_add

with open(CSV_FILE, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(all_rows)

print(f"CSV now has {len(all_rows) + 1} lines (header + {len(all_rows)} properties)")

# Validate
VALID_STATUS = {'ABANDONED','CHRONICALLY VACANT','CONDEMNED','DEMOLISHED','PROBABLY VACANT','VACANT'}
VALID_TYPE = {'COMMERCIAL','COMMERCIAL OFFICE','HOSPITALITY','INDUSTRIAL','INSTITUTIONAL','MIXED USE','RESIDENTIAL','RESTAURANT','RETAIL','WAREHOUSE'}

errors = 0
with open(CSV_FILE, 'r', newline='', encoding='utf-8-sig') as f:
    for i, r in enumerate(csv.DictReader(f), 2):
        try:
            assert r['status'] in VALID_STATUS, f"Row {i}: bad status '{r['status']}'"
            assert r['type'] in VALID_TYPE, f"Row {i}: bad type '{r['type']}'"
            assert 24.0 <= float(r['lat']) <= 49.5, f"Row {i}: bad lat {r['lat']}"
            assert -125.0 <= float(r['lon']) <= -66.5, f"Row {i}: bad lon {r['lon']}"
            assert r['link'].startswith('https://www.google.com/maps'), f"Row {i}: bad link"
        except AssertionError as e:
            print(f"VALIDATION ERROR: {e}")
            errors += 1
        except Exception as e:
            print(f"VALIDATION ERROR Row {i}: {e}")
            errors += 1

if errors == 0:
    print("All validation checks passed!")
else:
    print(f"{errors} validation errors found!")
