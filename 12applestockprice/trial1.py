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


def get_max_profit_2(stock_prices_yesterday):
    
    min_price = stock_prices_yesterday[0]
    max_profit = 0
    
    for current_price in stock_prices_yesterday:
        
        # ensure min_price is the lowest price we've seen so far
        min_price = min(min_price, current_price)

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

    return max_profit


def get_max_profit_3(stock_prices_yesterday):

    # make sure we have at least 2 prices
    if len(stock_prices_yesterday) < 2:
        raise IndexError('Getting a profit requires at least 2 prices')

    # we'll greedily update min_price and max_profit, so we initialize
    # them to the first price and the first possible profit
    min_price = stock_prices_yesterday[0]
    max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]

    for index, current_price in enumerate(stock_prices_yesterday):

        # skip the first (0th) time
        # we can't sell at the first time, since we must buy first,
        # and we can't buy and sell at the same time!
        # if we took this out, we'd try to buy /and/ sell at time 0.
        # this would give a profit of 0, which is a problem if our
        # max_profit is supposed to be /negative/--we'd return 0!
        if index == 0:
            continue

        # see what our profit would be if we bought at the
        # min price and sold at the current price
        potential_profit = current_price - min_price

        # update max_profit if we can do better
        max_profit = max(max_profit, potential_profit)

        # update min_price so it's always
        # the lowest price we've seen so far
        min_price  = min(min_price, current_price)

    return max_profit

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
    
    