#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:18.py
@time:2022/01/23
"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 排序
        nums.sort()
        n = len(nums)
        # 初始化答案列表
        res = []
        # 对一个数循环
        for first in range(0, n - 2):
            # 如果两次的数一样则跳过
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            # print('first', first)
            # 对第四个数循环
            for fourth in range(first + 3, n):
                # 如果两次的数一样则跳过
                if n - 1 > fourth and nums[fourth] == nums[fourth + 1]:
                    continue
                # print('fourth', fourth)
                second = first + 1
                third = fourth - 1
                # 循环条件,第二个数的下标小于第三个数的下标
                while second < third:
                    addition = nums[first] + nums[second] + nums[third] + nums[fourth]
                    # 如果和与目标相同
                    if addition == target:
                        # print(first, second, third, fourth)
                        # 加入列表
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        # 第二个数下标+1
                        second += 1
                        # 如果和上一个数相同,则找到下一个不同的数
                        if nums[second] != nums[second - 1]:
                            continue
                        while nums[second - 1] == nums[second] and second < third:
                            second += 1
                        # 第三个数下标-1
                        third -= 1
                        # 如果和上一个数相同,则找到下一个不同的数
                        if nums[third] != nums[third + 1]:
                            continue
                        while nums[third + 1] == nums[third] and second < third:
                            third -= 1
                    # 小于和大于的情况
                    if addition < target:
                        second += 1
                        if nums[second] != nums[second - 1]:
                            continue
                        while nums[second + 1] == nums[second] and second < third:
                            second += 1
                    if addition > target:
                        third -= 1
                        if nums[third] != nums[third + 1]:
                            continue
                        while nums[third - 1] == nums[third] and second < third:
                            third -= 1
        return res


if __name__ == '__main__':
    example = Solution()
    print(example.fourSum(nums=[-2, -1, -1, 1, 1, 2, 2], target=0))
