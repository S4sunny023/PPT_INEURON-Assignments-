def find_maximum(arr, n):
    # Base case: If there's only one element, it is the maximum
    if n == 1:
        return arr[0]

    # Recursive case: Compare the maximum of the subarray with the last element
    return max(arr[n - 1], find_maximum(arr, n - 1))



arr1 = [1, 4, 3, -5, -4, 8, 6]
print(find_maximum(arr1, len(arr1))) 

arr2 = [1, 4, 45, 6, 10, -8]
print(find_maximum(arr2, len(arr2)))  