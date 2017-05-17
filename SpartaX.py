#coding:utf-8
import requests
import re 
import os
import time

def getCookie(url, headers=None):
	return requests.get(url, headers= headers).cookies

def getHtml(url, headers=None, cookies=None):
	response = requests.get(url, headers= headers, cookies = cookies)
	# cookie = response.cookies
	# print(cookie)
	# print(response.encoding)
	response.encoding = 'utf-8'
	# print(response.text)
	return response.text



def getProp(html, prop):
	m = re.findall(('%s=.+?[\"|\'|>|\s]')%(prop), html , flags= re.I) 
	index = 0
	for x in m:

		x = x.split('=')
		m[index] = x[1].strip(' \"\'/>')
		index = index + 1
	return m

	 

def getAssets(src, name=None, headers=None, cookies=None, savePath=''):
	response = requests.get(src, headers= headers, cookies=cookies)
	src = src.split('/')
	if not os.path.exists(savePath):
		os.makedirs(savePath)
	savePath = savePath + src[len(src)-1]
	f = open(savePath, 'wb')
	f.write(response.content)
	f.close()


def getContent(html, label):
	m = re.findall(r'<%s>.+?</%s>'%(label,label), html, flags= re.I)
	if len(m)!=0:
		m = re.sub(r'<[^>]+>','', m[0])
		return m
	else:
		return ''	


	# for x in m:
	# 	jpg_link = 'http://'+website+'/'+x;
	# 	x = x.split('/')
	# 	path = x[1]
	# 	print(jpg_link)
	# 	response = requests.get(jpg_link, headers= headers, cookies= cookie)
	# 	data = response.content
	# 	f = open(path,'wb')
	# 	f.write(data)
	# 	f.close()
	# 	
	# 	
website = '91.t9n.space'
url = "http://"+website+"/viewthread.php?tid="
prop = 'file'
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host": website,
"Referer":"http://www.google.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
cookie = getCookie(url, headers)
html = getHtml(url, headers, cookie)
x = getProp(html, prop)
savePath = getContent(html, 'title')
n = len(savePath)-45
n = time.strftime("%Y%m%d", time.localtime())+n 
savePath = savePath[0:n]+'/'


 

for i in x:
	src =  'http://'+website+'/'+i;
	print(src)
	getAssets(src,headers= headers, cookies= cookie, savePath= savePath)


# http://blog.csdn.net/sinat_21302587/article/details/65634124 
# http://blog.csdn.net/shanzhizi/article/details/50903748
# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#cookie
# http://blog.csdn.net/ttdevs/article/details/53696261