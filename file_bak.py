#!/usr/bin/env python
# encoding: utf-8

"""
author:liuwj
datetime:2017-5-17
email:liuwenju0123@gmail.com
description:backup specified files
"""

import os
import time

source_dir='/home/zabbix/Documents'
bak_dir='/root/bak/'
name = bak_dir+time.strftime('%Y%m%d%H%M%S') + '.zip'
cmd = "zip -qr %s %s"%(name, source_dir)
if not os.path.exists(bak_dir):
    os.makedirs(bak_dir)
    os.chdir(bak_dir)
else:
    os.chdir(bak_dir)
if os.system('which zip') != 0:
    print 'Please install zip!'
elif os.system(cmd) == 0:
    print 'Congratulation,successfull backup!'
else:
    print 'Oops!backup failed!'
