#导入鼠标操作的相关的类
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)


driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://www.baidu.com/")

#鼠标悬浮操作
ActionChains(driver).move_to_element(driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[3]/div/a")).perform()

# click(element=None)	单击指定的元素
# double_click(element=None)	双击指定的元素
# context_click(element=None)	右击指定的元素
# drag_and_drop(source, target)	拖拽源元素到目标元素
# move_to_element(to_element)	将鼠标移动到指定元素的中心位置
# move_by_offset(xoffset, yoffset)	模拟鼠标移动，其中 xoffset 和 yoffset 分别表示鼠标在水平和垂直方向上的移动距离，单位为像素
# perform()	执行ActionChains类中存储的所有行为