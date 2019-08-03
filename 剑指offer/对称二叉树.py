"""
请实现一个函数，用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
"""
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.isSymmetricalTree(pRoot.left, pRoot.right)

    def isSymmetricalTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.isSymmetricalTree(root1.left, root2.right) and self.isSymmetricalTree(root1.right, root2.left)
        else:
            return False