def remove_duplicates(lst):
    seen = set()
    result = []

    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)

    return result

# Test the function
numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
result = remove_duplicates(numbers)
print("List after removing duplicates:", result)
