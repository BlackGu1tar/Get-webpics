#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import time
import re
import base64


cook = {"cookie":"#cookes"}


#for i in range(1,21):
#	url = "https://weibo.cn/u/3125368511?page=%d"%(i)
#	html = requests.get(url,cookies=cook).content
#	print html

url = "https://weibo.cn/u/3125368511?filter=1&page=3"
html = requests.get(url,cookies=cook).content
soup =BeautifulSoup(html,"html.parser")
#r = soup.findAll('span',attrs={"class" : "ctt"})
#html_content = re.findall(r'<span class="ctt">(.*?)</span>',html)
#for x in html_content:
#	print x
for x in soup.findAll('span',attrs={"class": "ctt"}):
	print x

