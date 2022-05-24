#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:36.py
@time:2022/05/24
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(9):
            assist_list = []
            nums = 0
            for num in board[i]:
                if num.isdigit():
                    nums += 1
                    if num not in assist_list:
                        assist_list.append(num)
            if len(assist_list) != nums:
                return False

        # check columns
        for i in range(9):
            assist_list = []
            nums = 0
            for j in range(9):
                num = board[j][i]
                if num.isdigit():
                    nums += 1
                    if num not in assist_list:
                        assist_list.append(num)
            if len(assist_list) != nums:
                return False

        # check 9
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                nums_9 = [board[i][j], board[i + 1][j], board[i + 2][j], board[i][j + 1], board[i][j + 2],
                          board[i + 1][j + 1], board[i + 1][j + 2], board[i + 2][j + 1], board[i + 2][j + 2]]
                nums = 0
                assist_list = []
                for num in nums_9:
                    if num.isdigit():
                        nums += 1
                        if num not in assist_list:
                            assist_list.append(num)
                if len(assist_list) != nums:
                    return False

        return True


if __name__ == '__main__':
    ex = Solution()
    ret = ex.isValidSudoku(
        [[".", ".", "4", ".", ".", ".", "6", "3", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", "9", "."],
         [".", ".", ".", "5", "6", ".", ".", ".", "."],
         ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
         [".", ".", ".", "7", ".", ".", ".", ".", "."],
         [".", ".", ".", "5", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]])
    print(ret)
