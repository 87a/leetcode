#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:19.py
@time:2022/01/24
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 创建一个头结点
        p = ListNode(next=head)
        first = head
        second = p
        # 先让first指针前进n步
        for i in range(n):
            first = first.next
        # 两个指针同时前进,直到first到达末尾,second指向的就是倒数第n个节点
        while first:
            first = first.next
            second = second.next
        # 改变second的next
        second.next = second.next.next
        return p.next


if __name__ == '__main__':
    pass
