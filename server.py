#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 333

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()

    print("received connection from " % str(address))

    message = 'Hello! Thank you for connecting to the server.' + "\r\n"
    
    clientsocket.send(message.encode('ascii'))

    clientsocket.close()
