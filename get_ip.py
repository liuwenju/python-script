# -*- coding: utf-8 -*-

"""
author:liuwenju
time:2017-3-30
email:liuwenju0123@gmail.com
description:get the ip info of the host
"""

#import requests
import os,commands


cmd = "ifconfig  | grep  'inet addr:' | grep -v '127.0.0.1' | cut -d: -f2 | awk '{ print $1}'"
ip = commands.getoutput(cmd)
url = "http://freeapi.ipip.net/" + ip

req = requests.get(url)
print req.text

