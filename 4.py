#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:qzz
@file:4.py
@time:2022/01/21
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)

        def getKthElement(k: int) -> int:
            index1, index2 = 0, 0
            while 1:
                if index1 == len1:
                    return nums2[index2 + k - 1]
                if index2 == len2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newIndex1 = min(index1 + k // 2 - 1, len1 - 1)
                newIndex2 = min(index2 + k // 2 - 1, len2 - 1)
                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        totalLength = len1 + len2
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            b = getKthElement(totalLength // 2)
            a = getKthElement(totalLength // 2 + 1)
            return (a + b) / 2


if __name__ == '__main__':
    pass
