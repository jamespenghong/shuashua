class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        alist = []
        for num in nums:
            alist.extend(num)
        if len(alist) < r * c:
            return nums
        blist = [[0 for i in range(c)] for i in range(r)]
        for row in range(r):
            blist[row] = alist[c * row : c* (row+1)]
        return blist
        
        """对矩阵进行转置，我这个是比较笨的方法了。
        """
# def matrixReshape(self, A, nR, nC):
#     if len(A) * len(A[0]) != nR * nC:
#         return A
        
#     vals = (val for row in A for val in row)
#     return [[vals.next() for c in xrange(nC)] for r in xrange(nR)]