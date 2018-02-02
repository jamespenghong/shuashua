class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = 0
        for i in array:
            ans ^= i 
        flag = len(bin(ans)) - bin(ans).index('1')
        list1 = []
        list2 = []
        for x in array:
            if bin(x)[-flag] == '1':
                list1.append(x)
            else:
                list2.append(x)
        ans1, ans2 = 0, 0
        for i in list1:
            ans1 ^= i 
        for i in list2:
            ans2 ^= i 
        return [ans1, ans2]