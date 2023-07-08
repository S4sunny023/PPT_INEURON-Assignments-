def containsDuplicate(nums):
    unique_nums = set()

    for num in nums:
        if num in unique_nums:
            return True
        unique_nums.add(num)

    return False

nums1 = [1, 2, 3, 1]
print(containsDuplicate(nums1))


nums2 = [1, 2, 3, 4]
print(containsDuplicate(nums2))


nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(containsDuplicate(nums3))




