# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 10:31:05 2016

@author: abgoswam
"""

import matplotlib.pyplot as plt
import pandas

def findSwapValues(a1, a2):
    target = getTarget(a1, a2)
    if target == None:
        return None
    else:
        for i in range(len(a1)):
            for j in range(len(a2)):
                if (a1[i] - a2[j]) == target:
                    return (a1[i], a2[j])

    return (None, None)

def findDifference(a1, a2):
    target = getTarget(a1, a2)
    if target == None:
        return None
    else:
        s2 = set()
        for item in a2:
            s2.add(item)

        for item in a1:
            item_dual = item - target
            if item_dual in s2:
                return (item, item_dual)

        return (None, None)

def findAlternateUsingSort(a1, a2):
    target = getTarget(a1, a2)
    if target == None:
        return None
    else:
        a1.sort()
        a2.sort()

        i = 0
        j = 0
        while ((i < len(a1)) and (j < len(a2))):
            x = a1[i] - a2[j]
            if (x > target):
                j = j + 1
            elif (x < target):
                i = i + 1
            else:
                return (a1[i], a2[j])

        return (None, None)


def getTarget(a1, a2):
    sum1 = sum(a1)
    sum2 = sum(a2)

    if (sum1 - sum2) %2 != 0:
        return None
    else:
        return (sum1 - sum2) / 2

if __name__ == "__main__":
#    array1 = [4,1,2,1,1,2]
#    array2 = [3,6,3,3]
#
#    array1 = [4,2]
#    array2 = [3,7,3,3]

    array1 = [4,4]
    array2 = [3,7,3,3]

    print getTarget(array1, array2)

    (x, y) = findSwapValues(array1, array2)
    if x == None:
        print("No values found to swap using 'findSwapValues'")
    else:
        print("Values to Swap : {0}, {1}".format(x, y))

    (x, y) = findDifference(array1, array2)
    if x == None:
        print("No values found to swap using 'findDifference'")
    else:
        print("Values to Swap : {0}, {1}".format(x, y))


    (x, y) = findAlternateUsingSort(array1, array2)
    if x == None:
        print("No values found to swap using 'findAlternateUsingSort'")
    else:
        print("Values to Swap : {0}, {1}".format(x, y))
