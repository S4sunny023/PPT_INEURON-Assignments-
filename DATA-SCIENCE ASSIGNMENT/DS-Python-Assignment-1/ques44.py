def is_perfect_number(number):
    if number <= 0:
        return False

    divisors = [1]  
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)

    return sum(divisors) == number





num = int(input("Enter a number: "))
result = is_perfect_number(num)
if result:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")
