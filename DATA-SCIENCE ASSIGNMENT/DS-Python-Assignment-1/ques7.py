def factorial(n):
    if n < 0 :
        return None
    if n ==0 :
        return 1
    else:
        result = 1
    for i in range(2, n+1):
        result = result * i

    return result    


n = int(input('Enter the number :'))
print(factorial(n))




