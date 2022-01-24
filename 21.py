#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:21.py
@time:2022/01/24
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 定义头结点和用来循环的a结点
        a = head = ListNode()
        # p,q是list1和list2的循环结点
        p = list1
        q = list2
        # 当p和q其中一个到达结尾时就停止
        while p and q:
            if p.val <= q.val:
                a.next = p
                p = p.next
                a = a.next
            else:
                a.next = q
                q = q.next
                a = a.next
        # 处理剩下的结点
        if p:
            while p:
                a.next = p
                p = p.next
                a = a.next
        else:
            while q:
                a.next = q
                q = q.next
                a = a.next

        return head.next


if __name__ == '__main__':
    pass
