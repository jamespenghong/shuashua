class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def self_devide(n):
            for d in str(n):
                if d == '0' or n % int(d) > 0:
                    return False
            return True
            #一开始return的位置有问题，导致全部return为True
            
        a = []
        for i in range(left, right+1):
            if self_devide(i):
                a.append(i)
        return a 
        #也是return位置问题，应该return最后的结果，而不是每一次都return。