#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:32.py
@time:2022/05/19
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxans = 0
        stack = list()
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans


if __name__ == '__main__':
    ex = Solution()
    print(ex.longestValidParentheses(')()())()()('))
