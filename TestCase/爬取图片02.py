"""
正则表达式findall匹配
列表的遍历
枚举函数自动生成从0开始的编号: enumerate()
"""
# 1.导包
import requests
import re
# 2.准备有效的url
url = 'http://127.0.0.1:9091/'
# 3.发送请求,获取响应对象
response = requests.get(url)
# 4.从响应对象中提取数据
html_str = response.content.decode()
# print(html_str)
# 5.正则表达式匹配想要的数据
img_list = re.findall('<img src="(.+?)" ', html_str)
print(img_list)
# 6.遍历图片列表,拼接url,批量发送请求获取资源
# 定义基础url
base_url = 'http://127.0.0.1:9091/'
for i,img_path in enumerate(img_list):
    # 拼接图片url
    img_url = base_url + img_path[3:]
    # 批量发送请求获取资源
    r = requests.get(img_url)
    # 从响应对象中提取数据
    data = r.content
    # 7.保存数据
    with open(f'load/图片/{i}.jpg', 'wb') as f:
        f.write(data)
