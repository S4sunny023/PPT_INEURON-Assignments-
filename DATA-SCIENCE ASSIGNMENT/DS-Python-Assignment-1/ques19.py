def remove_vowels(str):
    vowel = ['a','e','i','o','u']
    result = ''
    for i in str:
        if i.lower() not in vowel:
            result = result+i
    return result


str = input('Enter your word: ')
print(remove_vowels(str=str))
    
