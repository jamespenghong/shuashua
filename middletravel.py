class Solution:
    def GetNext(self, pNode):
        # write code here
        """根据中序遍历是“左根右”可以发现一共有两种情况：
        1.本结点是根，下一个结点是右：即本结点若有右子树，下一个结点是右子树中最左的那个。
        2.本结点是左，下一个结点是根：本结点是左孩子（没有右子树），下一个结点是根，或者继续向上遍历"""
        if not pNode:
            return
        if pNode.right:
            most_left = pNode.right
            while most_left.left:
                most_left = most_left.left
            return most_left
        else:
            if not pNode.next:
                return
            cur = pNode
            root = pNode.next
            while root and cur != root.left:
                cur = root
                root = root.next
            if not root:
                return
            else:
                return root