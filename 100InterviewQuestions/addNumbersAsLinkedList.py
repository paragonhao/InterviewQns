#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:40:16 2019

@author: paragonhao
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
   
    def addTwoNumbers1(self, l1, l2, c = 0):
        
        val = l1.val + l2.val + c
        
        c = val //10
        ret = ListNode(val % 10)
        
        if (l1.next !=None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers1(l1.next, l2.next, c)
        return ret
        
    def addTwoNumbers2(self, l1, l2, c = 0):
        dummy = ListNode(0)
        result = dummy
        counter = 0
        
        while (l1 != None) or (l2 != None) or (c != 0):
            counter +=1
            if l1 == None:
                l1 = ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            
            total = l1.val + l2.val
            currPos = total%10 + c
            c = total // 10
            
            result.next = ListNode(currPos)
            l1 = l1.next
            l2 = l2.next
            result = result.next
        
        return dummy
            

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers1(l1, l2)


while result:
    print(result.val)
    result = result.next