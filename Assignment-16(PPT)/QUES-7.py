def countWordsAfterDestruction(sequence):
    stack = []

    for word in sequence:
        if not stack or word != stack[-1]:
            stack.append(word)
        else:
            stack.pop()

    return len(stack)

# Example usage:
sequence = ["ab", "aa", "aa", "bcd", "ab"]
result = countWordsAfterDestruction(sequence)
print(result)  

sequence = ["tom", "jerry", "jerry", "tom"]
result = countWordsAfterDestruction(sequence)
print(result) 
