
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        for i, s in enumerate(matrix):
            if s==path[0] and self.visit([(i//cols, i%cols)], matrix, rows, cols, path):
                return True
        return False
     
    def visit(self, ans, matrix, rows, cols, path):
        if len(ans)==len(path):
            return True
        i,j = ans[-1]
        nex = [(ii,jj) for ii,jj in [(i,j-1),(i,j+1),(i-1,j),(i+1,j)]
               if 0<= ii <rows and 0<= jj <cols and 
               (ii,jj) not in ans and
               matrix[ii*cols +jj]==path[len(ans)]]
        return sum([self.visit(ans+[x], matrix, rows, cols, path) for x in nex])