# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res, tree = [],[pRoot]
        while tree:
            row,sub_tree =[], []
            for item in tree:
                row.append(item.val)
                if item.left:
                    sub_tree.append(item.left)
                if item.right:
                    sub_tree.append(item.right)
            res.append(row)
            tree = sub_tree
        return res