from socket import *

domain = input("Enter the host address to scan (can be IP address or domain name): ")
p = input("Enter the range of ports to scan (ex. 1,100 ): ")

port = p.split(',')
port_start = int(port[0])
port_end = int(port[1])


for i in range(port_start,port_end):
	skt = socket(family=AF_INET, type=SOCK_STREAM)
	skt.settimeout(4.00)
	result = skt.connect_ex((domain,i))

	if result == 0:
		print(f"port {i} is open.")

	skt.close()
