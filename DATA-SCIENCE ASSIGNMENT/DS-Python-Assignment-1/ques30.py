def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

# Test the function
numbers = [4, 5, 6, 7, 0, 1, 2]
result = find_minimum(numbers)
print("Minimum element:", result)
