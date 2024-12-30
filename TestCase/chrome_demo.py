import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("http://www.baidu.com")
driver.maximize_window()

time.sleep(2)
# 输入想要搜索的值
# driver.find_element(By.ID,value="kw").send_keys("你好呀") #通过id查找
# driver.find_element(By.NAME,value="wd").send_keys("hello") #通过name查找

# driver.find_element_by_class_name(“s_ipt”).send_keys(“hello”) #通过class查找
# driver.find_element(By.LINK_TEXT, value="登录").click()  # 通过超链接查找
# driver.find_element_by_partial_link_text(“About”).click() #通过超链接的部分关键字查找

# 当获取的是多个值时，方法记得用复数形式：find_elements_by
# 通过标签查找
input_list = driver.find_elements(By.TAG_NAME, value="input")
for result_list in input_list:
    if result_list.get_attribute("type") == "text":
        result_list.send_keys("圣诞快乐")
    # 点击“百度一下”按钮
    driver.find_element(By.ID, value="su").click()
    time.sleep(3)
    # driver.find_element_by_xpath(“//*[@id=‘1’]/h3/a[1]/em”).click() #通过xpath查找
    time.sleep(5)
    driver.quit()
