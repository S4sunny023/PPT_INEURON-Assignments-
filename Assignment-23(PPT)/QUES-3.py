from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_view(root):
    if root is None:
        return []

    right_view = []
    queue = deque([(root, 0)])
    current_level = -1

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            right_view.append(node.data)
            current_level = level

        if node.right:
            queue.append((node.right, level + 1))
        if node.left:
            queue.append((node.left, level + 1))

    return right_view


# Example 1
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.right.right.right = Node(8)

print(right_view(root1)) 

# Example 2
root2 = Node(1)
root2.left = Node(8)
root2.left.left = Node(7)

print(right_view(root2))  
