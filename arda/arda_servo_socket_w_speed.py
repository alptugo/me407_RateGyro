import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1", 80))
do_i_go=1
delay=100

while 1:
    input_=input("gimme\n")
    if input_:
        delay=int(input_)
        s.send((str(input_) + "s").encode("UTF-8"))