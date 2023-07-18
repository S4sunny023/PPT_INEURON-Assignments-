def prime_factors(n):
    factors = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return factors

# Test the function
num = int(input("Enter a number: "))
result = prime_factors(num)
print("Prime factors of", num, "are:", result)
