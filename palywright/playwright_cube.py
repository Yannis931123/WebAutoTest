import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://cube-front.product.poc.za-tech.net/sso/login.html?service=za-cube&target=aHR0cDovL2N1YmUtZnJvbnQucHJvZHVjdC5wb2MuemEtdGVjaC5uZXQvbG9naW4%2FcmVkaXJlY3Q9L3NoaXAvcHVibGlzaC9wcm9qZWN0")
    page.get_by_placeholder("请输入账号").click()
    page.get_by_placeholder("请输入账号").fill("zawb-yanxing")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("请输入密码!").click()
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").press("CapsLock")
    page.get_by_role("textbox", name="请输入密码").fill("AAA")
    page.get_by_role("textbox", name="请输入密码").press("CapsLock")
    page.get_by_role("textbox", name="请输入密码").fill("AAAbbb111")
    page.get_by_role("button", name="登 录").click()
    expect(page.locator("body")).to_contain_text("用户名或者密码错误")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("1qaz@")
    page.get_by_role("textbox", name="请输入密码").press("CapsLock")
    page.get_by_role("textbox", name="请输入密码").fill("1qaz@WSX")
    page.get_by_role("textbox", name="请输入密码").press("CapsLock")
    page.get_by_role("button", name="登 录").click()
    expect(page.locator("#form")).to_contain_text("请输入账号!")
    page.get_by_placeholder("请输入账号").click()
    page.get_by_placeholder("请输入账号").fill("zawb-yanxing")
    page.get_by_role("button", name="登 录").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
