# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 17:18:01 2017

@author: abgoswam
"""

def iisort(a):
    for i in range(1, len(a)):
        for j in range(i, 0, -1):
            if a[j] < a [j-1]:
#                swap a[j] and a[j-1]
                temp = a[j]
                a[j] = a[j-1]
                a[j-1] = temp
            else:
                break

def iqsort0(a):
    if len(a) <= 1:
        return a
        
#   we will put the a[0]th element in its correct spot, lets say a[j]
#   now, recursively sort a[:j] and a[j+1:]
    
    j = 0
    for i in range(1, len(a)):
        if a[i] > a[0]:
            continue
        else:
#            swap a[i] with a[j+1]. increment j
            temp = a[i]
            a[i] = a[j+1]
            a[j+1] = temp            
            j += 1
            
#   swap a[0] with a[j]
    temp = a[j]
    a[j] = a[0]
    a[0] = temp
        
    pre = iqsort0(a[:j])
    post = iqsort0(a[j+1:])
    return pre + [a[j]] + post
            
if __name__ == "__main__":
    a = [1,2,3,4,5,4,3,2,1]
    iisort(a) 
    print("Sorted 'a' : {0}".format(a))
    
    a = [1,2,3,4,5,4,3,2,1]
    sorted_a = iqsort0(a) 
    print("Sorted 'a' : {0}".format(sorted_a))