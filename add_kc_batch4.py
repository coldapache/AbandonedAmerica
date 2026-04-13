"""
Add fourth batch of Kansas City MO properties + user submissions from CT and TN.
17 KC dangerous buildings screened via SV + 2 user-submitted properties.
"""
import csv

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"
KC_SOURCE = "https://data.kcmo.org/Neighborhoods/Dangerous-Buildings-List/ax3m-jhxx"
USER_SOURCE = "User-submitted via Google Maps Street View"

new_properties = [
    # --- KC dangerous buildings, SV-screened ---
    {
        "address": "6412 E 15th Ter, Kansas City, MO 64126",
        "lat": "39.092895", "lon": "-94.507714",
        "city": "Kansas City", "state": "MO", "zip": "64126",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/6412+E+15th+Ter,+Kansas+City,+MO+64126/@39.092895,-94.507714,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2021-00160 filed Feb 2021; overgrown property"
    },
    {
        "address": "1511 E 18th St, Kansas City, MO 64108",
        "lat": "39.091166", "lon": "-94.564232",
        "city": "Kansas City", "state": "MO", "zip": "64108",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1511+E+18th+St,+Kansas+City,+MO+64108/@39.091166,-94.564232,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2021-00295 filed Aug 2019; large commercial building on hold"
    },
    {
        "address": "613 Forest Ave, Kansas City, MO 64106",
        "lat": "39.106720", "lon": "-94.568137",
        "city": "Kansas City", "state": "MO", "zip": "64106",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/613+Forest+Ave,+Kansas+City,+MO+64106/@39.10672,-94.568137,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2023-00126 filed May 2023; deteriorated building"
    },
    {
        "address": "6020 E 16th St, Kansas City, MO 64126",
        "lat": "39.092155", "lon": "-94.512264",
        "city": "Kansas City", "state": "MO", "zip": "64126",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/6020+E+16th+St,+Kansas+City,+MO+64126/@39.092155,-94.512264,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2021-00161 filed Mar 2020; house on dangerous list since 2020"
    },
    {
        "address": "2836 White Ave, Kansas City, MO 64129",
        "lat": "39.073167", "lon": "-94.513498",
        "city": "Kansas City", "state": "MO", "zip": "64129",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2836+White+Ave,+Kansas+City,+MO+64129/@39.073167,-94.513498,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00314 filed Nov 2025; house with vegetation"
    },
    {
        "address": "5209 E 12th St, Kansas City, MO 64127",
        "lat": "39.097778", "lon": "-94.521584",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5209+E+12th+St,+Kansas+City,+MO+64127/@39.097778,-94.521584,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2023-00133 filed Jun 2023; commercial/industrial building on E 12th St"
    },
    {
        "address": "2922 Spruce Ave, Kansas City, MO 64128",
        "lat": "39.072277", "lon": "-94.533179",
        "city": "Kansas City", "state": "MO", "zip": "64128",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2922+Spruce+Ave,+Kansas+City,+MO+64128/@39.072277,-94.533179,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00188 filed Jun 2025; structure behind vegetation"
    },
    {
        "address": "4145 Forest Ave, Kansas City, MO 64110",
        "lat": "39.051654", "lon": "-94.571041",
        "city": "Kansas City", "state": "MO", "zip": "64110",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4145+Forest+Ave,+Kansas+City,+MO+64110/@39.051654,-94.571041,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00198 filed Jul 2025; house visible in SV"
    },
    {
        "address": "4032 Oakley Ave, Kansas City, MO 64130",
        "lat": "39.051067", "lon": "-94.519843",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4032+Oakley+Ave,+Kansas+City,+MO+64130/@39.051067,-94.519843,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00072 filed Mar 2025; structure visible"
    },
    {
        "address": "5325 Chestnut Ave, Kansas City, MO 64130",
        "lat": "39.029584", "lon": "-94.552606",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5325+Chestnut+Ave,+Kansas+City,+MO+64130/@39.029584,-94.552606,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00093 filed Mar 2025; overgrown house"
    },
    {
        "address": "3705 E 9th St, Kansas City, MO 64124",
        "lat": "39.101988", "lon": "-94.538818",
        "city": "Kansas City", "state": "MO", "zip": "64124",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3705+E+9th+St,+Kansas+City,+MO+64124/@39.101988,-94.538818,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2024-00272 filed Nov 2024; building on residential street"
    },
    {
        "address": "5014 South Benton Ave, Kansas City, MO 64130",
        "lat": "39.035135", "lon": "-94.551271",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5014+S+Benton+Ave,+Kansas+City,+MO+64130/@39.035135,-94.551271,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2024-00127 filed May 2024; structure visible in SV"
    },
    {
        "address": "3912 Myrtle Ave, Kansas City, MO 64130",
        "lat": "39.054304", "lon": "-94.537580",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3912+Myrtle+Ave,+Kansas+City,+MO+64130/@39.054304,-94.53758,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2023-00269 filed Dec 2023; house in blighted area"
    },
    {
        "address": "3501 E 26th St, Kansas City, MO 64127",
        "lat": "39.078492", "lon": "-94.541956",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3501+E+26th+St,+Kansas+City,+MO+64127/@39.078492,-94.541956,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00272 filed Oct 2025; deteriorated structure"
    },
    {
        "address": "3004 E 49th St, Kansas City, MO 64130",
        "lat": "39.037258", "lon": "-94.549798",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3004+E+49th+St,+Kansas+City,+MO+64130/@39.037258,-94.549798,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2022-00305 filed Dec 2022; red brick building"
    },
    {
        "address": "3543 Prospect Ave, Kansas City, MO 64128",
        "lat": "39.061898", "lon": "-94.553168",
        "city": "Kansas City", "state": "MO", "zip": "64128",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3543+Prospect+Ave,+Kansas+City,+MO+64128/@39.061898,-94.553168,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2025-00156 filed May 2025; commercial building on Prospect Ave corridor"
    },
    {
        "address": "2914 E 40th St, Kansas City, MO 64130",
        "lat": "39.053562", "lon": "-94.550013",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2914+E+40th+St,+Kansas+City,+MO+64130/@39.053562,-94.550013,18z",
        "source": KC_SOURCE,
        "notes": "Dangerous building case 2022-00139 filed Jun 2022; deteriorating house with overgrown yard"
    },
    # --- User-submitted properties ---
    {
        "address": "262 Old Gate Ln, Milford, CT 06460",
        "lat": "41.232355", "lon": "-73.027470",
        "city": "Milford", "state": "CT", "zip": "06460",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/262+Old+Gate+Ln,+Milford,+CT+06460/@41.232355,-73.02747,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; property in Milford CT"
    },
    {
        "address": "1074 Latham St, Memphis, TN 38106",
        "lat": "35.118058", "lon": "-90.052323",
        "city": "Memphis", "state": "TN", "zip": "38106",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1074+Latham+St,+Memphis,+TN+38106/@35.118058,-90.052323,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; South Memphis neighborhood"
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
