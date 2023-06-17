def searchRange(nums, target):
    left = -1
    right = -1

    # Find leftmost position of the target
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            left = mid
            end = mid - 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Find rightmost position of the target
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if nums[mid] == target:
            right = mid
            start = mid + 1
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return [left, right]



nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
print(searchRange(nums1, target1)) 

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(searchRange(nums2, target2))

nums3 = []
target3 = 0
print(searchRange(nums3, target3)) 
