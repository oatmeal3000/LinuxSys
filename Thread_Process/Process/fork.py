"""a basic fork in action"""

import os

def my_fork():
    child_pid = os.fork()
    if child_pid == 0:
        print "Child Process: PID# %s" % os.getpid()
    else:
        print "Parent Process: PID# %s" % os.getpid()

if __name__ == "__main__":
    my_fork()
