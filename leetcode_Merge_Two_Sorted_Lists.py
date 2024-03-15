# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1, ListNode(2, ListNode(4)))
node2 = ListNode(1, ListNode(3, ListNode(4)))
node3 = ListNode(-9, ListNode(3))
node4 = ListNode(5, ListNode(7))
node5 = ListNode(None)
node6 = ListNode()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1

        new_list_head = ListNode()
        current_val = new_list_head
        while list1 and list2:
            if list1.val <= list2.val:
                current_val.val = list1.val
                list1 = list1.next
            else:
                current_val.val = list2.val
                list2 = list2.next
            if list1 or list2:
                current_val.next = ListNode()
                current_val = current_val.next
        if list1:
            current_val.val, current_val.next = list1.val, list1.next 
        elif list2:
            current_val.val, current_val.next = list2.val, list2.next 
        return new_list_head






a = Solution()
print(a.mergeTwoLists(list1 = node3, list2 = node4))
print(a.mergeTwoLists(list1 = node1, list2 = node2))
print(a.mergeTwoLists(list1 = node5, list2 = node6))
