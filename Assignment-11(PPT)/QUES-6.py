def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


nums1 = [3, 4, 5, 1, 2]
print(findMin(nums1))  

nums2 = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums2))  

nums3 = [11, 13, 15, 17]
print(findMin(nums3))  
