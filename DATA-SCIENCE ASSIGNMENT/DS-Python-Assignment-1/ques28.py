def square_root(n):
    if n < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    if n == 0:
        return 0
    x = n  
    while True:
        
        y = (x + n / x) / 2

      
        if abs(y - x) < 1e-10:
            break

        x = y

    return y

# Test the function
num = float(input("Enter a number: "))
result = square_root(num)
print("Square root:", result)
