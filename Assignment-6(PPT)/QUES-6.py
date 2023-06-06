def can_shift(s, goal):
    if len(s) != len(goal):
        return False

    sConcat = s + s
    if goal in sConcat:
        return True
    else:
        return False

# Example usage
s = "abcde"
goal = "cdeab"
print(can_shift(s, goal))  
