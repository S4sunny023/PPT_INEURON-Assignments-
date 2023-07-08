class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)

    return root

def constructBST(levelOrder):
    root = None

    for val in levelOrder:
        root = insertIntoBST(root, val)

    return root

def inorderTraversal(node):
    if node is None:
        return []

    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

# Example
levelOrder = [7, 4, 12, 3, 6, 8, 1, 5, 10]
root = constructBST(levelOrder)
inorder = inorderTraversal(root)
print(inorder)

