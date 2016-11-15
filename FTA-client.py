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
SOURCE_IP = int(sys.argv[1])
SOURCE_PORT = int(sys.argv[2])
window = 1
State = "NONE"

while (True):
   word = str(raw_input(''))
   word = str.split(word)
   if (word[0] == "connect"):
      if State == "NONE":
         print "connect"
         seq = 0
         acknum = 0
         packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "") #Flags = SYN, ACK, END
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         dest_addr = (SOURCE_IP, int(SOURCE_PORT))
         s.sendto(packet, dest_addr)
         #Three way handshake
         State = "CONNECTED"
   if (word[0] == "get"):
      if State == "CONNECTED":
         filename = word[1]
         packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "get " + filename)
         s.sendto(packet, dest_addr)
   if (word[0] == "window")
      window = word[1]