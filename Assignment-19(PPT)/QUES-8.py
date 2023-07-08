from collections import Counter

def intersect(nums1, nums2):
    freqMap = Counter(nums1)
    intersection = []

    for num in nums2:
        if num in freqMap and freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1

    return intersection

# Example 1
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))


# Example 2
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
print(intersect(nums3, nums4))

