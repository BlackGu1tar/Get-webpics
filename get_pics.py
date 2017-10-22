#!/usr/bin/python
# -*- coding:utf-8 -*-

import urllib,re,requests
import socket
import time

#定义获取html源码函数
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close
    return html

#使用正则表达式过滤图片文件名
page = getHtml('http://file.codecat.one/Driver/Ecup%E7%99%BE%E5%8F%98%E5%A5%B3%E7%A5%9E%20Vip%E4%BB%98%E8%B4%B9%E8%87%AA%E6%8B%8D%20%E8%90%BD%E5%85%A5%E5%87%A1%E9%97%B4%E7%9A%84%E5%B0%A4%E7%89%A9%20%E6%80%A7%E6%84%9F%E9%95%BF%E8%BA%AB%E6%B0%94%E8%B4%A8%E6%AD%A3%E5%A6%B9/')
mp4_url = re.findall(r'picture_icon jpg"><a href=\".\/(.*?)\" target=_Blank>',page)
http_url = 'http://file.codecat.one/Driver/Ecup%E7%99%BE%E5%8F%98%E5%A5%B3%E7%A5%9E%20Vip%E4%BB%98%E8%B4%B9%E8%87%AA%E6%8B%8D%20%E8%90%BD%E5%85%A5%E5%87%A1%E9%97%B4%E7%9A%84%E5%B0%A4%E7%89%A9%20%E6%80%A7%E6%84%9F%E9%95%BF%E8%BA%AB%E6%B0%94%E8%B4%A8%E6%AD%A3%E5%A6%B9/'


for x in mp4_url:
	#拼接完整URL并用urlretrieve方法下载
	imgurl = http_url+x
	#socket.setdefaulttimeout(10)
	urllib.urlretrieve(imgurl,'C:\\Python27\\get-pic\\videos\\%s' % x)
