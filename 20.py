#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:20.py
@time:2022/01/24
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # 如果是奇数个括号,那一定无效
        if len(s) % 2 == 1:
            return False
        # 创建一个列表存放右括号
        stack = list()
        # 判断左右括号是否配对的函数
        def valid(a: str, b: str) -> bool:
            if a == '(' and b == ")":
                return True
            if a == '[' and b == "]":
                return True
            if a == '{' and b == "}":
                return True
            return False

        right = [')', ']', '}']
        # 循环条件为字符串长度不为0
        while s:
            # 如果最后一个字符为右括号
            if s[-1] in right:
                # 将最后一个字符加入列表
                stack.append(s[-1])
                # s截断
                s = s[:-1]
                # 如果字符串最后一个字符是右括号,那一定无效
                if not s:
                    return False
            # 如果最后一个字符为左括号
            if s[-1] not in right:
                # 如果列表中已经没有字符,则一定无效
                if not stack:
                    return False
                # 如果和列表中最后一个右括号不匹配,则无效
                if not valid(s[-1], stack[-1]):
                    return False
                s = s[:-1]
                stack.pop()
        # 如果匹配完成后列表中有剩的字符,则无效
        if not stack:
            return True
        return False


if __name__ == '__main__':
    example = Solution()
    print(example.isValid('()'))
