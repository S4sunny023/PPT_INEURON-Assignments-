def second_largest(lst):
    if len(lst)<2:
        return None
    

    largest = lst[0]
    second_largest = float('-inf')

    for i in lst:
        if i>largest:
            second_largest=largest
            largest = i
        elif i>second_largest and i < largest:
            second_largest = i

    if second_largest == float('-inf'):
        return None
    else:
        return second_largest   


input_list = [12,21,21,3,5,6,9,6,7,5,88,65,75,65,]
print(second_largest(input_list))             

