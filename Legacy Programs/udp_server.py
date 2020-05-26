import socket
import fcntl
import struct


def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET,
		          socket.SOCK_DGRAM)
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s', ifname[:15].encode())
		)[20:24])

	
UDP_IP = get_ip_address('wlan0')
UDP_PORT = 5005

print ("Your Computer IP Address is:", UDP_IP)
print ("Your Open Port is:", UDP_PORT)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print (data.decode())
