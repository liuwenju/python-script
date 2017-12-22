#coding=utf-8

import os
import time
#import requests
#from bs4 import BeautifulSoup

s = os.system('apt-get update && apt-get -y upgrade && apt-get update && apt-get dist-upgrade -y')

if s == 0:
    print "\033[1;32;40m update successful!\033[0m"
    #print "update successful!"
    os.system('apt-get autoremove -y')
    print "\033[1;32;40m autoremove no need packages successful!\033[0m"
else:
    print "\033[1;31;40m please update mannully!\033[0m"
    #print "please update manually!"
