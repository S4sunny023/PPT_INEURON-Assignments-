from collections import Counter

def find_mode(numbers):
    
    count_dict = Counter(numbers)
    
   
    max_count = max(count_dict.values())
    
   
    modes = [num for num, count in count_dict.items() if count == max_count]
    
    return modes

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 5]
result = find_mode(numbers)
print("Mode(s):", result)
