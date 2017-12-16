class Solution:
	def Find(self, target, array):
		rows = len(array) - 1
		cols = len(array[0]) - 1
		i = rows
		j = 0
		while j <= cols and i >= 0:     #从左下角开始查询，如果查找目标比左下角的数小
			if target < array[i][j]:    #那么往上走，否则往右走，如果超出了边界就说明
				i -= 1                  #没有找到。
			elif target > array[i][j]:
				j += 1
			else:
				return True
		return False

s = Solution()
print(s.Find(5,[[1,2,3],[4,5,6]]))