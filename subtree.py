# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        def convert(p):
            if p:
                return str(p.val) + convert(p.left) + convert(p.right)
            else:
                return ''
        if pRoot2:
            return convert(pRoot2) in convert(pRoot1)
        else :
            return False
            """
            判断一棵树是不是另一棵树的子结构
            这里把两棵树转换成了字符串，然后用in判断
            """