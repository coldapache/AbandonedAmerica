import csv

NEW_PROPERTIES = [
    # === CASPER, WY (0 -> 1 entry — NEW STATE #38: Wyoming) ===
    {
        "address": "300 W F St, Casper, WY 82601",
        "lat": "42.857322", "lon": "-106.328020",
        "city": "Casper", "state": "WY", "zip": "82601",
        "type": "HOSPITALITY", "status": "CONDEMNED",
        "owner": "F STREET REHAB LLC",
        "assessment": "",
        "link": "https://www.google.com/maps/place/300+W+F+St,+Casper,+WY+82601/@42.857322,-106.328020,17z",
        "source": "https://oilcity.news/community/2023/06/29/photos-casper-hotel-condemned-after-sweep-reveals-flooding-squatters-%EF%BF%BC/",
        "notes": "Former Econo Lodge motel. Built 1964, 123,115 sqft, 200 rooms, 5.77 acres. Closed after pipes burst and flooding Nov 2022. City condemned Jun 2023 after sweep found squatters and severe damage. 200+ squatters caused millions in damage; 500 lbs of human waste reported. Boarded up. Purchased by F Street Rehab LLC (Sheridan WY) for planned rehabilitation as Riverside Hotel & Conference Center. Parcel 33790420100600 per Natrona County Assessor."
    },
    # === WICHITA, KS (0 -> 1 entry — NEW STATE #39: Kansas) ===
    {
        "address": "2747 Boulevard Plz, Wichita, KS 67211",
        "lat": "37.670957", "lon": "-97.305227",
        "city": "Wichita", "state": "KS", "zip": "67211",
        "type": "RETAIL", "status": "ABANDONED",
        "owner": "BOULEVARD PLAZA LLC",
        "assessment": "$331,000",
        "link": "https://www.google.com/maps/place/2747+Boulevard+Plz,+Wichita,+KS+67211/@37.670957,-97.305227,17z",
        "source": "https://ssc.sedgwickcounty.org/propertytax/realproperty.aspx?pin=30015144",
        "notes": "Boulevard Plaza Shopping Center. Opened 1951, designed by architect S.S. Platt. Community shopping hub for decades. Shuttered ~2019. Renovation attempt stalled by stop-work order for missing permits; further damaged by vandalism. Three outer buildings auctioned Mar 2023. Economic Class D+ (poor condition). 10,676 sqft retail, 0.62 acres. Appraised $331,000 per Sedgwick County 2026. PIN 30015144."
    },
    # === LAS VEGAS, NV (0 -> 1 entry — NEW STATE #40: Nevada) ===
    {
        "address": "899 Fremont St, Las Vegas, NV 89101",
        "lat": "36.167270", "lon": "-115.136197",
        "city": "Las Vegas", "state": "NV", "zip": "89101",
        "type": "HOSPITALITY", "status": "VACANT",
        "owner": "899 FREMONT L L C",
        "assessment": "$7,739,480",
        "link": "https://www.google.com/maps/place/899+Fremont+St,+Las+Vegas,+NV+89101/@36.167270,-115.136197,17z",
        "source": "https://maps.clarkcountynv.gov/assessor/AssessorParcelDetail/parceldetail.aspx?hdnParcel=13934612056",
        "notes": "Western Hotel & Casino. Built 1970, casino/hotel on 1.36 acres with 300 ft Fremont St frontage. Closed Jan 2012. Hotel portion demolished 2013; casino building still standing. Purchased Mar 2013 by Tony Hsieh's Downtown Project for $14M (multi-parcel). Estate (via 899 Fremont LLC) marketing for sale since Mar 2024 via Logic Commercial Real Estate. Taxable value $7,739,480 (assessed $2,708,818 at 35%) per Clark County Assessor FY2026-27. Parcel 139-34-612-056."
    },
    # === OGDEN, UT (0 -> 1 entry — NEW STATE #41: Utah) ===
    {
        "address": "600 Exchange Rd, Ogden, UT 84401",
        "lat": "41.226605", "lon": "-111.996304",
        "city": "Ogden", "state": "UT", "zip": "84401",
        "type": "COMMERCIAL", "status": "ABANDONED",
        "owner": "OGDEN CITY REDEVELOPMENT AGENCY",
        "assessment": "$799,634",
        "link": "https://www.google.com/maps/place/600+Exchange+Rd,+Ogden,+UT+84401/@41.226605,-111.996304,17z",
        "source": "https://webercountyutah.gov/parcelsearch/current-taxes.php?id=141390002",
        "notes": "Ogden Union Stockyard Exchange Building. Art Deco landmark designed by Leslie S. Hodgson, completed 1931. Features cast stone livestock heads (bulls, sheep, hogs) and geometric brick pilasters. 15,280 sqft, 1.81 acres. Long vacant. Purchased by Ogden City 2013; deterioration accelerated since. Preservation Utah 2025 Most Endangered list. City RFP for redevelopment Sep 2024 received no feasible submissions. At risk of demolition per Jan 2025 Landmarks Commission. Market value $799,634 (tax exempt, govt-owned) per Weber County 2025. Parcel 141390002."
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
