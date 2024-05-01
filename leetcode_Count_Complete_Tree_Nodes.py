# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree = TreeNode(1,
                TreeNode(2,
                         TreeNode(4), TreeNode(5)),
                TreeNode(3,
                         TreeNode(6)))


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def lefth(root):
            return 1 + lefth(root.left) if root else 0

        def righth(root):
            return 1 + righth(root.right) if root else 0

        l, r = lefth(root), righth(root)

        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 2 ** l - 1


a = Solution()
print(a.countNodes(tree))
