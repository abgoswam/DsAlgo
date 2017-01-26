# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:49:21 2017

@author: abgoswam
"""

def coinChangeCount(N, M_vec):
    if len(M_vec) <= 0:
        return 0
        
    if N < 0:
        return 0
    elif N == 0:
        return 1
    else:
        return coinChangeCount(N, M_vec[:-1]) + coinChangeCount(N - M_vec[-1], M_vec)

def coinChangeCountIter(N, M_vec): 
    M = len(M_vec)
    
#    n = np.zeros((N + 1, M + 1))
    n = [[0 for x in range(M+1)] for y in range(N+1)]
    
    for j in range(1, M+1):
        n[0][j] = 1
        
    for i in range(1, N+1):
        for j in range(1, M+1):
            n[i][j] = n[i][j-1] + (n[i - M_vec[j-1]][j] if (i-M_vec[j-1] >= 0) else 0)
            
    return int(n[N][M])
       
if __name__ == "__main__":
    N, M = raw_input().strip().split(' ')
    M_vec = raw_input().strip().split(' ')

    N = int(N)
    M = int(M)
    M_vec = map(int, M_vec)

#    print(coinChangeCount(N, M_vec))
    print(coinChangeCountIter(N, M_vec))
    
    