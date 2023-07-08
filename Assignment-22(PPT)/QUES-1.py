class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev = None
        self.next = None

def convertToDLL(root):
    def convertToDLLHelper(root, prev, head):
        if root is None:
            return head

        head = convertToDLLHelper(root.left, prev, head)

        if prev is not None:
            prev.next = root
            root.prev = prev
        else:
            head = root

        prev = root
        head = convertToDLLHelper(root.right, prev, head)

        return head

    return convertToDLLHelper(root, None, None)

def printDLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

# Create the binary tree
root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.right.left = Node(30)
root.right.right = Node(35)

# Convert the binary tree to a doubly linked list
head = convertToDLL(root)

# Print the doubly linked list
printDLL(head)
# Output: 5 10 30 20 35
