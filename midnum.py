class Solution:
    def __init__(self):
        self.data = []
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,n=None):
        # write code here
        length = len(self.data)
        if length%2 == 0:
            return (self.data[length/2-1]+self.data[length/2])/2.0
        else:
            return (self.data[length/2])