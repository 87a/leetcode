#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:23.py
@time:2022/01/25
"""
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        # dummy用于返回答案, p用于创建答案链表
        p = dummy = ListNode()
        # heap用于排序
        heap = []

        # 定义ListNode的比较方法
        def __lt__(self: ListNode, other: ListNode):
            return self.val < other.val

        ListNode.__lt__ = __lt__

        # 将每个链表的第一个节点放入堆
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, lists[i])
        # 堆中有结点时循环
        while heap:
            # 弹出最小的节点
            node = heapq.heappop(heap)
            # 加入答案链表
            p.next = ListNode(node.val)
            p = p.next
            # 如果最小结点还有下个结点,将其加入堆
            if node.next:
                heapq.heappush(heap, node.next)

        return dummy.next


if __name__ == '__main__':
    pass
