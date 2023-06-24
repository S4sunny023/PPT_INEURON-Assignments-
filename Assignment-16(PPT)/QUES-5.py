def reverseNumber(num):
    stack = []
    num_str = str(num)

    # Push each digit onto the stack
    for digit in num_str:
        stack.append(digit)

    reversed_str = ""

    # Pop each digit from the stack and append it to the reversed string
    while stack:
        reversed_str += stack.pop()

    # Convert the reversed string back to an integer
    reversed_num = int(reversed_str)

    return reversed_num

# Example usage:
num = 365
reversed_num = reverseNumber(num)
print(reversed_num) 


