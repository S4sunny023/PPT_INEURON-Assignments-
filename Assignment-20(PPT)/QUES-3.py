class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def canRepresentBST(arr):
    if not arr:
        return "No"

    stack = []
    root = TreeNode(arr[0])
    stack.append(root)

    for i in range(1, len(arr)):
        parent = stack[-1]
        node = TreeNode(arr[i])

        while stack and stack[-1].val < node.val:
            parent = stack.pop()

        if node.val < parent.val:
            parent.left = node
        else:
            parent.right = node

        stack.append(node)

    if not stack:
        return "Yes"
    else:
        return "No"

# Example 1
arr1 = [7, 4, 12, 3, 6, 8, 1, 5, 10]
print(canRepresentBST(arr1))


# Example 2
arr2 = [11, 6, 13, 5, 12, 10]
print(canRepresentBST(arr2))



