def find_missing_number(numbers):
    n = len(numbers) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    missing_number = total_sum - actual_sum
    return missing_number





numbers = [1, 2, 3, 5, 6, 7, 8]
result = find_missing_number(numbers)
print("Missing number:", result)
