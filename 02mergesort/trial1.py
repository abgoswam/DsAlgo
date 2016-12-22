# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 09:19:27 2016

@author: abgoswam
"""

def mergeSort(A):
    if ((A is None) or len(A) == 1):
        return A
        
    mid = len(A) / 2
    
    left_sorted = mergeSort(A[:mid])
    right_sorted = mergeSort(A[mid:])
    
    i = j = 0
    A_sorted = []
    
    while((i < len(left_sorted)) and (j < len(right_sorted))):
        if left_sorted[i] < right_sorted[j]:
            A_sorted.append(left_sorted[i])
            i = i + 1
        else:
            A_sorted.append(right_sorted[j])
            j = j + 1

    while i < len(left_sorted):
        A_sorted.append(left_sorted[i])
        i = i + 1
        
    while j < len(right_sorted):
        A_sorted.append(right_sorted[j])
        j = j + 1
        
    return A_sorted
    

if __name__ == "__main__":
    A = [3,2,4,1,5, 0]
    A_sorted = mergeSort(A)
    
    print("Sorted A : {0}".format(A_sorted))