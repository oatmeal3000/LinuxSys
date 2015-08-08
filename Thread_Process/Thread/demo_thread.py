import time  
def add_sum(n):  
    global sum,mutex  
    for i in range(0,n):  
#       mutex.acquire()  
        sum+=int(i)  
        #print threading.currentThread().getName()+"#"+str(sum)+"#"+str(time.time())  
#        mutex.release()  
  
  
import threading  
threads=[]  
global sum,mutex  
mutex=threading.Lock()  
  
  
sum=0  
for i in range(100):  
    threads.append(threading.Thread(target=add_sum,args=(10000,)))  
for i in threads:  
    i.start()  
  
  
for i in threads:  
    i.join()  
print sum  
