class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(map(len,s.replace('01','0 1').replace('10','1 0').split()))
        return sum(min(a, b) for a,b in zip(s, s[1:]))


"""
先把0和1的界限分隔开，然后生成一个
长度数组，然后分别前后两个比较，求和
注意在python3，map惰性运算，需要使用list
"""