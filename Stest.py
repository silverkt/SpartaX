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
		return err
	# cookie = response.cookies
	# print(cookie)
	# print(response.encoding)
	# print(response.text)
	
  
url = "http://91.p9b.space/viewthread.php?tid=244740"

x = getHtml(url)

print(x) 

##--------------------
# working on GC
# working on 管道流
