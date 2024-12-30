import datetime
import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

driver = webdriver.Edge()
driver.maximize_window()
driver.get('https://cube.anlink.com/')

# 等待加载
driver.implicitly_wait(4)
# 获取登录按钮
element = driver.find_element(By.ID, value='login-btn')
# 用户名输入框
userAccountEle = driver.find_element(By.ID, value="username")
# 密码输入框
passwordEle = driver.find_element(By.ID, value="temppassword")
# 验证码输入框
# veriCodeEle = driver.find_element(By.CSS_SELECTOR, value='input[placeholder="请输入验证码"]')
# 输入登录信息和验证码
driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "temppassword").send_keys("Admin@2024")
# driver.find_element(By.ID, "login-btn").click()
# userAccountEle.send_keys('zawb-yanxing')
# passwordEle.send_keys('AAAbbb111')
# veriCodeEle.send_keys('验证码')
# 点击登录
ActionChains(driver).move_to_element(element).click().perform()
# 获取当前活动窗口的url
current_url = driver.current_url
print(current_url)

iknowEle = driver.find_element(By.CLASS_NAME, value="za-cube-btn-default")
iknowEle.click()
# 点击发布管理菜单
# fbglMenuEle = driver.find_element(By.CLASS_NAME, value="za-cube-menu-item")
fbglMenuEle = driver.find_element(By.NAME, value="发布管理")
fbglMenuEle.click()

# 点击创建按钮
createBtnEle = driver.find_element(By.CLASS_NAME, value="ant-btn-primary")
createBtnEle.click()

# 选择类型容器
# containerTypeEle = driver.find_element(By.XPATH, value="//input[@class='ant-radio-input' and @type='radio' and @value='vm']")
# containerTypeEle.click()

# 输入发布单名称
fbdNameEle = driver.find_element(By.CLASS_NAME, value="ant-input")
today_date = datetime.datetime.now().strftime("%Y%m%d")  # 当期日期YYYYMMDD
random_letter = random.choice(string.ascii_uppercase)  # 随机大写字母
fbdNameEle.send_keys("自动化测试发布单" + today_date + random_letter)

# 选择系统下拉框
fbdSystemEle = driver.find_element(By.ID, value="project")
time.sleep(5)
fbdSystemEle.click()
fbdSystemEle.send_keys("演示系统")

fbdSystemEle.send_keys(Keys.ENTER)
# selectFbdSystem = Select(fbdSystemEle)
# selectFbdSystem.select_by_index(0)

#  选择流水线
# fbdPipelineEle = driver.find_element(By.CLASS_NAME, value="rc-virtual-list-holder-inner")
# fbdPipelineEle.click()
# fbdPipelineEle.send_keys("开发流水线")
time.sleep(3)

# 点击下一步
nextStepBtnEle = driver.find_element(By.ID, value="wizardform-next")
nextStepBtnEle.click()

# 点击添加应用
addAppBtnEle = driver.find_element(By.CLASS_NAME, value="ant-btn-primary")
addAppBtnEle.click()

# # 等待下拉框出现
# wait = WebDriverWait(driver, 10)
# dropdown_options = wait.until(
#     EC.visibility_of_all_elements_located((By.XPATH, "//ul[@class='ant-select-dropdown']")))

# 遍历下拉框选项，选择默认流水线关键字相关的流水线数据
# for option in dropdown_options:
#     if "默认流水线" in option.text:  # 根据选项文本判断是否符合条件
#         option.click()  # 点击选项
#         break  # 找到匹配的选项后，跳出循环
# selectPipeline = Select(fbdPipelineEle)
# selectPipeline.select_by_visible_text("默认流水线")
# 选择第一个流水线
# selectPipeline.select_by_index(0)

time.sleep(30)
