class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return num%9 if num%9!=0 else 9


"""
如果一个数是100a+10b+c, 那么 (100a+10b+c)%9=(a+99a+b+9b+c)%9=(a+b+c)%9
"""

