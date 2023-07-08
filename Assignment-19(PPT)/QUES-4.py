def moveZeroes(nums):
    n = len(nums)
    j = 0

    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    for i in range(j, n):
        nums[i] = 0

    return nums

# Example 1
nums1 = [1, 2, 0, 4, 3, 0, 5, 0]
print(moveZeroes(nums1))


# Example 2
nums2 = [1, 2, 0, 0, 0, 3, 6]
print(moveZeroes(nums2))



