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

### Philadelphia, PA (Philadelphia County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Office of Property Assessment (OPA)** | https://property.phila.gov/ | Owner, assessed value, property details, exterior condition ratings (1-7 scale, 7=worst). |
| **OPA Bulk Data / CARTO API** | https://phl.carto.com/api/v2/sql?q=SELECT * FROM opa_properties_public WHERE location='ADDRESS' | Programmatic access to all OPA property data. Filter by exterior_condition, zip_code, category. |
| **OPA Bulk CSV Download** | https://www.phila.gov/property/data/ | Full CSV/GeoJSON/SHP download of all property assessments. |
| **L&I Code Violations** | https://opendataphilly.org/datasets/licenses-and-inspections-code-violations/ | Violations from Dept of Licenses & Inspections — unsafe structures, condemned buildings. |
| **Abandoned Philadelphia (blog)** | https://abandonedphiladelphia.com/properties/ | Community-reported shell properties, vacant lots, tax delinquent properties. Categories: shell-properties, vacant-land, tax-delinquency. |
| **Philadelphia Atlas** | https://atlas.phila.gov/ | Geocoded address lookup with zoning, ownership, permits, violations. |

**Pro tip:** Query the CARTO API for `exterior_condition IN ('6','7')` to find properties rated in worst condition by city assessors. Filter out `building_code_description LIKE 'VACANT%'` to exclude empty lots. This yields hundreds of confirmed blighted buildings with official data.

### Memphis, TN (Shelby County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Shelby County Land Bank** | https://landbank.shelbycountytn.gov/ | Interactive map of tax-delinquent and abandoned properties in Shelby County. Searchable by address and parcel. |
| **Memphis Metropolitan Land Bank Authority (MMLBA)** | https://mmlba.org/property-sales/ | City land bank acquiring and disposing blighted properties for redevelopment. Property sales listings. |
| **Memphis Property Hub (DataMidSouth)** | https://info.datamidsouth.org | Vacancy, code enforcement, tax delinquency dashboard. Aggregates multiple city/county data sources into searchable interface. |
| **Downtown Memphis Commission** | https://downtownmemphis.com | Downtown revitalization updates, commercial vacancy monitoring, development pipeline tracking. |
| **Shelby County Assessor** | https://assessor.shelby.tn.us/ | Property assessments, ownership, tax records for all Shelby County parcels. |

### Reading, PA (Berks County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Certified Blighted Properties** | https://www.readingpa.gov/certified-blighted-properties | **400+ city-certified blighted properties** with downloadable Excel (`Blight_List_for_City_Website.xlsx`). Each row: address, owner + mailing address, certification date, room count, Res/Comm flag. Gold-standard source — city has formally certified each property as blighted. |
| **Berks County Assessor** | https://www.berkspa.gov/departments/assessment-office | Owner names, assessed values, parcel data for cross-referencing the blight list. |

### Erie, PA (Erie County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Erie Land Bank** | https://www.erielandbank.org/properties | City land bank inventory. Mostly vacant land from prior demolitions (filter out per Rule #11) plus a few standing structures available for development. |
| **Erie County Land Bank** | https://www.eriecountylandbank.org/ | Countywide land bank — separate from city land bank. Covers surrounding municipalities. |
| **Erie County Real Estate Tax Office** | https://eriecountypa.gov/departments/real-estate-tax-office/ | Tax delinquent property search, assessment lookups. |

### Scranton, PA (Lackawanna County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Lackawanna County Land Bank** | http://www.lackawannalandbank.com/properties/ | **~200 properties** in searchable inventory (filter by address, type, municipality, value). Mix of vacant lots and standing structures — verify each via Street View before adding. |
| **Lackawanna County Assessment Office** | https://www.lackawannacounty.org/government/departments/assessor/ | Owner, assessed value, parcel data. |
| **Lackawanna County Tax Claim Bureau** | https://www.lackawannacounty.org/government/departments/tax_claim_bureau/ | Tax-delinquent property listings; correlates strongly with abandonment. |

### Chester, PA (Delaware County) — Receivership City

| Source | URL | What You Get |
|--------|-----|-------------|
| **Chester Receivership** | https://dced.pa.gov/local-government/act-47-financial-distress-program/cities-in-act-47/chester/ | Chester is in state receivership (only second PA city ever). Receiver publishes recovery plans referencing problem properties. |
| **Delaware County Assessor** | https://delcopa.gov/treasurer/index.html | Owner, assessed value, tax delinquency for Delaware County parcels. |
| **Chester Code Enforcement** | https://www.chestercity.com/departments/licensing-inspections/ | Code violation reporting; ask for condemned/unsafe structure lists via the department. |

