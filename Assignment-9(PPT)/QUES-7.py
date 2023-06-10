def permute_string(S, left, right):
    if left == right:
        print(''.join(S))
    else:
        for i in range(left, right + 1):
            S[left], S[i] = S[i], S[left]  # Swap characters
            permute_string(S, left + 1, right)  # Recurse on the remaining characters
            S[left], S[i] = S[i], S[left]  # Restore the original order

def print_permutations(S):
    n = len(S)
    permute_string(list(S), 0, n - 1)




print_permutations("ABC")  
print_permutations("XY")  
