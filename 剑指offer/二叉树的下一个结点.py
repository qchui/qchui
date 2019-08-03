"""

给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

         A
       B   E
        C    F
       D    G
           H  K
比如上图二叉树遍历结果

    前序遍历：ABCDEFGHK

    中序遍历：BDCAEHGKF

    后序遍历：DCBHKGFEA
"""
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
     # def LeftNext(self,pNode):  中序遍历
     #    if not pNode:
     #        return
     #    print(pNode.val)
     #    self.LeftNext(pNode.left)
     #    self.LeftNext(pNode.right)
    def LeftNext(self,pNode):
        if  not pNode.left:
            return pNode
        return self.LeftNext(pNode.left)
    def GetNext(self, pNode):
        if pNode.left:
            return self.LeftNext(pNode).val
        return pNode.val

a=TreeLinkNode(1)
b=TreeLinkNode(2)
c=TreeLinkNode(3)
d=TreeLinkNode(4)
e=TreeLinkNode(5)
f=TreeLinkNode(6)
g=TreeLinkNode(7)
a.left=b
a.right=c
b.left=d
b.right=e
d.left=f
d.right=g
print(Solution().LeftNext(a))