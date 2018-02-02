class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        i2, i3, i5 = 0, 0, 0
        result = [1]
        for i in range(1, index):
            new2 = result[i2] * 2
            new3 = result[i3] * 3
            new5 = result[i5] * 5
            new = min(new2, new3, new5)
            if new == new2:
                i2 += 1
            if new == new3:
                i3 += 1
            if new == new5:
                i5 += 1
            result.append(new)
        return result[-1]
        """
        新的丑数是在原有丑数的基础上得到的
