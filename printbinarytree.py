# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        currentstack = [root]
        res = []
        while currentstack:
            nextstack = []
            for i in currentstack:
                if i.left:
                    nextstack.append(i.left)
                if i.right:
                    nextstack.append(i.right)
                res.append(i.val)
            currentstack = nextstack
        return res
        """
        每次打印一个节点
        """


    def PrintFromTopToBottom(self, root):
            if not root:
                return []
            q=[root]
            result_list=[]
            while len(q):
                a = q.pop(0)
                result_list.append(a.val)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            return result_list