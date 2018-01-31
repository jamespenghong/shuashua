class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.trans(matrix)
        return result
    def trans(self, matrix):
        return zip(*matrix)[::-1]
            
            """
            顺时针打印矩阵，取第一行，然后进行转置，然后继续取第一行
            """