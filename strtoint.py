class Solution:
    def StrToInt(self, s):
        # write code here
        if s == None:
            return 0
        dict_number = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        dict_flag = {'+':1,'-':-1}
        flag = 1
        value = 0
        for i in range(len(s)):
            if i == 0 and (s[i] == '+' or s[i] == '-'):
                flag = dict_flag[s[i]]
            elif s[i] in dict_number:
                value = value*10 + dict_number[s[i]]
            else:
                return 0
        return flag*value
        """
        将字符串转换为数字，这里利用字典映射