#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 21:51:49 2019

@author: paragonhao
"""
# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            
            temp = target - nums[i]
            
            if temp in result:
                return i, result[temp]
            else:
                result[nums[i]] = i
        