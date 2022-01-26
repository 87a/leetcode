#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:22.py
@time:2022/01/24
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 初始化答案列表
        ans = []

        # 定义回溯函数
        def backtrack(S: List, left: int, right: int):
            # 如果S的长度符合要求,则将其合并放入答案列表
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            # 如果左括号还未全部放入,则放入一个,进行回溯
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            # 如果右括号数量小于左括号,则放入一个,进行回溯
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    pass
