def product_of_array_elements(arr):
    product = 1
    for num in arr:
        product *= num
    return product



arr1 = [1, 2, 3, 4, 5]
print(product_of_array_elements(arr1))  

arr2 = [1, 6, 3]
print(product_of_array_elements(arr2))  