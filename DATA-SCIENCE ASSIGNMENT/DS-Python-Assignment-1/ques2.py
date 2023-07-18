def is_palindrome(string):
    string= string.replace(" ","").lower()
    return string == string[::-1]


input_string = input('Enter your string: ')
if is_palindrome(input_string):
    print('given string is Palindrome')
else :
    print('given string is not palindrome')   