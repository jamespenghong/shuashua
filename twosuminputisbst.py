class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
        a = set()
        self.f = False
        def dfs(root, k):
            if not root:
                return 
            if root.val not in a:
                a.add(k - root.val)
            else:
                self.f = True
            dfs(root.left, k)
            dfs(root.right, k)
        dfs(root, k)
        return self.f
        """
        在二分查找树里面找是否存在两个数的和为给定的数。
        """