'''解放日报

https://www.jfdaily.com/journal/2020-06-30/page_01.htm
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

	url = 'https://www.jfdaily.com/journal/' + year + '-' + month + '-' + day + '/page_01.htm'
	print (url)
	html = fetchUrl(url)
	bsobj = bs4.BeautifulSoup(html, 'html.parser')
	#print(bsobj)

	#pageList = bsobj.find('div', attrs={'id': 'pageList'}).ul.find_all('div', attrs={'class': 'right_title-name'})
	pageList = bsobj.find('div', attrs={'class': 'WH100 Left_bg01 iframeScroll'}).ul.find_all('li')
	pagenum=len(pageList)
	linkList = []

	for pg in range(1,pagenum+1):

		if pg<10:
			pg='0'+str(pg)
		else:
			pg=str(pg)

		url = 'https://www.jfdaily.com/journal/' + year + '-' + month + '-' + day + '/page_'+pg+'.htm'
		linkList.append(url)
	return linkList

def getTitleList(year, month, day, pageUrl):
	'''
	功能：获取报纸某一版面的文章链接，文章标题
	参数：年，月，日，该版面的链接
	返回类型：字典，参数：url链接，标题
	'''
	html = fetchUrl(pageUrl)
	bsobj = bs4.BeautifulSoup(html, 'html.parser')

	#titleList = bsobj.find('div', attrs={'id': 'titleList'}).ul.find_all('li')
	titleList = bsobj.find('div', attrs={'class': 'list'}).find_all('a')
	linkList=[]
	linkText={}
	for title in titleList:
		link = title['href']
		text=title.string.strip()

		# print (link)
		# print (text)
		if 'getArticle.htm?' in link:
			url = 'https://www.jfdaily.com/journal/' + year + '-' + month + '-' + day + '/' + link
			linkList.append(url)
			linkText[link]=text

	return linkText




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
	for page in pageList:
		titleList = getTitleList(year, month, day, page)
		for k,v in titleList.items():
			print (v)


