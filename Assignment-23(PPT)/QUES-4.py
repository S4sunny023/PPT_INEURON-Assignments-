from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottom_view(root):
    if root is None:
        return []

    bottom_view_map = {}
    queue = deque([(root, 0)])

    while queue:
        node, distance = queue.popleft()

        bottom_view_map[distance] = node.data

        if node.left:
            queue.append((node.left, distance - 1))
        if node.right:
            queue.append((node.right, distance + 1))

    sorted_distances = sorted(bottom_view_map.keys())
    bottom_view = [bottom_view_map[distance] for distance in sorted_distances]

    return bottom_view


# Example 1
root1 = Node(20)
root1.left = Node(8)
root1.right = Node(22)
root1.left.left = Node(5)
root1.left.right = Node(3)
root1.right.right = Node(25)
root1.left.right.left = Node(10)
root1.left.right.right = Node(14)

print(bottom_view(root1))  

# Example 2
root2 = Node(20)
root2.left = Node(8)
root2.right = Node(22)
root2.left.left = Node(5)
root2.left.right = Node(3)
root2.right.left = Node(4)
root2.right.right = Node(25)
root2.left.right.left = Node(10)
root2.left.right.right = Node(14)

print(bottom_view(root2))  
 

