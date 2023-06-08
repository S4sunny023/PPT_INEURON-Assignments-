def addStrings(num1, num2):
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        digit_sum = carry

        if i >= 0:
            digit_sum += int(num1[i])
            i -= 1

        if j >= 0:
            digit_sum += int(num2[j])
            j -= 1

        carry = digit_sum // 10
        digit_sum %= 10

        result = str(digit_sum) + result

    return result

# Example usage:
num1 = "11"
num2 = "123"
print(addStrings(num1, num2))  # Output: "134"
