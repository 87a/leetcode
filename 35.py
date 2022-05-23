#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:35.py
@time:2022/05/23
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1
        left = 0
        right = len(nums) - 1
        is_in = False
        out_boundary = False
        while left <= right:
            mid = (left + right) // 2
            if mid > 0:
                if nums[mid] == target:
                    is_in = True
                    break
                elif nums[mid - 1] < target < nums[mid]:
                    break
                elif nums[mid] < target:
                    if mid == len(nums) - 1:
                        out_boundary = True
                        break
                    left = mid + 1
                elif nums[mid] > target:
                    if mid == len(nums) - 1:
                        break
                    right = mid - 1
            else:
                if nums[mid] == target:
                    is_in = True
                    break
                elif nums[mid] > target:
                    break
                elif nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
        if not is_in and mid == len(nums) - 1 and out_boundary:
            mid = mid + 1
        return mid


if __name__ == '__main__':
    ex = Solution()
    print(ex.searchInsert([0, 2], 1))
