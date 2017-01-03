# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 14:55:33 2017

@author: abgoswam
"""

def onlinePoker(shuffled_deck, half1, half2):
    if len(shuffled_deck) != len(half1) + len(half2):
        return False

    i = j = 0

    for item in shuffled_deck:
        if i < len(half1) and item == half1[i]:
            i += 1
        elif j < len(half2) and item == half2[j]:
            j += 1
        else:
            return False
    
    return True
    
if __name__ == "__main__":
    shuffled_deck = [1,2,5,7,8,3,4,6]
    half1 = [1,3,4,6]
    half2 = [2,5,7,8]
    
    print onlinePoker(shuffled_deck, half1, half2)
    
    shuffled_deck = [2,5,7,1,3,8,6, 4]
    half1 = [1,3,4,6]
    half2 = [2,5,7,8]
    
    print onlinePoker(shuffled_deck, half1, half2)