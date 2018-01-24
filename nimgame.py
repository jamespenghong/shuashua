class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n % 4 == 0:
            return False
        return True


"""
有一堆石头，每次只能拿1或者2或者3块，谁拿最后一块谁赢，
在这个问题中，如果总数是4的倍数，那么先拿的的必输，因为四块
不管你拿多少，最后一块都是别人的，但如果不是4的倍数，那么你可以
先拿掉总数模4的余数，这样相当于让给了他
"""