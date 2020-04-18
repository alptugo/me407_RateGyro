import socket
import time
import threading as th

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1", 80))

while True:
    input_=input("gimme\n")
    s.send((str(input_) + "s").encode("UTF-8"))