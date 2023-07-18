def permutation(str,i=0):
    if i== len(str):
        print("".join(str))


    for k in range(i, len(str)):
        words = [c for c in str]
        words[i], words[k] = words[k], words[i]
        permutation(words,i+1)  


print(permutation('yup'))
