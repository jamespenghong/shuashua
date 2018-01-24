class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)
        if '00' not in s and '11' not in s:
            return True
        return False


"""
判断一个二进制数相邻两位是否总是不同
这种情况只需要找反例，如果出现了00或者11
那么肯定就不符合。这比正向查找简单多了。
这种思路要多学习。
"""