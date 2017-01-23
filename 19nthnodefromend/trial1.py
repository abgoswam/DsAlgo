# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:53:05 2017

@author: abgoswam
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        current = head
        N = 0
        while(current is not None):
            N += 1
            current = current.next
            
        if n == N:
            head = head.next
        else:
            prev = head
            current = head.next
            indexfromend = N - 1
            while(indexfromend != n):
                prev = current
                current = current.next
                indexfromend = indexfromend - 1
                
            prev.next = current.next

        return head            
            