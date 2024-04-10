# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node1 = ListNode(1,
                 ListNode(2,
                          ListNode(3,
                                   ListNode(3,
                                            ListNode(4,
                                                     ListNode(4,
                                                              ListNode(5)))))))


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fake = prev = ListNode(0, head)

        while head:
            if head.next and head.val == head.next.val:
                # skip the similar nodes
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return fake.next


a = Solution()
print(a.deleteDuplicates(node1))
