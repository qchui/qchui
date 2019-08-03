# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
list=[]
class Solution:
    def Serialize(self, root):
        if not root:
            return None
        list.append(root.val)
        self.Serialize(root.left)
        self.Serialize(root.right)
        return list


    def Deserialize(self, s):
        pass



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
print(Solution().Serialize(a))
