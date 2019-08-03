"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。

用递归思想

前序遍历是{1,2,4,7,3,5,6,8}，中序遍历是{4,7,2,1,5,3,8,6}，可以知道1是根节点，
则在中序遍历中，4,7,2都是1的左子树，5,3,8,6都是1的右子树；从前序遍历又可以知道2是1的左子节点，
是1的左子树中“根节点”的存在；3是1的右子节点，是1的右子树中“根节点”的存在；因而可以不断递归，直至明确每个节点的位置

"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        else:
            res = TreeNode(pre[0])
            res.left = self.reConstructBinaryTree(pre[1: tin.index(pre[0]) + 1], tin[: tin.index(pre[0])])
            res.right = self.reConstructBinaryTree(pre[tin.index(pre[0]) + 1: ], tin[tin.index(pre[0]) + 1: ])
        return res