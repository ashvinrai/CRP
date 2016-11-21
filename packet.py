import binascii
import array

class Packet:
	header = ""
	contents = ""
	source_port = ""
	dest_port = 0
	seq = 0
	acknum = 0
	syn = 0
	ack = 0
	end = 0
	window = 0

	def __init__(self, source_port, dest_port, seq, acknum, syn, ack, end, window, contents):
		self.header = "%s|%i|%i|%i|%r|%r|%r|%i" % (str(source_port), int(dest_port), int(seq), int(acknum), syn, ack, end, int(window))
		self.contents = contents
		self.source_port = source_port
		self.dest_port = dest_port
		self.seq = seq
		self.acknum = acknum
		self.syn = syn
		self.ack = ack
		self.end = end
		self.window = window
		self.checksum = create_checksum(self.header+self.contents)


	def to_bytestream():
		return bytestream

	def to_packet():
		return unpacked

	def create_checksum(packet):
		return str(binascii.crc32(packet) & 0xffffffff)