class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n and (n + self.Sum_Solution(n-1))



	def Sum_Solution(self, n):
        # write code here
        return reduce(lambda x, y: x + y, xrange(n+1))