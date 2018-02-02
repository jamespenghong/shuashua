# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.treedepth(pRoot.left)
        right = self.treedepth(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    
    def treedepth(self,pRoot):
        if not pRoot:
            return 0
        left = self.treedepth(pRoot.left)
        right = self.treedepth(pRoot.right)
        return max(left, right) + 1
        """
        判断是否是平衡二叉树，先求数的长度，
        然后判断左右子树的长度差是否大于1