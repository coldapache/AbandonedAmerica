"""
Add second batch of Kansas City, MO properties to the CSV.
Mix of dangerous buildings list candidates (screened via SV) and user-submitted properties.
"""
import csv

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"
SOURCE = "https://data.kcmo.org/Neighborhoods/Dangerous-Buildings-List/ax3m-jhxx"
USER_SOURCE = "User-submitted via Google Maps Street View"

new_properties = [
    # --- From dangerous buildings list, SV-screened ---
    {
        "address": "1621 Cambridge Ave, Kansas City, MO 64126",
        "lat": "39.091473", "lon": "-94.502248",
        "city": "Kansas City", "state": "MO", "zip": "64126",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1621+Cambridge+Ave,+Kansas+City,+MO+64126/@39.091473,-94.502248,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00036 filed Feb 2025; older house on residential street"
    },
    {
        "address": "2535 Montgall Ave, Kansas City, MO 64127",
        "lat": "39.080034", "lon": "-94.551071",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2535+Montgall+Ave,+Kansas+City,+MO+64127/@39.080034,-94.551071,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00293 filed Oct 2025; house with visible deterioration"
    },
    {
        "address": "2313 Askew Ave, Kansas City, MO 64127",
        "lat": "39.083749", "lon": "-94.540445",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2313+Askew+Ave,+Kansas+City,+MO+64127/@39.083749,-94.540445,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2022-00209 filed Oct 2022; run-down house in pre-bid demolition process"
    },
    {
        "address": "7409 E 49th St, Kansas City, MO 64129",
        "lat": "39.034138", "lon": "-94.498935",
        "city": "Kansas City", "state": "MO", "zip": "64129",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/7409+E+49th+St,+Kansas+City,+MO+64129/@39.034138,-94.498935,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00019 filed Jan 2025; neglected house in sparse residential area"
    },
    {
        "address": "2626 E 28th St, Kansas City, MO 64128",
        "lat": "39.074931", "lon": "-94.552216",
        "city": "Kansas City", "state": "MO", "zip": "64128",
        "type": "RESIDENTIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2626+E+28th+St,+Kansas+City,+MO+64128/@39.074931,-94.552216,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2021-00387 filed May 2018; large deteriorating two-story house with covered porch"
    },
    {
        "address": "4400 E 24th St, Kansas City, MO 64127",
        "lat": "39.082260", "lon": "-94.531636",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4400+E+24th+St,+Kansas+City,+MO+64127/@39.08226,-94.531636,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00204 filed Aug 2025; dark house with rusty garage/shed and debris"
    },
    {
        "address": "8202 E Bannister Rd, Kansas City, MO 64134",
        "lat": "38.951822", "lon": "-94.493952",
        "city": "Kansas City", "state": "MO", "zip": "64134",
        "type": "RETAIL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/8202+E+Bannister+Rd,+Kansas+City,+MO+64134/@38.951822,-94.493952,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2022-00110 filed Apr 2022; closed commercial storefront (former Robandee Market)"
    },
    {
        "address": "5932 Prospect Ave, Kansas City, MO 64130",
        "lat": "39.018768", "lon": "-94.555919",
        "city": "Kansas City", "state": "MO", "zip": "64130",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/5932+Prospect+Ave,+Kansas+City,+MO+64130/@39.018768,-94.555919,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2023-00252 filed Nov 2023; commercial building on Prospect Ave corridor"
    },
    {
        "address": "1227 Illinois Ave, Kansas City, MO 64127",
        "lat": "39.098268", "lon": "-94.545513",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1227+Illinois+Ave,+Kansas+City,+MO+64127/@39.098268,-94.545513,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00179 filed Jun 2025; deteriorating house with overgrown vegetation"
    },
    {
        "address": "1912 E 18th St, Kansas City, MO 64127",
        "lat": "39.091120", "lon": "-94.559211",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1912+E+18th+St,+Kansas+City,+MO+64127/@39.09112,-94.559211,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00174 filed Jun 2025; multi-story apartment building"
    },
    {
        "address": "3217 Troost Ave, Kansas City, MO 64109",
        "lat": "39.068067", "lon": "-94.571385",
        "city": "Kansas City", "state": "MO", "zip": "64109",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3217+Troost+Ave,+Kansas+City,+MO+64109/@39.068067,-94.571385,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00291 filed Oct 2025; large multi-story brick commercial building on Troost Ave corridor"
    },
    {
        "address": "3037 Main St, Kansas City, MO 64108",
        "lat": "39.072154", "lon": "-94.585214",
        "city": "Kansas City", "state": "MO", "zip": "64108",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3037+Main+St,+Kansas+City,+MO+64108/@39.072154,-94.585214,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00208 filed Aug 2025; large multi-story brick commercial building on Main St"
    },
    {
        "address": "1219 Garfield Ave, Kansas City, MO 64127",
        "lat": "39.098774", "lon": "-94.557126",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1219+Garfield+Ave,+Kansas+City,+MO+64127/@39.098774,-94.557126,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00273 filed Oct 2025; large deteriorating brick building with dark/boarded windows"
    },
    {
        "address": "2703 E 27th St, Kansas City, MO 64127",
        "lat": "39.076974", "lon": "-94.550770",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2703+E+27th+St,+Kansas+City,+MO+64127/@39.076974,-94.55077,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00229 filed Aug 2025; deteriorating multi-story Victorian-style house"
    },
    {
        "address": "704 Tracy Ave, Kansas City, MO 64106",
        "lat": "39.105254", "lon": "-94.567062",
        "city": "Kansas City", "state": "MO", "zip": "64106",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/704+Tracy+Ave,+Kansas+City,+MO+64106/@39.105254,-94.567062,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00032 filed Jan 2025; large commercial/warehouse building"
    },
    {
        "address": "4810 E 7th St, Kansas City, MO 64124",
        "lat": "39.103630", "lon": "-94.525687",
        "city": "Kansas City", "state": "MO", "zip": "64124",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4810+E+7th+St,+Kansas+City,+MO+64124/@39.10363,-94.525687,18z",
        "source": SOURCE,
        "notes": "Dangerous building case 2025-00321 filed Nov 2025; large Victorian-style house showing deterioration"
    },
    # --- User-submitted properties ---
    {
        "address": "1199 Indiana Ave, Kansas City, MO 64127",
        "lat": "39.098586", "lon": "-94.542104",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "RESIDENTIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1199+Indiana+Ave,+Kansas+City,+MO+64127/@39.098586,-94.542104,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building at Indiana Ave and E 12th St intersection area"
    },
    {
        "address": "3316 E 12th St, Kansas City, MO 64127",
        "lat": "39.098610", "lon": "-94.542755",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3316+E+12th+St,+Kansas+City,+MO+64127/@39.09861,-94.542755,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building adjacent to 3314 E 12th St on E 12th St commercial corridor"
    },
    {
        "address": "3007 E 12th St, Kansas City, MO 64127",
        "lat": "39.098649", "lon": "-94.546976",
        "city": "Kansas City", "state": "MO", "zip": "64127",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3007+E+12th+St,+Kansas+City,+MO+64127/@39.098649,-94.546976,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building on E 12th St commercial corridor"
    },
    {
        "address": "1700 E Truman Rd, Kansas City, MO 64106",
        "lat": "39.095183", "lon": "-94.561345",
        "city": "Kansas City", "state": "MO", "zip": "64106",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1700+E+Truman+Rd,+Kansas+City,+MO+64106/@39.095183,-94.561345,18z",
        "source": USER_SOURCE,
        "notes": "User-submitted; building on Truman Rd commercial corridor"
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
