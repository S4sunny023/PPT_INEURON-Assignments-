def reverseStr(s, k):
    chars = list(s)
    i = 0

    while i < len(chars):
        chars[i:i+k] = reversed(chars[i:i+k]) 
        i += 2 * k

    return ''.join(chars)

# Example usage:
s = "abcdefg"
k = 2
print(reverseStr(s, k)) 
