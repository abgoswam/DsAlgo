# -*- coding: utf-8 -*-
"""
Created on Wed Feb 08 16:52:50 2017

@author: agoswami
"""

import numpy as np

for n in range(1,10):
#    m = np.zeros((n,n), dtype=np.int)
    m = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        m[0][i] = 1
        
    for i in range(1, n):
        for j in range(i, n):
            m[i][j] = m[i-1][j] + m[i][j-1]

    print("n : {0}, cat(n) : {1}".format(n, m[n-1][n-1]))    