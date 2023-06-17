def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Move slow and fast pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Reset slow pointer to the beginning
    slow = nums[0]

    # Move slow and fast pointers until they meet
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the repeated number
    return slow



nums1 = [1, 3, 4, 2, 2]
print(findDuplicate(nums1))  # Output: 2

nums2 = [3, 1, 3, 4, 2]
print(findDuplicate(nums2))  # Output: 3
