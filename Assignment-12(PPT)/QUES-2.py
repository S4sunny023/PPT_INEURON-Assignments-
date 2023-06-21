class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectLoop(head):
    if head is None or head.next is None:
        return False

    slowPtr = head
    fastPtr = head

    while fastPtr is not None and fastPtr.next is not None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            return True

    return False

# Example usage
# Example 1
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = head1.next

print("Linked list contains a loop:", detectLoop(head1))

# Example 2
head2 = ListNode(1)
head2.next = ListNode(8)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)

print("Linked list contains a loop:", detectLoop(head2))
