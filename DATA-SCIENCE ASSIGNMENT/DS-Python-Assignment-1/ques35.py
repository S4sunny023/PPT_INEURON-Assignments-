def is_perfect_square(num):
    if num < 0:
        return False

    
    sqrt = int(num ** 0.5)

    return sqrt * sqrt == num




n
number = int(input("Enter a number: "))
result = is_perfect_square(number)
if result:
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
