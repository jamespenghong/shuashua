class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        set_a = set([i for i in range(1,length+1)])
        set_b = set(nums)
        list_a = list(set_a-set_b)
        return list_a
        """
        使用了set
        """