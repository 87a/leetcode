#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:16.py
@time:2022/01/22
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #  排序
        nums.sort()
        n = len(nums)
        # 初始化最小差值和最接近的答案
        minDiff = None
        best = None
        # 对第一个数遍历
        for first in range(n):
            # 第二个数的下标的初值为第一个数的下标+1
            second = first + 1
            # 第三个数的下标的初值为n-1
            third = n - 1
            # 循环条件:第二个数的下标<第三个数的下标
            while second < third:
                # 对三个数求和
                addition = nums[first] + nums[second] + nums[third]
                # 如果和与目标相同,则直接返回
                if addition == target:
                    return target
                # 和小于目标,则增大第二个数的下标
                if addition < target:
                    if minDiff is None:
                        minDiff = abs(target - addition)
                        best = addition
                    elif abs(target - addition) < minDiff:
                        minDiff = abs(target - addition)
                        best = addition

                    second += 1
                # 和大于目标,则减小第三个数的下标
                if addition > target:
                    if minDiff is None:
                        minDiff = abs(target - addition)
                        best = addition
                    elif abs(target - addition) < minDiff:
                        minDiff = abs(target - addition)
                        best = addition
                    third -= 1
        return best


if __name__ == '__main__':
    example = Solution()
    print(example.threeSumClosest([-1, 2, 1, -4], 1))
