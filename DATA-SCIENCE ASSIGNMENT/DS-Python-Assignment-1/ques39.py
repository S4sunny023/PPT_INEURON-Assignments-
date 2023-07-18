def sum_of_digits(number):
    number_str = str(number)

   
    digit_sum = 0

    
    for char in number_str:
        digit_sum += int(char)

    return digit_sum


num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("Sum of digits:", result)
