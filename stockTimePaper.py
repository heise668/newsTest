'''
证券时报

http://epaper.stcn.com/paper/zqsb/html/epaper/index/index.htm
'''

import requests
import bs4
import os
import datetime
import time

def fetchUrl(url):
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
	}

	r=requests.get(url,headers)
	r.raise_for_status()
	r.encoding=r.apparent_encoding
	return r.text


def getPageList(year, month, day):
	'''
	功能：获取当天报纸的各版面的链接列表
	参数：年，月，日
	返回类型：列表，参数：url
	'''

	url = 'http://epaper.stcn.com/paper/zqsb/html/epaper/index/index.htm'
	html = fetchUrl(url)
	bsobj = bs4.BeautifulSoup(html, 'html.parser')


	title=bsobj.find('div', attrs={'id': 'webtree'}).find_all('span')
	# print (title)

	#pageList = bsobj.find('div', attrs={'id': 'pageList'}).ul.find_all('div', attrs={'class': 'right_title-name'})
	pageList = bsobj.find('div', attrs={'id': 'webtree'}).find_all('li')
	# print (pageList)

	content={}
	for page in pageList:
		pg=page.find('a')
		link=pg['href']
		text=pg.get_text()
		content[link]=text
	return content



if __name__ == '__main__':
	'''
	主函数：程序入口
	'''
	t=datetime.date.today()
	year=str(t.year)
	month=str(t.month)
	if t.month < 10:
		month='0'+month
	day=str(t.day)
	if t.day <10:
		day = '0'+day
	pageList = getPageList(year, month, day)
	for k,v in pageList.items():
		print (v)



