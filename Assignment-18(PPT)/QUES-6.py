def findMinArrowShots(points):
    if not points:
        return 0

    points.sort(key=lambda x: x[1]) 
    end = points[0][1]
    arrows = 1

    for i in range(1, len(points)):
        if points[i][0] > end:
            end = points[i][1]
            arrows += 1

    return arrows

points1 = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(findMinArrowShots(points1))


points2 = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(findMinArrowShots(points2))


points3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
print(findMinArrowShots(points3))
