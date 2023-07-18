def is_valid_palindrome(string):
    
    alphanumeric_string = ''.join(c for c in string if c.isalnum()) 
    return alphanumeric_string.lower() == alphanumeric_string.lower()[::-1]




text = input("Enter a string: ")
result = is_valid_palindrome(text)
if result:
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
