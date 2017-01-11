# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 19:04:36 2017

@author: abgoswam
"""

def qsort0(A, p, r):
    if p < r:
        q = partition(A, p, r)
        qsort0(A, p, q-1)
        qsort0(A, q+1, r)
        
def partition(A, p, r):
    key = A[r]
    
    i = p - 1
    j = p
    while (j < r):
        if A[j] < key :
#            swap values at A[i+1] and A[j]
#            so A[i+1] is now less than 'key', need to update i to preserve the invariant
            temp = A[i+1]
            A[i+1] = A[j]
            A[j] = temp            
            i += 1
            
        j += 1
        
    A[r] = A[i+1]
    A[i+1] = key
    return i + 1
    
if __name__ == "__main__":
    A = [2,8,7,1,3,5,6,4]

    print A
    qsort0(A, 0, len(A) -1)
    
    print A