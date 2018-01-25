class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: 
            return ''
        left, right = '', ''
        if t.left or t.right:
            left = '({})'.format(self.tree2str(t.left))
        if(t.right):
            right = '({})'.format(self.tree2str(t.right))
        return '{}{}{}'.format(t.val, left, right)
        """
        将二叉树转换为字符串