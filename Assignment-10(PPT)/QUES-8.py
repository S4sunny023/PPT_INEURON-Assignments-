def count_consonants(str):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0

    for char in str:
        if char in consonants:
            count += 1

    return count

# Example usage
str = "geeksforgeeks portal"
total_consonants = count_consonants(str)
print(total_consonants)
