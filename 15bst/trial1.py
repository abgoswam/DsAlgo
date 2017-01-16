# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 11:45:32 2017

@author: abgoswam
"""
import random 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insertNode(self, val):
        newNode = Node(val)
        
        if self.root is None:
            self.root = newNode
        else:
            x = self.root
            y = x
            while(x):
                y = x
                if val <= x.val:
                    x = x.left
                else:
                    x = x.right
                    
            if val <= y.val:
                y.left = newNode
            else:
                y.right = newNode

    def inorderShow(self, node):
        if node is None:
            return 
            
        self.inorderShow(node.left)
        print(node.val)
        self.inorderShow(node.right)

if __name__ == "__main__":
#    myarr = [int(random.random() * 100) for _ in range(10)]
    myarr =  [25, 41, 73, 22, 13, 75, 72, 73, 58, 94]
    print(myarr)
    
    bst = BST()
    for item in myarr:
        bst.insertNode(item)
        
    bst.inorderShow(bst.root)
