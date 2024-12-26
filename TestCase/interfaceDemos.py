import requests
import json

url = "https://api.github.com/users/ghost"

payload = json.dumps({"name": "ghost"})

headers = {"Authorization": "token 96339953133718348836086754",
           "Content-Type": "application/json"}
response = requests.request("GET", url, data=payload, headers=headers)
print(response.text)

"""
安装requests模块
pip install requests
"""
# 1.导包
import requests

# 2.准备有效URL
url = 'http://www.baidu.com/'
# 3.使用requests发送请求,或者Response对象
res = requests.get(url)
print(res)
# 4.从Response对象中提取数据
# 获取url
print(res.url)
# 获取状态码
print(res.status_code)
# 获取头
print(res.headers)
# 获取cookies
print(res.cookies)
# 获取编码
print(res.encoding)
# 修改编码
# res.encoding = 'utf8'
# print(res.encoding)
# 获取文本
# print(res.text)
# 获取内容,默认二进制需要使用decode()解码
print(res.content.decode())
