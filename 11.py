#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:11.py
@time:2022/01/21
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        ans = 0
        while i < j:
            area = (j - i) * min(height[i], height[j])
            ans = max(area, ans)
            if height[i] >= height[j]:
                j -= 1
            else:
                i += 1
        return ans


if __name__ == '__main__':
    pass
