"""Geocode user-submitted Philadelphia properties."""
import json, time, urllib.request, urllib.parse

addresses = [
    "3310 Fox St, Philadelphia, PA",
    "2412 W Hunting Park Ave, Philadelphia, PA",
    "3537 N 24th St, Philadelphia, PA",
    "2299 Ruffner St, Philadelphia, PA",
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

with open("philly_user_geocoded.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\nDone! {len(results)} results saved.")
