def longest_common_prefix(strings):
    if not strings:
        return ""

   
    min_length = min(len(s) for s in strings)

    
    for i in range(min_length):
        for j in range(1, len(strings)):
            if strings[j][i] != strings[j-1][i]:
                return strings[j][:i]

    
    return strings[0][:min_length]

word_list = ["flower", "flow", "flight"]
result = longest_common_prefix(word_list)
print("Longest common prefix:", result)
