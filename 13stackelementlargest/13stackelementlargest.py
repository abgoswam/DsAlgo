# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:31:02 2017

@author: abgoswam
"""

class Stack:
    
#    initialize an empty list
    def __init__(self):
        self.items = []
        
#   push a new item to the last index
    def push(self, item):
        self.items.append(item)
        
#    remove the last item
    def pop(self):
        if not self.items:
            return None
            
        return self.items.pop()
        
    def peek(self):
        if not self.items:
            return None
            
        return self.items[-1]
        
class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()
        
    def push(self, item):
        self.stack.push(item)
        
        if not self.maxs_stack.items:
            self.maxs_stack.items.append(item)
            
        top = self.maxs_stack.peek()
        if item > top:
            self.maxs_stack.items.append(item)
        else:
            self.maxs_stack.items.append(top)
            
    def pop(self):        
        self.maxs_stack.pop()
        return self.stack.pop()
        
    def get_max(self):
        return self.maxs_stack.peek()
        
if __name__ == "__main__":
    ms = MaxStack()
    ms.push(1)
    ms.push(2)
    print ms.get_max()
    ms.push(3)
    print ms.get_max()
    ms.push(-1)
    print ms.get_max()
    ms.push(10)
    print ms.get_max()
    ms.pop()
    print ms.get_max()
    
        
        
        
        
        
