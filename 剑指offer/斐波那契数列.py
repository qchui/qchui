"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

"""

# -*- coding:utf-8 -*-
# class Solution:
#     def Fibonacci(self, n):
#         list=[]
#         if n<=2:
#             return 1
#
#         return self.Fibonacci(n-1)+self.Fibonacci(n-2)

class Solution:
    def Fibonacci(self, n):
        list = [0, 1]
        while n > 0:
            list[0], list[1] = list[1], list[0]+list[1]
            n -= 1
        return list[0]
