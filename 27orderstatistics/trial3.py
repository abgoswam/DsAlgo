# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 12:14:41 2017

@author: agoswami
"""

def cornercasemedian(A, A_left, A_right, B, B_left, B_right):
    X = sorted(A[A_left : A_right+1] + B[B_left: B_right + 1])
    X_med = len(X)/2 if len(X) % 2 == 1 else (len(X)/2 - 1)
    
    median = X[X_med] if len(X) % 2 == 1 else (X[X_med] + X[X_med + 1]) / 2.0
    return median
            
def med(A, A_left, A_right, B, B_left, B_right):
    print(A, A_left, A_right, B, B_left, B_right)
    
    A_numItems = (A_right - A_left) + 1
    B_numItems = (B_right - B_left) + 1
    
    if (A_numItems <= 2) or (B_numItems <= 2):
        return cornercasemedian(A, A_left, A_right, B, B_left, B_right)
    
    A_med = A_left + (A_numItems / 2 if A_numItems % 2 == 1 else (A_numItems / 2) - 1)
    B_med = B_left + (B_numItems / 2 if B_numItems % 2 == 1 else (B_numItems / 2) - 1)
    
    if A[A_med] <= B[B_med]:
        numitemsdiscard = A_med - A_left
        return med(A, A_med, A_right, B, B_left, B_right - numitemsdiscard)
    else:
        numitemsdiscard = B_med - B_left
        return med(A, A_left, A_right - numitemsdiscard, B, B_med, B_right)
        
A = [1,2,3]
B = []

median = med(A, 0, len(A)-1, B, 0, len(B)-1)
print(median) 