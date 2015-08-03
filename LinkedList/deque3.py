import collections  

print "From the right"  
d=collections.deque('abcdefg')  
while True:  
    try:  
        print d.pop(),  
    except IndexError:  
        break  
print  
  
print '\n From the left'  
d=collections.deque(xrange(6))  
while True:  
    try:  
        print d.popleft(),  
    except IndexError:  
        break  
print  
