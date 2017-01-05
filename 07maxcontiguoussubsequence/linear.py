# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 12:53:01 2017

@author: abgoswam
"""
import itertools

def max_sum_subsequence(seq):
    maxsofar = 0
    maxendinghere = 0
    for s in seq:
        maxendinghere = max(maxendinghere + s, 0)
        maxsofar = max(maxendinghere, maxsofar)
    
    return maxsofar

def stream_accumulate(stream):
    total = 0
    for s in stream:
        total += s
        yield total
        
def stream_floor(stream):
    m = 0
    for s in stream:
        m = min(m, s)
        yield m

def stream_diff(s, t):
    for ss, tt in itertools.izip(s, t):
        yield ss - tt

def stream_ceil(stream):
    m = 0
    for s in stream:
        m = max(m , s)
        yield m
    
def stream_last(stream, default=None):
    s = default    
    for s in stream:
        pass
    
    return s
    
if __name__ == "__main__":
    seq = [0,-1, -1, -1, 1, 1, 1, -1]
    maxsumsub = max_sum_subsequence(seq)
    print "max sum subsequence : {0}".format(maxsumsub)
    
    accu1, accu2 = itertools.tee(stream_accumulate(seq))
    
#    technique 1
#    maxsumsub2 = stream_last(stream_ceil(stream_diff(accu1, stream_floor(accu2))))
#    print "max sum subsequence streaming : {0}".format(maxsumsub2)
    
#    technique 2
    m = 0
    for s in stream_diff(accu1, stream_floor(accu2)):
        m = max(m, s)
        
    print "max sum subsequence streaming : {0}".format(m)
    
    
    