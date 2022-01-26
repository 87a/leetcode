#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:25.py
@time:2022/01/25
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"val={self.val}, next={self.next.val}"


def createLinkedList(vals: list):
    head = ListNode()
    cur = head
    for val in vals:
        cur.next = ListNode(val)
        cur = cur.next
    return head


def printLinkedList(head: ListNode):
    cur = head.next
    while cur:
        print(cur.val, end=' ')
        cur = cur.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = p = head
        while 1:
            cur = p
            count = 0

            while cur.next:
                cur = cur.next
                count += 1
                if count == k:
                    break
            if count < k:
                break
            r = p.next.next
            q = p.next
            for i in range(k - 1):
                # for _ in range(i + 2):
                #     q = q.next
                q.next = r.next
                r.next = p.next
                p.next = r
                r = q.next

            for i in range(k):
                p = p.next

        return dummy.next


if __name__ == '__main__':
    head = createLinkedList([1, 2, 3, 4, 5])
    example = Solution()
    head = example.reverseKGroup(head, 2)
    printLinkedList(head)
