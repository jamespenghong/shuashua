# -*- coding:utf-8 -*-
class Solution:
    def replaceSpace(self, s):
        # write code here
        s = s.split(' ')
        return '%20'.join(s)   #先分解成一个数组，然后join