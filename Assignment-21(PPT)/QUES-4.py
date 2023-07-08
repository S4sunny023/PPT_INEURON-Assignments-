class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nextRight = None

def connectNodes(root):
    if root is None:
        return

    queue = []
    queue.append(root)
    queue.append(None)

    while len(queue) > 1:
        node = queue.pop(0)

        if node is None:
            queue.append(None)
        else:
            node.nextRight = queue[0]

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def printConnectedNodes(root):
    while root:
        current = root
        while current:
            print(current.val, end=" ")
            current = current.nextRight
        print()
        root = root.left

# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# Connect nodes at the same level
connectNodes(root)

# Print the connected nodes at each level
printConnectedNodes(root)


