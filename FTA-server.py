import socket
import util
import sys
import array
debugMode = False
def log(s):
    if debugMode:
        print s

if len(sys.argv) < 2:
    print 'Too little arguments! Must input FTA-Server.py and port (optional: \'-d\' for debug mode)'
    sys.exit()
elif len(sys.argv) > 2:
    if len(sys.argv) == 3 and sys.argv[2] == "-d":
        debugMode = True
        log("Entering debug mode...")
    else:
        print 'Too many arguments! Must input FTA-Server.py and port (optional: \'-d\' for debug mode)'
        sys.exit()

window = 5
window_pointer = 0
SOURCE_PORT = int(sys.argv[1])
seq = 0
acknum = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', SOURCE_PORT))
print 'Listening on port', SOURCE_PORT, '...'
not_connected = True
while (not_connected):
	packet, addr = s.recvfrom(4096)
	header, data, checksum = util.unpack_packet(packet)
	log('Received packet. SYN = ' +  header[4] + '. . .')
	if (header[4].strip() == "True"): #Receive SYN
		packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, True, False, window, "") #Send SYNACK
		s.sendto(packet, addr)
		log('Sent SYN ACK . . .')
		packet, addr = s.recvfrom(4096)
		header, data, checksum = util.unpack_packet(packet)
		log('Received packet. ACK = ' + header[5])
		if (header[5].strip() == "True"):
			not_connected = False
			print 'Connection is Established'

while (True):
	packet, addr = s.recvfrom(4096)
	print packet
	print addr
	header, data, checksum = util.unpack_packet(packet)
	cmd = data.split(" ")[0]
	print 'cmd =', cmd
	if cmd == "get":
		seq = 0
		filename = data.split(" ")[1]
		log('Requesting filename: ' + filename)
		##TO-DO
		##Received filename from client. Now must send the file over to client
		data = util.request_file(filename)
		packets = []
		x = 0
		while x < len(data):
			seq += 1
			packet = util.make_packet("", SOURCE_PORT, seq, acknum, False, False, False, window, data[window_pointer])
			packets.append(packet)
			window_pointer += 1
			x += 1
		print packets[0]
		s.sendto(packets[0], addr)

	##This method of getting user input cannot work; can have a diff thread for listening to user input instead
	#word = str(raw_input(''))
	#if (word[0] == "window"):
	#	window = word[1]
	#if (word[0] == "terminate"):
	#	s.close()