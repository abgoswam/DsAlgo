# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:51:28 2017

@author: abgoswam
"""

def answer(x):
    s = sum(x)
    l = len(x)
    
    return l if s % l == 0 else (l-1)
    
