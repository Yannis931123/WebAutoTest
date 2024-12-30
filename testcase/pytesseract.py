import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image
import pytesseract


def get_code():
    # url="https://www.chaojiying.com/apiuser/login/"
    url = "https://blog.csdn.net/weixin_45566935/article/details/103232855#:~:text=%E4%B8%80%E3%80%81%E5%9B%BE%E5%BD%A2%E9%AA%8C%E8%AF%81%E7%A0%81%E6%98%AF%E4%BB%80%E4%B9%88%EF%BC%9F%20%E5%9B%BE%E5%BD%A2%E9%AA%8C%E8%AF%81%E7%A0%81%E6%98%AF%E4%B8%80%E4%BA%9B%E6%B2%A1%E6%9C%89%E8%A7%84%E5%88%99%E7%9A%84%E5%9B%BE%E6%96%87%E7%9A%84%E7%BB%84%E5%90%88%EF%BC%8C%E5%8F%82%E8%80%83%E4%B8%8B%E5%9B%BE,%E4%BA%8C%E3%80%81%E5%9B%BE%E5%BD%A2%E9%AA%8C%E8%AF%81%E7%A0%81%E6%9C%89%E4%BB%80%E4%B9%88%E7%94%A8%EF%BC%9F%20%E9%98%B2%E6%AD%A2%E6%81%B6%E6%84%8F%E6%94%BB%E5%87%BB%E8%80%85%E9%87%87%E7%94%A8%E6%81%B6%E6%84%8F%E5%B7%A5%E5%85%B7%E6%89%B9%E9%87%8F%E6%B3%A8%E5%86%8C%E8%B4%A6%E5%8F%B7%E6%88%96%E6%98%AF%E5%A4%A7%E9%87%8F%E9%A2%91%E7%B9%81%E8%B0%83%E7%94%A8%E6%9F%90%E4%BA%9B%E8%AF%B7%E6%B1%82%EF%BC%8C%E7%BB%99%E6%9C%8D%E5%8A%A1%E5%99%A8%E9%80%A0%E6%88%90%E5%8E%8B%E5%8A%9B%EF%BC%8C%E5%8D%A0%E7%94%A8%E5%A4%A7%E9%87%8F%E7%9A%84%E7%B3%BB%E7%BB%9F%E8%B5%84%E6%BA%90%E3%80%82"
    # chromepath = r"C:\Users\xyyxs\AppData\Local\Programs\Python\Python311\Scripts\chromedriver.exe"
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(2)
    t = time.time()
    name1 = str(t) + ".png"
    driver.maximize_window()
    driver.save_screenshot(name1)
    code = driver.find_element(By.XPATH, '//*[@id="content_views"]/p[1]/text()[3]')
    # 左上角位置
    left = code.location['x']
    top = code.location['y']
    # 右下角位置
    right = code.size['width'] + left
    bottom = code.size['height'] + top

    # right=code.size['height']+left
    # bottom=code.size['width']+top

    # 读取全屏截图
    img = Image.open(name1)
    # 获取验证码图片
    img_code = img.crop((left, top, right, bottom))
    name2 = str(t) + ".png"
    img_code.save(name2)

    mycode = pytesseract.image_to_string(name2)

    print(mycode)
    driver.close()
