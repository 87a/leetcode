#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:26.py
@time:2022/01/26
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:
            return 1
        first, second = 0, 0
        while 1:

            second += 1
            if second == len(nums):
                nums = nums[:first + 1]
                break
            if nums[first] != nums[second]:
                nums = nums[:first + 1] + nums[second:]
                second -= second - first - 1
                first = second
        # print(nums)
        return len(nums)


if __name__ == '__main__':
    example = Solution()
    print(example.removeDuplicates([1, 1, 2]))
