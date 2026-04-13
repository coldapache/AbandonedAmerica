"""Screenshot KC batch 4 candidates via Playwright."""
import asyncio
from playwright.async_api import async_playwright

candidates = [
    {"name": "1218_Bennington_Ave", "lat": 39.09663, "lon": -94.50541},
    {"name": "3611_Bellaire_Ave", "lat": 39.05907, "lon": -94.51526},
    {"name": "1212_Collins", "lat": 39.0973, "lon": -94.52102},
    {"name": "2410_E_26th_St", "lat": 39.07901, "lon": -94.55421},
    {"name": "1702_E_41st_St", "lat": 39.05217, "lon": -94.5639},
    {"name": "1748_Euclid", "lat": 39.09171, "lon": -94.55874},
    {"name": "1624_Lister_Ave", "lat": 39.0913, "lon": -94.52683},
    {"name": "3118_E_Linwood_Blvd", "lat": 39.06783, "lon": -94.54632},
    {"name": "4836_E_9th_St", "lat": 39.10165, "lon": -94.52427},
    {"name": "3513_Roberts_St", "lat": 39.1068, "lon": -94.5397},
    {"name": "5209_Norton_Ave", "lat": 39.03095, "lon": -94.53757},
    {"name": "6513_E_12th_St", "lat": 39.09739, "lon": -94.50576},
    {"name": "3336_Chestnut_Ave", "lat": 39.06488, "lon": -94.55077},
    {"name": "220_N_Clinton_Pl", "lat": 39.11475, "lon": -94.53411},
    {"name": "2428_Denver_Ave", "lat": 39.08066, "lon": -94.52233},
    {"name": "801_Gladstone_Ave", "lat": 39.10319, "lon": -94.54606},
    {"name": "5301_Prospect_Ave", "lat": 39.02989, "lon": -94.55497},
    {"name": "5829_Bellefontaine_Ave", "lat": 39.01976, "lon": -94.54989},
]

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        for c in candidates:
            addr = c["name"].replace("_", " ")
            url = f"https://www.google.com/maps/place/{c['name'].replace('_', '+')},+Kansas+City,+MO/@{c['lat']},{c['lon']},18z"
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
                await page.screenshot(path=f"sv_screenshots/kc4_{c['name']}.png")
                print(f"    -> saved")
            except Exception as e:
                print(f"    -> ERROR: {e}")
        await browser.close()
        print("Done!")

asyncio.run(main())
