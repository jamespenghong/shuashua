class Solution:
    def jumpFloor(self, number):
        if number < 0:
            return False
        elif number == 1:
            return 1
        elif  number == 2:
            return 2
        else:
            first, second, third = 1, 2, 0
            for  i in xrange(3,number+1,1):
                third = first + second
                first = second
                second = third
            return third
            """
            青蛙跳台阶问题，实际上是斐波那契数列
            这里用了迭代的方法
            """