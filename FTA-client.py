import util
import sys
import socket

def log(s):
    if debugMode:
        print s

if len(sys.argv) < 3:
    print 'Too little arguments! Must input FTA-Client.py, server IP and port (optional: \'-d\' for debug mode)'
    sys.exit()
elif len(sys.argv) > 3:
    if len(sys.argv) == 4 and sys.argv[3] == "-d":
        debugMode = True
        log("Entering debug mode...")
    else:
        print 'Too many arguments! Must input FTA-Client.py, server IP and port (optional: \'-d\' for debug mode)'
        sys.exit()
SOURCE_IP = sys.argv[1]
SOURCE_PORT = int(sys.argv[2])
window = 1
State = "NONE"
seq = 0
acknum = 0
dest_addr = (SOURCE_IP, int(SOURCE_PORT))
while (True):
   word = str(raw_input(''))
   word = str.split(word)
   if (word[0] == "connect"):
      if State == "NONE":
        #Three way handshake
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "SYN") #Send SYN. Flags = SYN, ACK, END
        s.sendto(packet, dest_addr)
        print 'Sent SYN'
        packet, addr = s.recvfrom(4096)
        print 'Received:'
        header, data, checksum = util.unpack_packet(packet)
        print 'SYN =', header[4], ' ACK = ', header[5]
        if (header[4].strip() == "True" and header[5].strip() == "True"):
          packet = util.make_packet("", SOURCE_PORT, seq, acknum, False, True, False, window, "ACK")
          s.sendto(packet, dest_addr)
          print 'Connection is established'
          State = "CONNECTED"
   if (word[0] == "get"):
      if State == "CONNECTED":
        print 'get command'
        filename = word[1]
        packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "get " + filename)
        s.sendto(packet, dest_addr)
   if (word[0] == "window"):
      window = word[1]