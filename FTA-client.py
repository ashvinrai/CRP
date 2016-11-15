
import sys

def log(s):
    if debugMode:
        print s

if len(sys.argv) < 3:
    print 'Too little arguments! Must input sensor-server-udp.py, port, and csv filename (optional: \'-d\') for debug mode'
    sys.exit()
elif len(sys.argv) > 3:
    if len(sys.argv) == 4 and sys.argv[3] == "-d":
        debugMode = True
        log("Entering debug mode...")
    else:
        print 'Too many arguments! Must input sensor-server-udp.py, port, and csv filename (optional: \'-d\') for debug mode'
        sys.exit()
SOURCE_IP = int(sys.argv[1])
SOURCE_PORT = int(sys.argv[2])

while (True):
   word = str(raw_input('type: '))
   word = str.split(word)
   if (word[0] == "connect"):
      print "connect"
   if (word[0] == "get"):
      filename = word[1]
   if (word[0] == "window")
      window = word[1]