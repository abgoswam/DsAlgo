# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:19:36 2017

@author: abgoswam
"""

T = raw_input().strip()
T = int(T)
#print(T)

for i in range(T):
    N = int(raw_input().strip())
    prices = raw_input().strip().split(' ')
    prices = map(int, prices)
    
    max_prices_future = [0 for _ in range(len(prices))]
#    print(max_prices_future)
    
    maxSoFarRev = 0
    for idx, item in reversed(list(enumerate(prices))):
        maxSoFarRev = max(item, maxSoFarRev)
        max_prices_future[idx] = maxSoFarRev
        
#    print(max_prices_future)
        
    max_profit = 0
    for i in range(len(prices)):
        max_profit += (max_prices_future[i] - prices[i])
        
    print(max_profit)