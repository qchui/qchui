"""
在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

[[1,2,3,4],
 [3,4,5,6],
 [5,6,7,8],
 [7,8,9,10]]       6
"""


# # -*- coding:utf-8 -*-
# class Solution:
#     # array 二维列表
#     def Find(self, target, array):
#         row = len(array) - 1
#         col = len(array[0]) - 1
#         start_r = int(row / 2)
#         start_c = col
#         if not array:
#             return  False
#         else:
#             while 0<= start_r <=row or 0 <= start_r <= col:
#                 if array[start_r][start_c] == target:
#                     return True
#                 elif array[start_r][start_c] < target:
#                     if start_c == col:
#                         start_r += 1
#                         start_c = 0
#                     else:
#                         start_c += 1
#                 else:
#                     if start_c == 0:
#                         start_r -= 1
#                         start_c =col
#                     else:
#                         start_c -= 1
#             return  False

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)-1
        cols = len(array[0])-1
        i = rows
        j = 0
        while j<=cols and i>=0:
            if target<array[i][j]:
                i -= 1
            elif target>array[i][j]:
                j += 1
            else:
                return True
        return False

print(Solution().Find(12,[[1,2,3,4],[3,4,5,6],[5,6,7,8],[7,8,9,10]]))