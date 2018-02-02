class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)