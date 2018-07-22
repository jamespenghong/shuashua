class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        matrix = [[sum(int(t) for t in str(i)+str(j))<=threshold for i in range(cols)] for j in range(rows)]
        if matrix[0][0]: nex =[(0,0)]
        else: nex=[]
        ans = 0
        while len(nex):
            ans +=len(nex)
            temp=[]
            for i,j in nex:
                if i+1 < rows and matrix[i+1][j] and (i+1,j) not in temp:
                    temp.append((i+1,j))
                if j+1 < cols and matrix[i][j+1] and (i,j+1) not in temp:
                    temp.append((i,j+1))
            nex = temp
        return ans