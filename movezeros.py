class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero],nums[i]
                zero += 1


nums = [2,0,1,0,3,12]
s = Solution()
print(s.moveZeroes(nums))


"""
注意，这里zero实际上是记录了0的位置
"""