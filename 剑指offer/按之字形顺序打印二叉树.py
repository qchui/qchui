"""
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
"""
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
           return []
        if pRoot.left is None and pRoot.right is None:
            return [[pRoot.val]]
        stack = [pRoot]
        output = []
        count=0
        while (stack):
            temp = []
            if count%2==0:
                for i in range(len(stack)):
                    out_node = stack.pop(0)
                    temp.append(out_node.val)
                    if out_node.left is not None:
                        stack.append(out_node.left)
                    if out_node.right is not None:
                        stack.append(out_node.right)
                output.append(temp)
            else:
                for i in range(len(stack)):
                    out_node = stack.pop(0)
                    temp.append(out_node.val)
                    if out_node.left is not None:
                        stack.append(out_node.left)
                    if out_node.right is not None:
                        stack.append(out_node.right)
                output.append(temp[::-1])
            count +=1
        return output



    # def Print(self, pRoot):
    #     # write code here
    #     nodelist = []
    #     outlist = []
    #     # 增加标志变量，初始化为从左至右
    #     lefttoright = True
    #     if pRoot:
    #         nodelist.append([pRoot])
    #     else:
    #         return outlist
    #     while len(nodelist) and len(nodelist[0]):
    #         # 如果当前层是从左到右遍历
    #         if lefttoright:
    #             outlist.append([node.val for node in nodelist[0]])
    #             # 修改标志变量
    #             lefttoright = False
    #         else:
    #             # 如果当前层是从右至左遍历输出，则逆序将结点值存入输出列表
    #             outlist.append([nodelist[0][i].val for i in range(len(nodelist[0]) - 1, -1, -1)])
    #             lefttoright = True
    #         curnodelist = []
    #         for i in range(len(nodelist[0])):
    #             curnode = nodelist[0][i]
    #             if curnode.left:
    #                 curnodelist.append(curnode.left)
    #             if curnode.right:
    #                 curnodelist.append(curnode.right)
    #         nodelist.append(curnodelist)
    #         del nodelist[0]
    #     return outlist




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
print(Solution().Print(a))
