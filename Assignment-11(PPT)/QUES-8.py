from collections import defaultdict

def intersect(nums1, nums2):
    freqMap = defaultdict(int)
    for num in nums1:
        freqMap[num] += 1

    intersection = []
    for num in nums2:
        if num in freqMap and freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1

    return intersection


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))
nums3 = [4, 9, 5]
nums4 = [9, 4, 9, 8, 4]
print(intersect(nums3, nums4))  

