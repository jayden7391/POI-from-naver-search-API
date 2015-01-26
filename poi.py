__author__ = 'JAYDEN'
#-*- coding: utf-8 -*-
import urllib2
import sys
import BeautifulSoup

def get_url(url):
	req_headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:2.0) Gecko/20100101 Firefox/4.0', 'Referer':'http://python.org'}
	request = urllib2.Request(url, headers=req_headers)
	opener = urllib2.build_opener()
	response = opener.open(request)
	contents = response.read()
	return contents

def get_POI(query):
	print query
	page = 1
	fw = open(query+'.txt','w')
	key = "your_key"
	while page < 101:
		url = 'http://openapi.naver.com/search?key='+ key + '+&query=' + query + '&target=local&start=' + str(page) + '&display=100'
		data = get_url(url)
		soup = BeautifulSoup.BeautifulSoup(data)
		contents = soup.findAll('item')
		n = 0
		while n < len(contents):
			title = contents[n].find('title').text
			if '&lt;b&gt;' in title:
				titles = title.split('&lt;b&gt;')
				title_1 = titles[0]
				title_2 = titles[1]
				title_2 = title_2.split('&lt;/b&gt;')
				i = 0
				title_3 = ""
				while i < len(title_2):
					title_3 = title_3 + title_2[i]
					i = i+1
				title = title_1 + title_3
			mapx = contents[n].find('mapx').text
			mapy = contents[n].find('mapy').text
			result = title + '|' + mapx + '|' + mapy + '\n'
			fw.write(result)
			print result
			n = n+1
		page = page+1
	fw.close()


reload(sys)
sys.setdefaultencoding('utf-8')
print sys.getdefaultencoding()
get_POI('산부인과')
get_POI('국민은행')
get_POI('sk주유소')
get_POI('영화관')