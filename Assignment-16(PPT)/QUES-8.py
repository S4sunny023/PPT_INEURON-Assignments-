def findMaxAbsoluteDiff(arr):
    n = len(arr)
    NSE = [0] * n
    NSR = [0] * n

    stack = []

    # Finding Next Smaller Element on the left (NSE)
    for i in range(n):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            NSE[i] = stack[-1]

        stack.append(arr[i])

    stack.clear()

    # Finding Next Smaller Element on the right (NSR)
    for i in range(n-1, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            NSR[i] = stack[-1]

        stack.append(arr[i])

    maxDiff = 0

    # Finding maximum absolute difference
    for i in range(n):
        diff = abs(NSE[i] - NSR[i])
        maxDiff = max(maxDiff, diff)

    return maxDiff

# Example usage:
arr = [2, 1, 8]
result = findMaxAbsoluteDiff(arr)
print(result)  

arr = [2, 4, 8, 7, 7, 9, 3]
result = findMaxAbsoluteDiff(arr)
print(result) 

arr = [5, 1, 9, 2, 5, 1, 7]
result = findMaxAbsoluteDiff(arr)
print(result)  
