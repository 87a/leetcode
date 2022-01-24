#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:14.py
@time:2022/01/21
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #  初始化答案
        res = ''
        #  找到最短字符串的长度
        minLength = len(strs[0])
        for s in strs:
            if len(s) < minLength:
                minLength = len(s)
        isEnd = False
        #  在每一位上比较
        for i in range(minLength):
            temp = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != temp:
                    isEnd = True
                    break
            if not isEnd:
                res += temp
            else:
                break
        return res


if __name__ == '__main__':
    example = Solution()
    print(example.longestCommonPrefix(["dog","racecar","car"]))
