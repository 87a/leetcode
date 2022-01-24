#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:5.py
@time:2022/01/21
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        slen = len(s)
        # 如果字符串只有1位或者为空,则返回原字符串
        if slen < 2:
            return s
        # 创建动态规划数组
        dp = [[False] * slen for _ in range(slen)]
        maxlen = 1  # 记录最长回文子串的长度
        begin = 0  # 记录最长回文子串的起始位置
        # 每个位置自身一个字符一定是回文的
        for i in range(slen):
            dp[i][i] = True

        #  L表示子串的长度,[2,slen]
        for L in range(2, slen + 1):
            for i in range(slen):
                j = i + L - 1
                if j >= slen:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    # 如果j和i之间距离小于等于2,那么s[i:j]是回文的
                    if j - i < 3:
                        dp[i][j] = True
                    # 否则状态转移
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > maxlen:
                    maxlen = j - i + 1
                    begin = i
        return s[begin:begin + maxlen]


if __name__ == '__main__':
    pass
