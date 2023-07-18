#11. Write a program to find the common elements between two lists

def common_lst(l1,l2):
    common_lst = []
    for i in l1:
        if i in set(l2):
            common_lst.append(i)
    return common_lst        


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = common_lst(list1, list2)
print(common_elements)
