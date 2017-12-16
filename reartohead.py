-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        if listNode == None:       #先进行判断是否为空，然后遍历整个链表，然后把每一个值都
            return l                #都插在位置0，这样就实现了逆置。
        
        while listNode:
            l.insert(0,listNode.val)
            listNode = listNode.next
        return l
            