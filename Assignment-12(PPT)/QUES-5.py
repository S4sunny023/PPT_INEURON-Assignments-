class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return

    slowPtr = head
    fastPtr = head

    # Detect the loop using Floyd's cycle-finding algorithm
    while fastPtr is not None and fastPtr.next is not None:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        if slowPtr == fastPtr:
            break

    # If there is no loop, return
    if fastPtr is None or fastPtr.next is None:
        return

    # Move slowPtr or fastPtr to the head and find the start of the loop
    slowPtr = head
    while slowPtr.next != fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    # Remove the loop by setting the next pointer of the previous node to None
    fastPtr.next = None

# Example usage
# Example 1
head1 = ListNode(1)
head1.next = ListNode(3)
head1.next.next = ListNode(4)
head1.next.next.next = head1.next

detectAndRemoveLoop(head1)

# Verify if the loop is removed
current = head1
while current is not None:
    print(current.val, end=" ")
    current = current.next

# Example 2
head2 = ListNode(1)
head2.next = ListNode(8)
head2.next.next = ListNode(3)
head2.next.next.next = ListNode(4)

detectAndRemoveLoop(head2)

# Verify if the loop is removed
current = head2
while current is not None:
    print(current.val, end=" ")
    current = current.next

