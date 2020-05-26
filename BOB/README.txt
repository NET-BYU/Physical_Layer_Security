How to use Bob.py

In it's current config, bob will ping alice automatically on start up, then sit and listen. When received packets will output to the terminal, and be written to a file. Upon exit (ctrl-c), bob will clean up and then print the session capture stats.

Bob has no parameters to run.

Output file should default to the Documents folder, as receivedmessage.txt

The only things to note when running bob on a new computer are:
- the function get_ip_address, may need to be updated in the variable assignment
	UDP_IP = get_ip_address(wlan0). Not all the computers have wifi chips set to wlan0 (ex. wlan1)
- the file path to the save location of the file
- the ip addr of Alice, if she is not the AP, with default ip of 10.10.0.1

Nothing else should need variation


