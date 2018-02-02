class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)

        """
        Given a non-empty integer array of size n, find the minimum number of moves 
        required to make all array elements equal, where a move is incrementing n - 1 
        elements by 1.
        原问题是所有数加一，只有一个不加，现将问题转换为把最大的数减一，其他不变，
        反向考虑，太厉害了。