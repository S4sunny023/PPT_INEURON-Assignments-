def count_occurrences(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count




numbers = [1, 2, 3, 4, 2, 2, 5, 2]
element = int(input("Enter an element: "))
result = count_occurrences(numbers, element)
print("Number of occurrences:", result)
