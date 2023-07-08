def find132pattern(nums):
    n = len(nums)
    stack = []
    potential_3 = float('-inf')

    for i in range(n-1, -1, -1):
        if nums[i] < potential_3:
            return True
        while stack and nums[i] > stack[-1]:
            potential_3 = stack.pop()
        stack.append(nums[i])

    return False


nums1 = [1, 2, 3, 4]
print(find132pattern(nums1))


nums2 = [3, 1, 4, 2]
print(find132pattern(nums2))


nums3 = [-1, 3, 2, 0]
print(find132pattern(nums3))

