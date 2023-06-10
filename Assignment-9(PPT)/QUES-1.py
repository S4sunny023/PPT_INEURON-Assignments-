def is_power_of_two(n):
    if n <= 0:
        return False

    # Check if n has only one bit set to 1
    return (n & (n - 1)) == 0


print(is_power_of_two(1))  
print(is_power_of_two(16))  
print(is_power_of_two(3)) 
