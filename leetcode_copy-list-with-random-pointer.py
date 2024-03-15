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
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        head_head = head
        copy_head = Node(head_head.val)
        copy = copy_head
        head_map, pointer = {0: head.random}, 1
        head_lst = [head]

        while head.next:
            head = head.next
            head_map[pointer] = head.random
            head_lst.append(head)
            copy.next = Node(head.val)
            copy, pointer = copy.next, pointer + 1
        print(copy)
        copy, pointer = copy_head, 0
        while copy:
            copy_random = copy_head
            target = head_map[pointer]
            if target:
                target_ind = head_lst.index(target)
                for i in range(target_ind):
                    copy_random = copy_random.next
                copy.random = copy_random
            copy, pointer = copy.next, pointer + 1


        return copy_head

a = Solution()
print(a.copyRandomList(head = node1))