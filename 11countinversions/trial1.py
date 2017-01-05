# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 13:33:26 2017

@author: abgoswam
"""

def countInversions(A):
    if A is None or len(A) == 0 or len(A) == 1:
        return (A, 0)
        
    mid = len(A) / 2
    
    left_sorted_A, num_left_inversions = countInversions(A[:mid])
    right_sorted_A, num_right_inversions = countInversions(A[mid:])
    
    i = j = 0
    sorted_A = []
    num_split_inversions = 0
    
    while((i < len(left_sorted_A)) and (j < len(right_sorted_A))):
        if left_sorted_A[i] < right_sorted_A[j]:
            sorted_A.append(left_sorted_A[i])
            i = i + 1
        else:
            num_split_inversions += len(left_sorted_A) - i
            sorted_A.append(right_sorted_A[j])
            j = j + 1

    while i < len(left_sorted_A):
        sorted_A.append(left_sorted_A[i])
        i = i + 1
        
    while j < len(right_sorted_A):
        sorted_A.append(right_sorted_A[j])
        j = j + 1
        
    total_inversions = num_left_inversions + num_right_inversions + num_split_inversions
    return (sorted_A, total_inversions)

if __name__ == "__main__":
    A = [1,5,2,4,3,6]
    (sorted_A, total_inversions) = countInversions(A) 
    print "sorted_A : {0}, total_inversions : {1}".format(sorted_A, total_inversions)
    
    B = [1,5,3,4,2,6]
    (sorted_B, total_inversions) = countInversions(B) 
    print "sorted_A : {0}, total_inversions : {1}".format(sorted_B, total_inversions)
    
    
    