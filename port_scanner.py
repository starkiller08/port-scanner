from socket import *
import time
import sys

def animate():
	for i in range(0,10):
		sys.stdout.write('\rloading |')
		time.sleep(0.1)
		sys.stdout.write('\rloading /')
		time.sleep(0.1)
		sys.stdout.write('\rloading ---')
		time.sleep(0.1)
		sys.stdout.write("\rloading \\")
		time.sleep(0.1)
		i += 1
	sys.stdout.write('\rProgram Started.... Welcome to Stealthy, the go to scanner for ethical hackers!!\n\n')

print('*' * 49)
print('     Stealthy -- The Ultimate Port Scanner!!')
print('*' * 49)
print('Initializing Program....')
time.sleep(0.7)
animate()


domain = input("Enter the host address to scan (IP address or domain name): ")
p = input("Enter the range of ports to scan (ex. 1,100 ): ")

port = p.split(',')
port_start = int(port[0])
port_end = int(port[1]) + 1


for i in range(port_start,port_end):
	skt = socket(family=AF_INET, type=SOCK_STREAM)
	skt.settimeout(10.00)
	print(f'Scanning port {i} of {port[1]}')
	result = skt.connect_ex((domain,i))

	if result == 0:
		print(f"port {i} is open.")

	skt.close()

print('\nStealthy has finished scanning. Have fun exploiting the shit out of those ports ;) :D :D')
