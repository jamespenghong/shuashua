class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return list(collections.Counter(t) - collections.Counter(s))[0]

 """
 collcetions模块
 """