#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = 'pi'
__email__ = 'pipisorry@126.com'

"""
import requests
 

LOGIN_URL = 'http://email.91dizhi.at.gmail.com.7h4.space/view_video.php?viewkey=06b01b5ffee811a23f8a'
response = requests.get(LOGIN_URL)

cj = response.cookies
print(cj)
cja = requests.utils.dict_from_cookiejar(cj)
print(cja) 

cjastr = str(cja)

f = open('a.txt', 'w')
f.write(cjastr)
f.close()

print(type(eval(cjastr)))
print(type(cjastr))
print(type(cja))


cja = eval(cjastr)
cj = requests.utils.cookiejar_from_dict(cja, cookiejar=None, overwrite=True)
print(cj)