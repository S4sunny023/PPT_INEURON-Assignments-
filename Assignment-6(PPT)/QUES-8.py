def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True
    
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        
        # Check if the current point lies on the same line
        if (x - x1) * (y2 - y1) != (x2 - x1) * (y - y1):
            return False
    
    return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result = checkStraightLine(coordinates)
print(result)
