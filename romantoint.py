class Solution:
	def romanToInt(self, s):
		romans = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
		preval_value = running_total = 0
		for i in range(len(s)-1, -1, -1):
			int_val = romans[s[i]]
			if int_val <preval_value:
				running_total -= int_val
			else:
				running_total += int_val
			preval_value = int_val
		return running_total
