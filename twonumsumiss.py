class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i = 0
        j = len(array) - 1
        while i < j:
            temp = array[i] + array[j]
            if temp == tsum:
                return [array[i],array[j]]
            elif temp > tsum:
                j -= 1
            elif temp < tsum:
                i += 1
        return []
        """
        一头一尾两个指针