def non_repeation_char(str):
    char_count = {}
    for i in str:
        char_count[i] = char_count.get(i,0)+1
    for i in str:
        if char_count[i]==1:
            return i
    else:
        print('No repeaction elements found ')


my_string = "abracadabra"
result = non_repeation_char(my_string)
print(result)  
