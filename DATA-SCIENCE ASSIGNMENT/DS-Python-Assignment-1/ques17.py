def lst_intersection(lst1, lst2):
    intersection = []
    for i in lst1:
        if i in lst2:
            intersection.append(i)
    return intersection  
  

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = lst_intersection(list1, list2)
print(intersection)  # Output: [4, 5]
