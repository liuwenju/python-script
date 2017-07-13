#!/usr/bin/env python
# encoding: utf-8


"""
date:2017-07-12
author:liuwenju
email:liuwenju0123@gmail.com
description:complete backup the small databases
"""
import os
import time

os.system("mysqldump --user='root' --password='mydbpasswd' wordpress > /root/dbbackup/%s.sql"%(time.strftime('%Y-%m-%d')))
