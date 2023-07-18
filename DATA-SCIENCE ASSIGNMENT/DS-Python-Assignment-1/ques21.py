def is_anagram(str1,str2):
    str1 = str1.lower().replace(' ','')
    str2 = str2.lower().replace(' ','')


    if len(str1)!=len(str2):
        return False
    
    str1_lst = sorted(list(str1))
    str2_lst = sorted(list(str2))


    if str1_lst==str2_lst:
        return True
    else:
        return False
    


string1 = "listen"
string2 = "silent"
result = is_anagram(string1, string2)
print(result)  

string3 = "hello"
string4 = "hola"
result = is_anagram(string3, string4)
print(result)  
