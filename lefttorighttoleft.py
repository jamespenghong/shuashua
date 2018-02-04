# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, tree, left_right = [], [pRoot], True
        while tree:
            sub_tree = []
            row = []
            for item in tree:
                row.append(item.val)
                if item.left:
                    sub_tree.append(item.left)
                if item.right:
                    sub_tree.append(item.right)
            if left_right:
                res.append(row)
            else:
                row.reverse()
                res.append(row)
            tree = sub_tree
            left_right = not left_right
        return res
        