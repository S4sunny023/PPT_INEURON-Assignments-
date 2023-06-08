def processString(string):
    stack = []
    for c in string:
        if c != '#':
            stack.append(c)
        elif stack:
            stack.pop()
    return ''.join(stack)

def backspaceCompare(s, t):
    s_processed = processString(s)
    t_processed = processString(t)
    return s_processed == t_processed

# Example usage:
s = "ab#c"
t = "ad#c"
print(backspaceCompare(s, t))  
