#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:27.py
@time:2022/01/27
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 判断如果列表中没有数,则返回0
        if not nums:
            return 0
        n = len(nums)
        # 如果列表中只有一个数,当val等于它时,返回0,否则返回1
        if n == 1:
            if val == nums[0]:
                return 0
            return 1
        # 排序
        nums.sort()
        # 初始化两个指针
        first, second = 0, 0
        # 找到要删除的数的第一个位置
        for first in range(n):
            if nums[first] == val:
                break
        # isLast用来记录要删除的数是否是最大的数
        isLast = False
        # 找到下一个不等于要删除的数,如果一直到列表最后都未找到,则要删除的数是最后一个(最大)的数
        for second in range(first, n):
            if nums[second] != val:
                break
            if second == n - 1:
                isLast = True
        # 如果要删除的数不是最后一个数
        if not isLast:
            # 调整要删除的数和最后几个数的位置
            if n - second > second - first:
                nums[-(second - first):], nums[first:second] = nums[first:second], nums[-(second - first):]
            else:
                m = second - first - (n - second)
                nums[second:], nums[first:first + m] = nums[first:first + m], nums[second:]
            # print(nums)
            return n - (second - first)
        # 如果不是,则直接返回个数
        else:
            # print(nums)
            return n - (n - first)


if __name__ == '__main__':
    example = Solution()
    print(example.removeElement([4, 5], 5))
