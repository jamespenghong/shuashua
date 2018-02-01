# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return 
        newnode = RandomListNode(pHead.label)
        newnode.random = pHead.random
        newnode.next = self.Clone(pHead.next)
        return newnode
        