import itertools
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        li = itertools.permutations(ss)
        result = []
        for i in li:
            result.append(''.join(list(i)))
        result = list(set(result))
        result.sort()
        return result
        