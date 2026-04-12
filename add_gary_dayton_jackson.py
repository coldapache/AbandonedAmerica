import csv

NEW_PROPERTIES = [
    # === GARY, IN (0 -> 6 entries — state #21: Indiana) ===
    {
        "address": "577 Washington St, Gary, IN 46402",
        "lat": "41.600392", "lon": "-87.338341",
        "city": "Gary", "state": "IN", "zip": "46402",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/577+Washington+St,+Gary,+IN+46402/@41.600392,-87.338341,17z",
        "source": "https://en.wikipedia.org/wiki/City_Methodist_Church_(Gary,_Indiana)",
        "notes": "City Methodist Church. Built 1925-26 for $800K, once largest Methodist church in Midwest. Closed 1975. Iconic ruin, roofless shell. Indiana Landmarks 10 Most Endangered. National Register eligible. On 6th Ave at Washington St."
    },
    {
        "address": "791 Broadway, Gary, IN 46407",
        "lat": "41.596791", "lon": "-87.337043",
        "city": "Gary", "state": "IN", "zip": "46407",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/791+Broadway,+Gary,+IN+46407/@41.596791,-87.337043,17z",
        "source": "https://en.wikipedia.org/wiki/Palace_Theater_(Gary,_Indiana)",
        "notes": "Palace Theater. John Eberson-designed 3,000-seat atmospheric theater, opened 1925, closed 1972. Emerson neighborhood. Sold for $2,500. City acquired for redevelopment. Still standing."
    },
    {
        "address": "185 Broadway, Gary, IN 46402",
        "lat": "41.606688", "lon": "-87.337113",
        "city": "Gary", "state": "IN", "zip": "46402",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/185+Broadway,+Gary,+IN+46402/@41.606688,-87.337113,17z",
        "source": "https://en.wikipedia.org/wiki/Gary_Union_Station",
        "notes": "Gary Union Station. Beaux-Arts railroad station built 1910, closed 1950s. Sits between two raised rail lines. National Register of Historic Places 2019. Indiana Landmarks 10 Most Endangered."
    },
    {
        "address": "716 E 7th Ave, Gary, IN 46402",
        "lat": "41.598517", "lon": "-87.328082",
        "city": "Gary", "state": "IN", "zip": "46402",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/716+E+7th+Ave,+Gary,+IN+46402/@41.598517,-87.328082,17z",
        "source": "https://en.wikipedia.org/wiki/Emerson_High_School_(Indiana)",
        "notes": "Ralph Waldo Emerson High School. William B. Ittner-designed school, opened 1909, closed 2008. Fire Dec 2023 severely damaged structure. National Register of Historic Places. Auditorium, gymnasium, pool, zoo."
    },
    {
        "address": "524 Garfield St, Gary, IN 46404",
        "lat": "41.600995", "lon": "-87.359454",
        "city": "Gary", "state": "IN", "zip": "46404",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/524+Garfield+St,+Gary,+IN+46404/@41.600995,-87.359454,17z",
        "source": "https://www.placesthatwere.com/2017/01/horace-mann-school-abandoned-gary-indiana.html",
        "notes": "Horace Mann High School. Built 1921-1928, served Gary's west side. Closed June 2004 due to budget cuts and declining enrollment (546 students, 1/5 capacity). Designed by William Wirt."
    },
    {
        "address": "1 Genesis Center Plz, Gary, IN 46402",
        "lat": "41.603803", "lon": "-87.338379",
        "city": "Gary", "state": "IN", "zip": "46402",
        "type": "INSTITUTIONAL", "status": "ABANDONED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/1+Genesis+Center+Plz,+Gary,+IN+46402/@41.603803,-87.338379,17z",
        "source": "https://en.wikipedia.org/wiki/Genesis_Convention_Center",
        "notes": "Genesis Convention Center. 7,000-seat arena built 1981. George Clinton, Public Enemy, Whitney Houston performed here. Closed 2020. City considering future plans as of 2025."
    },
    # === DAYTON, OH (0 -> 2 entries) ===
    {
        "address": "40 S Main St, Dayton, OH 45402",
        "lat": "39.758175", "lon": "-84.191394",
        "city": "Dayton", "state": "OH", "zip": "45402",
        "type": "COMMERCIAL OFFICE", "status": "VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/40+S+Main+St,+Dayton,+OH+45402/@39.758175,-84.191394,17z",
        "source": "https://en.wikipedia.org/wiki/Centre_City_Building",
        "notes": "Centre City Building. 21-story reinforced concrete skyscraper built 1904, once Dayton's tallest. Originally United Brethren HQ, Wright Brothers connection (father Milton was bishop). Chicago Commercial style. Long vacant. Renovation plans for 200 apartments announced."
    },
    {
        "address": "800 W Third St, Dayton, OH 45402",
        "lat": "39.756776", "lon": "-84.208214",
        "city": "Dayton", "state": "OH", "zip": "45402",
        "type": "COMMERCIAL", "status": "PROBABLY VACANT",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/800+W+Third+St,+Dayton,+OH+45402/@39.756776,-84.208214,17z",
        "source": "https://www.daytondailynews.com/news/special-reports/what-next-for-this-empty-building-dayton-west-side/XCTlB0gHn2G7729wb1IpNO/",
        "notes": "Central Motors Building. Built 1926 as Oldsmobile dealership. Outside Wright Dunbar Historic Business District. Owned by Wright Dunbar Inc. since 2010. Vacant commercial building."
    },
    # === JACKSON, MS (0 -> 1 entry — state #22: Mississippi) ===
    {
        "address": "2600 Belvedere Dr, Jackson, MS 39204",
        "lat": "32.268410", "lon": "-90.227218",
        "city": "Jackson", "state": "MS", "zip": "39204",
        "type": "RESIDENTIAL", "status": "CONDEMNED",
        "owner": "", "assessment": "",
        "link": "https://www.google.com/maps/place/2600+Belvedere+Dr,+Jackson,+MS+39204/@32.268410,-90.227218,17z",
        "source": "https://www.wlbt.com/2026/03/25/this-is-something-that-can-be-controlled-two-schools-located-near-dilapidated-jackson-apartment-complex/",
        "notes": "Belvedere Manor Apartments. Condemned by City of Jackson, residents ordered to vacate Mar 1 2025, demolition ordered Mar 13 2025. Demolition not yet completed as of Mar 2026. Squatters and illegal dumping reported. Near Key Elementary. Est. $500K to demolish."
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
