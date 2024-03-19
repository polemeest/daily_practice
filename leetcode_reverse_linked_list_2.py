# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
node2 = ListNode(5)
    

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(1, left):
            prev = prev.next
            head = head.next

        begin = prev
        end = head

        for _ in range(left, right + 1):
            next = head.next
            head.next = prev
            prev = head
            head = next
        
        begin.next = prev
        end.next = head

        return dummy.next

        
        return head_head


a = Solution()
print(a.reverseBetween(head = node1, left = 2, right = 4))
print(a.reverseBetween(head = node2, left = 1, right = 1))
