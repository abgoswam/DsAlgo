# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:16:46 2016

@author: abgoswam
"""

def cubic(X):
    maxSoFar = 0
    lowIndex = upperIndex = -1
    
    for i in range(len(X)):
        for j in range(i, len(X)):
            sumInner = 0
            for k in range(i, j+1):
                sumInner += X[k]
                
            if sumInner > maxSoFar:
                lowIndex = i
                upperIndex = j
                maxSoFar = sumInner
                
    
    return maxSoFar, lowIndex, upperIndex
 
def scanning(X):
    maxSoFar = 0
    for i in range(len(X)):
        sumScan = 0
        for j in range(i, len(X)):
            sumScan += X[j]
            if sumScan > maxSoFar:
                lowIndex = i
                upperIndex = j
                maxSoFar = sumScan
                
    return maxSoFar, lowIndex, upperIndex
                
def divideConquer(X):
    if ((X is None) or len(X) <= 0):
        return 0
    elif (len(X) == 1):
        return (X[0] if X[0] >= 0 else 0)
    else:
        mid = len(X) / 2
        
        maxLeftSum = divideConquer(X[:mid])
        maxRightSum = divideConquer(X[mid:])
        
        leftIdx = mid - 1
        maxLeftPivot = 0
        sumScan = 0
        while(leftIdx >= 0):
            sumScan += X[leftIdx]
            if sumScan > maxLeftPivot:
                maxLeftPivot = sumScan

            leftIdx -= 1            
            
        rightIdx = mid        
        maxRightPivot = 0
        sumScan = 0
        while(rightIdx < len(X)):
            sumScan += X[rightIdx]
            if sumScan > maxRightPivot:
                maxRightPivot = sumScan     
                
            rightIdx += 1
            
        maxStraddleSum = maxLeftPivot + maxRightPivot
        
        return max(maxLeftSum, maxRightSum, maxStraddleSum)
   
if __name__ == "__main__":
    X = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]    
    
    maxSubsequenceSum , lowIndex, upperIndex = cubic(X)
    print "{0}:{1}:{2}".format(maxSubsequenceSum, lowIndex, upperIndex)
            
    maxSubsequenceSum , lowIndex, upperIndex = scanning(X)
    print "{0}:{1}:{2}".format(maxSubsequenceSum, lowIndex, upperIndex)
    
    maxSubsequenceSum = divideConquer(X)
    print "{0}".format(maxSubsequenceSum)