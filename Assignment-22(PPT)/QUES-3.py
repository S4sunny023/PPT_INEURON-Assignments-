class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def printRootToLeafPaths(root):
    if root is None:
        return

    stack = []
    stack.append((root, []))

    while stack:
        node, path = stack.pop()
        path.append(node.val)

        if node.left is None and node.right is None:
            print("->".join(map(str, path)))
        
        if node.right:
            stack.append((node.right, path.copy()))

        if node.left:
            stack.append((node.left, path.copy()))

# Create the binary tree
root = Node(6)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)
root.right.right = Node(4)
root.left.right.left = Node(7)
root.left.right.right = Node(4)

# Print all the root-to-leaf paths
printRootToLeafPaths(root)


