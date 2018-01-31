class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        x, y = zip(*ops)
        return min(x) * min(y)
        """
        *ops将二维数组分成多个一维数组
        