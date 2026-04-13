"""Screenshot KC batch 3 candidates via Playwright."""
import asyncio
from playwright.async_api import async_playwright

candidates = [
    {"name": "1227_Illinois_Ave", "lat": 39.09769, "lon": -94.54567, "case": "2025-00179"},
    {"name": "1912_E_18th_St", "lat": 39.09109, "lon": -94.55933, "case": "2025-00174"},
    {"name": "911_E_Linwood_Blvd", "lat": 39.06874, "lon": -94.57349, "case": "2021-00288"},
    {"name": "1510_E_19th_St", "lat": 39.08986, "lon": -94.56371, "case": "2021-00298"},
    {"name": "2509_Myrtle_Ave", "lat": 39.07979, "lon": -94.53623, "case": "2025-00196"},
    {"name": "3217_Troost_Ave", "lat": 39.06807, "lon": -94.57145, "case": "2025-00291"},
    {"name": "3037_Main", "lat": 39.07155, "lon": -94.5849, "case": "2025-00208"},
    {"name": "4810_E_7th_St", "lat": 39.10356, "lon": -94.52523, "case": "2025-00321"},
    {"name": "1219_Garfield_Ave", "lat": 39.09831, "lon": -94.55722, "case": "2025-00273"},
    {"name": "2900_Flora_Ave", "lat": 39.07377, "lon": -94.56538, "case": "2025-00046"},
    {"name": "5320_Highland_Ave", "lat": 39.02975, "lon": -94.56548, "case": "2024-00244"},
    {"name": "525_E_54th_St", "lat": 39.02866, "lon": -94.58055, "case": "2024-00190"},
    {"name": "4930_Woodland_Ave", "lat": 39.03663, "lon": -94.56391, "case": "2025-00309"},
    {"name": "126_N_Chelsea_Ave", "lat": 39.11367, "lon": -94.52444, "case": "2025-00058"},
    {"name": "2703_E_27th_St", "lat": 39.07705, "lon": -94.55102, "case": "2025-00229"},
    {"name": "704_Tracy_Ave", "lat": 39.10517, "lon": -94.56733, "case": "2025-00032"},
    {"name": "2515_MLK_Jr_Blvd", "lat": 39.03913, "lon": -94.5552, "case": "2023-00134"},
    {"name": "6916_Bales_Ave", "lat": 39.0006, "lon": -94.54627, "case": "2025-00301"},
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        for c in candidates:
            addr = c["name"].replace("_", " ")
            url = f"https://www.google.com/maps/place/{c['name'].replace('_', '+')},+Kansas+City,+MO/@{c['lat']},{c['lon']},3a,75y,0h,90t"
            print(f"  {addr}...")
            try:
                await page.goto(url, wait_until="domcontentloaded", timeout=20000)
                await page.wait_for_timeout(5000)
                for sel in ["button[aria-label='Accept all']", "button.dismissButton"]:
                    try:
                        btn = page.locator(sel).first
                        if await btn.is_visible(timeout=800):
                            await btn.click()
                            await page.wait_for_timeout(300)
                    except:
                        pass
                await page.wait_for_timeout(2000)
                path = f"sv_screenshots/kc3_{c['name']}.png"
                await page.screenshot(path=path)
                print(f"    -> saved")
            except Exception as e:
                print(f"    -> ERROR: {e}")

        await browser.close()
        print("Done!")

asyncio.run(main())
