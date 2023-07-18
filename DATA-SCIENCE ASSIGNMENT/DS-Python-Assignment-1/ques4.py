def occurence_count(lst):
    count = {}
    for i in lst:
        if i in count:
            count[i]+=1
        else:
            count[i]=1    
    return count


input_list = [12,21,21,3,5,6,9,6,7,5,88,65,75,65,]
print(occurence_count(input_list))