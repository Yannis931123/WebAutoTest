# 实现basePage基类
# basePage基类的实现思想是不做过多的封装，尽量让测试人员直接使用selenium原装的方法，而不像其它框架一样什么都封装在这里面。
# 所以我对basePage的定义是：根据业务逻辑（测试用例）指定的元素，输入的数据，协助它完成元素定位和操作，仅此而已。
# 当然如果去封装各种东西也是可以的，直接在里面加就行了。

from selenium.webdriver.common.by import By
from selenium import webdriver
import os
import importlib
import logging

SimpleActions = ['clear()', 'send_keys()', 'click()', 'submit()', 'size', 'text', 'is_displayed()', 'get_attribute()']
logger = logging.getLogger('main.page')


class Page(object):

    def __init__(self, driver, page):
        self.driver = driver
        self.page = page
        self.elements = get_page_elements(page)
        self.by = ()
        self.action = None

    def _get_page_elem(self, elem):
        # _get_page_elem前面的下划线表示私有方法，不能直接调用，只能通过类名调用
        # 获取定位元素的 by，以及操作action
        for each in self.elements:
            if each['name'] == elem:
                self.by = each['by']
                if 'action' in each and each['action'] is not None:
                    self.action = each['action']
                else:
                    self.action = None

    def oper_elem(self, elem, args=None):
        self._get_page_elem(elem)
        cmd = self._selenium_cmd('find_element', args)
        return eval(cmd)

    def oper_elems(self, elem, args=None):
        self._get_page_elem(elem)
        cmd = self._selenium_cmd('find_elements', args)
        return eval(cmd)

    def _selenium_cmd(self, find_type='find_element', args=None):
        # 拼接 selenium 查找命令， 查找单个元素时find_type为'find_element'，多个元素时为'find_elements'
        cmd = 'self.driver.' + find_type + '(*self.by)'
        if self.action:
            if self.action in SimpleActions:
                cmd = cmd + '.' + self.action
                if args:
                    cmd = cmd[:-1] + 'args' + ')'
        return cmd


def get_page_elements(page):
    """动态加载页面定义文件，获取文件中定义的元素列表elements"""
    elements = None
    if page:
        try:
            m = importlib.import_module(page)
            elements = m.elements
        except Exception as e:
            logger.error('error info : %s' % (e))
    return elements
