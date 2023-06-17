def findMissingNumber(nums):
    n = len(nums)
    missing = n

    for i in range(n):
        missing ^= i ^ nums[i]

    return missing



nums1 = [3, 0, 1]
print(findMissingNumber(nums1))  

nums2 = [0, 1]
print(findMissingNumber(nums2))  

nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(findMissingNumber(nums3))  
