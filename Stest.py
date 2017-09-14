#coding:utf-8
import requests
import re 
import os
import time

 
def getHtml(url, headers=None, cookies=None):
	try:
		response = requests.get(url, headers= headers, cookies = cookies, timeout=10)
		response.encoding = 'utf-8'
		return response.text
	except Exception as err:
		return '<html></html>'
	# cookie = response.cookies
	# print(cookie)
	# print(response.encoding)
	# print(response.text)
	
  
url = "http://222.222.120.72:808/redsv9/webapi/quantity?rqfor=socialco2&tscope=4&ascope=1"

x = getHtml(url)

print(url) 

##--------------------
# working on GC
# working on 管道流
