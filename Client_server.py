import sys
import time
import socket

s = socket.socket()
host = input((str("Please enter the hostname of the server:")))
port = 8080
s.connect((host,port))
print("Connected to the server")
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print("Server:",incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode()
    s.send(message)
    print("Message has been send")
    print("")
