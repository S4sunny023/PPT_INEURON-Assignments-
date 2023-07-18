def find_smallest_missing_positive(numbers):
    n = len(numbers)

    
    for i in range(n):
        while 1 <= numbers[i] <= n and numbers[i] != numbers[numbers[i] - 1]:
            numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]

   
    for i in range(n):
        if numbers[i] != i + 1:
            return i + 1    
    return n + 1


numbers = [3, 4, -1, 1]
result = find_smallest_missing_positive(numbers)
print("Smallest missing positive integer:", result)
