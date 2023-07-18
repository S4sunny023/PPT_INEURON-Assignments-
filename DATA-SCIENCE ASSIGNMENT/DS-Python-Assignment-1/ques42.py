def longest_palindrome_substring(string):
    if not string:
        return ""

    n = len(string)
    start = 0
    max_length = 1
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2

    
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if string[i] == string[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length

    return string[start:start + max_length]


text = input("Enter a string: ")
result = longest_palindrome_substring(text)
print("Longest palindrome substring:", result)
