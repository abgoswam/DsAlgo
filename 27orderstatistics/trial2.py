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


