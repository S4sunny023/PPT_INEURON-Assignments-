def calculate_length(s):
    if s == "":
        return 0
    else:
        return 1 + calculate_length(s[1:])


# Test Examples
print(calculate_length("abcd")) 
print(calculate_length("GEEKSFORGEEKS"))  
