#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:12.py
@time:2022/01/21
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        #  创建哈希表
        hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
                   5: 'V', 4: 'IV', 1: 'I'}
        #  初始化输出字符串
        res = ''
        #  遍历哈希表中的键(从大到小,贪心)
        for key in hashmap.keys():
            if num // key != 0:
                count = num // key
                res += hashmap[key] * count
                num %= key
        return res


if __name__ == '__main__':
    example = Solution()
    print(example.intToRoman(num=1994))
