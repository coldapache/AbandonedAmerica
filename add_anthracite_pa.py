"""Add verified Anthracite Coal Region PA properties to the CSV."""

import csv

CSV_PATH = "Abandoned America - Abandoned or Unused Properties.csv"

new_properties = [
    {
        "address": "134 N Main St, Shenandoah, PA 17976",
        "lat": "40.822295",
        "lon": "-76.201686",
        "city": "Shenandoah",
        "state": "PA",
        "zip": "17976",
        "type": "COMMERCIAL",
        "status": "ABANDONED",
        "owner": "",
        "assessment": "",
        "link": "https://www.google.com/maps/@40.8222906,-76.2016861,3a,75y,250h,90t/data=!3m7!1e1!3m5!1sPQvLlg5lWBHnmBIMWzvCrw!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3DPQvLlg5lWBHnmBIMWzvCrw%26yaw%3D250!7i16384!8i8192",
        "source": "https://cinematreasures.org/theaters/13285",
        "notes": "Capitol Theatre. Art Deco movie theater, opened 1947, closed 1980, seating 1,400. Upper floors have broken/missing windows; ground floor has marginal retail use. Second theater on this site after 1946 fire destroyed the original. Aug 2025 Street View confirms still standing.",
    },
    {
        "address": "115 W Cherry St, Shenandoah, PA 17976",
        "lat": "40.818447",
        "lon": "-76.202499",
        "city": "Shenandoah",
        "state": "PA",
        "zip": "17976",
        "type": "INSTITUTIONAL",
        "status": "CONDEMNED",
        "owner": "",
        "assessment": "",
        "link": "https://www.google.com/maps/@40.8182982,-76.2025198,3a,75y,0h,90t/data=!3m7!1e1!3m5!1sm018En96Po9Dz1wfoJIZBA!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3Dm018En96Po9Dz1wfoJIZBA%26yaw%3D0!7i16384!8i8192",
        "source": "https://www.redfin.com/PA/Shenandoah/115-W-Cherry-St-17976/home/191978521",
        "notes": "St. John's Evangelical Lutheran Church. Gothic stone church with stained glass, built c.1880s. Rectory at 119 W Cherry condemned by Shenandoah Boro. Property sold $25,000 Aug 2024. Broken window panes, signs of neglect. Aug 2025 Street View confirms still standing.",
    },
    {
        "address": "211 E Sunbury St, Shamokin, PA 17872",
        "lat": "40.793357",
        "lon": "-76.553372",
        "city": "Shamokin",
        "state": "PA",
        "zip": "17872",
        "type": "COMMERCIAL",
        "status": "ABANDONED",
        "owner": "",
        "assessment": "",
        "link": "https://www.google.com/maps/@40.7931773,-76.5533479,3a,75y,0h,90t/data=!3m7!1e1!3m5!1sPILkitABi9qR-00-2fZIfQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3DPILkitABi9qR-00-2fZIfQ%26yaw%3D0!7i16384!8i8192",
        "source": "https://www.northcentralpa.com/life/fire-guts-shamokin-winery/article_4ee4beee-00c9-11ef-9353-bb7e7a55a438.html",
        "notes": "Former Liberty Hose Company / Firehouse Winery. Late 19th century firehouse converted to winery 2016. Gutted by 2-alarm fire April 21, 2024; owner uninsured. Ground floor boarded with plywood, upper windows covered with PolyPro sheeting. Aug 2025 Street View confirms still standing as fire-damaged shell.",
    },
    {
        "address": "725 N Shamokin St, Shamokin, PA 17872",
        "lat": "40.793017",
        "lon": "-76.550870",
        "city": "Shamokin",
        "state": "PA",
        "zip": "17872",
        "type": "MIXED USE",
        "status": "CONDEMNED",
        "owner": "HUSSAM ELAYYAN",
        "assessment": "",
        "link": "https://www.google.com/maps/@40.7930969,-76.5509063,3a,75y,180h,90t/data=!3m7!1e1!3m5!1sSX-e_09ESb_w-1jn0FcCVQ!2e0!6shttps:%2F%2Fstreetviewpixels-pa.googleapis.com%2Fv1%2Fthumbnail%3Fcb_client%3Dmaps_sv.tactile%26w%3D900%26h%3D600%26pitch%3D0%26panoid%3DSX-e_09ESb_w-1jn0FcCVQ%26yaw%3D180!7i16384!8i8192",
        "source": "https://www.newsitem.com/news/local/police-file-misdemeanors-against-owner-of-alleged-dilapidated-apartment-building-in-shamokin/article_e076de1b-d2d0-424f-8607-ac0778fde5be.html",
        "notes": "Three-story mixed-use building. All ground-floor openings boarded with plywood, upper windows broken/missing. Owner (Philadelphia, PA) charged with misdemeanor public nuisance for decay and deterioration. Adjacent to Domino's site. Aug 2025 Street View confirms abandoned.",
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
