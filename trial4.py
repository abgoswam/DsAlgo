# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 17:02:57 2017

@author: abgoswam
"""

import random

arr = []
for _ in range(10):
    x = random.randint(0,100)
    arr.append(x)
    

arr = [1,2,6,3]


minSoFar = arr[0]
maxSoFar = arr[0]
maxDiff = 0

arrmax = [maxSoFar]
arrmin = [minSoFar]
arrdiff = [maxDiff]

for i in range(1, len(arr)):
    maxDiff = max(maxDiff, max(maxSoFar - arr[i], arr[i] - minSoFar))
    maxSoFar = max(maxSoFar, arr[i])
    minSoFar = min(minSoFar, arr[i])
    
    arrmax.append(maxSoFar)
    arrmin.append(minSoFar)
    arrdiff.append(maxDiff)

print("arr : {0}".format(arr))
print("arrmin : {0}".format(arrmin))
print("arrmax : {0}".format(arrmax))
print("arrdif : {0}".format(arrdiff))
    
print(maxDiff)
print(max(arr) - min(arr))
    
    


