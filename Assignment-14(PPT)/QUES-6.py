class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(head):
    stack = []
    result = []

    # Step 1: Initialize an empty stack and result array
    while head is not None:
        # Step 2a: Process nodes with larger values
        while stack and stack[-1][1] < head.val:
            index, _ = stack.pop()
            result[index] = head.val

        # Step 2b: Push the current node onto the stack
        stack.append((len(result), head.val))
        result.append(0)

        head = head.next

    # Step 3: Set remaining elements in the result array to 0
    while stack:
        index, _ = stack.pop()
        result[index] = 0

    # Step 4: Return the result array
    return result
