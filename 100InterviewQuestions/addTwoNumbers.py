#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 22:25:06 2019

@author: paragonhao
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummy = ListNode(0)
        result = dummy 
        carry = 0 
        
        while l1 or l2 or carry:
            # assign the node to a ListNode with value 0
            # since the one that is none does not have any number anymore
            if l1 is None:
                l1 = ListNode(0)
            if l2 is None:
                l2 = ListNode(0)
            
            # sum up the value on the current position
            value = l1.val + l2.val + carry
            # find out the carry
            carry = value //10
            # find out the number to remain on the digit
            out = value % 10 
            
            result.next = ListNode(out)
            result = result.next
            l1 = l1.next
            l2 = l2.next
            
        return dummy.next