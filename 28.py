#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:28.py
@time:2022/01/27
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        m = len(haystack)
        n = len(needle)
        if m < n:
            return -1
        # 创建sunday算法所用的偏移表
        dic = {v: n - k for k, v in enumerate(needle)}
        # idx表示正在处理的位置
        idx = 0

        # 循环条件
        while idx + n <= m:
            # 取出对比的字符串
            str_cut = haystack[idx:idx + n]
            # 如果相同则返回idx
            if str_cut == needle:
                return idx
            # 如果已经到末尾且不同则返回-1
            elif idx + n == m:
                return -1
            # 不在末尾且不同,使用下一个字母的偏移量
            else:
                nextc = haystack[idx + n]
                idx += dic[nextc] if dic.get(nextc) else n + 1
        return -1


if __name__ == '__main__':
    example = Solution()
    print(example.strStr(haystack="checkthisout", needle="this"))
