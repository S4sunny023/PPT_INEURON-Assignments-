def reverseStr(s, k):
    char_list = list(s)
    length = len(char_list)

    for start in range(0, length, 2 * k):
        end = min(start + k - 1, length - 1)

        while start < end:
            char_list[start], char_list[end] = char_list[end], char_list[start]
            start += 1
            end -= 1

    return ''.join(char_list)

s = "abcdefg"
k = 2
print(reverseStr(s, k))  
