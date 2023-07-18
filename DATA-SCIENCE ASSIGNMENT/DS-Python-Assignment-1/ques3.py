def find_largest(lst):
    if lst == 0:
        return None
    
    largest = lst[0]
    for i in lst:
        if i>largest:
            largest = i
    return largest


lst = [1,52,86,-9,65,10]

print(find_largest(lst))
        

