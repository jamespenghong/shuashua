# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        res = []
        while pHead1:
            res.append(pHead1.val)
            pHead1 = pHead1.next
        while pHead2:
            res.append(pHead2.val)
            pHead2 = pHead2.next
        res.sort()
        dummy = ListNode(0)
        pre = dummy
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return dummy.next
        """
        这里主要是先把所有的元素取出来，然后
        构造一个新的链表

        另一种解法，在两个链表同时存在的情况下，比较头元素，然后向后移，
        当只剩一个链表的时候，只用接上去就行了
        """



class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        dummy = ListNode(0)
        pHead = dummy
         
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                dummy.next = pHead2
                pHead2 = pHead2.next
            else:
                dummy.next = pHead1
                pHead1 = pHead1.next
                 
            dummy = dummy.next
         
        if pHead1:
            dummy.next = pHead1
        elif pHead2:
            dummy.next = pHead2
         
        return pHead.next
