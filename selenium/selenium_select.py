# encoding:utf-8

# select_by_value()	通过value值定位下拉选项
# select_by_visible_text()	通过text值定位下拉选项
# select_by_index()	根据下拉选项的索引进行选择。第一个选项为0，第二个位选项为1

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option = webdriver.EdgeOptions()
option.add_experimental_option("detach", True)

driver = webdriver.Edge(options=option)
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_select")
driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))
element = driver.find_element(By.TAG_NAME, "select")

# select_by_value的使用
Select(element).select_by_value("saab")

# select_by_index的使用
time.sleep(5)
Select(element).select_by_index(2)
