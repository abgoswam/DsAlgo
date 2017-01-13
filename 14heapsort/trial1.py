# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:56:33 2017

@author: abgoswam
"""
import random 

def maxheapify(A, i):
    len_A = len(A) - 1 #making adjustment for the added item 
    leftchild_index = 2*i
    rightchild_index = 2*i + 1
    
    if leftchild_index > len_A:
        return
                
    if rightchild_index > len_A:
        compare_idx = leftchild_index
    else:
        compare_idx = (leftchild_index if A[leftchild_index] >= A[rightchild_index] else rightchild_index)
        
    if A[i] >= A[compare_idx]:
        return
    else:
        temp = A[compare_idx]
        A[compare_idx] = A[i]
        A[i] = temp
        return maxheapify(A, compare_idx)

def heapsort(A):
    len_A = len(A) - 1
    
#    A[1] with A[len_A]
#    A[1] with A[len_A - 1]
#    A[1] with A[len_A - 2]
#    A[1] with A[len_A - (len_A -1)]
    
    for i in range(len_A, 0, -1):
#        swap A[1] with A[len_A - i]
        temp = A[i]
        A[i] = A[1]
        A[1] = temp
        print(A.pop())
        maxheapify(A, 1)

    print(A)        
        
if __name__ == "__main__":
    A = [random.randint(0,1000) for r in range(10)] 
    
#    A = [10, 5, 3]
    A.append(-1)
    A = A[::-1]
    print(A)
    
    len_A = len(A) -1
    mid = int(len_A/2)
    for i in range(mid, 0, -1):
        maxheapify(A, i)
        
    print(A)
    
    heapsort(A)

    
    