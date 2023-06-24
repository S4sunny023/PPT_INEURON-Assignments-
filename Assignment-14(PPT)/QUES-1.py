class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def detectAndRemoveLoop(head):
    if head is None or head.next is None:
        return

    slow = head.next
    fast = head.next.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            break
        slow = slow.next
        fast = fast.next.next

    if slow != fast:
        return

    # Move slow pointer to the head
    slow = head

    # If the loop starts at the head node
    if slow == fast:
        while fast.next != slow:
            fast = fast.next
        fast.next = None
        return

    # Move slow and fast pointers at the same speed until they meet
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop by setting the next pointer of the last node to None
    fast.next = None

    return





