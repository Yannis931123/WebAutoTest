from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# def id_position_method():
#
#     # 实例化chromedriver
#     driver = webdriver.Chrome()
#     # 打开网站
#     driver.get('http://www.ceshiren.com')
#     # 等待一秒
#     time.sleep(1)
#     # 点击“精华帖”
#     driver.find_element(By.ID,"ember35").click()
#     # 等待两秒
#     time.sleep(2)
#
# if __name__ == '__main__':
#     id_position_method()

from selenium import webdriver

# 创建一个 WebDriver 实例
driver = webdriver.Chrome()

# 打开网页
driver.get("http://www.baidu.com")

# 定位文本框元素
input_element = driver.find_element("my_input")

# 获取文本框的当前文本值
current_value = input_element.get_attribute('value')

# 打印文本框的值
print("Current value:", current_value)

# 关闭 WebDriver
driver.quit()
