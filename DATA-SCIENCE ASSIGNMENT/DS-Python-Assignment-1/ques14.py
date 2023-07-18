def fibonacci(n):
    fib_seq = []
    if n>=1:
        fib_seq.append(0)
    if n>=2:
        fib_seq.append(1)
   
    for i in range(2,n):
        next_no = fib_seq[i-1] + fib_seq[i-2]
        fib_seq.append(next_no)
    return fib_seq
    



n = int(input('Enter the no. of seq:'))
fib_sequence = fibonacci(n)
print(fib_sequence)

