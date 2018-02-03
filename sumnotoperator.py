class Solution:
    def Add(self, num1, num2):
        # write code here
        return sum([num1,num2])




	def Add(self, num1, num2):
        # write code here
        num_bit = 2**32-1
        newnum1 = (num1&num_bit) ^ (num2 & num_bit)
        newnum2 = ((num1 & num2) << 1) & num_bit  #python中直接左移没有益出效果
        if newnum2:
            return self.Add(newnum1,newnum2)
        else :
            return newnum1