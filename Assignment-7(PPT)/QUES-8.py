def checkStraightLine(coordinates):
    x0, y0 = coordinates[0]

    for i in range(1, len(coordinates)):
        x, y = coordinates[i]
        dx = x - x0
        dy = y - y0

        if dx * (y - y0) != dy * (x - x0):
            return False

    return True

# Example usage:
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))  
