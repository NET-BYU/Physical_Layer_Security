import socket

UDP_IP = "10.10.0.4"
UDP_PORT = 5005
MESSAGE = "Hello, World! I want to test longer stings so I can more effectively be eve the hacker, but not that Eve was a bad person, it's just the name we give the baddie in this lab. Sorry Eve."

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))

