#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:17.py
@time:2022/01/23
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 如果长度为0,则返回空列表
        if not digits:
            return []
        n = len(digits)
        # 创建哈希表
        hashmap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        # combination存储每次用到的字母
        combination = []
        # combinations存储结果
        combinations = []

        def backtrack(index: int):
            # 如果index到达最后的位置,则将combination中的结果连接起来并放入combinations
            if index == n:
                combinations.append("".join(combination))
            # 如果不是最后位置
            else:
                # 对数字对应的所有字母循环
                for alpha in hashmap[digits[index]]:
                    # 将字母加入combination
                    combination.append(alpha)
                    # 对下一个index做运算
                    backtrack(index + 1)
                    # 弹出最后一个字母
                    combination.pop()

        backtrack(0)
        return combinations


if __name__ == '__main__':
    example = Solution()
    print(example.letterCombinations("23"))
