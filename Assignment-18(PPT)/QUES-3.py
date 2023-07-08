def firstBadVersion(n, bad):
    left = 1
    right = n

    while left < right:
        mid = left + (right - left) // 2
        if mid >= bad:
            right = mid
        else:
            left = mid + 1

    return left


n1 = 5
bad1 = 4
print(firstBadVersion(n1, bad1))  

n2 = 1
bad2 = 1
print(firstBadVersion(n2, bad2))  


