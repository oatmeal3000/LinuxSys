import threading
from time import sleep

semaphore = threading.Semaphore(2)
 
def func():
    if semaphore.acquire():
        print (threading.currentThread().getName() + ' get semaphore')
        sleep(3)
        semaphore.release()
        print (threading.currentThread().getName() + ' release semaphore')
       
       
for i in range(4):
  t1 = threading.Thread(target=func)
  t1.start()
