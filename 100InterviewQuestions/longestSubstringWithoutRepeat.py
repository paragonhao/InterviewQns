#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 23:00:46 2019

@author: paragonhao
"""
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currSet = {''}
        maxSubstring = 0 
        i=j=0
        
        while j < len(s):
            
            if s[j] in currSet:
                currSet.remove(s[i])
                i += 1
            else:
                currSet.add(s[j])
                j += 1
                maxSubstring = max(maxSubstring, j - i)
        
        return maxSubstring
        
        