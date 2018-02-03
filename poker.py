class Solution:
    def IsContinuous(self, numbers):
        numbers = list(filter(lambda x:x!=0,numbers))
        if numbers != [] and max(numbers) - min(numbers) <=4 and len(numbers)==len(set(numbers)):
            return True
        return False
        