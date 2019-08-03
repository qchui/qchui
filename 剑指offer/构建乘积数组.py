"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        mult = 1
        B = [1]*len(A)
        for i in range(len(A)):
            mult = mult * A[i-1] if i>0 else mult
            for a in A[i+1:]:
                B[i] = B[i] * a
            B[i] = B[i] * mult
        return B