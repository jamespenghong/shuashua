class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ''
        for s in s.split(' '):
            s = s[::-1]
            a +=''.join(s)
            a +=' '
        return a.rstrip()