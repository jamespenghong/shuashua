-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0))    #首先构造一棵树，根节点肯定是先序的第一个
        index = tin.index(root.val)     #然后再中序遍历中，属于根节点左边的就是左子树，右边就是右子数。
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index+1:])
        return root