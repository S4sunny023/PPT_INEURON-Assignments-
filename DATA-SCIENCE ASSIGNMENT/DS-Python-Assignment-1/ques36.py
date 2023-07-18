def calculate_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

# Test the function
numbers = [1, 2, 3, 4, 5]
result = calculate_product(numbers)
print("Product:", result)
