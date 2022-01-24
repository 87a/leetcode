#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:13.py
@time:2022/01/21
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        #  创建哈希表
        hashmap = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9,
                   'V': 5, 'IV': 4, 'I': 1}
        #  初始化答案
        res = 0
        #  循环条件:s长度不为0
        while len(s):
            #  从大到小在哈希表中查找
            for key in hashmap.keys():
                if s.startswith(key):
                    res += hashmap[key]
                    s = s[len(key):]
        return res


if __name__ == '__main__':
    example = Solution()
    print(example.romanToInt("MCMXCIV"))
