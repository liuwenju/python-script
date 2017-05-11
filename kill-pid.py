#coding=utf-8

"""
author: liuwenju
time:2017-3-16
email:liuwenju0123@gmail.com
descriptiom: kill the pid which you want 
"""
import os
import commands


#('./pipesocks pump -p 7473 -k qwer1234 > /dev/null')

def getPid(process):
    cmd = 'ps -aux | grep "%s"'% process
    infos = commands.getoutput(cmd)
    info = infos.split('\n')
    selfid = info[-1].split()[1]
    pid = info[1].split()[1]
    if pid == selfid:
        print 'the same pid,do nothing!'
    else:
        commands.getoutput('kill -9 "%s"'% pid)

if __name__ == '__main__':
    #process = 'pipesocks'#infomation of pid you want kill
    process = str(raw_input("please input the command you want to kill:(like:top)"))
    getPid(process)

