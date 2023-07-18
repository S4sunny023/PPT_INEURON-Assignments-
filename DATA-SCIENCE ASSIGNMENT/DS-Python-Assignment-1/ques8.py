def is_prime(n):
    if n < 0:
        print('Negative number is not a Prime Number')
    elif n == 0 or n ==1:
        return False
    elif n== 2:
        return True
    elif n>2:
        for i in range(2,n):
            if n%i == 0:
                return False
        return True
    

n = int(input('Enter the number :'))
print(is_prime(n))    

