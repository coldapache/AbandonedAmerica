"""Screenshot KC batch 5 candidates via Playwright."""
import asyncio
from playwright.async_api import async_playwright

candidates = [
    {"name": "6412_E_15th_Ter", "lat": 39.09285, "lon": -94.50721},
    {"name": "1511_E_18th_St", "lat": 39.09124, "lon": -94.56387},
    {"name": "613_Forest_Ave", "lat": 39.10645, "lon": -94.56822},
    {"name": "6020_E_16th_St", "lat": 39.09208, "lon": -94.51151},
    {"name": "2836_White_Ave", "lat": 39.0733, "lon": -94.51343},
    {"name": "5209_E_12th_St", "lat": 39.09784, "lon": -94.52161},
    {"name": "2922_Spruce_Ave", "lat": 39.07204, "lon": -94.53311},
    {"name": "4145_Forest_Ave", "lat": 39.05079, "lon": -94.57112},
    {"name": "3400_Hardesty_Ave", "lat": 39.0633, "lon": -94.52085},
    {"name": "4032_Oakley_Ave", "lat": 39.05028, "lon": -94.5199},
    {"name": "5325_Chestnut_Ave", "lat": 39.02901, "lon": -94.55271},
    {"name": "3705_E_9th_St", "lat": 39.10207, "lon": -94.53883},
    {"name": "5014_South_Benton_Ave", "lat": 39.03468, "lon": -94.5512},
    {"name": "4420_Wayne_Ave", "lat": 39.04578, "lon": -94.56576},
    {"name": "3912_Myrtle_Ave", "lat": 39.05423, "lon": -94.53749},
    {"name": "3501_E_26th_St", "lat": 39.07853, "lon": -94.54191},
    {"name": "3004_E_49th_St", "lat": 39.03716, "lon": -94.54925},
    {"name": "3736_Broadway_Blvd", "lat": 39.05998, "lon": -94.5912},
    {"name": "3543_Prospect", "lat": 39.06107, "lon": -94.55291},
    {"name": "2914_E_40th_St", "lat": 39.05348, "lon": -94.54948},
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
                await page.screenshot(path=f"sv_screenshots/kc5_{c['name']}.png")
                print(f"    -> saved")
            except Exception as e:
                print(f"    -> ERROR: {e}")
        await browser.close()
        print("Done!")

asyncio.run(main())
