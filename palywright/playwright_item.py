from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    print('页面标题', page.title())

    # 内置的强制等待方法，毫秒为单位（等待10s）
    page.wait_for_timeout(10000)
