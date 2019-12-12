#!/usr/bin/env python3
# encoding: utf-8
# tested on ubuntu18.04
#import commands
import subprocess
import time

#cmd = 'ifconfig eth0|grep "RX bytes"|awk '{print $3 $4}''
#cmd1 = "/sbin/ifconfig eth0 | awk '{print $3 $4}'|tail -n 2|head -n 1"
cmd1 = "/sbin/ifconfig eth0 |grep B |grep RX|awk '{ print $5 }'"
cmd2 = "/sbin/ifconfig eth0 |grep B |grep TX|awk '{ print $5 }'"

sum1 = subprocess.getoutput(cmd1)
sum2 = subprocess.getoutput(cmd2)

print ("截至" + time.strftime("%Y-%m-%d %H:%M:%m") + "接收(receive): %d"%(float(sum1)/10**9) + "GB")
print ("截至" + time.strftime("%Y-%m-%d %H:%M:%m") + "发送(transport): %d"%(float(sum2)/10**9) + "GB")
print ("*" * 50)
