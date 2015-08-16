import multiprocessing
from time import sleep

def writer_proc(q):      
    try:         
        q.put(1, block = False) 
    except:         
        pass   

def reader_proc(q):      
    try:         
        print q.get(block = False) 
    except:         
        pass

if __name__ == "__main__":
    q = multiprocessing.Queue()
    writer = multiprocessing.Process(target=writer_proc, args=(q,))  
    writer.start()   
 
    sleep(1)

    reader = multiprocessing.Process(target=reader_proc, args=(q,))  
    reader.start()  

    reader.join()  
    writer.join()
