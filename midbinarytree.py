# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        res = self.mid(pRoot)
        if k<=0 or k >len(res):
            return None
        return res[k-1]
            
    def mid(self,tree):
        if tree == None:
            return []
        left = self.mid(tree.left)
        right = self.mid(tree.right)
        return left+[tree]+right