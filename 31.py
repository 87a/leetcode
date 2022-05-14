#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:31.py
@time:2022/05/14
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # search first element which is smaller than its next element
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # search first element which is larger than nums[i] from rear
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]

        # reverse rest elements
        if i < 0:
            list.reverse(nums)
        elif i + 1 < len(nums) - 1:
            nums[i + 1:] = nums[:i:-1]
        # print(nums)


if __name__ == '__main__':
    ex = Solution()
    # ex.nextPermutation([1, 2, 3])
    # ex.nextPermutation([2, 3, 1])
    ex.nextPermutation([1, 5, 1])
