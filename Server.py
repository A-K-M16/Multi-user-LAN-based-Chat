import socket
import sys
import threading


host = socket.gethostbyname(socket.gethostname())
port = 10000
print(host,port)

def Con(connect,x):
    u = "User"+str(x+1)+"> "
    while True:
        data = connect[x].recv(1024).decode()
        data = u+data
        if(data=="exit"):
            break
        else:
            for i in connect:
                i.sendall(data.encode())
                print(data)

    connect[x].close()
    connect.pop(x)

class SocketServer:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def Bind(self,host,port):
        self.sock.bind((host,port))
        self.sock.listen(1)
    
    def Connect(self):
        x = 0
        connect=[]
        while x<10:
            cont,client = self.sock.accept()
            connect.append(cont)
            t = threading.Thread(target=Con, args=(connect,x))
            t.start()
            x+=1
            if(len(connect)==0):
                break

        

S = SocketServer()
S.Bind(host,port)
S.Connect()