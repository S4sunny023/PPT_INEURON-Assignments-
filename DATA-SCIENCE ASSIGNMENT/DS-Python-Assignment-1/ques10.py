def sum_all(lst):
    total = 0
    for i in lst:
        total = total+i
    return total

my_list = [1, 2, 3, 4, 5]
sum_of_numbers = sum_all(my_list)
print(sum_of_numbers)
