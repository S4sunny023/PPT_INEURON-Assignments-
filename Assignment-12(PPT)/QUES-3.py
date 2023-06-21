class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findNthFromEnd(head, N):
    if head is None:
        return -1

    firstPtr = head
    secondPtr = head

    # Move the firstPtr N nodes ahead
    for _ in range(N):
        if firstPtr is None:
            return -1
        firstPtr = firstPtr.next

    # Move both pointers until the firstPtr reaches the end
    while firstPtr is not None:
        firstPtr = firstPtr.next
        secondPtr = secondPtr.next

    return secondPtr.val

# Example usage
# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)
head1.next.next.next.next.next.next.next.next = ListNode(9)

N1 = 2

print("Nth node from the end:", findNthFromEnd(head1, N1))

# Example 2
head2 = ListNode(10)
head2.next = ListNode(5)
head2.next.next = ListNode(100)
head2.next.next.next = ListNode(5)

N2 = 5

print("Nth node from the end:", findNthFromEnd(head2, N2))
