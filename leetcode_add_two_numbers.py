# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n1 = ListNode(2, ListNode(4, ListNode(3)))
n2 = ListNode(5, ListNode(6, ListNode(4)))
n3 = ListNode(0)
n4 = ListNode(0)
n5 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
n6 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def read(file: ListNode, drive: int = 0, step: int = 0) -> list | None:
            if file.next is None:
                return drive + file.val * (10 ** step)
            return read(file.next, drive + file.val * (10 ** step), step + 1)
        
        def write(file: int, flag = False) -> ListNode | None:
            if file:
                return ListNode(file % 10, write(file // 10, True))
            return None if flag else ListNode(0)

        # file = read(write(read(l1) + read(l2)))  ## Just for IDE checks
        return write(read(l1) + read(l2)) # file



a = Solution()
print(a.addTwoNumbers(l1 = n1, l2 = n2))
print(a.addTwoNumbers(l1 = n3, l2 = n4))
print(a.addTwoNumbers(l1 = n5, l2 = n6))