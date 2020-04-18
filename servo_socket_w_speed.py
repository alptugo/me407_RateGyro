import socket
import time
import threading as th

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.4.1", 80))
do_i_go=1
delay=100
def loop():
    global delay, do_i_go
    while 1:
        if do_i_go:
            for step in range(60,120):
                s.send((str(step)+"s").encode("UTF-8"))
                time.sleep(delay/1000)

t=th.Thread(target=loop)
t.start()
while 1:
    input_=input("gimme\n")
    if input_:
        delay=int(input_)
        if not do_i_go:
            do_i_go=1
    else:
        do_i_go=0
