def is_anagram(str1, str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")

    if len(str1)!=len(str2):
        return False
    else:
        sorted_str1 = sorted(list(str1))
        sorted_str2 = sorted(list(str2))
        if sorted_str1 == sorted_str2:
            return True
        else:
            return False
        

str1 = "listen"
str2 = "silent"
print(is_anagram(str1, str2))  

str3 = "hello"
str4 = "world"
print(is_anagram(str3, str4))  
