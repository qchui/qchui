"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        total_array=len(numbers)
        half_array=int((total_array+1)/2)
        dict={}
        for i in numbers:
           if i not in dict:
               dict[i]=1
           else:
               dict[i] +=1
        for key in dict:
            if dict[key]>=half_array:
                return key
        return 0
print(Solution().MoreThanHalfNum_Solution([4,2,1,4,2,4]))