"""

输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
输出描述:
对应每个测试案例，输出两个数，小的先输出。
"""

# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        list=[]
        for r in range(len(array)):
            for c in range(r+1,len(array)):
                if array[c]==tsum-array[r]:
                    list.append((array[r],array[c]))
        if len(list)<=0:
            return []
        elif len(list)==1:
            return list[0]
        max=list[0][0]*list[0][1]
        for i in  range(1,len(list)):
            if list[i][0]*list[i][1]<max:
                return list[i]
        return list[0]

print(Solution().FindNumbersWithSum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],21))