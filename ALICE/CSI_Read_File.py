import CSI_Class
import CSI_Python_Parser
import CSI_Plot
import struct
import os
import sys


def parse_info(file_name):
    """
    Open the CSI log file and read the data from it into a list of objects
    :param file_name: name of the file to be opened and read
    :return: List of CSI objects
    """

    # try to open the file, if it fails exit the program
    try:
        f = open(file_name, "rb")
    except IOError:
        print("Couldn't open file!")
        sys.exit()

    # get the length of the entire file
    len_of_file = os.stat(file_name).st_size

    csi_packet_info = []
    cur = 0

    one_byte = struct.Struct("=B")
    two_byte = struct.Struct("=H")

    while cur < (len_of_file - 4):  # loop until the end of the file is reached

        cur_csi_obj = CSI_Class.CSI()  # Create new CSI obj to fill

        # read all the meta data from the current
        cur_csi_obj.buf_len = two_byte.unpack(f.read(2))[0]

        time_stamp = f.read(26)
        cur_csi_obj.time_stamp = time_stamp.decode("utf-8")

        tfs_stamp = f.read(8)
        cur_csi_obj.tfs_stamp = struct.unpack("=Q", tfs_stamp)[0]

        cur_csi_obj.csi_len = two_byte.unpack(f.read(2))[0]

        cur_csi_obj.channel = two_byte.unpack(f.read(2))[0]

        cur_csi_obj.phyerr = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.noise = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.rate = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.chan_bw = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.num_tones = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.nr = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.nc = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.rssi = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.rssi_0 = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.rssi_1 = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.rssi_2 = one_byte.unpack(f.read(1))[0]

        cur_csi_obj.payload_len = two_byte.unpack(f.read(2))[0]

        cur += 53

        # Check to see if there is any CSI data and if so read it from the file
        if cur_csi_obj.csi_len > 0:
            csi_buff = bytearray(f.read(cur_csi_obj.csi_len))
            cur_csi_obj.data = CSI_Python_Parser.record_CSI_data(
                csi_buff, cur_csi_obj.nr, cur_csi_obj.nc, cur_csi_obj.num_tones, True
            )
            cur += cur_csi_obj.csi_len

        # implement payload processing if needed, else just going to skip those bytes
        cur += cur_csi_obj.payload_len
        f.read(cur_csi_obj.payload_len)

        # Create a list of CSI packets
        csi_packet_info.append(cur_csi_obj)

        if cur + 420 > len_of_file:
            break
    return csi_packet_info


def main():
    if len(sys.argv) < 2:
        print("Provide file name to be processed")
        return
    if len(sys.argv) > 2:
        print("To many arguments")
        return
    file_name = sys.argv[1]

    csi_data = parse_info(file_name)

    # TODO: if info needs to be processed, do so right here

    print("num packets: ", len(csi_data))
    for i in range(0, 10):
        if len(csi_data[i].data) == 2:
            CSI_Plot.draw_two_stem_plots(csi_data[i].data)
        elif len(csi_data[i].data) == 4:
            CSI_Plot.draw_four_stem_plots(csi_data[i].data)

    print("done")

if __name__ == "__main__":
    main()
