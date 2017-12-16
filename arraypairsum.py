class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)   #先进行排序
        arraysum = 0
        for i in nums[::2]:   #步长为2取最小值，并累加
            arraysum += i
        return arraysum