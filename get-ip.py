#coding=utf-8

"""
author:liuwenju
email:liuwenju0123@gmail.com
time:2017-3-30
description:get detail of ip info though ipip.net
note:need python2 and requests;beautifulsoup4
"""

from bs4 import BeautifulSoup
import requests


url = "http://www.ipip.net/ip.html"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

req = requests.get(url,headers=header)

soup = BeautifulSoup(req.text, 'lxml')

for item in soup.find_all('td'):
    print item.text


