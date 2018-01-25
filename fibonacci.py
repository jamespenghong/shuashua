class Solution:
    def Fibonacci(self, n):
        # write code here
        res = [0, 1, 1, 2]
        while len(res) <= n:
            res.append(res[-1] + res[-2])
        return res[n]
    	"""
    	一个斐波那契数列，这里用到了列表，没有用递归
    	节省了很多空间
    	"""
    	