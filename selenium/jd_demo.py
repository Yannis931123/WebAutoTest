from selenium.webdriver.common.by import By

# page_url = 'https://www.jd.com'
#
# elements = [
#     {'name': 'search_ipt', 'desc': '搜索框点击', 'by': (By.ID, u'key'), 'ec': 'presence_of_element_located', 'action': 'send_keys()'},
#     {'name': 'search_btn', 'desc': '搜索按钮点击', 'by': (By.CLASS_NAME, u'button'), 'ec': 'presence_of_element_located', 'action': 'click()'},
# ]

# name: 每个元素 + 操作的唯一标识。一个元素可能由于操作不同，而要定义多个，但大部分只要定义一个。
# desc: 元素 + 操作的描述。
# by: 元素的定位方式，使用selenium的原生定位方式，不自己定义封装。
# ec: 等待元素出现的方式，这个暂时未用。
# action: 元素的对应操作。使用原生的selenium动作方法，不自己定义封装。

from selenium.webdriver.common.by import By

page_url = 'https://search.jd.com/'

elements = [
    {'name': 'result_list', 'desc': '结果列表', 'by': (By.CLASS_NAME, u'gl-item'),
     'ec': 'presence_of_all_elements_located', 'action': None},
    {'name': 'price', 'desc': '价格', 'by': (By.XPATH, u".//div[@class='p-price']/strong/i"),
     'ec': 'presence_of_element_located', 'action': 'text'},
    {'name': 'pname', 'desc': '描述', 'by': (By.XPATH, u".//div[@class='p-name p-name-type-2']/a/em"),
     'ec': 'presence_of_element_located', 'action': 'text'}
]
