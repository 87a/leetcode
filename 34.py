#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:34.py
@time:2022/05/22
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        not_found = False
        while 1:
            mid = (left + right) // 2
            if left >= right and nums[mid] != target:
                not_found = True
                break
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                break
        if not_found:
            return [-1, -1]
        i, j = mid, mid
        left_boundary, right_boundary = False, False

        while 1:
            change = False
            if nums[i] == target:
                if i > 0:
                    i -= 1
                    change = True
                else:
                    if nums[i] == target:
                        left_boundary = True
            if nums[j] == target:
                if j < len(nums)-1:
                    j += 1
                    change = True
                else:
                    if nums[j] == target:
                        right_boundary = True
            if not change:
                break
        left_index = i if left_boundary else i + 1
        right_index = j if right_boundary else j - 1
        return [left_index, right_index]


if __name__ == '__main__':
    ex = Solution()
    print(ex.searchRange([5,7,7,8,8,10], 8))
