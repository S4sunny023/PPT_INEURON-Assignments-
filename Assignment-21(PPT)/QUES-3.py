class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

def inorderTraversal(root, prev):
    if root is None:
        return prev

    prev = inorderTraversal(root.left, prev)
    root.prev = prev

    if prev is not None:
        prev.next = root

    prev = root
    prev = inorderTraversal(root.right, prev)

    return prev

def convertToDoublyLinkedList(root):
    if root is None:
        return None

    prev = inorderTraversal(root, None)
    prev.next = None

    head = prev
    while head is not None and head.prev is not None:
        head = head.prev

    return head

# Create the binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(30)
root.right.right = Node(35)


head = convertToDoublyLinkedList(root)

# Traverse the doubly linked list
while head is not None:
    print(head.val, end=" ")
    head = head.next


