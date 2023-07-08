class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxSubtreeSum(node):
    if node is None:
        return 0

    leftSum = maxSubtreeSum(node.left)
    rightSum = maxSubtreeSum(node.right)

    subtreeSum = leftSum + rightSum + node.val

    global maxSum
    maxSum = max(maxSum, subtreeSum)

    return subtreeSum

def findMaxSubtreeSum(root):
    global maxSum
    maxSum = float('-inf')

    maxSubtreeSum(root)

    return maxSum

# Example 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)
root1.right.left = TreeNode(6)
root1.right.right = TreeNode(7)
print(findMaxSubtreeSum(root1))


# Example 2
root2 = TreeNode(1)
root2.left = TreeNode(-2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(-6)
root2.right.right = TreeNode(2)
print(findMaxSubtreeSum(root2))

