def reverseString(S):
    stack = []
    for char in S:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string

# Example
S = "GeeksforGeeks"
reversed_str = reverseString(S)
print(reversed_str) 
