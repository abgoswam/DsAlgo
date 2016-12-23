# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 23:37:31 2016

@author: abgoswam
"""

class Stack:
    def __init__(self):
        self.sdata = []
        
    def push(self, val):
#        returns True if success, else False
        self.sdata.append(val)        
        return True
        
    def pop(self):
#        returns val if successful, else False
        if self.isEmpty():        
            return False
        else:
            return self.sdata.pop(len(self.sdata) - 1)
    
    def isEmpty(self):
#        returns True if empty, else False
        if len(self.sdata) > 0:
            return False
        else:
            return True
            
    def __repr__(self):
        return str(self.sdata)
        
class Queue:
    def __init__(self):
        self.stack = Stack()
        
    def enque(self, val):
#        returns True if success, else False
        return self.stack.push(val)
        
    def deque(self):
#        returns val if successful, else False
        if self.stack.isEmpty() == True:
            return False

        stack_new = Stack()            
        while(True):
            x = self.stack.pop()
            if (x is False):
                return False
                
            if self.stack.isEmpty() == True:
                break
            else:
                stack_new.push(x)

        self.stack = Stack()                
        while(not stack_new.isEmpty()):
            self.stack.push(stack_new.pop())
            
        return x

    def __repr__(self):
        return str(self.stack)
        
if __name__ == "__main__":
    q = Queue()
    
    q.enque(10)
    q.enque(20)
    q.enque(30)
                
    print q
    
    q.deque()
    q.deque()
    
    print q
    
    q.enque(40)
    q.enque(50)
    q.enque(60)
                
    print q
    
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    q.deque()
    print q