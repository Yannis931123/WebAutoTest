"""
字符串切割方法: split()
正则表达式match匹配
列表的定义和遍历
if判断
枚举函数自动生成从0开始的编号: enumerate()
"""
# 1.导包
import requests
import re

# 2.准备要爬取数据的页面有效url
url = 'www.baidu.com'

# 3.requests发送请求,获取响应对象
response = requests.get(url)

# 4.content从响应对象中提取数据
html_str = response.content.decode()

# 5.正则表达式从页面数据中匹配所有图片路径
# 把每一行放到列表中
html_list = html_str.split('\n')
# print(html_list) # ['    <img src="../images/0.jpg" width="350px" height="160px" style="margin-top:100px" >']
# 提前定义空列表用于存储图片路径
img_list = []
# 遍历列表依次匹配每一行数据
for line in html_list:
    data = re.match('.*<img src="(.+?)"', line)
    # 如果匹配成功,把路径存储起来
    if data:
        img_list.append(data.group(1))
# 循环外测试图片路径是否爬取到
print(img_list)

# 6.拼接图片url,并且批量发送请求
base_url = 'www.baidu.com'
# enumerate给容器中每个元素生成对应的从0开始的编号
# 遍历图片路径列表
for i, img_path in enumerate(img_list):
    # 拼接图片url
    img_url = base_url + img_path[2:]
    # 发送请求获取响应对象
    r = requests.get(img_url)
    # 从对象中获取资源
    data = r.content

    # 7.保存所有图片到本地
    with open(f'load/{i}.jpg', 'wb') as f:
        f.write(data)
        print(f"{i}.jpg保存成功!")
