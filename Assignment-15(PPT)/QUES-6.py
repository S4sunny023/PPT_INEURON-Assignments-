def evaluatePostfixExpression(S):
    stack = []

    for ch in S:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if ch == '+':
                result = operand1 + operand2
            elif ch == '-':
                result = operand1 - operand2
            elif ch == '*':
                result = operand1 * operand2
            elif ch == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()


# Example 1
S1 = "231*+9-"
result1 = evaluatePostfixExpression(S1)
print(result1)  

# Example 2
S2 = "123+*8-"
result2 = evaluatePostfixExpression(S2)
print(result2)  
