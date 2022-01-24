#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:6.py
@time:2022/01/21
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        slen = len(s)
        #  如果只有一行,则返回原字符串
        if numRows == 1:
            return s
        #  创建存储答案的列表
        res = [[] for _ in range(numRows)]
        #  将2 * numRows - 2个数分为一组
        group = 2 * numRows - 2
        for i in range(slen):
            pos = i % group
            #  如果是前numRows个数,则按照位置放入列表
            if 0 <= pos < numRows:
                res[pos].append(s[i])
            # 如果是后面几个数(即斜线上的),放入对应的位置
            else:
                res[-pos + group].append(s[i])
        result = ''
        for i in range(numRows):
            for j in res[i]:
                result += j
        return result


if __name__ == '__main__':
    pass
