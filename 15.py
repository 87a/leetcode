#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:15.py
@time:2022/01/21
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #  排序
        nums.sort()
        n = len(nums)
        ans = []
        #  循环第一个数
        for first in range(n):
            #  如果这一次和上一次第一个数一样,则跳过
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            #  初始化第三个数的位置
            third = n - 1
            #  剩下两个数的和
            target = -nums[first]

            #  循环第二个数, 从第一个数的下一个开始
            for second in range(first + 1, n):
                #  如果这一次和上一次第二个数一样,则跳过
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                #  找到第一个使二三数之和小于target的数
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                #  如果第二个数和第三个数相同,则跳过
                if second == third:
                    continue
                #  如果符合条件,则加入答案
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


if __name__ == '__main__':
    example = Solution()
    print(example.threeSum([-1, 0, 1, 2, -1, -4]))
