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
    def __init__(self):
        self.visited = {}


    def copyRandomList(self, head):
        if not head:
            return head
        
        old_to_copy = {None : None}

        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next
        
        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next
        
        return old_to_copy[head]

a = Solution()
print(a.copyRandomList(head = node1))