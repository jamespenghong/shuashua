class Solution:
    def jumpFloorII(self, number):
        # write code here
        return 2**(number-1)
        """
        变态青蛙跳进阶
		因为n级台阶，第一步有n种跳法：跳1级、跳2级、到跳n级
		跳1级，剩下n-1级，则剩下跳法是f(n-1)
		跳2级，剩下n-2级，则剩下跳法是f(n-2)
		所以f(n)=f(n-1)+f(n-2)+...+f(1)
		因为f(n-1)=f(n-2)+f(n-3)+...+f(1)
		所以f(n)=2*f(n-1)
		还有一种分析是对于每一级台阶只有跳或不跳两种选择，
		当然最后一级必须跳，所以就是2的阶乘