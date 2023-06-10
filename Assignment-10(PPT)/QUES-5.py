def count_contiguous_substrings(s):
    if len(s) <= 1:
        return len(s)
    else:
        count = 0
        if s[0] == s[-1]:
            count += 1
        count += count_contiguous_substrings(s[:-1])
        count += count_contiguous_substrings(s[1:])
        count -= count_contiguous_substrings(s[1:-1])  # To avoid double-counting
        return count


# Test Examples
print(count_contiguous_substrings("abcab"))  # Output: 7
print(count_contiguous_substrings("aba"))  # Output: 4


