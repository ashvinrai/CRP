import util
import sys
import socket

debugMode = False
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
acknum = 1
dest_addr = (SOURCE_IP, int(SOURCE_PORT))
while (True):
   word = str(raw_input('Commands: connect, get <filename>, window <size>: '))
   word = str.split(word)
   if (word[0] == "connect"):
      if State == "NONE":
        #Three way handshake
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "SYN") #Send SYN. Flags = SYN, ACK, END
        s.sendto(packet, dest_addr)
        log('Packet sent. SYN = True')
        packet, addr = s.recvfrom(4096)
        header, data, checksum = util.unpack_packet(packet)
        log('Received packet. SYN =' + header[4] + ' ACK = ' + header[5] + '. . .')
        if (header[4].strip() == "True" and header[5].strip() == "True"):
          packet = util.make_packet("", SOURCE_PORT, seq, acknum, False, True, False, window, "ACK")
          s.sendto(packet, dest_addr)
          log('Packet sent. ACK = True')
          print 'Connection is established'
          State = "CONNECTED"
   if (word[0] == "get"):
      if State == "CONNECTED":
        acknum = 0
        filename = word[1]
        log('get command with filename: ' + filename)
        packet = util.make_packet("", SOURCE_PORT, seq, acknum, True, False, False, window, "get " + filename)
        s.sendto(packet, dest_addr)
        ##TO-DO
        ##Sent filename to server. Server must now send the file back
        packets = []
        end = False
        while end != True:
          x = 0
          while x < window:
            packet, addr = s.recvfrom(4096)
            print packet
            header, data, checksum = util.unpack_packet(packet)
            if str(acknum) == header[2] and header[4] and util.check_checksum(packet):
              packets.append(packet)
              x += 1
              acknum += 1 
              if header[6] == "True":
                packet = util.make_packet("", SOURCE_PORT, seq, acknum, False, True, True, window, "END")
                s.sendto(packet, dest_addr)
                x = window
                end = True
            else:
              x = window
              print "missing or damaged packet"
          packet = util.make_packet("", SOURCE_PORT, seq, acknum, False, True, False, window, "ACK")
          s.sendto(packet, dest_addr)
      else:
        print 'Cannot get a file: You did not create a connection yet!'
   if (word[0] == "window"):
      window = word[1]