def length_of_longest_substring(s):
    max_length = 0
    start = 0
    seen = set()

    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[start])
            start += 1
        seen.add(s[i])
        max_length = max(max_length, i - start + 1)

    return max_length


print(length_of_longest_substring("abcabcbb"))   
print(length_of_longest_substring("bbbbb"))      
print(length_of_longest_substring("pwwkew"))    
