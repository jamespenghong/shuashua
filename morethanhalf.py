import math
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers.sort()
        for i in range (int((math.ceil(len(numbers)/2)))):
            if numbers[i] == numbers[i + int(math.floor(len(numbers)/2))]:
                return numbers[i]
        return 0

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        only = set(numbers)
        length = len(numbers)/2
        for i in only:
            if numbers.count(i) > length:
                return i
        return 0