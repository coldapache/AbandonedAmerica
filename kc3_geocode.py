"""Geocode KC batch 3 + Camden user submission."""
import json, time, urllib.request, urllib.parse

addresses = [
    "3611 Bellaire Ave, Kansas City, MO",
    "1212 Collins St, Kansas City, MO",
    "2410 E 26th St, Kansas City, MO",
    "1702 E 41st St, Kansas City, MO",
    "1624 Lister Ave, Kansas City, MO",
    "4836 E 9th St, Kansas City, MO",
    "3513 Roberts St, Kansas City, MO",
    "5209 Norton Ave, Kansas City, MO",
    "6513 E 12th St, Kansas City, MO",
    "3336 Chestnut Ave, Kansas City, MO",
    "2428 Denver Ave, Kansas City, MO",
    "801 Gladstone Ave, Kansas City, MO",
    "5301 Prospect Ave, Kansas City, MO",
    "5829 Bellefontaine Ave, Kansas City, MO",
    "519 County Rd 551, Camden, NJ",
]

results = []
for addr in addresses:
    url = "https://geocoding.geo.census.gov/geocoder/locations/onelineaddress?" + urllib.parse.urlencode({
        "address": addr, "benchmark": "Public_AR_Current", "format": "json"
    })
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read())
            matches = data.get("result", {}).get("addressMatches", [])
            if matches:
                m = matches[0]
                matched = m["matchedAddress"]
                coords = m["coordinates"]
                parts = matched.split(",")
                zip_code = parts[-1].strip().split()[-1] if parts else ""
                print(f"  {addr} -> ZIP {zip_code} (lat {coords['y']:.6f}, lon {coords['x']:.6f})")
                results.append({
                    "address": addr, "zip": zip_code,
                    "lat": round(coords["y"], 6), "lon": round(coords["x"], 6),
                    "matched": matched
                })
            else:
                print(f"  {addr} -> NO MATCH")
                results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    except Exception as e:
        print(f"  {addr} -> ERROR: {e}")
        results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    time.sleep(0.3)

with open("kc3_zips.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nDone! {len(results)} results saved.")
