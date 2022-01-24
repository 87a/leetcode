#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:9.py
@time:2022/01/21
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        strnum = str(x)
        length = len(strnum)
        for i in range(length):
            if strnum[i] != strnum[length - 1 - i]:
                return False
        return True


if __name__ == '__main__':
    pass
