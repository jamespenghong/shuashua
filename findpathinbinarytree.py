# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []
        if root.right == None and root.left == None and root.val == expectNumber:
            return [[root.val]]
        if root.right == None and root.left == None and root.val != expectNumber:
            return []
        res = []
        res_left = self.FindPath(root.left, expectNumber - root.val)
        res_right = self.FindPath(root.right, expectNumber - root.val)
        for i in res_left + res_right:
            res.append([root.val]+i)
        return res 
        """
        在一棵二叉树里查找和为某一个数的路径
        递归方法
        """