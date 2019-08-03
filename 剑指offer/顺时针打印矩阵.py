"""
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵： 1 2  3  4
                         5 6  7  8
                         9 10 11 12
                         13 14 15 16

则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.


# a = [1,2,3]
# b = [4,5,6]
# c = [4,5,6,7,8]
# zipped = zip(a,b,c)     # 打包为元组的列表
# print(zipped.__next__())
"""

# -*- coding:utf-8 -*-
# class Solution:
#     # matrix类型为二维列表，需要返回列表
#     def printMatrix(self, matrix):
#         #matrix[:] = map(list,zip(*matrix[::-1]))
#         matrix[:] = map(list, zip(*matrix[::-1]))
#         return matrix
#
# print(Solution().printMatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
def printMatrix( matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            print(res)
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res
def printMatrix1( matrix):
    x0 = y0 = 0
    xn = len(matrix)-1
    yn = len(matrix[0])-1
    list = []
    while x0<=xn and y0<=yn:
        for y in range(y0, yn+1):
            list.append(matrix[x0][y])
        for x in range(x0+1, xn+1):
            list.append(matrix[x][yn])
        if x0 < xn:
            for y in range(yn-1, y0-1, -1):
                list.append(matrix[xn][y])
        if y0 < yn:
            for x in range(xn-1, x0, -1):
                list.append(matrix[x][y0])
        x0 += 1
        y0 += 1
        xn -= 1
        yn -= 1
    return list

print(printMatrix1([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
