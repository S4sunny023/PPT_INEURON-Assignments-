def maximumGap(nums):
    n = len(nums)
    if n < 2:
        return 0

    max_num = max(nums)

    exp = 1
    buckets = [[] for _ in range(10)]

    while max_num // exp > 0:
        for num in nums:
            digit = (num // exp) % 10
            buckets[digit].append(num)

        nums = [num for bucket in buckets for num in bucket]
        buckets = [[] for _ in range(10)]

        exp *= 10

    max_gap = 0
    for i in range(1, n):
        max_gap = max(max_gap, nums[i] - nums[i-1])

    return max_gap


nums1 = [3, 6, 9, 1]
print(maximumGap(nums1))


nums2 = [10]
print(maximumGap(nums2))

