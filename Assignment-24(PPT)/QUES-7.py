from collections import deque

def max_sliding_window(nums, k):
    window = deque()
    result = []

    for i, num in enumerate(nums):
        while window and window[0] <= i - k:
            window.popleft()
        while window and nums[window[-1]] <= num:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])

    return result


print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))


