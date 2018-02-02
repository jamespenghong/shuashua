# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        list1, list2 = [], []
        while pHead1 != None:
            list1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2 != None:
            list2.append(pHead2)
            pHead2 = pHead2.next
        for node in list1:
            if node in list2:
                return node
        return None