def maxSubarraySumCircular(nums):
    max_sum = float('-inf')
    min_sum = float('inf')
    current_max = 0
    current_min = 0
    array_sum = 0
    
    for num in nums:
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)
        
        current_min = min(current_min + num, num)
        min_sum = min(min_sum, current_min)
        
        array_sum += num
    
    if max_sum > 0:
        return max(max_sum, array_sum - min_sum)
    else:
        return max_sum


print(maxSubarraySumCircular([1, -2, 3, -2]))  
print(maxSubarraySumCircular([5, -3, 5]))  
print(maxSubarraySumCircular([-3, -2, -3])) 

