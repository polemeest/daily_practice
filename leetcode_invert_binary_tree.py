
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def __str__(self):
        return f"{self.val}, {self.left}, {self.right}" 


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:  
        if root is None:
            return
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root 
    
tree = TreeNode(2, TreeNode(1), TreeNode(3))


a = Solution()
print(a.invertTree(root = tree))