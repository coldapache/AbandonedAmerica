"""Geocode KC batch 2 properties for ZIP codes."""
import json, time, urllib.request, urllib.parse

addresses = [
    "1640 Corrington Ave, Kansas City, MO",
    "1621 Cambridge Ave, Kansas City, MO",
    "2535 Montgall Ave, Kansas City, MO",
    "2313 Askew Ave, Kansas City, MO",
    "7409 E 49th St, Kansas City, MO",
    "2626 E 28th St, Kansas City, MO",
    "4400 E 24th St, Kansas City, MO",
    "8202 E Bannister Rd, Kansas City, MO",
    "5932 Prospect Ave, Kansas City, MO",
    "1199 Indiana Ave, Kansas City, MO",
    "3316 E 12th St, Kansas City, MO",
    "3007 E 12th St, Kansas City, MO",
    "1227 Illinois Ave, Kansas City, MO",
    "1912 E 18th St, Kansas City, MO",
    "3217 Troost Ave, Kansas City, MO",
    "3037 Main St, Kansas City, MO",
    "1219 Garfield Ave, Kansas City, MO",
    "2703 E 27th St, Kansas City, MO",
    "704 Tracy Ave, Kansas City, MO",
    "4810 E 7th St, Kansas City, MO",
    "1700 E Truman Rd, Kansas City, MO",
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
                    "address": addr,
                    "zip": zip_code,
                    "lat": round(coords["y"], 6),
                    "lon": round(coords["x"], 6),
                    "matched": matched
                })
            else:
                print(f"  {addr} -> NO MATCH")
                results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    except Exception as e:
        print(f"  {addr} -> ERROR: {e}")
        results.append({"address": addr, "zip": "", "lat": 0, "lon": 0, "matched": ""})
    time.sleep(0.3)

with open("kc2_zips.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nDone! {len(results)} results saved.")
