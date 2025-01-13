import pytest
import re
from playwright.sync_api import Page, expect, sync_playwright


@pytest.fixture(scope="module")
def browser():
    # 初始化浏览器实例
    browser = sync_playwright().start()
    context = browser.new_context()
    yield context
    # 关闭浏览器实例
    browser.close()


def test_example(page: Page) -> None:  # 只有一个参数 page，它被注解为 Page 类型  -> None 表示这个函数没有返回值，即它的返回类型是 None
    page.goto(
        "http://cube-front.product.poc.za-tech.net/sso/login.html?service=za-cube&target=aHR0cDovL2N1YmUtZnJvbnQucHJvZHVjdC5wb2MuemEtdGVjaC5uZXQvbG9naW4%2FcmVkaXJlY3Q9L3NoaXAvcHVibGlzaC9wcm9qZWN0")
    page.get_by_placeholder("请输入账号").click()
    page.get_by_placeholder("请输入账号").fill("zawb-yanxing")
    page.get_by_role("button", name="登 录").click()
    page.get_by_text("请输入密码!").click()
    page.get_by_role("textbox", name="请输入密码").click()
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
