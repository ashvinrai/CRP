 def make_packet(source_port, dest_port, seq, acknum, syn, ack, end, window, data):
 	flags = 0 | (SYN << 2) | (ACK << 1) | END 
    header = "%H|%H|%I|%I|%r|%r|%r|%S" % (source_port, dest_port, seq, acknum, int(syn), int(ack), int(end), window) 
    checksum = create_checksum(header + data)
    packet = "%s|%s|%s" % (header, data, checksum)
    #SYN, ACK, END = 0, 1, 1
    #00000000 | (SYN << 2) | (ACK << 1) | END 
    return packet

def unpack_packet(self, packet):
	parts = packet.split('|')
	header = parts[0:8]
	data = parts[8]
	checksum = parts[-1]
	return header, data, checksum

def create_checksum(packet):
	return str(binascii.crc32(packet) & 0xffffffff)

def check_checksum(packet):
	header, data, checksum = unpack_packet(packet)
	return create_checksum(header + data) == checksum