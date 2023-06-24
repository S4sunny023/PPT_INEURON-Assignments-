def sortStack(stack):
    temp_stack = []
    while stack:
        temp = stack.pop()
        while temp_stack and temp_stack[-1] > temp:
            stack.append(temp_stack.pop())
        temp_stack.append(temp)
    while temp_stack:
        stack.append(temp_stack.pop())

# Example usage:
stack = [34, 3, 31, 98, 92, 23]
sortStack(stack)
print(stack) 


stack = [34, 3, 31, 98, 92, 23]
sortStack(stack)
print(stack)  

