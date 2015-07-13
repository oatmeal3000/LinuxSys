import socket 
import select 
import Queue 
   
server=('127.0.0.1',21345) 
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
sock.setblocking(False) 
sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) 
sock.bind(server) 
sock.listen(5) 
   
rlists=[sock] 
wlists=[] 
msg_que={} 
   
timeout=10 
   
while True:  
    rs,ws,es=select.select(rlists,wlists,rlists,timeout) 
   
    if not(rs or ws or es): 
        print 'timeout...' 
        continue 
       
    for s in rs: 
        if s is sock: 
            conn,addr=s.accept() 
            print 'connect by',addr 
            conn.setblocking(False) 
            rlists.append(conn) 
            msg_que[conn]=Queue.Queue()             
        else: 
            data =s.recv(1024) 
            if data: 
                print data 
                msg_que[s].put(data) 
                if s not in wlists: 
                    wlists.append(s) 
            else: 
                if s in wlists: 
                    wlists.remove(s) 
                rlists.remove(s) 
                s.close 
                del msg_que[s] 

    for  s in ws: 
        try: 
            msg=msg_que[s].get_nowait() 
        except Queue.Empty: 
            print 'msg empty' 
            wlists.remove(s) 
        else: 
            s.send(msg) 
    for s in es: 
        print 'except',s.getpeername() 
        if s in rlists: 
            rlists.remove(s) 
        if s in wlists: 
            wlists.remove(s)         
        s.close 
        del msg_que[s] 
