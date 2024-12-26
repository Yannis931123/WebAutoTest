# # 导入必要的库
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# if __name__ == '__main__':
#     driver=webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://www.baidu.com/")
#     driver.find_element(By.ID,'kw').clear()
#     driver.find_element(By.ID, 'kw').send_keys('zxn')
#     driver.find_element(By.ID,'su').click()
#     time.sleep(2)
#     driver.back()
#     time.sleep(2)
#     driver.forward()
#     time.sleep(2)
#     driver.refresh()
#     time.sleep(2)
#     driver.close()
#     driver.quit()
#     print('ok')


from selenium import webdriver

def main():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

if __name__ == '__main__':
    main()