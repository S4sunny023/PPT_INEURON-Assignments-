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

# Example 1
# LinkedList: 1->2->2->4->5->6->7->8
# K = 4
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

k = 4
head = reverseKNodes(head, k)

# Print the modified linked list
while head is not None:
    print(head.data, end=' ')
    head = head.next
# Output: 4 2 2 1 8 7 6 5

# Example 2
# LinkedList: 1->2->3->4->5
# K = 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

k = 3
head = reverseKNodes(head, k)

# Print the modified linked list
while head is not None:
    print(head.data, end=' ')
    head = head.next
