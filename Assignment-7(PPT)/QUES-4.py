def reverseWords(s):
    words = s.split()
    for i in range(len(words)):
        words[i] = words[i][::-1]  
    return ' '.join(words)

# Example usage:
s = "Let's take LeetCode contest"
print(reverseWords(s)) 
