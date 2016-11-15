import socket
import util
import sys

def log(s):
    if debugMode:
        print s

if len(sys.argv) < 2:
    print 'Too little arguments! Must input FTA-Server.py and port (optional: \'-d\' for debug mode)'
    sys.exit()
elif len(sys.argv) > 2:
    if len(sys.argv) == 3 and sys.argv[3] == "-d":
        debugMode = True
        log("Entering debug mode...")
    else:
        print 'Too many arguments! Must input FTA-Server.py and port (optional: \'-d\' for debug mode)'
        sys.exit()

window = 1
SOURCE_PORT = int(sys.argv[1])
seq = 0
acknum = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', SOURCE_PORT))
print 'Listening on port', SOURCE_PORT, '...'
not_connected = True
while (not_connected):
	packet, addr = s.recvfrom(4096)
	print 'received packet'
	header, data, checksum = util.unpack_packet(packet)
	print 'SYN = ', header[4]
	if (header[4].strip() == "True"): #Receive SYN
		packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, True, False, window, "") #Send SYNACK
		s.sendto(packet, addr)
		print 'Sent SYN ACK'
		packet, addr = s.recvfrom(4096)
		header, data, checksum = util.unpack_packet(packet)
		print 'Received. ACK = ', header[5]
		if (header[5].strip() == "True"):
			not_connected = False
			print 'Connection is Established'

while (True):
	packet, addr = s.recvfrom(4096)
	cmd = data.split(" ")[0]
	print 'cmd =', cmd
	if cmd == "get":
		filename = data.split(" ")[1]
		print filename

	#word = str(raw_input(''))
	#if (word[0] == "window"):
	#	window = word[1]
	#if (word[0] == "terminate"):
	#	s.close()