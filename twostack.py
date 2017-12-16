class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
        
    def push(self, node):
        self.stackA.append(node)        #A主要用来入队，B用来出队

    def pop(self):
        if self.stackB:
            return self.stackB.pop()   #当B有值的时候，直接从B弹出来，否则的话，
        elif not self.stackA:          #把所有A中的值放到B中，当A中也没有的时候，返回None
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()