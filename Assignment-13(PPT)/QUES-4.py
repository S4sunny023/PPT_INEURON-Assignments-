class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseKNodes(head, k):
    count = 0
    prev = None
    curr = head
    next = None

    # Reverse the first k nodes
    while curr is not None and count < k:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # Recursively reverse the remaining nodes
    if next is not None:
        head.next = reverseKNodes(next, k)

    return prev

def reverseAlternateKNodes(head, k):
    curr = head
    count = 0

    # Traverse the first k nodes and reverse
    while curr is not None and count < k:
        curr = curr.next
        count += 1

    # Reverse the next k nodes if there are more
    if count == k:
        curr = reverseKNodes(curr, k)

    # Skip the next k nodes and recursively reverse the remaining
    count = 0
    while curr is not None and count < k - 1:
        curr = curr.next
        count += 1

        if curr is not None:
            curr.next = reverseAlternateKNodes(curr.next, k)

    return head

