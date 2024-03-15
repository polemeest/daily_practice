# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

node1 = Node(7, Node(13, Node(11, Node(10, Node(1, None)))))
head = node1
head.random = node1.next.next.next.next.next
head.next.random = node1
head.next.next.random = node1.next.next.next.next
head.next.next.next.random = node1.next.next
head.next.next.next.next.random = node1



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return head

        head_head = head
        head_map = {None: None}

        while head:
            copy = Node(head.val)
            head_map[head] = copy
            head = head.next
        head = head_head
        while head:
            copy = head_map[head]
            copy.next, copy.random = head_map[head.next], head_map[head.random]
            head = head.next
        return head_map[head_head]

a = Solution()
print(a.copyRandomList(head = node1))