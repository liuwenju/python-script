import os

s1 = os.system('docker pull silentyang/shadowsocks')
s2 = os.system('docker container stop ss&&docker container rm ss&&docker run -d --restart always --name ss -v /etc/localtime:/etc/localtime:ro -p 10000:10000/tcp -p 10000:10000/udp -e SSPASSWORD=password silentyang/shadowsocks')

if s1&s2 == 0:
    print ("\033[1;32;40m SS update successful!\033[0m")
else:
    print ("\033[1;31;40m please update mannully!\033[0m")

