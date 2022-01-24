#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:3.py
@time:2022/01/21
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = ''
        maxLength = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        for i in range(len(s)):
            hashtable = []
            for j in range(i, len(s)):
                if s[j] in hashtable:
                    if j - i > maxLength:
                        maxLength = j - i
                        result = s[i:j]
                    break
                if j == len(s) - 1:
                    if j - i + 1 > maxLength:
                        maxLength = j - i + 1
                        result = s[i:j + 1]
                        return len(result)
                hashtable.append(s[j])
        return len(result)


if __name__ == '__main__':
    pass
