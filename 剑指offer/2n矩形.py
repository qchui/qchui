"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""

# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number==0:
            return 0
        list = [1, 2]
        while number > 1:
            list[0], list[1] = list[1], list[0] + list[1]
            number -= 1
        return list[0]

print(Solution().rectCover(2))