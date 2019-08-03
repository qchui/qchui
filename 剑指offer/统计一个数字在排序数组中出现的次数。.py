"""
统计一个数字在排序数组中出现的次数。
"""

# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        count=0
        for i in data:
            if i == k:
                count+=1

        return count