"""
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}，
{2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
"""
# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.list=[]
    def maxInWindows(self, num, size):
        if size>0:
            for i in range(len(num)-size+1):
                self.list.append(max(num[i:size+i]))
            return self.list
        else:
            return []

print(Solution().maxInWindows([2,3,4,2,6,2,5,1],3))