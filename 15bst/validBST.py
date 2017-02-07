# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:43:31 2017

@author: abgoswam
"""

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right
        
def validBST(n, _min, _max):
    if n is None:
        return True
        
    if (_min is not None) and (_min >= n.value):
        return False
        
    if (_max is not None) and (_max < n.value):
        return False
        
    return validBST(n.left, _min, n.value) \
        and validBST(n.right, n.value, _max)
    
        
head = BinaryTreeNode(50)
head.insert_left(30)
head.insert_right(70)
head.left.insert_left(20)
#head.left.insert_right(100)
head.left.insert_right(35)
head.right.insert_left(70)
head.right.insert_right(80)


print(validBST(head, None, None))