from playwright.sync_api import Playwright, sync_playwright
import json


def run(playwright_demo: Playwright) -> None:
    browser = playwright_demo.chromium.launch(headless=False)

    # 加载状态
    with open("state.json") as f:
        storage_state = json.loads(f.read())
    context = browser.new_context(storage_state=storage_state)

    # Open new page
    page = context.new_page()

    # Go to http://www.glidedsky.com/login
    page.goto("http://www.glidedsky.com/")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)