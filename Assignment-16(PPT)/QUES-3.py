def deleteMiddle(stack, index):
    if index == len(stack) // 2:
        stack.pop()
        return
    temp = stack.pop()
    deleteMiddle(stack, index + 1)
    stack.append(temp)

# Example usage:
stack = [1, 2, 3, 4, 5]
deleteMiddle(stack, 0)
print(stack)

stack = [1, 2, 3, 4, 5]
deleteMiddle(stack, 0)
print(stack)  
