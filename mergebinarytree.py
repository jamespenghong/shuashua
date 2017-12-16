class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.right = self.mergeTrees(t1.right , t2.right)   #递归
            root.left = self.mergeTrees(t1.left , t2.left)    #递归
            return root
        return t1 or t2