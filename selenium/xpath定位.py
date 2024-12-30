# <html>
#   <head>...<head/>
#   <body>
#     <div id="aa">
#       <div class="bb">
#         <div class="cc">
#           <div class="dd">...</div>
#           <div class="ff">
#             <div class="ee">
# 			<div class="hh">
# 				<input id="ww" autocomplete="off" type="text" value="" placeholder="自动化测试">

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")

# # 绝对路径（层级关系）定位
# driver.find_element(By.XPATH, value="/html/body/div/div/div/div[2]/div/div/input[1]")
#
# # 利用元素属性定位
# driver.find_element(By.XPATH, value="//*[@id='ww']")
#
# # 层级定位
# driver.find_element(By.XPATH, value="//div[@id='aa']/div/div/div[2]/div/div/input[1]")
# driver.find_element(By.XPATH, value="//div[@class='bb']/div/div/div[2]/div/div/input[1]")
#
# # 层级+元素属性定位
# driver.find_element(By.XPATH, value="//div[@id='aa']/div/div/div[2]/div/div/input[1]")
#
# # 逻辑运算符定位
# driver.find_element(By.XPATH, value="//*[@id='ww' and @autocomplete='off']")

# 定位搜索输入框
text_label = driver.find_element(By.XPATH, value='//*[@id="kw"]')

# 在搜索框中输入 自动化测试
text_label.send_keys('自动化测试')

# 清除搜索框中的内容
text_label.clear()

# 输出搜索框元素是否可见
print(text_label.is_displayed())

# 输出placeholder的值
print(text_label.get_attribute('placeholder'))

# 定位搜索按钮
button = driver.find_element(By.XPATH, value='//*[@id="su"]')
# 输出按钮的大小
print(button.size)
# 输出按钮上的文本
print(button.text)
