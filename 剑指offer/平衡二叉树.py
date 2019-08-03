"""
输入一棵二叉树，判断该二叉树是否是平衡二叉树。

平衡二叉搜索树（Balanced Binary Tree）具有以下性质：它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，
并且左右两个子树都是一棵平衡二叉树。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def deep(self, root):
        if root == None:
            return 0
        return max(self.deep(root.left), self.deep(root.right)) + 1

    def IsBalanced_Solution(self, root):
        # write code here
        if root == None:
            return True
        if (abs(self.deep(root.left) - self.deep(root.right)) < 2 and self.IsBalanced_Solution(
                root.left) and self.IsBalanced_Solution(root.right)):
            return True
        else:
            return False

a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(3)
print(Solution().deep(a))