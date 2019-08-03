"""
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        if pRoot.left is None and pRoot.right is None:
            return [[pRoot.val]]
        stack=[pRoot]
        output=[]
        while(stack):
            temp=[]
            for i in range(len(stack)):
                out_node=stack.pop(0)
                temp.append(out_node.val)
                if out_node.left is not None:
                    stack.append(out_node.left)
                if out_node.right is not None:
                    stack.append(out_node.right)
            output.append(temp)
        return output

a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)
f=TreeNode(6)
g=TreeNode(7)
h=TreeNode(8)
i=TreeNode(9)
a.left=b
a.right=c
b.left=d
b.right=e
d.left=f
d.right=g
c.left=h
c.right=i
print(Solution().Print(a))
"""
        a
      b    c
    d  e  g  i
  f  g
"""