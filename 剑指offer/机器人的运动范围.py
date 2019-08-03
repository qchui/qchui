"""
地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），
因为3+5+3+7 = 18。但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子？
"""
# -*- coding:utf-8 -*-
class Solution: # 注意和矩阵路径的区别，不一定到头，只要满足条件即可，可以返回（回溯法的特点）
    # 且路径节点可重复，无步数限制
    def __init__(self):  # 机器人可以倒回来，但不能重复计数。
        self.count = 0
    def movingCount(self, threshold, rows, cols):
        # write code here
        flag = [[1 for i in range(cols)] for j in range(rows)]
        self.findWay(flag,0,0,threshold)  # 从（0，0）开始走
        return self.count
    def findWay(self,flag,i,j,k):
        if i >= 0 and j >= 0 and i < len(flag) and j < len(flag[0]) and sum(list(map(int,str(i)))) + sum(list(map(int,str(j)))) <= k and flag[i][j] == 1:
            flag[i][j] = 0
            self.count += 1
            self.findWay(flag,i-1,j,k)
            self.findWay(flag,i+1,j,k)
            self.findWay(flag,i,j-1,k)
            self.findWay(flag,i,j+1,k)
