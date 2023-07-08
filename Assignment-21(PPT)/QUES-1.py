class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    if root is None:
        return []

    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

def convertToBST(root):
    inorderList = inorderTraversal(root)
    inorderList.sort()

    def convertToBSTHelper(root, inorderList, index):
        if root is None:
            return None

        root.val = inorderList[index]
        root.left = convertToBSTHelper(root.left, inorderList, 2 * index + 1)
        root.right = convertToBSTHelper(root.right, inorderList, 2 * index + 2)

        return root

    newRoot = convertToBSTHelper(root, inorderList, 0)

    return newRoot

# Example
root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(8)
root.left.right = TreeNode(4)

newRoot = convertToBST(root)


inorder = inorderTraversal(newRoot)
print(inorder)

