#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:8.py
@time:2022/01/21
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        if len(s) == 0:
            return 0
        if len(s) == 1 and not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if s[i] != ' ':
                break
        s = s[i:]
        if not s[0].isdigit() and s[0] != '-' and s[0] != '+':
            return 0
        if s[0] == '-':
            start = 1
            negative = -1
        elif s[0] == '+':
            start = 1
            negative = 1
        else:
            start = 0
            negative = 1
        last = True
        for j in range(start, len(s)):
            if j == start and not s[j].isdigit():
                return 0
            if not s[j].isdigit():
                last = False
                break
        if j == len(s) - 1 and last:
            s = s[start:]
        else:
            s = s[start:j]
        num = int(s) * negative
        if -2 ** 31 <= num <= 2 ** 31 - 1:
            return num
        elif num >= 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return -2 ** 31


if __name__ == '__main__':
    pass
