# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        if pHead.val != pHead.next.val:
            pHead.next = self.deleteDuplication(pHead.next)
        else:
            temp = self.deleteDuplication(pHead.next.next)
            if temp is not None and temp.val == pHead.val:
                pHead = None
            else:
                pHead = temp
        return pHead