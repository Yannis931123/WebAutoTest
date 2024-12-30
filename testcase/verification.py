import os
import time
import pytesseract
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By


def verification(browser, xpath):
    time.sleep(2)
    # 获取当前时间作为存储图片的名字
    t = time.time()
    # 获取当前项目路径
    path = os.path.dirname(os.path.dirname(__file__)) + "\\screenshots"
    # 获取验证码图片,设置存放位置
    pic_name1 = path + '\\' + str(t) + '.png'
    browser.save_screenshot(pic_name1)
    # 定位到验证码的位置
    ce = browser.find_element(By.XPATH, xpath)
    # 打印位置
    print(ce.location)
    # 设置需要截取的范围
    left = ce.location['x']
    top = ce.location['y']
    right = ce.size['width'] + left
    height = ce.size['height'] + top
    im = Image.open(pic_name1)  # 打开已经保存的图片
    img = im.crop((left, top, right, height))
    t = time.time()
    pic_name2 = path + '\\' + str(t) + '.png'
    img.save(pic_name2)
    # login().driver.close()

    # 读取截取到的图片中的文字
    image = Image.open(pic_name2)
    s = pytesseract.image_to_string(image).replace(" ", "")
    # 读取出来的验证码有空格，所以我在这里去空格了
    print(s)
    return s
