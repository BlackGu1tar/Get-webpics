#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests,urllib
from bs4 import BeautifulSoup
import time
import re
import os
import sys



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',}

url_domain = 'https://f.wonderfulday29.live/viewthread.php?tid='



#定义获取html源码函数
def getHtml(url):
    html = requests.get(url,headers =headers).content
    img_keys = re.findall('attachments(.*?)"', html)
    return img_keys


#start 351146, 351200

for i in range(203276, 300000): #256805
    all_url = url_domain + str(i)
    url_head = 'http://pic.w26.rocks/attachments'
    html_code = requests.get(all_url,headers =headers)
    if not html_code.status_code == 404:
        print '[+] Current Task ID : ' + str(i)
        html = requests.get(all_url,headers =headers).content
        keys = re.findall('<h1>(.*?)</h1>', html)
        try:
            fileName = keys[0].decode('utf-8').encode('gbk')
            fileName = re.sub('[\/:*?"<>|.~]','-',fileName)
        except Exception as e:
            #print '[+] 91Forum Page Access Denied!!--------' + 'ID: ' + str(i)
            pass
        if not os.path.exists(fileName) and len(fileName) == 0:
            pass
        elif not os.path.exists(fileName) and len(fileName) > 0:
            os.mkdir(fileName)
        if len(getHtml(all_url)) == 0:
            print '[+] Current Page is not have Pics...'
        elif len(getHtml(all_url)):
            for u in getHtml(all_url):
                img_url = url_head + u
                response = requests.get(img_url,headers=headers)
                with open(fileName + '/' + img_url.split('/')[-1],'wb') as f: #打印图片到本地
                    f.write(response.content)
                    f.flush()
                    print '[+] ' + img_url +'     *Downling Success!*'



