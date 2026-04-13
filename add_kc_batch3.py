"""
Add third batch of Kansas City MO properties + 1 Camden NJ user submission.
14 KC dangerous buildings screened via SV + 1 user-submitted Camden property.
"""
import csv

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"
KC_SOURCE = "https://data.kcmo.org/Neighborhoods/Dangerous-Buildings-List/ax3m-jhxx"
USER_SOURCE = "User-submitted via Google Maps Street View"

new_properties = [
    # --- KC dangerous buildings, SV-screened ---
    {
        "address": "3611 Bellaire Ave, Kansas City, MO 64129",
        "lat": "39.059072", "lon": "-94.515219",
        "city": "Kansas City", "state": "MO", "zip": "64129",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3611+Bellaire+Ave,+Kansas+City,+MO+64129/@39.059072,-94.515219,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00241 filed Sep 2025; heavily overgrown property with structure partially visible"
    },
    {
        "address": "1212 Collins St, Kansas City, MO 64127",
        "lat": "39.096776", "lon": "-94.521137",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1212+Collins+St,+Kansas+City,+MO+64127/@39.096776,-94.521137,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00118 filed Apr 2025; building on tree-lined street"
    },
    {
        "address": "2410 E 26th St, Kansas City, MO 64127",
        "lat": "39.079042", "lon": "-94.554527",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2410+E+26th+St,+Kansas+City,+MO+64127/@39.079042,-94.554527,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00249 filed Sep 2025; neglected brick house"
    },
    {
        "address": "1702 E 41st St, Kansas City, MO 64110",
        "lat": "39.052262", "lon": "-94.564115",
        "city": "Kansas City", "state": "MO", "zip": "64110",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1702+E+41st+St,+Kansas+City,+MO+64110/@39.052262,-94.564115,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2021-00002 filed Mar 2021; residential building on dangerous list since 2021"
    },
    {
        "address": "1624 Lister Ave, Kansas City, MO 64127",
        "lat": "39.091988", "lon": "-94.526880",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1624+Lister+Ave,+Kansas+City,+MO+64127/@39.091988,-94.52688,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00242 filed Sep 2025; small house in poor condition"
    },
    {
        "address": "4836 E 9th St, Kansas City, MO 64124",
        "lat": "39.101749", "lon": "-94.525496",
        "city": "Kansas City", "state": "MO", "zip": "64124",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4836+E+9th+St,+Kansas+City,+MO+64124/@39.101749,-94.525496,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00180 filed Jun 2025; commercial/industrial building"
    },
    {
        "address": "3513 Roberts St, Kansas City, MO 64124",
        "lat": "39.106807", "lon": "-94.540217",
        "city": "Kansas City", "state": "MO", "zip": "64124",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3513+Roberts+St,+Kansas+City,+MO+64124/@39.106807,-94.540217,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00057 filed Feb 2025; deteriorating house"
    },
    {
        "address": "5209 Norton Ave, Kansas City, MO 64130",
        "lat": "39.030784", "lon": "-94.537528",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5209+Norton+Ave,+Kansas+City,+MO+64130/@39.030784,-94.537528,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2022-00118 filed May 2022; overgrown house"
    },
    {
        "address": "6513 E 12th St, Kansas City, MO 64126",
        "lat": "39.097336", "lon": "-94.506016",
        "city": "Kansas City", "state": "MO", "zip": "64126",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/6513+E+12th+St,+Kansas+City,+MO+64126/@39.097336,-94.506016,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2024-00082 filed Mar 2024; commercial building on E 12th St"
    },
    {
        "address": "3336 Chestnut Ave, Kansas City, MO 64128",
        "lat": "39.065472", "lon": "-94.550809",
        "city": "Kansas City", "state": "MO", "zip": "64128",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3336+Chestnut+Ave,+Kansas+City,+MO+64128/@39.065472,-94.550809,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2023-00051 filed Feb 2023; house on residential street"
    },
    {
        "address": "2428 Denver Ave, Kansas City, MO 64127",
        "lat": "39.081090", "lon": "-94.522396",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2428+Denver+Ave,+Kansas+City,+MO+64127/@39.08109,-94.522396,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2021-00362 filed Nov 2020; heavily overgrown house"
    },
    {
        "address": "801 Gladstone Ave, Kansas City, MO 64124",
        "lat": "39.103249", "lon": "-94.545941",
        "city": "Kansas City", "state": "MO", "zip": "64124",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/801+Gladstone+Ave,+Kansas+City,+MO+64124/@39.103249,-94.545941,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00104 filed Apr 2025; commercial/industrial structures"
    },
    {
        "address": "5301 Prospect Ave, Kansas City, MO 64130",
        "lat": "39.030089", "lon": "-94.554876",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5301+Prospect+Ave,+Kansas+City,+MO+64130/@39.030089,-94.554876,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2023-00176 filed Aug 2023; commercial building on Prospect Ave corridor"
    },
    {
        "address": "5829 Bellefontaine Ave, Kansas City, MO 64130",
        "lat": "39.020283", "lon": "-94.549808",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5829+Bellefontaine+Ave,+Kansas+City,+MO+64130/@39.020283,-94.549808,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00318 filed Nov 2025; overgrown house"
    },
    # --- User-submitted Camden NJ ---
    {
        "address": "519 Broadway, Camden, NJ 08103",
        "lat": "39.938440", "lon": "-75.119388",
        "city": "Camden", "state": "NJ", "zip": "08103",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/519+Broadway,+Camden,+NJ+08103/@39.93844,-75.119388,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building on Broadway (County Rd 551) in Camden"
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

status_counts = {}
for prop in to_add:
    s = prop['status']
    status_counts[s] = status_counts.get(s, 0) + 1

print(f"\nSummary of added properties:")
for s, c in sorted(status_counts.items()):
    print(f"  {s}: {c}")
