class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddleNode(head):
    if head is None or head.next is None:
        return None

    # Initialize pointers
    slowPtr = head
    fastPtr = head
    prevPtr = None

    # Traverse the linked list to find the middle node
    while fastPtr is not None and fastPtr.next is not None:
        fastPtr = fastPtr.next.next
        prevPtr = slowPtr
        slowPtr = slowPtr.next

    # Adjust the pointers to delete the middle node
    prevPtr.next = slowPtr.next
    slowPtr.next = None

    return head

# Helper function to print the linked list
def printLinkedList(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()





# Example usage
# Example 1
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)

print("Original linked list:")
printLinkedList(head1)

head1 = deleteMiddleNode(head1)

print("Modified linked list:")
printLinkedList(head1)

# Example 2
head2 = ListNode(2)
head2.next = ListNode(4)
head2.next.next = ListNode(6)
head2.next.next.next = ListNode(7)
head2.next.next.next.next = ListNode(5)
head2.next.next.next.next.next = ListNode(1)

print("Original linked list:")
printLinkedList(head2)

head2 = deleteMiddleNode(head2)

print("Modified linked list:")
printLinkedList(head2)
