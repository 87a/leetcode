#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:test.py
@time:2022/01/15
"""
from typing import List


def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)

    def matches(i: int, j: int) -> bool:
        if i == 0:
            return False
        if p[j - 1] == '.':
            return True
        return s[i - 1] == p[j - 1]

    f = [[False] * (n + 1) for _ in range(m + 1)]
    f[0][0] = True
    for i in range(m + 1):
        for j in range(n + 1):
            if p[j - 1] == '*':
                f[i][j] |= f[i][j - 2]
                if matches(i, j - 1):
                    f[i][j] |= f[i - 1][j]
            else:
                if matches(i, j):
                    f[i][j] |= f[i][j - 1]
    return f[m][n]


if __name__ == '__main__':
    print(isMatch("aab","c*a*b"))
