# Sources Guide

Where to find data on abandoned, blighted, and vacant properties. This guide is organized from national down to local. AI agents should use these sources when researching properties for any area.

---

## National Sources

These apply everywhere in the US.

### Property Records & Parcel Data

| Source | URL | What You Get |
|--------|-----|-------------|
| **Regrid** | https://app.regrid.com/ | Nationwide parcel data, ownership, boundaries. Free tier available. |
| **NETR Online** | https://publicrecords.netronline.com/ | Directory of every county's assessor, recorder, and tax office websites. Start here to find the right local portal. |
| **Parcel-Viewer.us** | https://www.parcel-viewer.us/ | Directory of free government parcel viewers by county. Enter an address and get directed to the official local GIS. |
| **LoopNet** | https://www.loopnet.com/ | Commercial property listings. Great for finding vacant commercial/industrial/retail buildings. Often has owner, assessment, and vacancy info. |
| **Zillow / Redfin / Trulia** | https://www.zillow.com/ | Residential property data. Long-listed or off-market properties may indicate vacancy. |

### Vacancy & Abandonment Data

| Source | URL | What You Get |
|--------|-----|-------------|
| **HUD USPS Vacant Address Data** | https://www.huduser.gov/portal/datasets/usps.html | Quarterly vacancy data from USPS mail carriers. Addresses vacant 90+ days. Aggregated by Census tract. Available to government and nonprofits. |
| **USPS Occupancy Trends** | https://postalpro.usps.com/ot | Aggregate vacant address counts by ZIP code, carrier route, county. |
| **Data.gov** | https://catalog.data.gov/dataset/?tags=abandoned-properties | Federal open data tagged "abandoned properties." Datasets vary by agency and locality. |
| **HUD USER Research** | https://www.huduser.gov/portal/periodicals/em/winter14/highlight1.html | HUD policy research on vacant/abandoned properties — useful for understanding the landscape. |

### Visual Verification

| Source | URL | What You Get |
|--------|-----|-------------|
| **Google Maps / Street View** | https://www.google.com/maps | Ground-level visual confirmation of property condition. Check multiple Street View dates when available. |
| **Google Earth** | https://earth.google.com/ | Historical satellite imagery via time slider. Compare a property across years to confirm long-term vacancy/deterioration. |

---

## How to Find Local Sources for Any City/County

Every city and county has different portals. Here's the search playbook:

### Step 1: Find the Assessor/GIS Portal

Search for:
```
"[county name] [state] property tax records"
"[county name] [state] GIS parcel viewer"
"[county name] [state] assessor property search"
```

This gets you owner names, assessed values, property details, and sale history.

### Step 2: Find Condemned/Blighted Property Lists

Search for:
```
"[city] condemned properties list"
"[city] blighted properties"
"[city] nuisance properties"
"[city] vacant property registry"
"[city] code enforcement demolition list"
site:[city].gov condemned
```

Many cities publish official PDFs or web pages listing condemned/nuisance properties. These are the highest-quality sources — if a city says a property is condemned, that's authoritative.

### Step 3: Find Code Enforcement / Violations Data

Search for:
```
"[city] code enforcement violations"
"[city] open data" violations OR complaints
"[city] property maintenance enforcement"
```

Some cities have open data portals (Socrata, ArcGIS Hub) with searchable violation records.

### Step 4: Find Tax Delinquent / Lien Properties

Search for:
```
"[county] tax delinquent properties"
"[county] tax lien sale list"
"[county] delinquent real estate taxes"
```

Tax-delinquent properties often correlate with abandonment.

### Step 5: Check Local News

Search for:
```
"[city] abandoned buildings"
"[city] blight" demolition
"[address] condemned"
```

Local journalists often cover the worst abandoned properties and demolition plans.

---

## Example: Virginia / Hampton Roads

These are examples of what you'll find when you follow the playbook above. Every state and locality will have equivalents.

### State Level

| Source | URL | What You Get |
|--------|-----|-------------|
| **Virginia Mercury** | https://virginiamercury.com/ | Investigative journalism covering blight and abandonment across Virginia. |
| **DHCD Downtown Revitalization** | https://www.dhcd.virginia.gov/downtown-revitalization | Virginia's Department of Housing & Community Development programs for blighted areas. |

### Regional (Hampton Roads)

| Source | URL | What You Get |
|--------|-----|-------------|
| **HRGEO** | https://www.hrgeo.org/ | Hampton Roads regional GIS data exchange. Parcel data for the region. |

### City of Hampton

| Source | URL | What You Get |
|--------|-----|-------------|
| **Condemned Properties List** | https://www.hampton.gov/DocumentCenter/View/100/condemned_properties | Official city list of condemned/public nuisance properties. Updated periodically. |
| **Assessor of Real Estate** | https://www.hampton.gov/235/Assessor-of-Real-Estate | Owner names, assessed values, property details. |
| **GIS Parcel Viewer** | http://webgis.hampton.gov/sites/ParcelViewer/ | Interactive map with parcel boundaries, zoning, ownership. |
| **Property Maintenance & Zoning** | https://www.hampton.gov/259/Property-Maintenance-Zoning-Enforcement | Code enforcement info, complaint process, property standards. |
| **Code Violations Map** | https://www.hampton.gov/3332/Maps-of-recent-inspections-codes-violati | Interactive maps of recent permits, inspections, and code violations. |
| **King Street Corridor Plan** | https://www.hampton.gov/515/King-Street | Master plan for the N King St corridor — acknowledges need for revitalization. |
| **Brownfields** | https://www.hampton.gov/2107/Brownfields | EPA-funded brownfield assessments covering 100+ acres in Hampton. |

---

## Tips for Agents

1. **Always record your source URL** in the `source` column when adding properties.
2. **Official government sources are best.** A condemned list from a city website is stronger than a LoopNet listing.
3. **The assessor is your friend.** Almost every county has one online. It gives you owner, assessment, and property type — three columns filled from one source.
4. **NETR Online is the master directory.** If you don't know where to start for a county, go to https://publicrecords.netronline.com/ and find the county.
5. **Stack your sources.** A property found on a condemned list, confirmed via the assessor, and visually verified on Google Maps is rock-solid data.
6. **If you can't find a source, say so.** Leave the `source` column empty rather than linking to something irrelevant. Properties without sources are candidates for the `/repair-data` command later.
