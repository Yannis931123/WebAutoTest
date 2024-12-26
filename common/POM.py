# POM 页面-对象-模型
from selenium.webdriver.common.by import By
from time import sleep
from Pages.BasePage import BasePage


class UserLoginPage(BasePage):
    # 首先声明定位器
    language = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div/div/div/div[1]")
    chinese = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div/div/div/div[2]/ul/li[2]/div")
    username_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div/form/div[1]/div/div/input')
    pwd_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div/form/div[2]/div/div/input')
    captcha_input = (By.XPATH, '/html/body/div/div[1]/div[2]/div/form/div[3]/div/div/input')
    login_btn = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div/button")

    # 初始化方法传参driver驱动
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 得到登录的页面
    def goto_login_page(self):
        self.driver.get('http://*****.com/')
        # self.driver.get('http://*****com/')
        self.driver.maximize_window()

    # 选择登录的语言
    def choose_language(self):
        self.click(*self.language)

    def goto_chinese(self):
        self.click(*self.chinese)

    # 输入用户名并调用基类方法进行实现
    def input_username(self, username):
        self.clear(*self.username_input)
        self.type_text(username, *self.username_input)

    # 清空密码/输入密码
    def input_pwd(self, password):
        self.clear(*self.pwd_input)
        self.type_text(password, *self.pwd_input)

    # 输入验证码
    def input_captcha(self, captcha):
        self.clear(*self.captcha_input)
        self.type_text(captcha, *self.captcha_input)

    # 点击登录按钮
    def click_login_btn(self):
        self.click(*self.login_btn)
        sleep(3)
