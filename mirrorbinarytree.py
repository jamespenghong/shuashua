class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root:
            root.right, root.left = self.Mirror(root.left), self.Mirror(root.right)
            return root
        else:
            return None
            """
            递归解决二叉树镜像
            """