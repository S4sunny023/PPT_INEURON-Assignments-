def decodeString(s):
    stack = []

    for c in s:
        if c.isdigit():
            num = int(c)
        elif c == '[' or c.isalpha():
            stack.append(c)
        elif c == ']':
            partial = ''
            while stack[-1] != '[':
                partial = stack.pop() + partial
            stack.pop()  # Pop the opening square bracket

            # Repeat the string 'partial' num times and push it back onto the stack
            stack.append(partial * num)

    decoded_string = ''.join(stack)
    return decoded_string

# Test the code
s = "3[a]2[bc]"
decoded = decodeString(s)
print(decoded)
