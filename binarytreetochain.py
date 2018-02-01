# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return 
        self.arr = []
        self.midTraver(pRootOfTree)
        for i,v in enumerate(self.arr[:-1]):
            v.right = self.arr[i+1]
            self.arr[i+1].left = v
        return self.arr[0]
    def midTraver(self,root):
        if not root:return
        self.midTraver(root.left)
        self.arr.append(root)
        self.midTraver(root.right)
        """
        将二叉树转换为双向链表