"""Geocode KC batch 4 + user submissions."""
import json, time, urllib.request, urllib.parse

addresses = [
    "6412 E 15th Ter, Kansas City, MO",
    "1511 E 18th St, Kansas City, MO",
    "613 Forest Ave, Kansas City, MO",
    "6020 E 16th St, Kansas City, MO",
    "2836 White Ave, Kansas City, MO",
    "5209 E 12th St, Kansas City, MO",
    "2922 Spruce Ave, Kansas City, MO",
    "4145 Forest Ave, Kansas City, MO",
    "4032 Oakley Ave, Kansas City, MO",
    "5325 Chestnut Ave, Kansas City, MO",
    "3705 E 9th St, Kansas City, MO",
    "5014 South Benton Ave, Kansas City, MO",
    "3912 Myrtle Ave, Kansas City, MO",
    "3501 E 26th St, Kansas City, MO",
    "3004 E 49th St, Kansas City, MO",
    "3543 Prospect Ave, Kansas City, MO",
    "2914 E 40th St, Kansas City, MO",
    "262 Old Gate Ln, Milford, CT",
    "1074 Latham St, Memphis, TN",
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
                results.append({"address": addr, "zip": zip_code,
                    "lat": round(coords["y"], 6), "lon": round(coords["x"], 6), "matched": matched})
            else:
                print(f"  {addr} -> NO MATCH")
                results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    except Exception as e:
        print(f"  {addr} -> ERROR: {e}")
        results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    time.sleep(0.3)

with open("kc4_zips.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nDone! {len(results)} results saved.")
