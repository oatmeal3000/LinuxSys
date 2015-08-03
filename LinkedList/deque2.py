import collections  

d1=collections.deque()  
d1.extend('abcdefg')  

print 'extend:',d1  
d1.append('h')  
print 'append:',d1  

# add to left  
d2=collections.deque()  
d2.extendleft(xrange(6))  

print 'extendleft:',d2  
d2.appendleft(6)  
print 'appendleft:',d2 
