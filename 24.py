#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:24.py
@time:2022/01/25
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 创建一个dummy结点,使其指向head
        dummy = ListNode()
        dummy.next = head
        # p用于循环
        p = dummy
        # 循环条件,p的后两个结点存在
        while p.next and p.next.next:
            # 交换两个结点
            node1 = p.next
            node2 = p.next.next
            p.next = node2
            node1.next = node2.next
            node2.next = node1
            # p前进
            p = node1
        return dummy.next


if __name__ == '__main__':
    pass
