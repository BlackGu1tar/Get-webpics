#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests,urllib
from bs4 import BeautifulSoup
import time
import re
import os
import sys



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',}
url_id = '350918'
url_domain = 'https://f.wonderfulday30.live/viewthread.php?tid=' + url_id



#定义获取html源码函数
def getHtml(url):
    html = requests.get(url,headers =headers).content
    img_keys = re.findall('attachments(.*?)"', html)
    return img_keys



#拼接完整URL下载
url_head = 'http://pic.w26.rocks/attachments'
html = requests.get(url_domain,headers =headers).content
keys = re.findall('<h1>(.*?)</h1>', html)
fileName = keys[0].decode('utf-8').encode('gbk')
if not os.path.exists(fileName):
    os.mkdir(fileName)
    for u in getHtml(url_domain):
        img_url = url_head + u
        response = requests.get(img_url,headers=headers)
        with open(fileName + '/' + img_url.split('/')[-1],'wb') as f: #打印图片到本地
            f.write(response.content)
            f.flush()
            print img_url +'	 *Downling Success!*'



