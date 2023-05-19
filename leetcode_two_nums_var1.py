from typing import Optional
import time
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def recursion(lst: list) -> Optional[ListNode]:
            if lst:
                return ListNode(lst.pop(), recursion(lst))
            return None

        def unpack(lst: Optional[ListNode]) -> list:
            if lst.next:
                return [str(lst.val)] + unpack(lst.next)
            return [str(lst.val)]

        summ = [''.join(unpack(l1)[::-1])] + [''.join(unpack(l2)[::-1])]
        summ = sum(map(int, summ))
        summ = '.'.join(str(summ)).split('.')
        end = recursion(summ)

        return print(unpack(end))

        # print([ListNode(i, ListNode(i)) for i in end])
        # print('.'.join(str(summ)).split('.')[::-1])
        # ListNode(7, ListNode(0, ListNode(8)))


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
a = Solution()
start = time.time()
a.addTwoNumbers(l1, l2)
print(time.time() - start)





# summ = [''.join([str(i) for i in reversed(l1)])] + [''.join([str(i) for i in reversed(l2)])]
# summ = sum(map(int, summ))
# print('.'.join(str(summ)).split('.')[::-1])