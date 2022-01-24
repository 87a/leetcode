#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:1.py
@time:2022/01/21
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return hashtable[target - num], i
            hashtable[num] = i
if __name__ == '__main__':
    pass
