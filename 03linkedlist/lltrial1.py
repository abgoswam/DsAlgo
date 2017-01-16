# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 11:52:12 2017

@author: abgoswam
"""

import random

class Node():
    def __init__(self, elem):
        self.val = elem
        self.next = None
    
class LL():
    def __init__(self):
        self.head = None
        
    def insertNode(self, elem):
        newNode = Node(elem)
        if self.head is None:
            self.head = newNode
        else:
            p = self.head
            while(p.next is not None):
                p = p.next
                
            p.next = newNode

    def reverse(self, node):
        if node is None:
            return None
            
        if node.next is None:
            self.head = node
        else:
            tail = self.reverse(node.next)
            tail.next = node
            
#        node.next = None
        return node
            
            
    def __str__(self):
        p = self.head
        
        vals = []
        while p is not None:
            vals.append(p.val)
            p = p.next
            
        return ','.join([str(i) for i in vals])
          
     
if __name__ == "__main__":
    
    randomVals = [int(random.random() * 100) for _ in range(2)]
    print(randomVals)
    
    mylist = LL()
    for val in randomVals:
        mylist.insertNode(val)
    print(mylist)
    
    mylist.reverse(mylist.head)
    print(mylist)
    
        