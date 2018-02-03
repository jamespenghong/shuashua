class Solution:
    def multiply(self, A):
        # write code here
        B = []
        for i in range(len(A)):
            b = 1
            for j in range(len(A)):
                if j!=i:
                    b *=A[j]
            B.append(b)
        return B