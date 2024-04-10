# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node1 = ListNode(1)
node2 = ListNode(1, ListNode(2))


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int
                         ) -> Optional[ListNode]:
        if not head:
            return head

        fake = ListNode(0, head)
        left = fake
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left, right = left.next, right.next

        left.next = left.next.next
        return fake.next


a = Solution()
print(a.removeNthFromEnd(node1, 1))
print(a.removeNthFromEnd(node, 2))
print(a.removeNthFromEnd(node2, 1))
