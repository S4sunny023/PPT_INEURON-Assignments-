def checkValidString(s):
    stack = []

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        else:  # c == ')'
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '*':
                stack.pop()
            else:
                return False

    while stack:
        if stack[-1] == '(':
            return False
        stack.pop()

    return True

s = "()"
result = checkValidString(s)
print(result)  
