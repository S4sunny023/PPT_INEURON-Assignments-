from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def left_view(root):
    if root is None:
        return []

    left_view = []
    queue = deque([(root, 0)])
    current_level = -1

    while queue:
        node, level = queue.popleft()

        if level > current_level:
            left_view.append(node.data)
            current_level = level

        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))

    return left_view


# Example 1
root1 = Node(4)
root1.left = Node(5)
root1.right = Node(2)
root1.right.left = Node(3)
root1.right.right = Node(1)
root1.right.left.left = Node(6)
root1.right.left.right = Node(7)

print(left_view(root1))  

# Example 2
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.right = Node(4)
root2.left.right.right = Node(5)
root2.left.right.right.right = Node(6)

print(left_view(root2))  
