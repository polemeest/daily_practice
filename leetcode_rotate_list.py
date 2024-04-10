# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node2 = ListNode(0, ListNode(1, ListNode(2)))


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int
                    ) -> Optional[ListNode]:
        if not head or k == 0 or not head.next:
            return head

        counter = 1
        last = head
        while last.next:
            counter += 1
            last = last.next

        k = k % counter
        if k == 0:
            return head

        new_last = head
        for i in range(counter - k - 1):
            new_last = new_last.next

        new_head = new_last.next
        new_last.next = None
        last.next = head
        return new_head


a = Solution()
print(a.rotateRight(node1, 2))
print(a.rotateRight(node2, 4))
