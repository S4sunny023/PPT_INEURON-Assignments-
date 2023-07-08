def mergeArrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    merged.extend(arr1[i:])
    merged.extend(arr2[j:])

    return merged

# Example 1
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
print(mergeArrays(arr1, arr2))


# Example 2
arr3 = [5, 8, 9]
arr4 = [4, 7, 8]
print(mergeArrays(arr3, arr4))

