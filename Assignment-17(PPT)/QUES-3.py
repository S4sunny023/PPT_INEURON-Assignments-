def countStudents(students, sandwiches):
    unable_to_eat = 0
    n = len(students)
    i = 0

    while students and i < n:
        if students[0] == sandwiches[0]:
            students.pop(0)
            sandwiches.pop(0)
            unable_to_eat = 0
        else:
            students.append(students.pop(0))
            unable_to_eat += 1

        i += 1

    return unable_to_eat


print(countStudents([1, 1, 0, 0], [0, 1, 0, 1])) 
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])) 
