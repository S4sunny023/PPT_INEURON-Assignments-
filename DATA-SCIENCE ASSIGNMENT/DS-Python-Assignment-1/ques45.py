def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)


text = input("Enter a string: ")
result = remove_duplicates(text)
print("String after removing duplicates:", result)
