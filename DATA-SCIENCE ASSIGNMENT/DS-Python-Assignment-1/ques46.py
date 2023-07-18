def find_first_missing_positive(nums):
    n = len(nums)

    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    
        if nums[i] != i + 1:
            return i + 1

    
    return n + 1



numbers = [3, 4, -1, 1]
result = find_first_missing_positive(numbers)
print("First missing positive:", result)
