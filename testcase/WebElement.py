# By.ID	根据id定位
# By.XPATH	根据xpath定位
# By.CLASS_NAME	根据class的名称
# By.LINK_TEXT	元素链接文本定位
# By.TAG_NAME	元素标签名定位
# By.CSS_SELECTOR	根据元素 CSS 选择器定位
# By.PARTIAL_LINK_TEXT	根据元素部分链接文本定位
# By.NAME	根据元素名称定位

# tag_name	获取元素的标签名
# text	获取元素的文本信息
# click()	点击
# send_keys(values)	输入文字
# submit()	提交表单from
# clear()	清除文本
# get_property(name)	获取 JavaScript 属性值，name表示属性名
# get_dom_attribute(name)	获取 DOM 属性的值，name表示属性名
# is_selected()	判断元素是否被选中，用于复选框和单选框
#第一步
#导入模块
from selenium import webdriver
from selenium.webdriver.common.by import By

#禁止浏览器自动关闭
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

#第二步
# 创建 Chrome 浏览器实例
driver=webdriver.Chrome(options=option)

#第三步
# 在浏览器中打开百度网站
driver.get("https://www.baidu.com/")

#窗口最大化
driver.maximize_window()

#第四步
#定位元素
driver.find_element(By.ID,"kw").send_keys("selenium")