### Bridgeport, CT (Fairfield County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Anti-Blight Division** | https://www.bridgeportct.gov/blight | Active anti-blight enforcement. As of March 2026, vacant blighted properties fined $250/day; the development administrator maintains an internal blighted-properties list. |
| **Cited for Blight** | https://www.bridgeportct.gov/government/departments/housing-code/anti-blight/cited-blight | Citation process info; the list of currently cited properties is not posted but can be requested via FOIA. |
| **Anti-Blight Ordinance (Ch. 8.76)** | https://library.municode.com/ct/bridgeport/codes/code_of_ordinances?nodeId=TIT8HESA_CH8.76ANIGPR_8.76.020DE | Legal definition of blight in Bridgeport. |
| **Bridgeport GIS / Assessor** | https://www.bridgeportct.gov/government/departments/finance/tax-assessor | Owner, assessed value, parcel data. |

### Hartford, CT (Hartford County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Blight Remediation Team** | https://www.hartfordct.gov/Government/Departments/DDS/DDS-Divisions/Blight-Remediation | City enforces Anti-Blight & Property Maintenance Ordinance against deteriorated occupied + vacant properties. **City reports 400+ vacant/abandoned properties citywide.** Public list not posted; request via department. |
| **Blight Lien Forbearance Program (PDF)** | https://www.hartfordct.gov/files/assets/public/v/1/development-services/licenses-inspections/li-documents/brt_lienforbearanceprogam.pdf | Identifies properties under blight liens. |
| **Hartford 20 Blighted Sites Story** | https://hartfordbusiness.com/article/hartford-identifies-20-blighted-sites-for-new-housing/ | City flagged 20 specific sites for housing redevelopment — paywalled, but addresses surface in news coverage. |
| **Hartford Land Bank** | https://www.hartfordlandbank.org/ | New land bank; conducting citywide property survey funded by Hartford Foundation. |
| **Hartford Assessor** | https://www.hartfordct.gov/Government/Departments/Assessor | Owner, assessed value, parcel data. |

### New Haven, CT (New Haven County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Livable City Initiative (LCI)** | https://www.newhavenct.gov/government/departments-divisions/livable-city-initiative | LCI enforces anti-blight ordinance, monitors building licensing. Mobile pop-up offices take blight complaints. List not posted publicly. |
| **Housing Code Enforcement** | https://www.newhavenct.gov/government/departments-divisions/livable-city-initiative/housing-code-enforcement | Code enforcement info; ask department for current cited-properties list. |
| **New Haven Open Data** | https://data.newhavenct.gov/ | Open data portal — search for code violations, blight citations datasets. |
| **New Haven Assessor** | https://www.newhavenct.gov/government/departments-divisions/assessors-office | Owner, assessed value, parcel data. |

### Providence, RI (Providence County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Providence Inspections — Blight Confirmation** | https://www.providenceri.gov/inspection/rhode-island-housing-acquisition-and-revitalization-program/ | City confirms whether properties meet HUD blight definition (failing HUD Housing Quality Standards or unsafe). Used to qualify properties for RI Housing Acquisition & Revitalization Program (ARP). |
| **RIHousing ARP-Funded Properties** | https://www.rihousing.com/rihousing-funding-approvals-revitalize-blighted-and-vacant-properties/ | Press releases naming specific blighted properties receiving state revitalization funding. |
| **Providence Tax Assessor** | https://www.providenceri.gov/assessor/ | Owner, assessment, parcel data. |
| **Providence Open Data** | https://data.providenceri.gov/ | Open data portal — search for code violations, demolitions, vacant building registry datasets. |

### Westerly, RI (Washington County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Inventory of Abandoned Properties** | https://www.westerlyri.gov/839/Inventory-of-Abandoned-Properties | Town Clerk's published inventory of abandoned properties. Small list, but every entry is town-certified. |

### Pawtucket / Woonsocket, RI

| Source | URL | What You Get |
|--------|-----|-------------|
| **Pawtucket Planning & Development** | https://www.pawtucketri.com/departments/planning-and-redevelopment | Tracks redevelopment of blighted sites (e.g., 71 Dexter St / Dexter Street Commons). |
| **Woonsocket Building & Zoning** | https://www.woonsocketri.org/building-zoning | Code enforcement contact for blight inquiries; ask for unsafe-structures list. |
| **RI Vacant Properties Commission Report (PDF)** | https://www.rilegislature.gov/commissions/VPC/commdocs/02-13-2023---DOA%20Vacant%20Property%20Commission%20FINAL.pdf | State-level analysis of vacant property in RI, includes data on Pawtucket / Woonsocket / Central Falls. |

### Massachusetts — Statewide Receivership

