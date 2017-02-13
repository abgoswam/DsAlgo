# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 11:09:53 2017

@author: agoswami
"""

import numpy as np

#a = np.random.randint(20, size=10)
#b = np.random.randint(20, size=10)
#
#a_sorted = sorted(a)
#b_sorted = sorted(b)

a_sorted = np.array([3, 4, 5, 6, 9])
b_sorted = np.array([0, 3, 5, 6, 9])

suml = []
for a_i in a_sorted:
    sum_ai = []
    for b_i in b_sorted:
        sum_ai.append(a_i + b_i)
    
    print(sum_ai)
    suml.append(sum_ai)
    
sumarr = np.array(suml)
sumarrtrans = np.transpose(sumarr)