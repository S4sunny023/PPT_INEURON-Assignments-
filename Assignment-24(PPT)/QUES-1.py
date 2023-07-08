def roman_to_int(s):
    symbol_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(s)

    for i in range(n):
        if i < n - 1 and symbol_values[s[i]] < symbol_values[s[i+1]]:
            total -= symbol_values[s[i]]
        else:
            total += symbol_values[s[i]]

    return total


print(roman_to_int("III"))    
print(roman_to_int("LVIII"))   
