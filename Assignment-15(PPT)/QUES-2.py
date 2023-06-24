def findNearestSmallerElements(a):
    stack = []
    output = [-1] * len(a)

    for i in range(len(a)):
        while stack and stack[-1] >= a[i]:
            stack.pop()

        if stack:
            output[i] = stack[-1]

        stack.append(a[i])

    return output

# Example 1
a1 = [1, 6, 2]
result1 = findNearestSmallerElements(a1)
print(result1)  


# Example 2
a2 = [1, 5, 0, 3, 4, 5]
result2 = findNearestSmallerElements(a2)
print(result2) 
