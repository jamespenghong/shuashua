class Solution:
    def NumberOf1(self, n):
        # write code here
        if n == 0:
            return 0
        if n>0:
            return bin(n).replace('0b','').count('1')
        else:
            return bin(2**32+n).replace('0b','').count('1')
            """
            求二进制数1的个数，主要主要负数的情况
            """