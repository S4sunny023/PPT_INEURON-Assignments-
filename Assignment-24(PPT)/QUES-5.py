def nth_ugly_number(n):
    ugly = [0] * n
    ugly[0] = 1
    p2 = p3 = p5 = 0

    for i in range(1, n):
        next_ugly = min(ugly[p2] * 2, ugly[p3] * 3, ugly[p5] * 5)
        ugly[i] = next_ugly

        if next_ugly == ugly[p2] * 2:
            p2 += 1
        if next_ugly == ugly[p3] * 3:
            p3 += 1
        if next_ugly == ugly[p5] * 5:
            p5 += 1

    return ugly[n - 1]


print(nth_ugly_number(10)) 
print(nth_ugly_number(1))  

