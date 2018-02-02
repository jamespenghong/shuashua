class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in range(1,n+1):
            for i in str(i):
                if i == '1':
                    count += 1
        return count


        def countDigitOne(self, n):
		    if n <= 0:
		        return 0
		    q, x, ans = n, 1, 0
		    while q > 0:
		        digit = q % 10
		        q /= 10
		        ans += q * x
		        if digit == 1:
		            ans += n % x + 1
		        elif digit > 1:
		            ans += x
		        x *= 10
		    return ans
		    """
The idea is to calculate occurrence of 1 on every digit. There are 3 scenarios, for example

if n = xyzdabc

and we are considering the occurrence of one on thousand, it should be:

(1) xyz * 1000                     if d == 0
(2) xyz * 1000 + abc + 1           if d == 1
(3) xyz * 1000 + 1000              if d > 1
