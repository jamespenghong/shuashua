# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot==None:
            return True
        def isMirror(self,p1,p2):
            if p1==None and p2==None:
                return True
            elif (p1!=None and p2!=None) and p1.val==p2.val:
                return isMirror(self,p1.left,p2.right) and isMirror(self,p1.right,p2.left)
            else:
                return False
        return isMirror(self,pRoot.left,pRoot.right)
        """通过递归判断是否是对称二叉树