"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，
按结点数值大小顺序第三小结点的值为4。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
list=[]
class Solution:
    def KthNode1(self, pRoot):
        if not pRoot:
            return  None
        self.KthNode1(pRoot.left)
        list.append(pRoot.val)
        self.KthNode1(pRoot.right)
        return list
    def KthNode(self, pRoot, k):
        l=self.KthNode1(pRoot)
        target_list=sorted(l)
        if k<1:
            return
        if k>len(list):
            return
        else:
            return target_list[k-1]
"""
        a1
      b2    c3
    d4  e5  g8  i9
  f6  g7
  [[1], [2, 3], [4, 5, 8, 9], [6, 7]]
"""

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
h = TreeNode(8)
i = TreeNode(9)
a.left = b
a.right = c
b.left = d
b.right = e
d.left = f
d.right = g
c.left = h
c.right = i
print(Solution().KthNode(a,3))
