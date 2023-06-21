def is_circular_linked_list(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

