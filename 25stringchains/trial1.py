# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 19:04:08 2017

@author: abgoswam
"""

#_words_cnt = int(raw_input().strip())
#_words_i=0
#_words = []
#
#while _words_i < _words_cnt:
#    _words_item = raw_input().strip()
#    _words.append(_words_item)
#    _words_i += 1
#    
#print(_words)


#def longestChain(words):

#words = ['a', 'b', 'ba', 'bca', 'bdca', 'bda']

words = ['ab', 'abc']
#if words is None or len(words) <= 0:
#    return 0
    
words_sorted = sorted(words, key=lambda x: len(x))
chain = {}
for s in words_sorted:
    print("word 's' : {0}".format(s))
    if len(s) == 1:
        chain[s] = 1
    else:
#        iterate over the characters in s
        _m = 0            
        for i in range(len(s)):
            s_prime = (s[:i] + s[i+1:])
            print("word 's_prime' : {0}".format(s_prime))
            if s_prime in chain:
                _m = max(_m, chain[s_prime])
                
        if _m > 0:
            _m += 1
            
        chain[s] = _m
        
argmax_s =  max(chain, key=lambda i:chain[i])  

#return chain[argmax_s]     
    
#words = ['a', 'b', 'ba', 'bca', 'bdca', 'bda']
##words = ['ab', 'ba']
#print(longestChain(words))