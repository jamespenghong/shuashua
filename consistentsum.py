class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        total = array[0]
        maxsum = array[0]
        for i in range(1, len(array)):
            if total >= 0 :
                total += array[i]
            else:
                total = array[i]
            if total > maxsum:
                maxsum = total
        return maxsum
        """

用total记录累计值，maxSum记录和最大
基于思想：对于一个数A，若是A的左边累计数非负，那么加上A能使得值不小于A，认为累计值对
整体和是有贡献的。如果前几项累计值负数，则认为有害于总和，total记录当前值。
此时 若和大于maxSum 则用maxSum记录下来