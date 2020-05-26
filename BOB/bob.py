import socket
import fcntl
import time
import struct
import os
from signal import signal, SIGINT

def main():
	packetCounter = 0
	start = 0
	end = 0
	exitMsg = updateExitMsg(packetCounter, start, end)

	# Run the ping command as a background process
	# Flags -i (interval) -s (byte payload to send) -a (audible confirmation)
	print('Starting to Ping Server for CSI Data')
	os.system('nohup ping -s 698 -i 0.2 -a 10.10.0.1 > ping_data.txt &')
	time.sleep(0.1) # Wait for nohup to finish init
	# Output current processes to make sure that it ran appropriately
	print('\nOutput the current background processes:')
	os.system('ps T')

	# Open file to save received messages to 
	nameOfFile = "receivedMessage"
	fileName = os.path.join("/home/icelab2/Documents", nameOfFile + ".txt")
	myFile = open(fileName, 'w')

	# Define the handler in the function, so that it inherets the main variables
	def handler(*args):
		print ("\n\nCTRL-C detected. Attempting Graceful Exit ")

		#Handle the clean up
		print ("Closing [ " + nameOfFile + ".txt ] output file")
		myFile.close()
		
		print('Killing background ping to server')
		os.system('pkill -f ping')
		
		print(updateExitMsg(packetCounter, start, end) + "\n")
		
		exit(0)
		
	# Set IP address and port
	UDP_IP = get_ip_address('wlan0')
	UDP_PORT = 5005
	
	# Signal process to handle exit gracefully
	signal(SIGINT, handler)

	# Output Port and IP addr
	print ("\nYour Computer IP Address is:", UDP_IP)
	print ("Your Open Port is:", UDP_PORT)
	
	# Open socket to listen on
	sock = socket.socket(socket.AF_INET, # Internet
		             socket.SOCK_DGRAM) # UDP
	sock.bind((UDP_IP, UDP_PORT))

	# Listen and record packets from socket
	while True:
	    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	    if packetCounter == 0:
	    	 start = time.time()
	    print (data.decode())	
	    myFile.write(str(data.decode()))

	    # Update the exit message
	    packetCounter += 1
	    end = time.time()
	    #exitMsg = updateExitMsg(packetCounter, start, end)
	    

	
def get_ip_address(ifname):
	s = socket.socket(socket.AF_INET, #Internet
		          socket.SOCK_DGRAM) #UDP
	return socket.inet_ntoa(fcntl.ioctl(
		s.fileno(),
		0x8915,
		struct.pack('256s', ifname[:15].encode())
		)[20:24])


def updateExitMsg(packetCounter, start, end):
	capture = "Packets Captured: {}".format(packetCounter)
	elapsedTime = end - start
	msgTime = "Elapsed time: " + time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
	# Calculate Transmission Rate
	if packetCounter > 0:
		rr = (packetCounter * 1024) / elapsedTime
		rx = (rr * 8) / 1000
		msgTime   = "Elapsed time: " + time.strftime("%H:%M:%S", time.gmtime(elapsedTime))
		rxRate    = "RxRate: {} Bytes/Second".format(rr)
		bps       = "        {} KBits/Second".format(rx)
	else:
		msgTime   = "Elapsed time: 00:00:00  \t[ No Packets Received ]" 
		rxRate    = "RxRate: 0 Bytes/second  \t[ No Packets Received ]"
		bps       = "        0 KBits/second  \t[ No Packets Received ]"
	return "Session info:\t" + capture + "\n\t\t" + msgTime + "\n\t\t" + rxRate + "\n\t\t" + bps


#Start the Main Function
if __name__ == '__main__':
	main()







