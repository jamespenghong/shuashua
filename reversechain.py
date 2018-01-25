# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        pre = None
        while pHead:
            pos = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = pos
        return pre
            """
            翻转一个链表，首先pre为空，
            然后POS指向next，然后把pre置为next
            然后把遍历过的赋给pre，然后head向前移一位