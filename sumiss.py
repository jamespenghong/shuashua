class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        ans = []
        res = []
        val = 0
        for i in range(1, tsum):
            val += i 
            res.append(i)
            while val > tsum:
                val -= res[0]
                res.pop(0)
            if val == tsum:
                ans.append(res[::])
        return ans
        """
        和为s的连续正数序列