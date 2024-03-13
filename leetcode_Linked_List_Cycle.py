

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        while pointer:
            if pointer.val == "seen":
                return True
            else:
                pointer.val == "seen"
            pointer = pointer.next
        return False


a = Solution()
print(a.hasCycle(node1))