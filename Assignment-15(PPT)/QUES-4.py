def reverseStack(stack):
    if len(stack) <= 1:
        return

    top_element = stack.pop()

    reverseStack(stack)

    insertAtBottom(stack, top_element)


def insertAtBottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
        return

    top_element = stack.pop()

    insertAtBottom(stack, element)

    stack.append(top_element)


# Example 1
St1 = [3, 2, 1, 7, 6]
reverseStack(St1)
print(St1)  



# Example 2
St2 = [4, 3, 9, 6]
reverseStack(St2)
print(St2)  

