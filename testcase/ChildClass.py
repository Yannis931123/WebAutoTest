from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from BaseClass import BaseClass


class LoginClass(BaseClass):
    # 定位元素
    username = (By.ID, "input1")
    password = (By.ID, "input2")
    sign_in = (By.ID, "submit")

    # 设置用户名
    def set_username(self, username):
        name = self.driver.find_element(*LoginClass.username)
        name.send.keys(username)

    # 设置密码
    def set_password(self, password):
        pwd = self.driver.find_element(*LoginClass.password)
        pwd.send.keys(password + Keys.RETURN)

    #提交登录信息
    def sign(self):
        submit= self.driver.find_element(*LoginClass.sign_in)
        submit.click()
