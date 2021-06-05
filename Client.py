import socket
import sys
import threading
import tkinter as tk

def Send():
    global stream_socket,root
    data = e1.get()
    e1.delete(0,'end')
    stream_socket.send(data.encode())

    
root = tk.Tk()
root.title("Chat")
root.configure(background='#41B3A3')

msg = ["","","","","",""]
l1 = tk.Label(root,text=msg[0],font=("Helvetica", 15),width=50,anchor="w",bg="#E8A87C",fg="#FFFFFF")
l1.grid(row=0,columnspan=2,pady=(20,0))
l2 = tk.Label(root,text=msg[1],font=("Helvetica", 15),width=50,anchor="w",bg="#E27D60",fg='#FFFFFF')
l2.grid(row=1,columnspan=2)
l3 = tk.Label(root,text=msg[2],font=("Helvetica", 15),width=50,anchor="w",bg="#E8A87C",fg="#FFFFFF")
l3.grid(row=2,columnspan=2)
l4 = tk.Label(root,text=msg[3],font=("Helvetica", 15),width=50,anchor="w",bg="#E27D60",fg='#FFFFFF')
l4.grid(row=3,columnspan=2)
l5 = tk.Label(root,text=msg[4],font=("Helvetica", 15),width=50,anchor="w",bg="#E8A87C",fg="#FFFFFF")
l5.grid(row=4,columnspan=2)
l6 = tk.Label(root,text=msg[5],font=("Helvetica", 15),width=50,anchor="w",bg="#E27D60",fg='#FFFFFF')
l6.grid(row=5,columnspan=2)
e1 = tk.Entry(root,width=45,font=("Helvetica", 12) ,bg='#E7717D',fg='#FFFFFF')
e1.grid(row=6,column=0, padx = (20,10), pady=(10,20))
b1 = tk.Button(root,text="Send",width=20,command=Send,bg='#659BDB',fg='#FFFFFF')
b1.grid(row=6,column=1,padx=(0,20), pady  = (10,20))


def recv(s,arr):
    while True:
        try:
            data = s.recv(1024).decode()
            arr.pop(0)
            arr.append(data)
            #print(arr)
            l1.config(text=arr[0])
            l2.config(text=arr[1])
            l3.config(text=arr[2])
            l4.config(text=arr[3])
            l5.config(text=arr[4])
            l6.config(text=arr[5])
        except:
            break
    s.close()


host = input("Enter server ip address :")
port = 10000
stream_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ((host,port))
stream_socket.connect(server_address)

a = threading.Thread(target=recv,args=(stream_socket,msg,))
a.start()
root.mainloop()