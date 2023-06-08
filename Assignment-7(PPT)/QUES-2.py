def isStrobogrammatic(num):
    mapping = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }

    left = 0
    right = len(num) - 1

    while left <= right:
        if num[left] not in mapping or num[right] not in mapping or mapping[num[left]] != num[right]:
            return False

        left += 1
        right -= 1

    return True

# Example usage:
num = "69"
print(isStrobogrammatic(num))  
