# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:36:24 2017

@author: agoswami
"""

import numpy as np

def space1timen(a_sorted, b_sorted):
    total_len = len(a_sorted) + len(b_sorted)
    m_idx = (total_len/2) if (total_len%2==1) else ((total_len/2)-1)
    i = 0
    j = 0
    for k in range(m_idx):
        if a_sorted[i] <= b_sorted[j]:
            i += 1
        else:
            j += 1
    
    if total_len % 2 == 1:    
        median = a_sorted[i] if (a_sorted[i] <= b_sorted[j]) else b_sorted[j]    
    else:
        median = (a_sorted[i] + b_sorted[j]) / 2.0

    print(median)
 
def spacentimen(a_sorted, b_sorted):
    i = 0
    j = 0
    ab_sorted = []
    while (i < len(a_sorted)) and (j < len(b_sorted)):
        if a_sorted[i] <= b_sorted[j]:
            ab_sorted.append(a_sorted[i])
            i += 1
        else:
            ab_sorted.append(b_sorted[j])
            j += 1
            
    while(i < len(a_sorted)):
        ab_sorted.append(a_sorted[i])
        i += 1
        
    while(j < len(b_sorted)):
        ab_sorted.append(b_sorted[j])
        j += 1
        
    print(ab_sorted)
    total_len = len(ab_sorted)
    
    m_idx = (total_len/2) if (total_len%2==1) else ((total_len/2)-1)
    if total_len % 2 == 1:    
        median = ab_sorted[m_idx]    
    else:
        median = (ab_sorted[m_idx] + ab_sorted[m_idx + 1]) / 2.0

    print(median)

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
    
a = np.random.randint(20, size=5)
b = np.random.randint(30, size=6)
a_sorted = sorted(a)
b_sorted = sorted(b)
#a_sorted = np.array([3, 4, 5, 6])
#b_sorted = np.array([0, 3, 6, 6, 9])
print("a_sorted : {0}".format(a_sorted))
print("b_sorted : {0}".format(b_sorted))
ab = np.concatenate([a,b])
print("{0}. len : {1}".format(sorted(ab), len(ab)))
print("-------")
spacentimen(a_sorted, b_sorted)
space1timen(a_sorted, b_sorted)

x = med(a_sorted, 0, len(a_sorted)-1, b_sorted, 0, len(b_sorted)-1)
print(x)


