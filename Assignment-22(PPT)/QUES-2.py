class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def flipBinaryTree(root):
    if root is None or (root.left is None and root.right is None):
        return root

    newRoot = flipBinaryTree(root.left)

    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return newRoot

def printBinaryTree(root):
    if root is None:
        return

    print(root.val, end=" ")
    printBinaryTree(root.left)
    printBinaryTree(root.right)

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Flip the binary tree
flippedRoot = flipBinaryTree(root)

# Print the flipped binary tree
printBinaryTree(flippedRoot)

