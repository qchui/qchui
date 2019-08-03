"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
#太low

# -*- coding:utf-8 -*-
# class Solution:
#     def IsUglyNumber(self,number):
#         while True:
#             if number % 2 == 0:
#                 number = number // 2
#             elif number % 3 == 0:
#                 number = number // 3
#             elif number % 5 == 0:
#                 number = number // 5
#             else:
#                 if number == 1:
#                     return True
#                 else:
#                     return False
#     def GetUglyNumber_Solution(self, index):
#         number=1
#         count=1
#         while count!=index:
#             number += 1
#             if self.IsUglyNumber(number):
#                 count+=1
#         return number
#
#
# print(Solution().IsUglyNumber(64))


# -*- coding:utf-8 -*-
class Solution:
    """
    因为丑数只包含质因子2，3，5，假设我们已经有n-1个丑数，按照顺序排列，且第n-1的丑数为M。
    那么第n个丑数一定是由这n-1个丑数分别乘以2，3，5，得到的所有大于M的结果中，最小的那个数。

    事实上我们不需要每次都计算前面所有丑数乘以2，3，5的结果，然后再比较大小。
    因为在已存在的丑数中，一定存在某个数T2，在它之前的所有数乘以2都小于已有丑数，而T2×2的结果一定大于M，
    同理，也存在这样的数T3，T5我们只需要标记这三个数即可。

    """
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        # 1作为特殊数直接保存
        baselist = [1]
        min2 = min3 = min5 = 0
        curnum = 1
        while curnum < index:
            minnum = min(baselist[min2] * 2, baselist[min3] * 3, baselist[min5] * 5)
            baselist.append(minnum)
            # 找到第一个乘以2的结果大于当前最大丑数M的数字，也就是T2
            while baselist[min2] * 2 <= minnum:
                min2 += 1
            # 找到第一个乘以3的结果大于当前最大丑数M的数字，也就是T3
            while baselist[min3] * 3 <= minnum:
                min3 += 1
            # 找到第一个乘以5的结果大于当前最大丑数M的数字，也就是T5
            while baselist[min5] * 5 <= minnum:
                min5 += 1
            curnum += 1
        return baselist[-1]
print(Solution().GetUglyNumber_Solution(1000000))

