"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        list2=[]
        for r in range(len(array)):
            for c in range(r+1,len(array)):
                if array[r]==array[c]:
                    list2.append(array[r])
        list1= list(set(array))
        list2= list(set(list2))
        for i in list2:
            list1.remove(i)
        return list1
print(Solution().FindNumsAppearOnce([4,6,1,1,1,1]))