| Source | URL | What You Get |
|--------|-----|-------------|
| **MA Abandoned Housing Initiative (AHI)** | https://www.mass.gov/abandoned-housing-initiative-ahi | Attorney General's program that petitions courts to appoint receivers for vacant/abandoned housing across the state. Active in all Gateway Cities. **Court filings list specific addresses.** |
| **AHI Receivership Manual (PDF)** | https://www.mass.gov/files/documents/2016/08/uc/ahi-manual.pdf | Process documentation; references how cases are identified and tracked. |
| **MassLandRecords** | https://www.masslandrecords.com/ | All MA registries of deeds searchable here — confirms owner, sale history. |
| **MassGIS Parcels** | https://www.mass.gov/info-details/massgis-data-property-tax-parcels | Statewide parcel data with assessor-keyed attributes (owner, use code, value). |

### Springfield, MA (Hampden County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Office of Housing** | https://www.springfield-ma.gov/housing/ | Runs City of Homes program transferring distressed vacant properties to nonprofits for rehab. |
| **Code Enforcement / Receivership** | https://www.springfield-ma.gov/cos/housing-services/ | Springfield initiates more receivership actions than any MA city. Receiver-assigned properties surface in court filings. |
| **Hampden County Registry of Deeds** | https://www.masslandrecords.com/Hampden/ | Owner, sale history. |

### Holyoke, MA (Hampden County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Building Department** | https://www.holyoke.org/departments-services/building-department/ | Emergency-action lists for abandoned properties posing fire/safety threats. |
| **Office of Planning & Economic Development** | https://www.holyoke.org/departments-services/planning-and-development/ | Tracks redevelopment of mill-district blight (Lyman Mills, Open Square area). |

### Worcester / Lawrence / Lowell / Fall River / New Bedford, MA (Gateway Cities)

| Source | URL | What You Get |
|--------|-----|-------------|
| **MassDevelopment TDI** | https://www.massdevelopment.com/what-we-offer/key-initiatives/tdi | Transformative Development Initiative districts in Chelsea, Chicopee, Fall River, Fitchburg, Lawrence, Springfield, Worcester — published target-property lists by district. |
| **Worcester Inspectional Services** | https://www.worcesterma.gov/inspections | Problem property complaints; ask for active condemnation list. |
| **Lawrence Inspectional Services** | https://www.cityoflawrence.com/departments/inspectional-services | Vacant/abandoned building reporting. |
| **Lowell Department of Inspectional Services** | https://www.lowellma.gov/170/Department-of-Inspectional-Services | Code enforcement and unsafe structure tracking. |
| **Fall River Inspectional Services** | https://www.fallriverma.org/departments/inspectional-services/ | Vacant/condemned property tracking; large mill-district inventory. |
| **New Bedford Inspectional Services** | https://www.newbedford-ma.gov/inspectional-services/ | Code enforcement; many former waterfront industrial sites. |

### Elizabeth City, NC (Pasquotank County)

| Source | URL | What You Get |
|--------|-----|-------------|
| **Pasquotank County Parcel Search** | https://www.pasquotankcountync.org/tcs | Property assessments searchable by address, owner, or parcel number. |
| **Pasquotank County GIS** | https://www.arcgis.com/apps/Viewer/index.html?appid=7155a34043534443aaaa3fed8f8a492e | Interactive parcel map with boundaries and property data. |
| **Pasquotank Delinquent Taxes** | https://www.pasquotankcountync.org/delinquent-taxes | Tax lien notices listing delinquent property owners and parcel numbers. |
| **Elizabeth City Code Enforcement** | https://elizabethcitync.gov/index.asp?SEC=653B1CA7-43A7-4675-B83B-40840B293FB5 | Report nuisance properties, code violations, complaint process. |
| **Elizabeth City Code of Ordinances** | https://codelibrary.amlegal.com/codes/elizabethcity/latest/elizabeth_nc/0-0-0-2 | Full municipal code including minimum housing standards (Ch. 150). |
| **NC DPS (State)** | https://www.ncdps.gov/ | State-level press releases on nuisance abatement cases (e.g., Whistling Pines Motel). |

---

## Tips for Agents

1. **Always record your source URL** in the `source` column when adding properties.
2. **Official government sources are best.** A condemned list from a city website is stronger than a LoopNet listing.
3. **The assessor is your friend.** Almost every county has one online. It gives you owner, assessment, and property type — three columns filled from one source.
4. **NETR Online is the master directory.** If you don't know where to start for a county, go to https://publicrecords.netronline.com/ and find the county.
5. **Stack your sources.** A property found on a condemned list, confirmed via the assessor, and visually verified on Google Maps is rock-solid data.
6. **If you can't find a source, say so.** Leave the `source` column empty rather than linking to something irrelevant. Properties without sources are candidates for the `/repair-data` command later.
