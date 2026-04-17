"""Add verified Mon Valley PA properties to the CSV."""

import csv

CSV_PATH = "Abandoned America - Abandoned or Unused Properties.csv"

new_properties = [
    {
        "address": "62 Market St, Brownsville, PA 15417",
        "lat": "40.022180",
        "lon": "-79.885740",
        "city": "Brownsville",
        "state": "PA",
        "zip": "15417",
        "type": "COMMERCIAL OFFICE",
        "status": "ABANDONED",
        "owner": "REDEVELOPMENT AUTH CO OF FAYETTE",
        "assessment": "$28,630",
        "link": "https://www.google.com/maps/@40.0224285,-79.8861382,3a,75y,180h,90t/data=!3m7!1e1!3m5!1szZHgry5i-_YyLkuRiGy8fg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3DzZHgry5i-_YyLkuRiGy8fg%26yaw%3D180!7i16384!8i6656",
        "source": "http://property.co.fayette.pa.us/detail.aspx?uxParid=02060157",
        "notes": "Second National Bank / Monongahela National Bank. Neoclassical bank building, built 1900, 5,840 sq ft. Boarded windows, completely abandoned. Sold to Redevelopment Authority for $1 in 2009. Part of Brownsville Commercial Historic District.",
    },
    {
        "address": "56 Market St, Brownsville, PA 15417",
        "lat": "40.022350",
        "lon": "-79.885960",
        "city": "Brownsville",
        "state": "PA",
        "zip": "15417",
        "type": "COMMERCIAL",
        "status": "ABANDONED",
        "owner": "REDEVELOPMENT AUTH CO OF FAYETTE",
        "assessment": "$59,950",
        "link": "https://www.google.com/maps/@40.0223549,-79.8863874,3a,75y,0h,90t/data=!3m7!1e1!3m5!1sxM3QSa-P-HINOCj2IbYMLg!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3DxM3QSa-P-HINOCj2IbYMLg%26yaw%3D0!7i16384!8i6656",
        "source": "http://property.co.fayette.pa.us/detail.aspx?uxParid=02060158",
        "notes": "Union Station / Monongahela Railway Building. Massive 5-story brick, built 1900, 36,093 sq ft. Completely boarded up, all entrances sealed. Sold to Redevelopment Authority for $1 in 2009. Former train station hosted 68 daily passenger trains at peak (1915). Oct 2023 Street View confirms still standing.",
    },
    {
        "address": "31 Market St, Brownsville, PA 15417",
        "lat": "40.022246",
        "lon": "-79.887098",
        "city": "Brownsville",
        "state": "PA",
        "zip": "15417",
        "type": "COMMERCIAL",
        "status": "ABANDONED",
        "owner": "33 MARKET STREET HOLDINGS LLC",
        "assessment": "$28,360",
        "link": "https://www.google.com/maps/place/31+Market+St,+Brownsville,+PA+15417/@40.021950,-79.885350,17z",
        "source": "http://property.co.fayette.pa.us/detail.aspx?uxParid=02060143",
        "notes": "Odd Fellows Building. Built 1876, 6,390 sq ft downtown row type. Absentee owner in Boca Raton, FL. Sold for $55,000 in Sept 2019. Part of Brownsville Commercial Historic District.",
    },
    {
        "address": "647 McKean Ave, Donora, PA 15033",
        "lat": "40.178400",
        "lon": "-79.856100",
        "city": "Donora",
        "state": "PA",
        "zip": "15033",
        "type": "MIXED USE",
        "status": "CONDEMNED",
        "owner": "DONORA BOROUGH",
        "assessment": "$65,500",
        "link": "https://www.google.com/maps/@40.1784056,-79.8561427,3a,75y,90h,90t/data=!3m7!1e1!3m5!1s6TKQ4pf8gCvBAWxi-kAGpw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3D6TKQ4pf8gCvBAWxi-kAGpw%26yaw%3D90!7i16384!8i6656",
        "source": "https://tyler.washcopa.org/pt/Datalets/Datalet.aspx?sIndex=1&idx=1",
        "notes": "Blighted downtown commercial building. Year built 1907, downtown row type, mixed retail/apartments. Lead-based paint found in environmental report. Borough received $90K demolition grant from DCED. Still standing as of Nov 2021 Street View.",
    },
    {
        "address": "618 McKean Ave, Donora, PA 15033",
        "lat": "40.178241",
        "lon": "-79.855875",
        "city": "Donora",
        "state": "PA",
        "zip": "15033",
        "type": "COMMERCIAL",
        "status": "CONDEMNED",
        "owner": "",
        "assessment": "",
        "link": "https://www.google.com/maps/place/618+McKean+Ave,+Donora,+PA+15033/@40.1782414,-79.8558745,17z",
        "source": "https://www.observer-reporter.com/news/local-news/2024/jul/13/donora-seeks-emergency-demolition-for-condemned-building/",
        "notes": "Condemned commercial building next to borough parking garage. Roof caved in through 3 floors per drone inspection. Emergency demolition authorized July 2024 but may still be standing. Out-of-state owner (NJ) reportedly bought on eBay for $6K. Exempt from tax rolls.",
    },
]

# Read existing CSV
with open(CSV_PATH, "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    headers = reader.fieldnames
    existing = list(reader)

# Check for duplicates
existing_addresses = {r["address"].lower().strip() for r in existing}
to_add = []
for prop in new_properties:
    if prop["address"].lower().strip() in existing_addresses:
        print(f"SKIP (duplicate): {prop['address']}")
    else:
        to_add.append(prop)
        print(f"ADD: {prop['address']}")

if not to_add:
    print("Nothing to add.")
else:
    # Append new rows
    all_rows = existing + to_add
    with open(CSV_PATH, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=headers, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"\nAdded {len(to_add)} properties. Total: {len(all_rows)}")
