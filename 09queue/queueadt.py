# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 19:22:36 2016

@author: abgoswam
"""

class Queue:
    def __init__(self, limit = 5):
        self.que = []
        self.size = 0
#        self.front = None
#        self.rear = None
        self.limit = limit
        
    def enqueue(self, val):
        if self.size >= self.limit:
            print "Queue Full"
            return
        else:
            self.que.append(val)
            
#        if self.front is None:
#            self.rear = self.front = 0
#        else:
#            self.rear = self.size

        self.size += 1            
        print "Queue Status : {0}. Size : {1}".format(self.que, self.size)
        
    def dequeue(self):
        if self.size <= 0:
            print "Queue Empty"
            return
        else:
            self.que.pop(0)
            self.size -= 1
        
        print "Queue Status : {0}. Size : {1}".format(self.que, self.size)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("p")
    q.enqueue("q")
    q.enqueue("r")
    q.enqueue("s")
    q.enqueue("t")
    
    q.dequeue()
    q.dequeue()
    