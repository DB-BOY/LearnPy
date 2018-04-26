# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.douban.com/')  # 豆瓣首页
code = r.status_code
print(code)

t = r.text
# print(t)


r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
url = r.url
print('url: ', url)
encodeing = r.encoding

print('encoding: ', encodeing)

content = r.content

print('content: ', content)

r = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(r.json())

# 传入一个dict作为headers参数
print('----传入一个dict作为headers参数')

r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
# print(r.text)


# post 使用
print()
print('-----post 使用,    data传参')

r = requests.post('https://www.douban.com/search', data={'q': 'python', 'cat': '1001'})
url = r.url
print('url: ', url)
print(r.content)

print('-----    json')
r = requests.post('https://www.douban.com/search', json={'q': 'python', 'cat': '1001'})
url = r.url
print('url: ', url)
print(r.content)

# 上传文件
# upload_files = {'file': open('report.xls', 'rb')}
# r = requests.post(url, files=upload_files)
