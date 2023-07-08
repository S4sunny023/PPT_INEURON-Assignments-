def rearrangeArray(nums):
    n = len(nums)
    j = 0

    for i in range(n):
        if (nums[i] > 0 and i % 2 == 0) or (nums[i] < 0 and i % 2 == 1):
            nums[i], nums[j] = nums[j], nums[i]
            j += 1

    return nums

# Example 1
nums1 = [1, 2, 3, -4, -1, 4]
print(rearrangeArray(nums1))


# Example 2
nums2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(rearrangeArray(nums2))



