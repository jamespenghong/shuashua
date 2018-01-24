class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))

"""
找最长非公共子串，首先如果两个字符串不一样长
那么肯定是长的字符串为最长非公共子串，如果两个长度相等，
只有当两者内容不相等的时候，才有非公共子串。
比如 aaaa和bbbb长度相同但内容不同。只有两者内容和长度都相等
那么返回-1
"""
