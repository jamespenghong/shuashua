class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ''
        list_s = list(s)
        stack = []
        for i in range(n):
            stack.append(list_s.pop(0))
        return ''.join(list_s+stack)



    def LeftRotateString(self, s, n):
        # write code here
        if s == "":
            return s
        n = n%len(s)
        return s[n:]+s[:n]
        """
        旋转字符串，既可以用切片，也可以用列表