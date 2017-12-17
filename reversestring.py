class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)[::-1]
        s = ''.join(s)        #还可以直接使用s[::-1],我这里先转换成了list，多此一举
        return s