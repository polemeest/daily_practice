class ListNode:

    def __init__(self, val=0, next=None):

        self.val = val

        self.next = next


def reverseKGroup(head, k):
    head_head = head

    # check if node is long enough
    counter = 0
    while head and counter < k:
        head = head.next
        counter += 1
    if counter < k:
        return head_head

    # main loop
    head = head_head
    prev = None

    for _ in range(k):
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    head_head.next = reverseKGroup(head, k)

    return prev




# Driver code and test cases

# Test Case 1: Reverse groups of 2 nodes

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Output: 2 -> 1 -> 4 -> 3 -> 5 -> None

head1 = ListNode(1)

head1.next = ListNode(2)

head1.next.next = ListNode(3)

head1.next.next.next = ListNode(4)

head1.next.next.next.next = ListNode(5)

k1 = 2

reversed_list1 = reverseKGroup(head1, k1)

while reversed_list1:

    print(reversed_list1.val, end=" -> ")

    reversed_list1 = reversed_list1.next

print("None")


# Test Case 2: Reverse groups of 3 nodes

# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None

# Output: 3 -> 2 -> 1 -> 4 -> 5 -> None

head2 = ListNode(1)

head2.next = ListNode(2)

head2.next.next = ListNode(3)

head2.next.next.next = ListNode(4)

head2.next.next.next.next = ListNode(5)

k2 = 3

reversed_list2 = reverseKGroup(head2, k2)

while reversed_list2:

    print(reversed_list2.val, end=" -> ")

    reversed_list2 = reversed_list2.next

print("None")