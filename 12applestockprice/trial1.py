# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 15:15:11 2017

@author: abgoswam
"""

import itertools

def stream_min(stream):
    m = stream[0]
    for item in stream:
        m = min(m, item)
        yield m
        
def stream_diff(ss, tt):
    for s, t in itertools.izip(ss, tt):
        yield (s - t)
    
def get_max_profit_stream(stock_prices_yesterday):
    if stock_prices_yesterday is None or len(stock_prices_yesterday) == 0:
        return 0
        
    maxProfit = 0
    for item in stream_diff(stock_prices_yesterday, stream_min(stock_prices_yesterday)):
#        print item        
        maxProfit = max(maxProfit, item)
        
    return maxProfit

def get_max_profit(stock_prices_yesterday):
    if stock_prices_yesterday is None or len(stock_prices_yesterday) == 0:
        return 0
        
    stock_prices_min = [stock_prices_yesterday[0]]
    minSoFar = stock_prices_yesterday[0]
    
    for i in range(1, len(stock_prices_yesterday)):
        minSoFar = min(minSoFar, stock_prices_yesterday[i])
        stock_prices_min.append(minSoFar)
        
    maxProfit = 0
    for i in range(1, len(stock_prices_yesterday)):
        profit = stock_prices_yesterday[i] - stock_prices_min[i]
        maxProfit = max(maxProfit, profit)
        
    return maxProfit


if __name__ == "__main__":
    stock_prices_yesterday = [10, 7, 5, 8, 11, 9]
    max_profit = get_max_profit(stock_prices_yesterday)
    max_profit_stream = get_max_profit_stream(stock_prices_yesterday)
    print "max profit : {0}".format(max_profit)
    print "max profit stream : {0}".format(max_profit_stream)
    
    stock_prices_yesterday = [1,2,3,4,5,6]
    max_profit = get_max_profit(stock_prices_yesterday)
    max_profit_stream = get_max_profit_stream(stock_prices_yesterday)
    print "max profit : {0}".format(max_profit)
    print "max profit stream : {0}".format(max_profit_stream)
    
    stock_prices_yesterday = [6,5,4,3,2,1]
    max_profit = get_max_profit(stock_prices_yesterday)
    max_profit_stream = get_max_profit_stream(stock_prices_yesterday)
    print "max profit : {0}".format(max_profit)
    print "max profit stream : {0}".format(max_profit_stream)
    
    