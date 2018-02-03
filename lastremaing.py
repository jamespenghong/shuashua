class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n<1:
            return -1
        con = range(n)
        final = -1
        start = 0
        while con:
            k = (start + m - 1 )%n
            final = con.pop(k)
            n -= 1
            start = k
        return final 
        """
        最后一个剩下的人，只要模拟这个过程就行了
        