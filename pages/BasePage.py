# 设置基类，很多事件都是重复的比如点击，文本输入。所以写下这个基类
class BasePage(object):
    # 初始化方法
    def __init__(self, driver):
    # 传参driver，就不需要在导入驱动了
        self.driver = driver


# 根据*loc（*代表可变参，一定是最后一个参数否则会报错）查找元素
    def find_element(self, *loc):
        return self.driver.find_element(*loc)


# 向某个元素输入内容text
    def type_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)


# 对某个元素操作点击事件
    def click(self, *loc):
        print("----------", self.driver)
        self.find_element(*loc).click()


# 清空某个元素内容
    def clear(self, *loc):
        self.find_element(*loc).clear()


# 获取页面的title
def get_title(self):
    return self.driver.title
