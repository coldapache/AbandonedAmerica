import csv

NEW_PROPERTIES = [
    # === BIRMINGHAM, AL (0 -> 4 entries, state #20: Alabama) ===
    {
        "address": "2012 1st Ave N, Birmingham, AL 35203",
        "lat": "33.514598", "lon": "-86.805487",
        "city": "Birmingham", "state": "AL", "zip": "35203",
        "type": "COMMERCIAL OFFICE", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2012+1st+Ave+N,+Birmingham,+AL+35203/@33.514598,-86.805487,17z",
        "source": "https://www.abandonedalabama.com/city/northern-alabama/birmingham/",
        "notes": "Brown Marx Building. 16-story 1906 Chicago-style tower, 193K sq ft. NE corner 20th St & 1st Ave N. Part of 'Heaviest Corner on Earth'. One of Birmingham's most prominent abandoned skyscrapers."
    },
    {
        "address": "2211 Avenue G, Birmingham, AL 35218",
        "lat": "33.509339", "lon": "-86.896797",
        "city": "Birmingham", "state": "AL", "zip": "35218",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2211+Avenue+G,+Birmingham,+AL+35218/@33.509339,-86.896797,17z",
        "source": "https://www.abandonedalabama.com/city/northern-alabama/birmingham/",
        "notes": "Bush School (Ernest F. Bush Middle School). Built 1901 as Ensley School. Closed. Historic school in Ensley neighborhood."
    },
    {
        "address": "2301 Avenue J, Birmingham, AL 35218",
        "lat": "33.506851", "lon": "-86.894373",
        "city": "Birmingham", "state": "AL", "zip": "35218",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2301+Avenue+J,+Birmingham,+AL+35218/@33.506851,-86.894373,17z",
        "source": "",
        "notes": "Ensley High School. Founded 1901, current building 1908. Closed 2006, caught fire fall 2018. Historic school building in Ensley."
    },
    {
        "address": "1600 6th Ave N, Birmingham, AL 35203",
        "lat": "33.516657", "lon": "-86.814515",
        "city": "Birmingham", "state": "AL", "zip": "35203",
        "type": "RESIDENTIAL", "status": "CONDEMNED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1600+6th+Ave+N,+Birmingham,+AL+35203/@33.516657,-86.814515,17z",
        "source": "https://www.birminghamal.gov/2024/09/27/statement-regarding-bankhead-towers/",
        "notes": "Bankhead Towers. Senior/disabled living high-rise, condemned Oct 2024 by City of Birmingham due to fire, building, and housing code violations. Residents evacuated."
    },
    # === YOUNGSTOWN, OH (0 -> 2 entries, state #20 or 21) ===
    {
        "address": "27 W Federal St, Youngstown, OH 44503",
        "lat": "41.100628", "lon": "-80.650816",
        "city": "Youngstown", "state": "OH", "zip": "44503",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/27+W+Federal+St,+Youngstown,+OH+44503/@41.100628,-80.650816,17z",
        "source": "",
        "notes": "Paramount Theatre (formerly Liberty Theatre). 1,700-seat theater designed by C. Howard Crane, opened 1918, closed 1976. Still standing. Plans for redevelopment."
    },
    {
        "address": "20 Federal Place, Youngstown, OH 44503",
        "lat": "41.100709", "lon": "-80.650699",
        "city": "Youngstown", "state": "OH", "zip": "44503",
        "type": "COMMERCIAL OFFICE", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/20+Federal+Place,+Youngstown,+OH+44503/@41.100709,-80.650699,17z",
        "source": "",
        "notes": "Downtown office building. Mahoning County Land Bank involvement for remediation. Federal Street corridor."
    },
    # === FLINT, MI (0 -> 2 entries) ===
    {
        "address": "425 S Saginaw St, Flint, MI 48502",
        "lat": "43.016597", "lon": "-83.691147",
        "city": "Flint", "state": "MI", "zip": "48502",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/425+S+Saginaw+St,+Flint,+MI+48502/@43.016597,-83.691147,17z",
        "source": "",
        "notes": "Paterson Building. Historic downtown commercial building, condemned then partially collapsed into Brush Alley. Mott Foundation granted $3.5M to Communities First for renovation."
    },
    {
        "address": "1425 N Saginaw St, Flint, MI 48502",
        "lat": "43.028698", "lon": "-83.693647",
        "city": "Flint", "state": "MI", "zip": "48502",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1425+N+Saginaw+St,+Flint,+MI+48502/@43.028698,-83.693647,17z",
        "source": "https://www.cityofflint.com/genesee-county-land-bank-announces-plans-to-demolish-vacant-and-damaged-buildings-in-flint/",
        "notes": "Commercial building on N Saginaw corridor. Genesee County Land Bank announced demolition plans."
    },
    # === ST. LOUIS, MO (4 -> 8 entries) ===
    {
        "address": "4256 Natural Bridge Ave, St. Louis, MO 63115",
        "lat": "38.667869", "lon": "-90.232255",
        "city": "St. Louis", "state": "MO", "zip": "63115",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4256+Natural+Bridge+Ave,+St.+Louis,+MO+63115/@38.667869,-90.232255,17z",
        "source": "",
        "notes": "Natural Bridge Ave commercial corridor in north St. Louis. Area documented with extensive commercial blight."
    },
    {
        "address": "4200 N Grand Blvd, St. Louis, MO 63107",
        "lat": "38.666640", "lon": "-90.212707",
        "city": "St. Louis", "state": "MO", "zip": "63107",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/4200+N+Grand+Blvd,+St.+Louis,+MO+63107/@38.666640,-90.212707,17z",
        "source": "",
        "notes": "N Grand Blvd corridor in north St. Louis. Area with extensive vacancy and commercial blight."
    },
    {
        "address": "3818 N Broadway, St. Louis, MO 63147",
        "lat": "38.664108", "lon": "-90.196213",
        "city": "St. Louis", "state": "MO", "zip": "63147",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/3818+N+Broadway,+St.+Louis,+MO+63147/@38.664108,-90.196213,17z",
        "source": "",
        "notes": "N Broadway corridor in north St. Louis. Area documented by STL City Talk and Exploring St. Louis blogs for extensive blight."
    },
    {
        "address": "2801 Cass Ave, St. Louis, MO 63106",
        "lat": "38.645784", "lon": "-90.215951",
        "city": "St. Louis", "state": "MO", "zip": "63106",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2801+Cass+Ave,+St.+Louis,+MO+63106/@38.645784,-90.215951,17z",
        "source": "",
        "notes": "Cass Ave corridor near NGA construction site. Jeff Vander Lou / St. Louis Place neighborhood. Area with extensive commercial vacancy."
    },
]

CSV_FILE = "Abandoned America - Abandoned or Unused Properties.csv"

with open(CSV_FILE, "r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    existing = list(reader)

existing_addresses = {r["address"].strip().lower() for r in existing}
added = []
skipped = []
for prop in NEW_PROPERTIES:
    if prop["address"].strip().lower() in existing_addresses:
        skipped.append(prop["address"])
    else:
        added.append(prop)
        existing.append(prop)

with open(CSV_FILE, "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(existing)

print(f"Added {len(added)} properties, skipped {len(skipped)} duplicates")
for a in added:
    print(f"  + {a['address']} ({a['status']}) [{a['city']}, {a['state']}]")
for s in skipped:
    print(f"  SKIP: {s}")
