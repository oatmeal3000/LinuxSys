import socket 
import time 
   
server=('127.0.0.1',21345) 
   
msg=['first','second','third','fourth','fifth','sixth'] 
   
socks=[] 
for i in range(10): 
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    socks.append(sock) 
       
for s in socks: 
    s.connect(server) 
   
counter =0 
for m in msg: 
    for s in socks: 
        s.send('%d send %s' %(counter,m)) 
        counter=counter+1 
    for s in socks: 
        data =s.recv(1024) 
        print '%s echo %s' %(s.getpeername(),data) 
        if not data: 
            s.close() 
    time.sleep(2)
