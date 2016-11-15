import socket

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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', SOURCE_PORT))
print 'Listening on port', UDP_SOURCE_PORT, '...'
while (True):
	word = str(raw_input(''))
   if (word[0] == "window")
      window = word[1]
   if (word[0] == "terminate")
      s.close()