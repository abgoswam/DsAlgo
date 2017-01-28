# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 13:56:24 2017

@author: abgoswam
"""


a = list('abhishekgoswami')
b = list('abhishekgoswami')

if len(a) != len(b):
    print("non rotating arrays")
else:
    n = len(a)
    for i in range(n):
        #    i will go from 0th item to (n-1)th i.e last item
        #    check if item 0-i (i+1) in "a" match the last (i+1) items in b

        if (a[: i+ 1] == b[n-1-i:]) and (a[i+1:] == b[:n-1-i]):
            print("arrays are rotation")
            


