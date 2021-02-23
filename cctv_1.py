import urllib3
import requests
import json
from bs4 import BeautifulSoup

#  忽略警告：InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
requests.packages.urllib3.disable_warnings()
# 一个PoolManager实例来生成请求, 由该实例对象处理与线程池的连接以及线程安全的所有细节
http = urllib3.PoolManager()
# 通过request()方法创建一个请求：
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
    }

#7x24快讯api接口
url='http://tv.cctv.com/lm/xwlb/'

r = http.request('GET',
                 url,
                 headers=header)

soup = BeautifulSoup(r.data.decode(), 'html.parser')

##class="md_bd"
item = soup.find('div', class_='right_con01')
#print(item)

str=item.find_all('a')
for str1 in str:
    print (str1.string.strip())
