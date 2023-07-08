def mergeAndCount(left, right):
    result = []
    i, j = 0, 0
    count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            result.append(count)
            i += 1
        else:
            result.append(right[j])
            j += 1
            count += 1

   
    result.extend(left[i:])
    result.extend(right[j:])

    return result, count

def mergeSortAndCount(nums, start, end):
    if start >= end:
        return [], 0

    mid = (start + end) // 2

    left, left_count = mergeSortAndCount(nums, start, mid)
    right, right_count = mergeSortAndCount(nums, mid + 1, end)

    merged, count = mergeAndCount(left, right)

    return merged, left_count + right_count + count

def countSmaller(nums):
    _, counts = mergeSortAndCount(nums, 0, len(nums) - 1)
    return counts

# Example 1
nums1 = [5, 2, 6, 1]
print(countSmaller(nums1))


# Example 2
nums2 = [-1]
print(countSmaller(nums2))


# Example 3
nums3 = [-1, -1]
print(countSmaller(nums3))



