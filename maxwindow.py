class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not num or size==0 or len(num)<size:
            return []
        length = len(num)-size+1
        result = [0]*length

        for i in range(length):
            result[i] = max(num[i:i+size])

        return result