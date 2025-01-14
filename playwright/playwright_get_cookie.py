from playwright.sync_api import Playwright, sync_playwright
import json


def run(playwright_demo: Playwright) -> None:
    browser = playwright_demo.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://www.glidedsky.com/login
    page.goto("http://www.glidedsky.com/login")

    # Click input[name="email"]
    page.click("input[name=\"email\"]")

    # Fill input[name="email"]
    page.fill("input[name=\"email\"]", "账号")

    # Click input[name="password"]
    page.click("input[name=\"password\"]")

    # Fill input[name="password"]
    page.fill("input[name=\"password\"]", "密码")

    # Click button:has-text("Login")
    page.click("button:has-text(\"Login\")")
    # assert page.url == "http://www.glidedsky.com/"

    # 获得登录后 cookie
    storage = context.storage_state()
    with open("state.json", "w") as f:
        f.write(json.dumps(storage))

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
