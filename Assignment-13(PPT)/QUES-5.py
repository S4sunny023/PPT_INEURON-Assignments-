class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def deleteLastOccurrence(head, key):
    if head is None:
        return None

    prev = None
    last = None
    curr = head

    # Traverse the linked list to find the last occurrence of the key
    while curr is not None:
        if curr.data == key:
            last = curr
        curr = curr.next

    # Key not found in the linked list
    if last is None:
        return head

    # Update the linked list to remove the last occurrence of the key
    if last == head:
        head = head.next
    else:
        curr = head
        while curr.next != last:
            curr = curr.next
        curr.next = last.next

    return head
