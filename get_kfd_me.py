#-*- coding: utf-8 -*-

import time
import requests
import urllib2
from bs4 import BeautifulSoup
import os


if not os.path.exists('/root/imges'):
    os.mkdir('/root/imges')
    os.chdir('/root/imges')
else:
    os.chdir('/root/imges')


def getImg(i):
    url = "http://10pic.kfd.me/page/" + str(i)
    print "Downloading from %s"%url
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
    req = requests.get(url,headers = headers)
    soup = BeautifulSoup(req.text, 'lxml')
    lists = []
    for item in soup.find_all('p'):
        lists.append(item.find_all('img'))

    lists.pop(0)
    lists.pop(0)
    for list in lists:
        #s = list
        s = str(list).split('\"')[-2]
        t = str(list).split('.')[-2].replace('/','-')
        #local = "/root/images/"
        f = urllib2.urlopen(s)
        with open("%s.jpg"%t, "wb") as code:
            code.write(f.read())


if __name__=='__main__':
    try:
        n = int(raw_input("Please input how many page do you want(total 365)?"))
        if n >=1:
            for n in range(1, n+1):
                try:
                    getImg(n+1)
                    time.sleep(1)
                except:
                    print "oh, some errors,ignore"
            print "congratulations!"
            print "The picture saved in /root/image/ "
        else:
            print "It's not a positive integer!"
            print "***********"+"stop"+"******************"
    except ValueError:
        print "Please input a number"
        print "***********"+"stop"+"******************"
