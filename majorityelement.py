class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
        """
        这个题目里规定了肯定存在这个数，出现了一半以上
        那么排序之后，它肯定在中间