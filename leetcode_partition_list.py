# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5, ListNode(2))))))
node2 = ListNode(2, ListNode(1))

class Solution:
    def print_node(self, head):
        while head:
            print(head.val, sep=" -> ")
            head = head.next

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # before = []
        # after = []
        # head_head = head

        # while head:
        #     if head.val < x:
        #         before.append(head)
        #     else:
        #         after.append(head)
        #     head = head.next

        # if before:
        #     for index in range(len(before) - 1):
        #         before[index].next = before[index + 1]
        #     if after:
        #         before[-1].next = after[0]
        # if after:
        #     for index in range(len(after) - 1):
        #         after[index].next = after[index + 1]
        #     after[-1].next = None

        # head = head_head
        # self.print_node(head)

        # return before[0] if before else after[0]
        dummy1 = pointer1 = ListNode(0)
        dummy2 = pointer2 = ListNode(0)

        while head:
            if head.val < x:
                pointer1.next = head
                pointer1 = pointer1.next
            else:
                pointer2.next = head
                pointer2 = pointer2.next
            head = head.next
        pointer2.next = None
        pointer1.next = dummy2.next

        return dummy1.next



a = Solution()
print(a.partition(node2, 2))
print(a.partition(node1, 3))
