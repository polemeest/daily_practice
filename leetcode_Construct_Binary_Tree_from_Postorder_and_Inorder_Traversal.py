# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]
                  ) -> Optional[TreeNode]:
        hashmap = {v: i for i, v in enumerate(inorder)}

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None

            root = TreeNode(postorder.pop())
            mid = hashmap[root.val]
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)
            return root

        return build(0, len(inorder) - 1)


def treeprint(tree: TreeNode) -> None:
    if tree.left:
        treeprint(tree.left)
    if tree.right:
        treeprint(tree.right)
    print(tree.val, end=" ")


a = Solution()
treeprint(a.buildTree([9, 3, 15, 20, 7], [9, 15, 7, 20, 3]))  # 14.05.24
