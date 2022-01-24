#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:7.py
@time:2022/01/21
"""


class Solution:
    def reverse(self, x: int) -> int:
        negative = 1
        if x < 0:
            x = -x
            negative = -1

        xstr = str(x)
        result = xstr[::-1]
        i = 0
        for i in range(len(result)):
            if i != '0':
                break
        result = result[i:]
        result = int(result) * negative
        return result if -2 ** 31 <= result <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    pass
