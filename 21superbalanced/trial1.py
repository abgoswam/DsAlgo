# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:19:34 2017

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

class Queue:
    def __init__(self):
        self.qentries = []
        
    def isEmpty(self):
        if len(self.qentries) <= 0:
            return True
        else:
            return False
            
    def enque(self, item):
        self.qentries.append(item)
        
    def deque(self):
        dequed_item = self.qentries.pop(0)
        return dequed_item
        
        
def dfs(root):
    if root is None:
        return 
        
    print("{0}.".format(root.value))
    dfs(root.left)
    dfs(root.right)
    
    return

def dfs_leafheights(root, h, leaf_heights):
    if root is None:
        return leaf_heights
        
    print("{0}.".format(root.value))
    
    if (root.left is None) and (root.right is None):
#        i.e. tree rooted at 'root' is leaf
        leaf_heights.add(h)
        
    dfs_leafheights(root.left, h+1, leaf_heights)
    dfs_leafheights(root.right, h+1, leaf_heights)
    
    return leaf_heights

def bfs(root):
    q = Queue()
    q.enque(root)
    
    while(q.isEmpty() is False):
        n = q.deque()
        print("{0}..".format(n.value))

        if n.left is not None:
            q.enque(n.left)
            
        if n.right is not None:
            q.enque(n.right)



if __name__ == "__main__":
    node1 = root = BinaryTreeNode(1)
    node2 = node1.insert_left(2)
    node3 = node1.insert_right(3)
#    node4 = node3.insert_left(4)
    node5 = node3.insert_right(5)
#    node6 = node4.insert_left(6)
#    node7 = node4.insert_right(7)
#    node8 = node5.insert_left(8)
    node9 = node5.insert_right(9)

    print("Depth First")    
    dfs(node1)
    
    print("Breadth First")
    bfs(node1)
    
    leaf_heights = dfs_leafheights(node1, 0, set())
    print("Max Difference in Height : {0}".format(max(leaf_heights) - min(leaf_heights)))
