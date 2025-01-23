from playwright.sync_api import sync_playwright
"""
context常用操作

context.pages :获取context所有page对象

context.new_page():生成一个新的page对象

context.close()：关闭context

context.add_cookies()：将cookie添加到此浏览器上下文中。此上下文中的所有页面都将安装这些cookie。

只能传入列表

List[{name: str, value: str, url: Union[str, None], domain: Union[str, None], path: Union[str, None], expires: Union[float, None]

context.clear_cookies()：清除context的cookie

context.grant_permissions()：授予浏览器上下文的指定权限，具体见api

context.clear_permissions()：清除授权
"""
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://www.baidu.com')
    print('页面标题', page.title())

    # 内置的强制等待方法，毫秒为单位（等待10s）
    page.wait_for_timeout(10000)
