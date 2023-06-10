class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(s):
    if not s:
        return None
    if '(' not in s:
        return TreeNode(int(s))

    # Find the index of the first opening parenthesis
    idx = s.index('(')
    value = int(s[:idx])
    node = TreeNode(value)

    # Find the index of the matching closing parenthesis
    count = 0
    for i in range(idx, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
        if count == 0:
            left_subtree = s[idx + 1:i]
            right_subtree = s[i + 2:-1]
            break

    node.left = constructTree(left_subtree)
    node.right = constructTree(right_subtree)

    return node

def inorderTraversal(node, result):
    if node:
        inorderTraversal(node.left, result)
        result.append(node.val)
        inorderTraversal(node.right, result)

# Test the code
s = "4(2(3)(1))(6(5))"
root = constructTree(s)
output = []
inorderTraversal(root, output)
print(output)

