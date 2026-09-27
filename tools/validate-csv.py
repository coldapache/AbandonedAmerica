#!/usr/bin/env python
"""Validate the ABNC CSV against the CLAUDE.md schema rules."""
import csv, io, re, sys, collections

CSV = "Abandoned America - Abandoned or Unused Properties.csv"
STATUSES = {"ABANDONED", "CHRONICALLY VACANT", "CONDEMNED", "DEMOLISHED",
            "PROBABLY VACANT", "VACANT"}
TYPES = {"COMMERCIAL", "COMMERCIAL OFFICE", "HOSPITALITY", "INDUSTRIAL", "INSTITUTIONAL",
         "MIXED USE", "RESIDENTIAL", "RESTAURANT", "RETAIL", "WAREHOUSE"}
FIELDS = ["address", "lat", "lon", "city", "state", "zip", "type", "status", "owner",
          "assessment", "link", "source", "notes", "human_confirmed"]
STATES = set("AL AK AZ AR CA CO CT DE DC FL GA HI ID IL IN IA KS KY LA ME MD MA MI MN MS MO "
             "MT NE NV NH NJ NM NY NC ND OH OK OR PA RI SC SD TN TX UT VT VA WA WV WI WY".split())

raw = open(CSV, encoding="utf-8-sig").read()
rd = csv.DictReader(io.StringIO(raw, newline=""))
rows = list(rd)
err = collections.defaultdict(list)
warn = collections.defaultdict(list)

def bad(cat, addr, msg):
    err[cat].append("%s :: %s" % (addr, msg))

for i, r in enumerate(rows, start=2):
    a = (r.get("address") or "").strip()
    if not a:
        bad("empty address", "line %d" % i, ""); continue

    # required basics
    for f in ("city", "state", "zip", "type", "status", "lat", "lon"):
        if not (r.get(f) or "").strip():
            warn("missing %s" % f, a, "")

    # enums
    if r["status"] not in STATUSES:
        bad("invalid status", a, repr(r["status"]))
    if r["type"] not in TYPES:
        bad("invalid type", a, repr(r["type"]))

    # DEMOLISHED must not be present (rule 11)
    if r["status"] == "DEMOLISHED":
        bad("DEMOLISHED present", a, "")

    # coordinates
    try:
        lat = float(r["lat"]); lon = float(r["lon"])
        if not (24.0 <= lat <= 49.5):
            bad("lat out of range", a, lat)
        if not (-125.0 <= lon <= -66.5):
            bad("lon out of range", a, lon)
    except (TypeError, ValueError):
        bad("unparseable lat/lon", a, "%r/%r" % (r["lat"], r["lon"]))

    # en-dash trap (rule 5)
    if "\u2013" in r["lon"] or "\u2014" in r["lon"]:
        bad("en/em dash in lon", a, r["lon"])

    # state valid
    if r["state"] not in STATES:
        bad("invalid state", a, repr(r["state"]))

    # zip
    if not re.fullmatch(r"\d{5}", (r["zip"] or "").strip()):
        warn("zip not 5 digits", a, repr(r["zip"]))

    # link (rule 3)
    if not (r["link"] or "").startswith("https://"):
        warn("no https link", a, (r["link"] or "")[:60])

    # coords must be within the property's own city bounding box? (sanity, loose)
    if not r["link"]:
        warn("no link at all", a, "")

# duplicates
seen = collections.defaultdict(list)
for r in rows:
    k = re.sub(r"[.,]", "", re.sub(r"\s+", " ", r["address"].upper()).strip())
    seen[k].append(r)
dups = {k: v for k, v in seen.items() if len(v) > 1}
for k, v in dups.items():
    bad("duplicate address", k, "%d rows" % len(v))

# column order / count
if list(rd.fieldnames) != FIELDS:
    bad("column mismatch", "header", str(rd.fieldnames))

print("rows: %d   unique addresses: %d" % (len(rows), len(seen)))
print()
for cat, items in sorted(err.items(), key=lambda kv: -len(kv[1])):
    print("ERROR %-28s %4d" % (cat, len(items)))
    for s in items[:5]:
        print("        %s" % s)
if not err:
    print("no schema ERRORS")
print()
for cat, items in sorted(warn.items(), key=lambda kv: -len(kv[1])):
    print("warn  %-28s %4d   e.g. %s" % (cat, len(items), items[0] if items else ""))
sys.exit(1 if err else 0)
