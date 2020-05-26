import pyshark
import struct
import sys
import signal
import os


def main():
    """
    Packet sniffer (Eve) that uses pyshark to parse the packets
    :return:
    """
    if len(sys.argv) < 3:
        print("to few arguments")
        return
    if len(sys.argv) > 3:
        print("to many arguments")

    cap_file = sys.argv[1]
    write_file = sys.argv[2]

    try:
        print("Opening write file:",write_file)
        write_file = open(write_file,'w')
    except IOError:
        print("couldn't open write file")

    print("Opening capture file:",cap_file)
    capture = pyshark.FileCapture(cap_file,display_filter="udp && not dns && not mdns")

    packets_received = 0
    prev = ''

    print("Processing capture file")
    for packet in capture:
        if 'udp' in packet:
            if packet['udp'].dstport == '5005':
                if prev == packet.wlan.seq:
                   continue

                packets_received += 1
                prev = packet.wlan.seq
                write_file.write(bytes.fromhex(packet["data"].data).decode())

    write_file.close()
    print("Received packets:", packets_received)


if __name__ == "__main__":
    main()
