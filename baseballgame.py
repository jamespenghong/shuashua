class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        total = []
        for op in ops:
            if op == 'C':
                total.pop()       #一开始还把问题想复杂了，主要就是进行判断。
            elif op == 'D':
                total.append(total[-1]*2)    
            elif op == '+':
                total.append(total[-1] + total[-2])
            else:
                total.append(int(op))
        return sum(total)