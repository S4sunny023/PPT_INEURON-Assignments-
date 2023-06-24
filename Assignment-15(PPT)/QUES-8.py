def trapWater(height):
    left = 0
    right = len(height) - 1
    left_max = 0
    right_max = 0
    total_water = 0

    while left <= right:
        if height[left] <= height[right]:
            if height[left] > left_max:
                left_max = height[left]
            else:
                total_water += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                total_water += right_max - height[right]
            right -= 1

    return total_water


# Example 1
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
water1 = trapWater(height1)
print(water1)

# Example 2
height2 = [4, 2, 0, 3, 2, 5]
water2 = trapWater(height2)
print(water2)  
