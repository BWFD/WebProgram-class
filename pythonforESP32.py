import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)

try :
    s.connect(('192.168.4.1', 80))
except:
    print("ERROR!")
    exit()

def sendMes() :
    while(true):
        s.sendall(input())

def revMes() :
    while(true) :
        data = s.recv(1024)
        if data!='' :
            print("recv : "+ data)

t1 = threading.Thread(target=sendMes)
t1.start()

t2 = threading.Thread(target=revMes)
t2.start() 