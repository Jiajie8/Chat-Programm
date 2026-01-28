import socket
import time

#Use IP address of Socket server and non-privileged port >1023
addr=('192.168.0.100',2222)

#Client Socket Objekt erzeugen
client=socket.socket()

#Client Socket Objekt mit Server verbinden
client.connect(addr)

#Daten senden
for i in range (1,10):
    client.send("Hello_world".encode("UTF-8"))

client.close()