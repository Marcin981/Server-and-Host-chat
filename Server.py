import sys
import socket
import time

s = socket.socket()
host = socket.gethostname()
print("Server will start on host:",host)
port = 8080
s.bind((host,port))
print("")
print("Server done binding to host and port successfully")
print("")
print("Server is now waiting for any connections.")
print("")
s.listen(1)
conn,addr = s.accept()
print(addr,"Has connected to the server and now is online")
print("")
while 1:
    message = input(str(">>"))
    message = message.encode()
    conn.send(message)
    print("Message has been send")
    print("")
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print("Client:", incoming_message)
    print("")
