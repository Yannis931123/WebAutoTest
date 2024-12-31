import re
import os
import requests

filename = 'music\\'

# 如果没有则创建文件夹
if not os.path.exists(filename):
    os.makedirs(filename)

# 请求网址（如果想要爬取其他的榜单的歌曲内容，只需要改这个 url 即可）
url = 'https://music.163.com/playlist?id=3778678'

# 伪造请求头
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

# 发送请求
response = requests.get(url, headers=headers)

# re.findall
# 这个函数用于在字符串中查找所有与正则表达式模式匹配的部分，并返回一个包含所有匹配项的列表
# r 前缀表示这是一个原始字符串，其中的反斜杠不会被解释为转义字符
# (\d+): 捕获组，匹配一个或多个数字
# (.*?): 捕获组，非贪婪匹配任何字符（包括空字符），直到遇到 </a>
html_data = re.findall(r'<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)

# 正则表达式提取出来的一个内容返回是列表 里面每一个元素都是元组
for num_id, title in html_data:
    # 调用接口
    music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'

    # 发送请求获取二进制数据
    music_content = requests.get(music_url, headers=headers)

    # 保存
    with open('music\\' + title + '.mp3', 'wb') as f:
        f.write(music_content.content)
        print(num_id, title)