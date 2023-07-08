def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - 1

    while right - left + 1 > k:
        if x - arr[left] >= arr[right] - x:
            left += 1
        else:
            right -= 1

    return arr[left:right+1]


print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))


print(find_closest_elements([1, 2, 3, 4, 5], 4, -1))

