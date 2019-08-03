"""
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        n = len(tinput)
        if k <= 0 or k > n:
            return list()
        # 建立大顶堆
        self.heapAjust(tinput, 0, k - 1)
        for i in range(k, n):
            if tinput[i] < tinput[0]:
                tinput[0], tinput[i] = tinput[i], tinput[0]
                # 调整前k个数
                self.heapAjust(tinput, 0, k - 1)
        return sorted(tinput[:k])

    def heapAjust(self, nums, start, end):
        temp = nums[start]
        # 记录较大的那个孩子下标
        child = 2 * start + 1
        while child <= end:
            # 比较左右孩子，记录较大的那个
            if child + 1 <= end and nums[child] < nums[child + 1]:
                # 如果右孩子比较大，下标往右移
                child += 1
            # 如果根已经比左右孩子都大了，直接退出
            if temp >= nums[child]:
                break
            # 如果根小于某个孩子,将较大值提到根位置
            nums[start],nums[child] = nums[child],nums[start]
            # nums[start], nums[child] = nums[child], nums[start]
            # 接着比较被降下去是否符合要求，此时的根下标为原来被换上去的那个孩子下标
            start = child
            # 孩子下标也要下降一层
            child = child * 2 + 1
        # 最后将一开始的根值放入合适的位置(如果前面是交换，这句就不要)
        # nums[start] = temp

print(Solution().GetLeastNumbers_Solution([1,5,2,3,4,7,4,3,1],4))
""" 
              1(0)
        5(1)         2(2)
    3(3)   4(4)  7(5)    4(6)
 3(7)   1(8)
"""