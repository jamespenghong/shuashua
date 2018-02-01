class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        i = 0
        for node in sequence[:-1]:
            i += 1
            if node > root:
                break
            
        for node in sequence[i:-1]:
            if node < root:
                return False
        left = True
        if i > 1:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 2 and left:
            right = self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
        """
        验证一个序列是否是后序遍历，
        后序遍历的序列最后一个为根节点，然后左子树全部小于根节点
        右子树全部大于根节点