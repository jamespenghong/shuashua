class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        alist = [str(i) for i in range(1, n+1)]
        for i in range(2, n, 3):
            alist[i] = "Fizz"
        for i in range(4, n, 5):
            alist[i] = "Buzz"
        for i in range(14, n, 15):
            alist[i] = "FizzBuzz"
        return alist
            
"""
替换列表，首先生成一个列表，然后在对应位置替换。