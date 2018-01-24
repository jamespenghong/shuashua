class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for num in nums:
            res ^= num
        return res


"""
一个list，每个数字都出现了两次，只有一个出现了一次，找到出现一次的数
这里用了^运算符，0异或其他数还等于其他数，然后相等的数异或又为0，这样最终只剩下一个
数
"""
