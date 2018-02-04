# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        l = []
        if not pHead:
            return None
        while pHead:
            if pHead  not in l:
                l.append(pHead)
                pHead = pHead.next
            else:
                return pHead