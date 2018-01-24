class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        res = 0
        for num in nums:
            if num == 1:
                one += 1
                res = max(one, res)
            else:
                one = 0
        return res

"""
找一个二进制序列最长的1的数量
这里对数列循环，遇到1增加，遇到0置0，
同时保留之前的最大值
"""