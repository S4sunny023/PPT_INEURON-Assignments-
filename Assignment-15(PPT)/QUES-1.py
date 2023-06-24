def findNextGreaterElements(arr):
    stack = []
    output = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            output[stack.pop()] = arr[i]
        stack.append(i)

    return output

# Example 1
arr1 = [1, 3, 2, 4]
result1 = findNextGreaterElements(arr1)
print(result1) 

# Example 2
arr2 = [6, 8, 0, 1, 3]
result2 = findNextGreaterElements(arr2)
print(result2) 



