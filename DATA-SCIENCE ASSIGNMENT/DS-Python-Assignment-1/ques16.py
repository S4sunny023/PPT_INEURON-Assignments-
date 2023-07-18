def sorted_lst(lst):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            return False
       
    return True
        

my_list = [1, 3, 5, 5, 7, 9]
print(sorted_lst(my_list))  

my_list = [2, 4, 1, 7, 6]
print(sorted_lst(my_list))  
