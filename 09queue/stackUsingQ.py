# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 22:17:08 2016

@author: abgoswam
"""

class Queue:
    def __init__(self, limit = 5):
        self.qdata = []
        self.qlimit = limit
        return
        
    def enqueue(self, val):
        if len(self.qdata) < self.qlimit:
            self.qdata.append(val)
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty() is False:
            return self.qdata.pop(0)
        else:
            return False
        
    def isEmpty(self):
        if len(self.qdata) > 0:
            return False
        else:
            return True
        
    def __repr__(self):
        return str(self.qdata)        
        
class Stack:
    def __init__(self):
        self.q = Queue()
        return
        
    def push(self, val):
        retval = self.q.enqueue(val)
        if retval is False:
            print "Underlying Queue is Full"
        
        return retval
        
    def pop(self):
        if self.q.isEmpty() is True:
            print "Unqerlying queue is empty"
            return False
            
        q_new = Queue()        
        while (True):
            x = self.q.dequeue()
            if self.q.isEmpty() == True:
                break
            else:
                q_new.enqueue(x)

        self.q = q_new
        return x
    
    def __repr__(self):
        return str(self.q)
        
if __name__ == "__main__":
    s = Stack()
    
    s.push(10)
    s.push(20)
    s.push(60)    
    s.push(40) 
    s.push(50)
    s.push(30) 
    print s
    
    s.pop()
    s.pop()
    s.pop()
    print s
    
    s.push(100)
    print s
    
    s.pop()
    s.pop()
    s.pop()
    print s
    
    s.push(200)
    print s