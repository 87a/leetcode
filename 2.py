#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:2.py
@time:2022/01/21
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next
if __name__ == '__main__':
    pass
