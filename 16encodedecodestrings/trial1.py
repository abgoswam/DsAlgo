# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 13:25:45 2017

@author: abgoswam
"""

# "abcd" -> 1
# "efgh" -> 2
# ["abcd", "efgh"] -> [1,2]

#if __name__ == "_main__":
    
s_list = ['abhishek', 'goswa,mi', ",mi", 'goswa,mi']
print("s_list : {0}".format(s_list))

s_set = set()
for item in s_list:
    s_set.add(item)

print("s_set : {0}".format(s_set))
     
s_str = ",".join(s for s in s_list)
print("s_str : {0}".format(s_str))

s_split = s_str.split(',')
s_list_new = []

carryover = []
for item in s_split:
    carryover.append(item)

    lookup_str = ','.join(s for s in carryover)       
    if lookup_str in s_set:
        s_list_new.append(lookup_str)
        carryover = []

        
print(s_list_new)
