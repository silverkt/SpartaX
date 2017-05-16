#coding:utf-8
import requests
import re 


website = '91.t9n.space'
url = "http://"+website+"/viewthread.php?tid=229471"
headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Encoding":"utf-8",
"Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
"Connection":"keep-alive",
"Host": website,
"Referer":"http://www.google.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
response = requests.get(url, headers= headers)

cookie = response.cookies 
 
print(response.encoding)
response.encoding = 'utf-8'
print(response.text)

m = re.findall(r'file=".+?"', response.text)
print(m[1])

index = 0
for x in m:

	x = x.split('"')
	m[index] = x[1]
	#print(m[index])
	index = index + 1

 




for x in m:
	jpg_link = 'http://'+website+'/'+x;
	x = x.split('/')
	path = x[1]
	print(jpg_link)
	response = requests.get(jpg_link, headers= headers, cookies= cookie)
	data = response.content
	f = open(path,'wb')
	f.write(data)
	f.close()
 
 
# http://blog.csdn.net/sinat_21302587/article/details/65634124 
# http://blog.csdn.net/shanzhizi/article/details/50903748
# http://cn.python-requests.org/zh_CN/latest/user/quickstart.html#cookie
# http://blog.csdn.net/ttdevs/article/details/53696261