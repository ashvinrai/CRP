import binascii
import array

class Packet:

	def __init__(self, source_port, dest_port, seq, acknum, syn, ack, end, window, contents):
		global header
		header = "%s|%i|%i|%i|%r|%r|%r|%i" % (str(source_port), int(dest_port), int(seq), int(acknum), syn, ack, end, int(window))
		print header
		self.contents = contents
		self.source_port = source_port
		self.dest_port = dest_port
		self.seq = seq
		self.acknum = acknum
		self.syn = syn
		self.ack = ack
		self.end = end
		self.window = window
		self.checksum = self.create_checksum(header, contents)


	def to_bytestream():
		return bytestream

	def to_packet():
		return unpacked

	def create_checksum(header, contents):
		return str(binascii.crc32(header + contents) & 0xffffffff)