class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findDistance(root, node1, node2):
    if root is None:
        return 0

    if node1.val < root.val and node2.val < root.val:
        return findDistance(root.left, node1, node2)
    elif node1.val > root.val and node2.val > root.val:
        return findDistance(root.right, node1, node2)
    else:
        return findDistanceFromNode(root, node1) + findDistanceFromNode(root, node2)

def findDistanceFromNode(root, node):
    if root is None:
        return 0

    if node.val == root.val:
        return 0
    elif node.val < root.val:
        return 1 + findDistanceFromNode(root.left, node)
    else:
        return 1 + findDistanceFromNode(root.right, node)

def constructBST(values):
    n = len(values)
    if n == 0:
        return None

    root = TreeNode(values[0])

    for i in range(1, n):
        insertIntoBST(root, values[i])

    return root

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root

# Example 1
values1 = [8, 3, 1, 6, 4, 7, 10, 14, 13]
node1 = TreeNode(6)
node2 = TreeNode(14)
root1 = constructBST(values1)
distance1 = findDistance(root1, node1, node2)
print("The distance between the two keys:", distance1)


# Example 2
values2 = [8, 3, 1, 6, 4, 7, 10, 14, 13]
node3 = TreeNode(3)
node4 = TreeNode(4)
root2 = constructBST(values2)
distance2 = findDistance(root2, node3, node4)
print("The distance between the two keys:", distance2)

