import os
import signal
from time import sleep

def onsignal_term(a, b):
    print 'received SIGTERM signal'


signal.signal(signal.SIGTERM, onsignal_term)


def onsignal_usr1(a, b):
    print 'received SIGUSR1 signal'


signal.signal(signal.SIGUSR1, onsignal_usr1)

while 1:
    print 'my process id ', os.getpid()
    sleep(5)
