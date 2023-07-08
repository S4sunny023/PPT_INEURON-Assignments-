class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSameTree(preorder, inorder, postorder):
    if not preorder and not inorder and not postorder:
        return True

    if not (preorder and inorder and postorder):
        return False

    root_val = preorder[0]
    idx = inorder.index(root_val)

    if inorder[:idx] == postorder[-(len(inorder)-idx):] and inorder[idx+1:] == postorder[:-(len(inorder)-idx-1)]:
        left_subtree = isSameTree(preorder[1:idx+1], inorder[:idx], postorder[:-(len(inorder)-idx-1)])
        right_subtree = isSameTree(preorder[idx+1:], inorder[idx+1:], postorder[-(len(inorder)-idx):])
        return left_subtree and right_subtree

    return False

# Example 1:
preorder1 = [1, 2, 4, 5, 3]
inorder1 = [4, 2, 5, 1, 3]
postorder1 = [4, 5, 2, 3, 1]
if isSameTree(preorder1, inorder1, postorder1):
    print("Yes")
else:
    print("No")


# Example 2:
preorder2 = [1, 5, 4, 2, 3]
inorder2 = [4, 2, 5, 1, 3]
postorder2 = [4, 1, 2, 3, 5]
if isSameTree(preorder2, inorder2, postorder2):
    print("Yes")
else:
    print("No")



