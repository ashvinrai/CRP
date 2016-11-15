
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

while (True):
   word = str(raw_input(''))
   word = str.split(word)
   if (word[0] == "connect"):
      if s is null:
         print "connect"
         packet = make_packet(source_port, dest_port, seq, acknum, syn, ack, end, window, data):
         s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         dest_addr = (SOURCE_IP, int(SOURCE_PORT))
         s.sendto(packet, dest_addr)
   if (word[0] == "get"):
      filename = word[1]
   if (word[0] == "window")
      window = word[1]