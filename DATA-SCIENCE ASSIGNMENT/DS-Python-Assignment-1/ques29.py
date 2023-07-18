import re

def is_valid_palindrome(string):
   
    alphanumeric_string = re.sub(r'[^a-zA-Z0-9]', '', string).lower()

    
    return alphanumeric_string == alphanumeric_string[::-1]

# Test the function
text = input("Enter a string: ")
result = is_valid_palindrome(text)
if result:
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
